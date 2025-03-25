import discord
from discord.ext import commands
from discord import app_commands
import json
import re

# Set up Discord bot
with open('token.txt', 'r') as file:
    TOKEN = file.read()

DEV_GUILD_ID = discord.Object(id = 1044032993666285619);  # Your guild ID

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
    #Send a "Hello!" message to all text channels that the bot is in
    for guild in client.guilds:
        for channel in guild.text_channels:
            await channel.send("Hello! I'm here to moderate your messages! 😇")

    # Force command sync
    try:
        synced = await client.tree.sync(guild=DEV_GUILD_ID)
        print(f"Synced {len(synced)} commands to guild {DEV_GUILD_ID.id}")
    except Exception as e:
        print(f"Error syncing commands: {e}")


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

@client.tree.command(name = "add_banned_word", 
                     description = "Add a banned word to the list",
                     guild = DEV_GUILD_ID)
async def add_banned_word(interaction: discord.Interaction, word: str):
    if word in banned_words:
        await interaction.response.send_message(f"🤔 {word} is already a banned word!")
        return

    banned_words.append(word)
    with open('bannedWords.json', 'w', encoding='utf-8') as f:
        json.dump({"banned_words": banned_words}, f, indent=4)
    await interaction.response.send_message(f"✅ Added {word} to the banned words list!")

@client.tree.command(name = "remove_banned_word",
                     description = "Remove a banned word from the list",
                     guild = DEV_GUILD_ID)
async def remove_banned_word(interaction: discord.Interaction, word: str):
    if word not in banned_words:
        await interaction.response.send_message(f"🤔 {word} is not a banned word!")
        return
    
    banned_words.remove(word)
    with open('bannedWords.json', 'w', encoding='utf-8') as f:
        json.dump({"banned_words": banned_words}, f, indent=4)
    await interaction.response.send_message(f"✅ Removed {word} from the banned words list!")

@client.tree.command(name = "list_banned_words",
                     description = "List all banned words",
                     guild = DEV_GUILD_ID)
async def list_banned_words(interaction: discord.Interaction):
    if not banned_words:
        await interaction.response.send_message("🤔 There are no banned words!")
        return
    
    banned_words_str = "\n".join(banned_words)
    await interaction.response.send_message(f"📜 Banned words:\n{banned_words_str}")
    
@client.tree.command(name = "clear_banned_words",
                     description = "Clear all banned words",
                     guild = DEV_GUILD_ID)
async def clear_banned_words(interaction: discord.Interaction):
    if not banned_words:
        await interaction.response.send_message("🤔 There are no banned words to clear!")
        return
    
    banned_words.clear()
    with open('bannedWords.json', 'w', encoding='utf-8') as f:
        json.dump({"banned_words": banned_words}, f, indent=4)
    await interaction.response.send_message("✅ Cleared all banned words!")


# Run the bot
client.run(TOKEN)