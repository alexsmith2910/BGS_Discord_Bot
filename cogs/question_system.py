# Main Imports

# Discord Imports
from discord.ext import commands


# Main Program
class QuestionSystemCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=["questions"])
    @commands.has_permissions(administrator=True)
    async def get_questions(self, ctx):
        await ctx.channel.purge(limit=amount)


def setup(bot):
    bot.add_cog(QuestionSystemCog(bot))
