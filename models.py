import asyncio
import functools
import openai


async def create_chat_completion_gpt35turbo(history):
    loop = asyncio.get_event_loop()
    system_message = {"role": "system", "content": "You are a sarcastic assistant. Your name is Пафнутий"}
    messages_with_system = [system_message] + history
    partial = functools.partial(openai.ChatCompletion.create,
                                model='gpt-3.5-turbo',
                                messages=messages_with_system,
                                max_tokens=1024,
                                temperature=0,
                                timeout=60)
    return await loop.run_in_executor(None, partial)


async def create_chat_completion_davinci(prompt):
    loop = asyncio.get_event_loop()
    partial = functools.partial(openai.Completion.create,
                                model='text-davinci-003',
                                prompt=prompt,
                                max_tokens=1024,
                                temperature=0,
                                timeout=60)
    return await loop.run_in_executor(None, partial)
