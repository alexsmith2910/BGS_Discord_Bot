# Main Imports

# Discord Imports
from discord.ext import commands


# Main Program
class QuestionAskCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=["ask"])
    async def ask(self, ctx, *, words):
        await ctx.channel.purge()


def setup(bot):
    bot.add_cog(QuestionAskCog(bot))
