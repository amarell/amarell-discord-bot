from numpy import diff
import requests
from discord.ext import commands
import json
import discord
import asyncio
import random

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

            category = trivia_question['results'][0]['category']
            question = trivia_question['results'][0]['question']
            question_cleanup1 = question.replace("&quot;", "\"")
            question_cleanup2 = question_cleanup1.replace("&#039;", "\'")
            
            incorrect_answers = trivia_question['results'][0]['incorrect_answers']
            correct_answer = trivia_question['results'][0]['correct_answer']
            correct_answer_cleanup1 = correct_answer.replace("&quot;", "\"")
            correct_answer_cleanup2 = correct_answer_cleanup1.replace("&#039;", "\'")

            
            answers = []
            answers.append(correct_answer_cleanup2)

            for item in incorrect_answers:
                incorrect_answer_cleanup1 = item.replace("&quot;", "\"")
                incorrect_answer_cleanup2 = incorrect_answer_cleanup1.replace("&#039;", "\'")
                answers.append(incorrect_answer_cleanup2)

            random.shuffle(answers)

            position_of_correct_answer = answers.index(correct_answer_cleanup2)
            if(position_of_correct_answer == 0):
                correct_letter = 'a'
            elif(position_of_correct_answer == 1):
                correct_letter = 'b'
            elif(position_of_correct_answer == 2):
                correct_letter = 'c'
            elif(position_of_correct_answer == 3):
                correct_letter = 'd'

            print(answers)
            print(correct_letter)

            embed = discord.Embed(colour=discord.Colour(0xd15659), description="**" + question_cleanup2 + "**")
            embed.add_field(name="Category", value="```" + category + "```", inline=True)
            embed.add_field(name="Difficulty", value="```" + difficulty.capitalize() + "```", inline=True)
            embed.add_field(name="A", value=answers[0], inline=False)
            embed.add_field(name="B", value=answers[1], inline=False)
            embed.add_field(name="C", value=answers[2], inline=False)
            embed.add_field(name="D", value=answers[3], inline=False)
            await ctx.send(embed=embed)

            try: 
                msg = await self.bot.wait_for('message', timeout=10)
                if(len(msg.content) == 1):
                    if(msg.content.lower() == correct_letter):
                        await ctx.send("That's right! Congratulations!")
                    else:
                        await ctx.send("Close but no cigar! The correct answer is " + correct_letter)


            except asyncio.TimeoutError:
                await ctx.send("Time's up!\nThe correct answer was: " + correct_letter)

            


def setup(bot):
    bot.add_cog(Trivia(bot))