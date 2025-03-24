# Discord Bot (Syne) Setup Guide

Welcome to our Discord Bot project! This guide will walk you through the steps needed to set up and run the Discord Bot for testing and development on your own Discord server.

## Prerequisites

Before you begin, make sure you have:
- A Discord account and administrative access to a Discord server.
- Python installed on your computer (version 3.6 or newer).
- Git installed for cloning the repository.
- Visual Studio Code installed, if you prefer using an IDE for Python development.

## Step 1: Clone the Repository

Start by cloning the bot code repository to your local machine:

```bash
git clone [URL of the repository]
cd [repository name]
```

## Step 2: Create a Discord Bot Account

1. Navigate to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on **New Application**, name your application, and click **Create**.
3. In the application settings, go to the **Bot** tab and click **Add Bot**.
4. Confirm the action by clicking **Yes, do it!**.
5. Note down the `TOKEN` for your bot, as you will need this in the bot script.
6. Replace the current `TOKEN` in the moderation_bot.py script.

```bash
TOKEN = 'your_token_here'
```

## Step 3: Install Dependencies
Install the necessary Python packages:

```bash
pip install discord spacy transformers
python -m spacy download en_core_web_sm
```
## Step 4: Invite the Bot to Your Server

1. In the application settings, go to the **OAuth2** tab and select **URL Generator**.
2. Under **Scopes**, check the box for **bot**.
3. Under **Bot Permissions**, select the permissions your bot requires (e.g., Read Messages, Send Messages).
4. Copy the generated URL, paste it into your web browser, and select the server to invite your bot to.

## Step 5: Run the Bot and Verify the Bot Is Running
1. Run the script:
```bash
python moderation_bot.py
```
2. Send a message in your Discord server to test if the bot responds as expected. If set up correctly, the bot should be able to read and respond to messages according to its programming.

## Troubleshooting
If the bot does not respond:

1. Ensure the bot has the correct permissions in your server.
2. Check that all dependencies are installed correctly.
3. Make sure the bot token is correctly placed in the script.
