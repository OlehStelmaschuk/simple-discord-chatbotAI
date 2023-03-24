# Simple ChatGPT-bot for Discord by GPT-4

Simple chat with authorization and registration written on Python with GPT-4 (ChatGPT)

The project was created to analyze the capabilities of ChatGPT and possible ideas for the implementation of this tool in
the future.

## Installation

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

## Changelog

### v0.0.3

- Added sarcastic personality
- Add async support for OpenAI requests with exception if request failed

### v0.0.2

- Added support of GPT-3.5-TURBO model
- Added name support

### v0.0.1

- Created basic functionality of the chat application on GPT-2 model
