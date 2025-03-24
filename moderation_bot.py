import discord
import json
import re

# Set up Discord bot
TOKEN = "MTM1MzQyNTA5ODExNTEyMTE1Mw.GP3vJ0.mI1BfPFOp_Em_F_O6Ae8ywacwlBKa4T6MJD3W4"

# Enable intents
intents = discord.Intents.default()
intents.messages = True  # To read messages
intents.message_content = True  # To access message content

client = discord.Client(intents=intents)

# Load banned words from JSON
try:
    with open('bannedWords.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        banned_words = data.get("banned_words", [])
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error loading banned words: {e}")
    banned_words = []

print(f"Banned words: {banned_words}")

@client.event
async def on_ready():
    channel = discord.utils.get(client.get_all_channels(), name="general")
    await channel.send("Hello! I'm here to moderate your messages! 😇")


@client.event
async def on_message(message):
    print(f"--- Debugging on_message ---")
    
    # Check if the message is from the bot itself
    if message.author == client.user:
        return

    text = message.content.lower()

    # Check for banned words
    if any(re.search(rf"\b{re.escape(word)}\b", text) for word in banned_words):
        print(f"Detected banned word in message: {text}")
        await message.delete()
        await message.channel.send(f"🚨 That's a naughty word! {message.author.mention}!")
        return 

# Run the bot
client.run(TOKEN)