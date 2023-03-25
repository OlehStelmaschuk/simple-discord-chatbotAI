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
Title: Technical Specification for a Discord Chatbot with OpenAI API Integration

Objective: Develop a Discord chatbot that interacts with users using OpenAI API, allowing users to have conversations with the AI model and manage the chat history.

**Functional Requirements:**

1. Integration with OpenAI API:
   1.1. Support for GPT-3 and GPT-3.5-turbo models.
   1.2. Use OpenAI API tokens for authentication.
   1.3. Allow changing the AI model at runtime.

2. Discord bot functionality:
   2.1. Respond to user messages when the bot is mentioned or when a specific command is used.
   2.2. Support for basic user commands:
        2.2.1. "!gen": Start a conversation with the AI model.
        2.2.2. "!clear": Clear the user's message history.
   2.3. Support for administrator commands:
        2.3.1. "!changemodel": Change the AI model being used by the bot.
        2.3.2. "!clearall": Clear the message history for all users.

3. Chat history management:
   3.1. Store and retrieve user chat history from a SQLite database.
   3.2. Automatically clear the chat history for a user when requested.
   3.3. Clear chat history for all users when requested by an administrator.

4. User interface:
   4.1. Use Discord's button and view components to create interactive dialogs for changing the AI model and clearing chat history.

**Non-Functional Requirements:**

1. Asynchronous programming using Python's asyncio library to avoid blocking the bot during API calls.
2. Error handling for missing permissions and other issues during command execution.
3. Use of environment variables or database storage for API tokens.

**Technologies and Libraries:**

1. Python 3
2. Pycord (Discord API library)
3. OpenAI Python library
4. SQLite3
5. dotenv

**Deliverables:**

1. Source code for the Discord bot:
   1.1. main.py
   1.2. model_db.py
   1.3. views.py
   1.4. models.py
2. SQLite database schema for storing chat history and configuration data.
3. Detailed comments and documentation within the code.
4. A requirements.txt file specifying the necessary Python libraries.
```

## Changelog

### v0.0.5b

- Minor bugfixes

### v0.0.5a

- Added `!clearall` command for clear all user history in database
- After using the commands `!changemodel` and `!clearall`, the buttons go into the inactive state, thus prohibiting
  their reuse
- Added argument `-cleartoken` to delete API tokens from database. Usage: `chatbot.exe -cleartoken`

### v0.0.5

- Added favicon support
- Added saving user history. The user can clear his history with the command `!clear`

### v0.0.4b

- Added SQLite support for storing data about the current model instead of storing data in a file (config.db)
- Added support for saving token in SQLite database on first launch
- Added a check to see if the user is a server administrator when trying to change ChatGPT models

### v0.0.4a

- Added command `!changemodel` for changing OpenAI model
- Added "text-davinci-003" (more quickly but more inaccurate than GPT-3.5-TURBO) model support
- Moved model files to models.py

### v0.0.4

- Change library to PyCord
- Added base button support

### v0.0.3

- Added sarcastic personality
- Add async support for OpenAI requests with exception if request failed

### v0.0.2

- Added support of GPT-3.5-TURBO model
- Added name support

### v0.0.1

- Created basic functionality of the chat application on GPT-2 model
