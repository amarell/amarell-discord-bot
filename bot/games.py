import asyncio
from urllib.error import ContentTooShortError
from discord.ext import commands
import numpy as np
import discord


class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hs(self, ctx):
        """Starts a new game of hangman!"""
        word = "hangman"
        mistakes = 0
        guessed_letters = []
        progress = ""

        for i in range(len(word)):
            progress = progress + "\_ "

        await ctx.send("This is the chosen word: \n{0}".format(progress))

        try:
            while(mistakes < 6):
                msg = await self.bot.wait_for('message', timeout=30)
                if(len(msg.content) == 1):
                    if(msg.content in word):
                        guessed_letters.append(msg.content)
                        unique_guesses = np.unique(guessed_letters)

                        progress = ""
                        for i in range(len(word)):
                            if(word[i] in unique_guesses):
                                progress = progress + word[i] + " "
                            else:
                                progress = progress + "_ "

                        if("_" not in progress):
                            await ctx.send("Well done! The word was **" + progress + "**")
                            return
                        else:
                            if mistakes == 0:
                                embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                    0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃..............\n.┃.............. \n.┃.............. \n /-\\")
                                embed.add_field(
                                    name="Current word:", value="```"+progress+"```")

                                await ctx.send(embed=embed)
                            elif mistakes == 1:
                                embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                    0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃.............😲\n.┃............. \n.┃.............. \n /-\\")
                                embed.add_field(
                                    name="Current word:", value="```"+progress+"```")

                                await ctx.send(embed=embed)
                            elif mistakes == 2:
                                embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                    0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃.............😲\n.┃............./  \n.┃.............. \n /-\\")
                                embed.add_field(
                                    name="Current word:", value="```"+progress+"```")

                                await ctx.send(embed=embed)
                            elif mistakes == 3:
                                embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                    0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃.............😲\n.┃............./ | \n.┃.............. \n /-\\")
                                embed.add_field(
                                    name="Current word:", value="```"+progress+"```")

                                await ctx.send(embed=embed)
                            elif mistakes == 4:
                                embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                    0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃.............😲\n.┃............./ | \\ \n.┃.............. \n /-\\")
                                embed.add_field(
                                    name="Current word:", value="```"+progress+"```")

                                await ctx.send(embed=embed)
                            elif mistakes == 5:
                                embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                    0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃.............😲\n.┃............./ | \\ \n.┃............../  \n /-\\")
                                embed.add_field(
                                    name="Current word:", value="```"+progress+"```")

                                await ctx.send(embed=embed)
                            else:
                                await ctx.send("Your current progress is: ```"+progress+"```")

                    else:
                        guessed_letters.append(msg.content)
                        mistakes = mistakes + 1
                        if mistakes == 0:
                            embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃..............\n.┃.............. \n.┃.............. \n /-\\")
                            embed.add_field(
                                name="Current word:", value="```"+progress+"```")

                            await ctx.send(embed=embed)
                        elif mistakes == 1:
                            embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃.............😲\n.┃............. \n.┃.............. \n /-\\")
                            embed.add_field(
                                name="Current word:", value="```"+progress+"```")

                            await ctx.send(embed=embed)
                        elif mistakes == 2:
                            embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃.............😲\n.┃............./  \n.┃.............. \n /-\\")
                            embed.add_field(
                                name="Current word:", value="```"+progress+"```")

                            await ctx.send(embed=embed)
                        elif mistakes == 3:
                            embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃.............😲\n.┃............./ | \n.┃.............. \n /-\\")
                            embed.add_field(
                                name="Current word:", value="```"+progress+"```")

                            await ctx.send(embed=embed)
                        elif mistakes == 4:
                            embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃.............😲\n.┃............./ | \\ \n.┃.............. \n /-\\")
                            embed.add_field(
                                name="Current word:", value="```"+progress+"```")

                            await ctx.send(embed=embed)
                        elif mistakes == 5:
                            embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃.............😲\n.┃............./ | \\ \n.┃............../  \n /-\\")
                            embed.add_field(
                                name="Current word:", value="```"+progress+"```")

                            await ctx.send(embed=embed)
                        else:
                            await ctx.send("Your current progress is: ```"+progress+"```")
                elif(msg.content == word):
                    await ctx.send("That's the word we're looking for!")
                    return
                else:
                    mistakes = mistakes + 1
                    await ctx.send("That's not quite right! One life less!")

            embed = discord.Embed(title="Hangman", colour=discord.Colour(
                0x29664c), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃.............😲\n.┃............./ | \\ \n.┃............../ \\ \n /-\\")

            embed.add_field(name="*You died*",
                            value="The word was **" + word + "**")

            await ctx.send(embed=embed)

        except asyncio.TimeoutError:
            await ctx.send("Time's up!\nThe word we were looking for was " + word)


def setup(bot):
    bot.add_cog(Game(bot))
