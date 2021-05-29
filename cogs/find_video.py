# Main Imports
import discord
from youtubesearchpython import VideosSearch

# Discord Imports
from discord.ext import commands

# GLOBALS
STATEMENT = "Craig'n'Dave AQA A'Level "
URL = "https://www.youtube.com/results?search_query="


# Main Program
class FindVideoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=["find_video", "fv"])
    async def find_video_cmd(self, ctx, *, words=None):
        try:
            if words is None:
                return await ctx.send("Please type a topic name or video title to search for.")

            text_to_search = STATEMENT + words

            videoSearch = VideosSearch(text_to_search, limit=1).result()['result'][0]

            embed = discord.Embed(title=videoSearch["title"],
                                  description=videoSearch["accessibility"]["title"],
                                  color=0xff0000,
                                  url=videoSearch["link"])
            embed.set_thumbnail(url=videoSearch["thumbnails"][0]["url"])
            embed.set_author(name=videoSearch["channel"]["name"])
            embed.set_footer(text=videoSearch["duration"])

            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send("Something went wrong, please contact the Admin.")
            print(e)


def setup(bot):
    bot.add_cog(FindVideoCog(bot))
