# Main Imports
import json
import time
from os import listdir
from os.path import isfile, join

# Discord Imports
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound

# Importing config.json
with open("config.json") as config_file:
    data = json.load(config_file)
    config_file.close()

# GLOBALS
TOKEN = data["token"]
COMMAND_PREFIX = data["prefix"]
USER_ID = data["alexander291002"]["id"]
COGS_PATH = "./cogs"

# Main Program
client = commands.Bot(command_prefix=COMMAND_PREFIX, activity=discord.Activity(type=discord.ActivityType.watching,
                                                                               name="Craig'n'Dave"))

client.remove_command('help')


@client.event
async def on_ready():
    print("BGS CS Helper is ready.")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error


@commands.command(pass_context=True, aliases=["help"])
async def help_cmd(ctx):
    embed = discord.Embed(title="How to use the BGS CS Helper Bot",
                          description="This is a help message which will display all the commands and how to use"
                                      "them.",
                          color=0xff0000)
    user = client.get_user(USER_ID)
    embed.set_author(name="alexander291002", icon_url=user.avatar_url)

    embed.add_field(name="Find Video (find_video, fv)",
                    value="This will return a video relating to the keywords given."
                          " It passes in Craig'n'Dave and AQA A'Level as a parameter.\n"
                          "```!fv big o notation```")

    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(administrator=True)
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000, 2)}ms")


@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, *, cog_name=None):
    if cog_name is None:
        return await ctx.send("You need to use type a Cog's name.")

    try:
        client.load_extension(f"cogs.{cog_name}")
        print(f"Cog: {cog_name} loaded.")
        return await ctx.send(f"Cog: {cog_name} loaded.")
    except Exception as error:
        print(error)
        return await ctx.send(f"Failed to load Cog: {cog_name} (Possibly doesn't exist)")


@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, *, cog_name=None):
    if cog_name is None:
        return await ctx.send("You need to use type a Cog's name.")

    try:
        client.unload_extension(f"cogs.{cog_name}")
        print(f"Cog: {cog_name} unloaded.")
        return await ctx.send(f"Cog: {cog_name} unloaded.")
    except Exception as error:
        print(error)
        return await ctx.send(f"Failed to unload Cog: {cog_name} (Possibly doesn't exist)")


@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, *, cog_name=None):
    if cog_name is None:
        return await ctx.send("You need to use type a Cog's name.")

    try:
        client.unload_extension(f"cogs.{cog_name}")
        await ctx.send(f"Cog: {cog_name} reloading...")
        print(f"Cog: {cog_name} reloading...")
        time.sleep(3)
        print(f"Cog: {cog_name} reloaded.")
        client.load_extension(f"cogs.{cog_name}")
        await ctx.send(f"Cog: {cog_name} reloaded.")
    except Exception as error:
        print(error)
        return await ctx.send(f"Failed to reload Cog: {cog_name} (Possibly doesn't exist)")


@client.command(aliases=["quit"])
@commands.has_permissions(administrator=True)
async def close(ctx):
    await client.close()
    print("BGS CS Helper has stopped via command.")


cogs = [f for f in listdir(COGS_PATH) if isfile(join(COGS_PATH, f))]
for cog in cogs:
    cog_string = f"cogs.{cog[:-3]}"
    try:
        client.load_extension(cog_string)
        print(f"Loaded {cog_string} ...")
    except Exception as e:
        print(f"Could not load {cog_string} ...\n"
              f"\tException: {e}")

client.run(TOKEN)
