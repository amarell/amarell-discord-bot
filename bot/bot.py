# This example requires the 'members' privileged intents

import datetime
import discord
from discord.ext import commands
import random
import os


description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

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
    
bot.run(os.environ["discord-api-token"])