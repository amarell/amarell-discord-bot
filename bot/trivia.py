from numpy import diff
import requests
from discord.ext import commands
import json
import discord

class Trivia(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["ts"])
    async def trivia_start(self, ctx, difficulty: str = None):
        """Responds with a trivia question"""
        
        if(difficulty is None) :
            await ctx.send("You have to provide the difficulty. It can be ```easy, medium or hard```")
        else: 
            response = requests.get("https://opentdb.com/api.php?amount=1&type=multiple&difficulty=" + difficulty)

            trivia_json = json.dumps(response.json(), sort_keys=True, indent=4)
            trivia_question = json.loads(trivia_json)

            print(trivia_question['results'][0])

            question = trivia_question['results'][0]['question']
            reformated_question = question.replace("&quot;", "\"")

            embed = discord.Embed(colour=discord.Colour(0xd15659), description=reformated_question)
            embed.add_field(name="A", value=trivia_question['results'][0]['correct_answer'], inline=False)
            embed.add_field(name="B", value="incorrect 1", inline=False)
            embed.add_field(name="C", value="incorrect 2", inline=False)
            embed.add_field(name="D", value="incorrect 3", inline=False)

            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Trivia(bot))