# This example requires the 'members' privileged intents

import datetime
import discord
from discord.ext import commands
import vars
import asyncpraw
import random
import os

reddit = asyncpraw.Reddit(
    client_id="zRz7g1nCkdYbL8954UCong",
    client_secret="gqbxdWjbVqfnzmz0Ovyc0vGiaoJ8gA",
    user_agent="discord:com.amarellBot:v1.0.0 (by /u/Snoopy34)",
)





description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents().all()

# Initializing the bot
bot = commands.Bot(command_prefix='-', description=description, intents=intents)
# Here we are going to add all the extensions (external .py files)
bot.load_extension('bot_commands')
bot.load_extension('wiki')
bot.reload_extension('wiki')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def wallpaper(ctx):
    wallpapers = []
    subreddit = await reddit.subreddit("wallpapers", fetch=True)

    async for submission in subreddit.top(limit=100):
        wallpapers.append(submission)

    random_wallpaper = random.choice(wallpapers)

    embed = discord.Embed(
            title="Wallpapers from r/wallpapers",
            colour=discord.Colour.orange(), 
            url="https://www.reddit.com" + random_wallpaper.permalink, 
            timestamp=datetime.datetime.utcfromtimestamp(random_wallpaper.created_utc)
        )

    embed.set_image(url=random_wallpaper.url)
    embed.set_footer(
            text="Wallpaper posted on reddit on",
            icon_url="https://www.redditinc.com/assets/images/site/reddit-logo.png"
        )

    await ctx.send(content="Here is your random wallpaper:", embed=embed)

@bot.command()
async def nature_wallpaper(ctx):
    wallpapers = []
    subreddit = await reddit.subreddit("earthporn", fetch=True)

    async for submission in subreddit.top(limit=100):
        wallpapers.append(submission)

    random_wallpaper = random.choice(wallpapers)

    embed = discord.Embed(
            title="Wallpapers from r/wallpapers",
            colour=discord.Colour.orange(), 
            url="https://www.reddit.com" + random_wallpaper.permalink, 
            timestamp=datetime.datetime.utcfromtimestamp(random_wallpaper.created_utc)
        )

    embed.set_image(url=random_wallpaper.url)
    embed.set_footer(
            text="Wallpaper posted on reddit on",
            icon_url="https://www.redditinc.com/assets/images/site/reddit-logo.png"
        )

    await ctx.send(content="Here is your random wallpaper:", embed=embed)
    
bot.run(os.environ["discord-api-token"])