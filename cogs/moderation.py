import discord
from discord.ext import commands
import json
import re

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
        data = {"banned_words": self.banned_words}
        with open('bannedWords.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    
    def save_banned_words(self):
        with open("data/bannedWords.json", "w", encoding="utf-8") as f:
            json.dump({"banned_words": self.banned_words}, f, indent=4)
    
    ## COMMANDS ---------------------------------------------------------------------------------------------
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        
        text = message.content.lower()
        if any(re.search(rf"\b{re.escape(word)}\b", text) for word in self.banned_words):
            await message.delete()
            await message.channel.send(f"🚨 That's a naughty word! {message.author.mention}!")
            return  
    
    @commands.command(name="add_banned_word")
    async def add_banned_word(self, ctx, word: str):
        if word in self.banned_words:
            await ctx.send(f"🤔 `{word}` is already banned!")
            return

        self.banned_words.append(word)
        self.save_banned_words()
        await ctx.send(f"✅ Added `{word}` to the banned words list!")

    @commands.command(name="remove_banned_word")
    async def remove_banned_word(self, ctx, word: str):
        if word not in self.banned_words:
            await ctx.send(f"🤔 `{word}` is not in the banned list!")
            return
        
        self.banned_words.remove(word)
        self.save_banned_words()
        await ctx.send(f"✅ Removed `{word}` from the banned words list!")

    @commands.command(name="list_banned_words")
    async def list_banned_words(self, ctx):
        if not self.banned_words:
            await ctx.send("🤔 No banned words yet!")
            return
        
        banned_words_str = "\n".join(self.banned_words)
        await ctx.send(f"📜 **Banned words:**\n{banned_words_str}")

    @commands.command(name="clear_banned_words")
    async def clear_banned_words(self, ctx):
        self.banned_words.clear()
        self.save_banned_words()
        await ctx.send("✅ Cleared all banned words!")
        

# Add the cog
async def setup(bot):
    await bot.add_cog(Moderation(bot))