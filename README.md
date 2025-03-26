# Chat Moderating Discord Bot

## Discription
Welcome to our **Chat Moderating Discord Bot!** This guide provides step-by-step instructions to set up, configure, and run the bot on your own Discord server for testing and development.

## Features
- Automatic message moderation
- Customizable moderation settings
- User management commands
- Logging and reporting functionality

## Setup Guide

### Prerequisites

Before you begin, make sure you have:
- A Discord account and administrative access to a Discord server.
- Python (version 3.6 or newer) installed on your system.
- Git installed for cloning the repository.
- An IDE for Python development

### Step 1: Clone Repository
Clone the repository to your local machine:
```bash
git clone [URL of the repository]
cd [repository name]
```

### Step 2: Create Discord Bot Account
1. Navigate to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on **New Application**, name your application, and click **Create**.
3. In the application settings, navigate to the **Bot** tab and click **Add Bot**.
4. Click **Yes, do it!** to confirm.
5. Copy the **TOKEN** and store it safely for later use.
6. Enable **Privileged Gateway Intents** (Presence Intent, Server Members Intent, and Message Content Intent).
7. Click **Save Changes**.

### Step 3: Invite the Bot to Your Server
1. Go to the **OAuth2** tab and select **URL Generator**.
2. Under **Scopes**, check the box for **bot**.
3. Under **Bot Permissions**, select **Administrator** (or customize as needed).
4. Copy the generated URL, paste it into your web browser, and select your server to invite the bot.


### Step 4: Create a Virtual Environment
Navigate to your project directory and run:
```bash
python -m venv env
```

### Step 5: Activate the Virtual Environment
Tto activate your **Virtual Environment** run:
```bash
venv_name\Scripts\activate
```
Your prompt should now show <code>(env)</code>, indicating the virtual environment is active.

To deactivate your **Virtual Environment** run:
```bash
deactivate
```

### Step 6: Install Dependencies
Install all required dependencies:
```bash
pip install -r requirements.txt
```

## Step 7: Configure Bot Token
Create a **.env** file in the project directory:
```bash
touch .env
```
Add your bot token to the **Environment File**:
```bash
echo "token" > .env
```

### Step 8: Start the Bot
Run the main script to launch the bot:
```bash
python main.py
```
To stop the bot, press <code>Ctrl + C</code> in the terminal.

## Troubleshooting
If the bot does not respond:
1. Verify that the bot has the correct permissions on your Discord server.
2. Check that all dependencies are installed correctly.
3. Ensure your bot token is correct and has not expired (reset it in the Developer Portal if needed).
4. Look for errors in the console output and debug accordingly.

## Contributing
1. Fork the repository.
2. Create a new branch:
```bash
git checkout -b feature-name
```
3. Commit changes:
```bash
git commit -m 'Add new feature'
```
4. Push to the branch:
```bash
git push origin feature-name
```
5. Open a pull request.

## Licence
This project is licensed under the MIT License.
