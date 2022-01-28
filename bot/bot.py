# This example requires the 'members' privileged intents

import discord
from discord.ext import commands
import random


description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents().all()

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, left: int, right:int):
    """Adds two numbers together!"""
    await ctx.send(left + right)

@bot.command()
async def subtract(ctx, left: int, right: int):
    """Subtracts two numbers!"""
    await ctx.send(left-right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command(description="Repeats content n times")
async def repeat(ctx, times: int, content: str):
    for x in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send('{0} joined on {0.joined_at}'.format(member))


@bot.command()
async def check_spotify_activity(ctx, *, member: discord.Member):
    """Checks user's current Spotify activity!"""
    listening = member.activities

    if listening == None:
        await ctx.send("The user is currently not listening to anything!")
    else:
        await ctx.send("{0.name} is listening to: {1[0].title} by {1[0].artist}".format(member, listening))

bot.run('Nzk3NjA5MTc0NjQ0NDI0NzE0.X_o9bg.dX4_nkNYem45L01kdwQgm8Gqdow')