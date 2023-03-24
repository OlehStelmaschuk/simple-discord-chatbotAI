import sys
import discord
import openai
import os
import asyncio
import functools
from dotenv import load_dotenv
from discord.ext import commands
from views import OptButtonView
from models import create_chat_completion_gpt35turbo, create_chat_completion_davinci

load_dotenv()

print("FC Discord Bot for OpenAI. Build: v0.0.4a-alpha")
print("Pycord Lib version: ", discord.__version__)

if not os.path.exists("model.db"):
    with open("model.db", "w") as f:
        f.write("gpt-3.5-turbo")

TOKEN = os.getenv("DISCORD_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")

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
async def changemodel(ctx):
    await ctx.send("Выберите одну из следующих опций:", view=OptButtonView())


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

        if message.content.startswith('!gen'):
            prompt = message.content[5:]
        elif message.content.startswith(bot_mention):
            prompt = message.content[len(bot_mention) + 1:]
        else:
            role_mention = next(role_mention for role_mention in bot_roles if message.content.startswith(role_mention))
            prompt = message.content[len(role_mention) + 1:]

        # Загрузка текущей модели из файла
        with open("model.db", "r") as file:
            current_model = file.read().strip()

        try:
            if current_model == 'gpt-3.5-turbo':
                response = await asyncio.wait_for(create_chat_completion_gpt35turbo(prompt), 60)
                response_text = response.choices[0].message['content']
            elif current_model == 'text-davinci-003':
                response = await asyncio.wait_for(create_chat_completion_davinci(prompt), 60)
                response_text = response.choices[0].text

            if isinstance(message.channel, discord.TextChannel):
                chunks = [response_text[i:i + 2000] for i in range(0, len(response_text), 2000)]
                for chunk in chunks:
                    await message.channel.send(chunk)
        except asyncio.TimeoutError:
            await message.channel.send("Ошибка генерации сообщения 💀")


bot.run(TOKEN)
