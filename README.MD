# Simple ChatGPT-bot for Discord by GPT-4

Simple chat with authorization and registration written on Python with GPT-4 (ChatGPT)

The project was created to analyze the capabilities of ChatGPT and possible ideas for the implementation of this tool in
the future.

## Installation

Install dependencies:

```
discord.py
py-cord
openai
python-dotenv 
```

Create file .env:

```env
DISCORD_TOKEN=your_discord_token
OPENAI_API_KEY=your_openai_token
```

## Launch

The server is started with the command

### `py main.py`

## Description

The application uses the following technologies:

- Python
- OpenAI
- asyncio

## Technical Description by AI

```text
This project consists of a Discord bot that utilizes OpenAI's GPT-3.5-turbo model to generate responses to user
messages. The bot is built using the Pycord library and features a simple interactive menu with buttons.

main.py:
1. Import necessary libraries and modules, including Discord, OpenAI, asyncio, functools, dotenv, and commands from the discord.ext module. Also, import the ButtonView class from the views module.
2. Load environment variables from the .env file.
3. Set the bot's token and OpenAI API key from the environment variables.
4. Configure the bot's intents, allowing it to handle typing, messages, and message content events.
5. Create a bot instance with a command prefix '!' and the configured intents.
6. Define an asynchronous function, create_chat_completion(), that takes a prompt as an input and generates a response from the GPT-3.5-turbo model using the OpenAI API.
7. Define an on_ready event handler that prints the bot's username when it logs in.
8. Create a command called opt that sends a message with the ButtonView, allowing the user to select an option from the interactive menu.
9. Define an on_message event handler that processes commands, checks for mentions of the bot, and generates a response using the create_chat_completion() function. The response is then sent back to the user in the same channel.
10. Run the bot with the provided token.

views.py:
1. Import the discord library.
2. Define a ButtonView class that inherits from discord.ui.View.
3. Create three buttons within the ButtonView class with different labels and styles.
4. Define asynchronous button event handlers for each button that send a message with the user's choice when the button is clicked.
```

## Changelog

### v0.0.4

- Change library to PyCord
- Added base button support by "!opt" command

### v0.0.3

- Added sarcastic personality
- Add async support for OpenAI requests with exception if request failed

### v0.0.2

- Added support of GPT-3.5-TURBO model
- Added name support

### v0.0.1

- Created basic functionality of the chat application on GPT-2 model
