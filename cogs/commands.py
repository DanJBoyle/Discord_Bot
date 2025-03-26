import discord
from discord.ext import commands



class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(name="display_github")
    async def display_github(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="GitHub Repository",
            url="https://github.com/DanJBoyle/Discord_Bot",
            description="Check out the code for this bot on GitHub!",
            color=0x5865F2
        )
        embed.set_thumbnail(url="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png")
        await interaction.response.send(embed=embed)

# Add the cog
async def setup(bot):
    await bot.add_cog(GeneralCommands(bot))