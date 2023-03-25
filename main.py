import sys
import sqlite3
import argparse
import discord
import openai
import os
import asyncio
import functools
from dotenv import load_dotenv
from discord.ext import commands
from views import OptButtonView, ClearAllButton
from models import create_chat_completion_gpt35turbo, create_chat_completion_davinci
from model_db import get_current_model, set_current_model, get_api_tokens, set_api_tokens, get_user_history, \
    add_user_message, add_assistant_message, clear_user_history, clear_all_user_histories, clear_tokens
import ctypes

parser = argparse.ArgumentParser()
parser.add_argument("-cleartoken", help="Очистить токены Discord и OpenAI", action="store_true")
args = parser.parse_args()

if args.cleartoken:
    clear_tokens()
    print("Токены Discord и OpenAI были успешно удалены.")

# Изменение здесь - использование абсолютного пути к файлу .env
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
load_dotenv(env_path)

print("FC Discord Bot for OpenAI. Build: v0.0.5-alpha")
ctypes.windll.kernel32.SetConsoleTitleW("FC Discord Bot (v0.0.5-alpha")
print("Pycord Lib version: ", discord.__version__)

# Получение токенов из файла .env или базы данных
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not DISCORD_TOKEN or not OPENAI_API_KEY:
    DISCORD_TOKEN, OPENAI_API_KEY = get_api_tokens()

# Если токены отсутствуют, запросите их у пользователя и сохраните в базе данных
if not DISCORD_TOKEN or not OPENAI_API_KEY:
    DISCORD_TOKEN = input("Введите API токен Discord: ")
    OPENAI_API_KEY = input("Введите API токен OpenAI: ")
    set_api_tokens(DISCORD_TOKEN, OPENAI_API_KEY)

openai.api_key = OPENAI_API_KEY

intents = discord.Intents.default()
intents.typing = True
intents.presences = False
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))


@bot.command()
async def clear(ctx):
    user_id = ctx.author.id
    clear_user_history(user_id)
    await ctx.send(f"История сообщений пользователя {ctx.author.mention} была успешно удалена.")


@bot.command()
@commands.has_permissions(administrator=True)
async def changemodel(ctx):
    view = OptButtonView(model_change_listener=set_current_model)
    await ctx.send("Выберите одну из следующих опций:", view=view)


@bot.command()
@commands.has_permissions(administrator=True)
async def clearall(ctx):
    view = discord.ui.View()
    clear_all_button = ClearAllButton(clear_all_user_histories)
    view.add_item(clear_all_button)
    await ctx.send("Нажмите кнопку ниже, чтобы очистить историю всех пользователей:", view=view)


@changemodel.error
@clearall.error
async def forbidden_action(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("У вас нет прав администратора для выполнения этой команды.")
    else:
        await ctx.send("Произошла ошибка при выполнении команды.")


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author.bot:
        return

    bot_mention = bot.user.mention
    bot_roles = [f'<@&{role.id}>' for role in message.guild.me.roles if not role.is_default()]

    if message.content.startswith('!gen') or message.content.startswith(bot_mention) or any(
            message.content.startswith(role_mention) for role_mention in bot_roles):

        print('=====================')
        print(f"Получено новое от автора: {message.author}")
        print(f"Сообщение: {message.content}")
        print('=====================')
        print('')

        prompt = None  # добавьте это
        if message.content.startswith('!gen'):
            prompt = message.content[5:]
        elif message.content.startswith(bot_mention):
            prompt = message.content[len(bot_mention) + 1:]
        else:
            for role_mention in bot_roles:
                if message.content.startswith(role_mention):
                    prompt = message.content[len(role_mention) + 1:]
                    break

        if prompt:  # добавьте это
            # Загрузка текущей модели из базы данных
            current_model = get_current_model()

            user_id = str(message.author.id)
            user_history = get_user_history(user_id)

            if not user_history:
                user_history = [{"role": "system", "content": "You are sarcastic assistant. Your name is Пафнутий"}]

            user_history.append({"role": "user", "content": prompt})

            try:
                if current_model == 'gpt-3.5-turbo':
                    response = await asyncio.wait_for(create_chat_completion_gpt35turbo(user_history), 60)
                    response_text = response.choices[0].message['content']
                elif current_model == 'text-davinci-003':
                    response = await asyncio.wait_for(create_chat_completion_davinci(prompt), 60)
                    response_text = response.choices[0].text

                user_history.append({"role": "assistant", "content": response_text})
                add_user_message(user_id, prompt)
                add_assistant_message(user_id, response_text)

                if isinstance(message.channel, discord.TextChannel):
                    chunks = [response_text[i:i + 2000] for i in range(0, len(response_text), 2000)]
                    for chunk in chunks:
                        await message.channel.send(chunk)
            except asyncio.TimeoutError:
                await message.channel.send("Ошибка генерации сообщения 💀")


bot.run(DISCORD_TOKEN)
