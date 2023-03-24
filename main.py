import sys
import discord
import openai
import os
import asyncio
import functools
from dotenv import load_dotenv
from discord.ext import commands
from views import ButtonView

load_dotenv()

print("FC Discord Bot for OpenAI. Build: v0.0.4-alpha")
print("Pycord Lib version: ", discord.__version__)

TOKEN = os.getenv("DISCORD_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")

intents = discord.Intents.default()
intents.typing = True
intents.presences = False
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


async def create_chat_completion(prompt):
    loop = asyncio.get_event_loop()
    partial = functools.partial(openai.ChatCompletion.create,
                                model='gpt-3.5-turbo',
                                messages=[
                                    {"role": "system", "content": "You are sarcastic assistant. Your name is Пафнутий"},
                                    {"role": "user", "content": prompt}],
                                max_tokens=1024,
                                temperature=0,
                                timeout=25)
    return await loop.run_in_executor(None, partial)


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))


@bot.command()
async def opt(ctx):
    await ctx.send("Выберите одну из следующих опций:", view=ButtonView())


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author.bot:
        return

    bot_mention = bot.user.mention
    # Получаем все упоминания ролей бота

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

        try:
            response = await asyncio.wait_for(create_chat_completion(prompt), 30)

            if isinstance(message.channel, discord.TextChannel):
                response_text = response.choices[0].message['content']
                chunks = [response_text[i:i + 2000] for i in range(0, len(response_text), 2000)]
                for chunk in chunks:
                    await message.channel.send(chunk)
        except asyncio.TimeoutError:
            await message.channel.send("Ошибка генерации сообщения 💀")


bot.run(TOKEN)
