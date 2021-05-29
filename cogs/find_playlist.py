# Main Imports
import discord
from youtubesearchpython import PlaylistsSearch

# Discord Imports
from discord.ext import commands

# GLOBALS
STATEMENT = "Craig'n'Dave AQA A'Level "
URL = "https://www.youtube.com/results?search_query="


# Main Program
class FindPlaylistCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=["find_playlist", "fp"])
    async def find_playlist_cmd(self, ctx, *, words=None):
        try:
            if words is None:
                return await ctx.send("Please type a topic name or playlist title to search for.")

            text_to_search = STATEMENT + words

            playlistSearch = PlaylistsSearch(text_to_search, limit=1).result()['result'][0]

            embed = discord.Embed(title=playlistSearch["title"],
                                  color=0xff0000,
                                  url=playlistSearch["link"])
            embed.set_thumbnail(url=playlistSearch["thumbnails"][0]["url"])
            embed.set_author(name=playlistSearch["channel"]["name"])
            embed.set_footer(text="Videos: " + playlistSearch["videoCount"])

            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send("Something went wrong, please contact the Admin.")
            print(e)


def setup(bot):
    bot.add_cog(FindPlaylistCog(bot))
