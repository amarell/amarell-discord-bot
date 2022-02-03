from discord.ext import commands
import discord
import random
import asyncpraw
import datetime
import os

reddit = asyncpraw.Reddit(
    client_id=os.environ["reddit-client-id"],
    client_secret=os.environ["reddit-client-secret"],
    user_agent=os.environ["reddit-user-agent"],
)

class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wallpaper(self, ctx):
        """Generates a random wallpaper from r/wallpapers"""
        wallpapers = []
        subreddit = await reddit.subreddit("wallpapers", fetch=True)

        async for submission in subreddit.hot(limit=15):
            wallpapers.append(submission)

        random_wallpaper = random.choice(wallpapers)

        embed = discord.Embed(
                title=random_wallpaper.title,
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
        """Generates a random wallpaper from subreddit r/earthporn"""
        wallpapers = []
        subreddit = await reddit.subreddit("earthporn", fetch=True)

        async for submission in subreddit.hot(limit=15):
            wallpapers.append(submission)

        random_wallpaper = random.choice(wallpapers)

        embed = discord.Embed(
                title=random_wallpaper.title,
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
    async def art(self, ctx):
        """Displays random art posts from reddit!"""
        artworks = []

        subreddit = await reddit.subreddit("art")

        async for submission in subreddit.hot(limit=100):
            artworks.append(submission)

        random_artwork = random.choice(artworks)

        embed = discord.Embed(
                title=random_artwork.title,
                colour=discord.Colour.dark_gold(), 
                url="https://www.reddit.com" + random_artwork.permalink, 
                timestamp=datetime.datetime.utcfromtimestamp(random_artwork.created_utc)
            )

        embed.set_image(url=random_artwork.url)
        embed.set_footer(
                text="Artwork posted on reddit on",
                icon_url="https://www.redditinc.com/assets/images/site/reddit-logo.png"
            )

        await ctx.send(
                content="Here is your random artwork from reddit\n" + 
                        "If you like it please consider supporting the artist", 
                embed=embed
            )

    @commands.command()
    async def meme(self, ctx):
        """Displays a fresh meme from reddit"""
        fresh_memes = []

        subreddit = await reddit.subreddit("memes")

        async for submission in subreddit.hot(limit=100):
            fresh_memes.append(submission)

        random_fresh_meme = random.choice(fresh_memes)

        embed = discord.Embed(
                title=random_fresh_meme.title,
                colour=discord.Colour.dark_gold(), 
                url="https://www.reddit.com" + random_fresh_meme.permalink, 
                timestamp=datetime.datetime.utcfromtimestamp(random_fresh_meme.created_utc)
            )

        embed.set_image(url=random_fresh_meme.url)
        embed.set_footer(
                text="Meme posted on reddit on",
                icon_url="https://www.redditinc.com/assets/images/site/reddit-logo.png"
            )

        await ctx.send(
                content="Here is your random meme from reddit\n", 
                embed=embed
            )

    @commands.command()
    async def anarchy(self, ctx):
        """Displays a fresh meme from one of my favorite subreddits r/AnarchyChess"""
        horsey_memes = []

        subreddit = await reddit.subreddit("anarchychess")

        async for submission in subreddit.hot(limit=100):
            horsey_memes.append(submission)

        random_horsey_meme = random.choice(horsey_memes)

        embed = discord.Embed(
                title=random_horsey_meme.title,
                colour=discord.Colour.dark_gold(), 
                url="https://www.reddit.com" + random_horsey_meme.permalink, 
                timestamp=datetime.datetime.utcfromtimestamp(random_horsey_meme.created_utc)
            )

        embed.set_image(url=random_horsey_meme.url)
        embed.set_footer(
                text="Meme posted on reddit on",
                icon_url="https://www.redditinc.com/assets/images/site/reddit-logo.png"
            )

        await ctx.send(
                content="Here is your random meme from Anarchy Chess\n", 
                embed=embed
            )
    
    @commands.command()
    async def whenthe(self, ctx):
        """Displays a fresh meme from one of my favorite subreddits r/whenthe"""
        whenthe_memes = []

        subreddit = await reddit.subreddit("whenthe")

        async for submission in subreddit.hot(limit=100):
            whenthe_memes.append(submission)

        random_whenthe_meme = random.choice(whenthe_memes)

        embed = discord.Embed(
                title=random_whenthe_meme.title,
                colour=discord.Colour.dark_gold(), 
                url="https://www.reddit.com" + random_whenthe_meme.permalink, 
                timestamp=datetime.datetime.utcfromtimestamp(random_whenthe_meme.created_utc)
            )

        embed.set_image(url=random_whenthe_meme.url)
        embed.set_footer(
                text="Meme posted on reddit on",
                icon_url="https://www.redditinc.com/assets/images/site/reddit-logo.png"
            )

        await ctx.send(
                content="Here is your random meme from r/whenthe:\n", 
                embed=embed
            )

    @commands.command()
    async def programmer_meme(self, ctx):
        """Gets a random meme from r/ProgrammerHumour"""
        memes = []
        subreddit = await reddit.subreddit("programmerhumour", fetch=True)

        async for submission in subreddit.hot(limit=15):
            memes.append(submission)

        random_meme = random.choice(memes)

        embed = discord.Embed(
                title=random_meme.title,
                colour=discord.Colour.orange(), 
                url="https://www.reddit.com" + random_meme.permalink, 
                timestamp=datetime.datetime.utcfromtimestamp(random_meme.created_utc)
            )

        embed.set_image(url=random_meme.url)
        embed.set_footer(
                text="Meme posted on reddit on",
                icon_url="https://www.redditinc.com/assets/images/site/reddit-logo.png"
            )

        await ctx.send(content="Here is your meme:", embed=embed)



def setup(bot):
    bot.add_cog(Reddit(bot))



