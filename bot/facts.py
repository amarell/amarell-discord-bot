import requests
from discord.ext import commands
import json

class Facts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fun_fact(self, ctx):
        """Responds with a random fun fact"""
        response = requests.get("https://asli-fun-fact-api.herokuapp.com/")

        fact_json = json.dumps(response.json(), sort_keys=True, indent=4)
        fact = json.loads(fact_json)

        await ctx.send("Here is a random fact: \n")
        await ctx.send("```" + fact['data']['fact'] + "```")



def setup(bot):
    bot.add_cog(Facts(bot))