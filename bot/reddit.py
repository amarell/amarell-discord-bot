from discord.ext import commands
import discord
import random
import asyncpraw
import datetime

reddit = asyncpraw.Reddit(
    client_id="zRz7g1nCkdYbL8954UCong",
    client_secret="gqbxdWjbVqfnzmz0Ovyc0vGiaoJ8gA",
    user_agent="discord:com.amarellBot:v1.0.0 (by /u/Snoopy34)",
)

class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wallpaper(self, ctx):
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

        
    @commands.command()
    async def nature_wallpaper(self, ctx):
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

    @commands.command()
    async def testcommand(self, ctx):
        """just testing"""
        await ctx.send("just testing! how you doing? ")

def setup(bot):
    bot.add_cog(Reddit(bot))



