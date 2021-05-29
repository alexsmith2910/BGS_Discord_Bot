# Main Imports

# Discord Imports
from discord.ext import commands


# Main Program
class ClearCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=["cls"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)


def setup(bot):
    bot.add_cog(ClearCog(bot))
