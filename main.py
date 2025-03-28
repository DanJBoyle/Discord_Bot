import discord
from discord.ext import commands
from dotenv import load_dotenv

import asyncio
import os
from os import listdir

## SETUP -----------------------------------------------------------------------------------------------

# Load environment variables from .env file
load_dotenv()

TOKEN = os.getenv("TOKEN")
DEV_GUILD = discord.Object(id=int(os.getenv("DEV_GUILD_ID"))) 

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

## FUNCTIONS ------------------------------------------------------------------------------------------

async def force_sync():
    try:
        synced = await client.tree.sync(guild=DEV_GUILD)
        print(f"Synced {len(synced)} commands to guild {DEV_GUILD.id}")
    except Exception as e:
        print(f"Error syncing commands: {e}")

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

    await force_sync()

asyncio.run(main())