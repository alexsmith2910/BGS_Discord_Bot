# Main Imports
import json

# Discord Imports
import discord
from discord.ext import commands


# Main Program
class QuestionAskCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=["ask"])
    async def ask_question(self, ctx, *, words):

        try:
            with open("./questions/unanswered.json") as f:
                data = json.load(f)
                data.update({"question": words, "author": ctx.author.name})
                f.seek(0)
                json.dump(data, f)
            f.close()
        except Exception as e:
            print(e)
            return await ctx.send("Something went wrong, please contact the Admin.")

        embed = discord.Embed(title="Question Asked",
                              description=words,
                              color=0xff0000)

        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_author(name=ctx.author)
        embed.set_footer(text="Your message will be answered as soon as its seen.")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(QuestionAskCog(bot))
