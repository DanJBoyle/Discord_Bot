import os
import discord
from discord.ext import commands
import json
import re
import asyncio
from os import listdir
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up Discord bot
TOKEN = os.getenv("TOKEN")
DEV_GUILD = int(os.getenv("DEV_GUILD_ID"))

# Enable intents
intents = discord.Intents.default()
intents.message_content = True  # To access message content

client = commands.Bot(command_prefix='!', intents=intents)

async def load_cogs():
    for cog in listdir('./cogs'):
        if cog.endswith('.py') == True:
            await client.load_extension(f'cogs.{cog[:-3]}')

async def main():
    async with client:
        await load_cogs()
        await client.start(TOKEN)

## EVENTS ---------------------------------------------------------------------------------------------

@client.event
async def on_ready():
    #Send a "Hello!" message to all text channels that the bot is in
    for guild in client.guilds:
        for channel in guild.text_channels:
            await channel.send("Hello! I'm here to moderate your messages! 😇")

    # Force command sync
    try:
        synced = await client.tree.sync(guild=DEV_GUILD)
        print(f"Synced {len(synced)} commands to guild {DEV_GUILD.id}")
    except Exception as e:
        print(f"Error syncing commands: {e}")

asyncio.run(main())