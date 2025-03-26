import os
import discord
from discord.ext import commands
from discord import app_commands
import json
import re

DEV_GUILD = discord.Object(id=int(os.getenv("DEV_GUILD_ID"))) 

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.load_banned_words()

    def load_banned_words(self):
        try:
            with open('bannedWords.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.banned_words = data.get("banned_words", [])
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading banned words: {e}")
            self.banned_words = []
    
    def save_banned_words(self):
        with open("bannedWords.json", "w", encoding="utf-8") as f:
            json.dump({"banned_words": self.banned_words}, f, indent=4)
    
    ## EVENTS ---------------------------------------------------------------------------------------------
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        
        text = message.content.lower()
        if any(re.search(rf"\b{re.escape(word)}\b", text) for word in self.banned_words):
            await message.delete()
            await message.channel.send(f"🚨 That's a naughty word! {message.author.mention}!")
            return  
    
    ## SLASH COMMANDS ---------------------------------------------------------------------------------------------
    
    @app_commands.command(name="add_banned_word", description="Add a banned word to the list")
    @app_commands.guilds(DEV_GUILD)
    async def add_banned_word(self, interaction: discord.Interaction, word: str):
        if word in self.banned_words:
            await interaction.response.send_message(f"🤔 `{word}` is already a banned word!", ephemeral=True)
            return
        
        self.banned_words.append(word)
        self.save_banned_words()
        await interaction.response.send_message(f"✅ Added `{word}` to the banned words list!")

    @app_commands.command(name="remove_banned_word", description="Remove a banned word from the list")
    @app_commands.guilds(DEV_GUILD)
    async def remove_banned_word(self, interaction: discord.Interaction, word: str):
        if word not in self.banned_words:
            await interaction.response.send_message(f"🤔 `{word}` is not in the banned words list!", ephemeral=True)
            return

        self.banned_words.remove(word)
        self.save_banned_words()
        await interaction.response.send_message(f"✅ Removed `{word}` from the banned words list!")

    @app_commands.command(name="list_banned_words", description="List all banned words")
    @app_commands.guilds(DEV_GUILD)
    async def list_banned_words(self, interaction: discord.Interaction):
        if not self.banned_words:
            await interaction.response.send_message("🤔 There are no banned words!", ephemeral=True)
            return

        banned_words_str = "\n".join(self.banned_words)
        await interaction.response.send_message(f"📜 **Banned words:**\n{banned_words_str}")

    @app_commands.command(name="clear_banned_words", description="Clear all banned words")
    @app_commands.guilds(DEV_GUILD)
    async def clear_banned_words(self, interaction: discord.Interaction):
        if not self.banned_words:
            await interaction.response.send_message("🤔 There are no banned words to clear!", ephemeral=True)
            return

        self.banned_words.clear()
        self.save_banned_words()
        await interaction.response.send_message("✅ Cleared all banned words!")
        

# Add the cog
async def setup(bot):
    await bot.add_cog(Moderation(bot))