
import discord
from discord.ext import commands
import os


description = '''
Amarell is a multipurpose bot designed for fun by @amar#9535
'''

intents = discord.Intents().all()

# Initializing the bot
bot = commands.Bot(command_prefix='-', description=description, intents=intents)
# Here we are going to add all the extensions (external .py files)
bot.load_extension('bot_commands')
bot.load_extension('wiki')
bot.load_extension('reddit')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def testcommand(ctx):
    await ctx.send("Hello there dumbass!")
    
bot.run(os.environ["discord-api-token"])