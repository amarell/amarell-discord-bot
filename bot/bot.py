# This example requires the 'members' privileged intents

import discord
from discord.ext import commands
import vars


description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents().all()

bot = commands.Bot(command_prefix='-', description=description, intents=intents)
bot.load_extension('bot_commands')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(vars.token)