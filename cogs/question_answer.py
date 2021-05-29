# Main Imports

# Discord Imports
from discord.ext import commands


# Main Program
class QuestionAnswerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=["ans"])
    @commands.has_permissions(manage_messages=True)
    async def answer(self, ctx, q_id, *, words):
        await ctx.channel.purge()


def setup(bot):
    bot.add_cog(QuestionAnswerCog(bot))
