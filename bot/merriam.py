import requests
from discord.ext import commands
from dotenv import load_dotenv
import os
import json

load_dotenv()


class Merriam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def define(self, ctx, word: str = None):
        """Defines a given word from Merriam-Webster!"""
        if word is None:
            await ctx.send("You need to provide a word to define!")
        else:
            response = requests.get(
                'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'
                + word +
                '?key='+os.environ['merriam-api-key'])

            definition_json = json.dumps(
                response.json(), sort_keys=True, indent=4)
            definition = json.loads(definition_json)

            list_of_definitions = definition[0]["shortdef"]
            defs = ""

            for x in range(len(list_of_definitions)):
                defs = defs + str(x+1) + ". " + list_of_definitions[x] + ",\n"

            await ctx.send("These are the definitinos of the given word:\n")
            await ctx.send("```"+defs[:-2]+"```")


def setup(bot):
    bot.add_cog(Merriam(bot))
