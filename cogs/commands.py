import os
import discord
from discord.ext import commands
from discord import app_commands

DEV_GUILD = discord.Object(id=int(os.getenv("DEV_GUILD_ID"))) 

class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="display_github",
                      description="Display the GitHub repository for this bot")
    @app_commands.guilds(DEV_GUILD)
    async def display_github(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="GitHub Repository",
            url="https://github.com/DanJBoyle/Discord_Bot",
            description="Check out the code for this bot on GitHub!",
            color=0x5865F2
        )
        embed.set_thumbnail(url="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png")
        await interaction.response.send_message(embed=embed)

# Add the cog
async def setup(bot):
    await bot.add_cog(GeneralCommands(bot))