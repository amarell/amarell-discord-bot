import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()


description = '''
Amarell is a multipurpose bot designed for fun by @amar#9535
'''

intents = discord.Intents().all()

# Initializing the bot
bot = commands.Bot(command_prefix='-',
                   description=description, intents=intents)
# Loading all the extensions (external .py files)
bot.load_extension('bot_commands')
bot.load_extension('wiki')
bot.load_extension('reddit')
bot.load_extension('merriam')
bot.load_extension('games')
bot.load_extension('facts')
bot.load_extension('trivia')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


bot.run(os.environ["discord-api-token"])
