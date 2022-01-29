# This example requires the 'members' privileged intents

import discord
import requests
import pprint
import json
from discord.ext import commands
import random
import vars
import random
import string


description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents().all()

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

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
    try:
        if listening == None:
            await ctx.send("The user is currently not listening to anything!")
        else:
            new_embed = discord.Embed()
            message = member.display_name + " is listening to " + listening[0].title + " by " + listening[0].artist
            
            artists = listening[0].artist.split("; ")

            response = requests.get("https://api.lyrics.ovh/v1/" + artists[0] + "/" + listening[0].title)
            lyrics_json = json.dumps(response.json(), sort_keys=True, indent=4)
            lyrics = json.loads(lyrics_json)

            new_embed.set_image(url = listening[0].album_cover_url)
            new_embed.add_field(name="Activity", value=message)

            await ctx.send(embed=new_embed)

            if "error" in lyrics.keys():
                await ctx.send("Error trying to find lyrics!")
            else:
                await ctx.send("Lyrics:\n```"+lyrics["lyrics"] + "```")
    except Exception as err:
        await ctx.send(err)
@bot.command()
async def generate_password(ctx, length: int = None):
    try:
        if(length is None):
            await ctx.send("The proper usage is: \n```generate_password <int>```")
        elif(isinstance(length, int)):
            chars = string.ascii_letters
            digits = string.digits
            punct = string.punctuation

            all = chars + digits + punct

            temp = random.sample(all, length)
            password = "".join(temp)

            await ctx.send("The generated password is:\n" + "```" + password + "```")
        else:
            await ctx.send("The proper usage is: \n```generate_password <int>```")
    except Exception as err:
        await ctx.send(err)


bot.run(vars.token)