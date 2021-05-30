# Main Imports
import json

# Discord Imports
import discord
from discord.ext import commands


# Main Program
class QuestionSystemCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=["questions"])
    @commands.has_permissions(administrator=True)
    async def get_questions(self, ctx):
        embed = discord.Embed(title="Questions", color=0xff0000)

        with open("./questions/unanswered.json") as f:
            data = json.load(f)  # this is a list
            embed.description = f"There are {len(data)} entries in the unanswered questions."
            count = 0
            for question in data:
                count += 1
                embed.add_field(name=f"Question {count}, asked by {question['author']}",
                                value=question['question'],
                                inline=False)
        f.close()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(QuestionSystemCog(bot))
