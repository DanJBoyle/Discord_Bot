import discord
from discord.ext import commands
from discord import app_commands
import json
import re

# Set up Discord bot
TOKEN = "MTM1MzQyNTA5ODExNTEyMTE1Mw.GP3vJ0.mI1BfPFOp_Em_F_O6Ae8ywacwlBKa4T6MJD3W4"

# Enable intents
intents = discord.Intents.default()
intents.messages = True  # To read messages
intents.message_content = True  # To access message content

client = commands.Bot(command_prefix='!', intents=intents)

# Load banned words from JSON
try:
    with open('bannedWords.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        banned_words = data.get("banned_words", [])
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error loading banned words: {e}")
    banned_words = []

## EVENTS ---------------------------------------------------------------------------------------------

@client.event
async def on_ready():
    for guild in client.guilds:
        for channel in guild.text_channels:
            await channel.send("Hello! I'm here to moderate your messages! 😇")


@client.event
async def on_message(message):
    
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

## COMMANDS ---------------------------------------------------------------------------------------------

@client.command(name = "add_banned_word", 
                description = "Add a banned word to the list")
@commands.has_permissions(administrator=True)
async def add_banned_word(ctx, word: str):
    if word in banned_words:
        await ctx.send(f"🤔 {word} is already a banned word!")
        return

    banned_words.append(word)
    with open('bannedWords.json', 'w', encoding='utf-8') as f:
        json.dump({"banned_words": banned_words}, f, indent=4)
    await ctx.send(f"✅ Added {word} to the banned words list!")

# Run the bot
client.run(TOKEN)