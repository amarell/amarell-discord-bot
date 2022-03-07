import asyncio
from urllib.error import ContentTooShortError
from discord.ext import commands
import numpy as np
import discord
import random


class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["hs"])
    async def hangman_start(self, ctx):
        """Starts a new game of hangman!"""
        words = ["Guardians of the galaxy",
                 "Titanic", "Prisoners",
                 "Prometheus", "Saving private Ryan",
                 "Interstellar", "The Imitation Game",
                 "Tomorrowland", "Frozen", "Now You See Me",
                 "Dawn of the Planet of the Apes",
                 "Ant-Man", "The Conjuring", "Nightcrawler",
                 "X-Men: Days of the Future Past",
                 "Pacific Rim", "Inferno", "Sicario",
                 "The Hunger Games", "Django Unchained",
                 "Shutter Island", "The Great Gastby",
                 "The Wolf of Wall Street",
                 "No Country for Old Men",
                 "Furious 6", "Whiplash", "The Shallows",
                 "Into the woods",
                 "Transformers: Age of Extinction",
                 "The Revenant", "The Dark Knight Rises",
                 "Divergent", "Finding Dory",
                 "10 Cloverfield Lane", "300",
                 "Ex Machina", "12 Years a Slave",
                 "Harry Potter and the Deathly Hallows: Part 2",
                 "Hell or High Water", "The Martian", "Thor",
                 "Avengers: Age of Ultron", "Warcraft",
                 "Gone Girl", "Jurassic World",
                 "Inception", "Zootopia", "The Avengers",
                 "Pirates of the Caribbean: Dead Man's Chest",
                 "Inglorious Basterds",
                 "Kingsman: The Secret Service",
                 "The Prestige",
                 "Fifty Shades of Gray",
                 "The Girl on the Train",
                 "Sully",
                 "Batman v Superman: Dawn of Justice",
                 "Me Before You", "Don't Breathe",
                 "The Dark Knight",
                 "John Wick", "Doctor Strange",
                 "Deadpool", "Arrival", "Passengers",
                 "The Lost City of Z",
                 "Fantastic Beasts and Where to Find Them"]
        word = random.choice(words)
        mistakes = 0
        guessed_letters = []
        progress = ""

        for i in range(len(word)):
            if(word[i] == ' '):
                progress = progress + " "
            else:
                progress = progress + "_ "

        await ctx.send("This is the chosen word: \n```{0}```".format(progress))

        try:
            while(mistakes < 6):
                msg = await self.bot.wait_for('message', timeout=30)
                if(len(msg.content) == 1):
                    if(msg.content.lower() in word.lower()):
                        guessed_letters.append(msg.content.lower())
                        unique_guesses = np.unique(guessed_letters)

                        progress = ""
                        for i in range(len(word)):
                            if(word[i] == ' '):
                                progress = progress + " "
                            elif(word[i].lower() in unique_guesses):
                                progress = progress + word[i] + " "
                            else:
                                progress = progress + "_ "

                        if("_" not in progress):
                            await ctx.send("Well done! The word was **" + word + "**")
                            return
                        else:
                            if mistakes == 0:
                                embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                    0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃..............\n.┃.............. \n.┃.............. \n /-\\")
                                embed.add_field(
                                    name="Current word:", value="```"+progress+"```")

                                guessed_letters_string = ""
                                for letter in guessed_letters:
                                    guessed_letters_string = guessed_letters_string + letter + ", "

                                embed.add_field(
                                    name="Guessed letters:", value="```" + guessed_letters_string + "```",
                                    inline=False
                                )

                                await ctx.send(embed=embed)
                            elif mistakes == 1:
                                embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                    0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃.............😲\n.┃............. \n.┃.............. \n /-\\")
                                embed.add_field(
                                    name="Current word:", value="```"+progress+"```")

                                guessed_letters_string = ""
                                for letter in guessed_letters:
                                    guessed_letters_string = guessed_letters_string + letter + ", "

                                embed.add_field(
                                    name="Guessed letters:", value="```{0}```".format(guessed_letters_string),
                                    inline=False
                                )

                                await ctx.send(embed=embed)
                            elif mistakes == 2:
                                embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                    0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃.............😲\n.┃............./  \n.┃.............. \n /-\\")
                                embed.add_field(
                                    name="Current word:", value="```"+progress+"```")

                                guessed_letters_string = ""
                                for letter in guessed_letters:
                                    guessed_letters_string = guessed_letters_string + letter + ", "

                                embed.add_field(
                                    name="Guessed letters:", value="```" + guessed_letters_string + "```",
                                    inline=False
                                )

                                await ctx.send(embed=embed)
                            elif mistakes == 3:
                                embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                    0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃.............😲\n.┃............./ | \n.┃.............. \n /-\\")
                                embed.add_field(
                                    name="Current word:", value="```"+progress+"```")

                                guessed_letters_string = ""
                                for letter in guessed_letters:
                                    guessed_letters_string = guessed_letters_string + letter + ", "

                                embed.add_field(
                                    name="Guessed letters:", value="```" + guessed_letters_string + "```",
                                    inline=False
                                )

                                await ctx.send(embed=embed)
                            elif mistakes == 4:
                                embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                    0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃.............😲\n.┃............./ | \\ \n.┃.............. \n /-\\")
                                embed.add_field(
                                    name="Current word:", value="```"+progress+"```")

                                guessed_letters_string = ""
                                for letter in guessed_letters:
                                    guessed_letters_string = guessed_letters_string + letter + ", "

                                embed.add_field(
                                    name="Guessed letters:", value="```" + guessed_letters_string + "```",
                                    inline=False
                                )

                                await ctx.send(embed=embed)
                            elif mistakes == 5:
                                embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                    0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃.............😲\n.┃............./ | \\ \n.┃............../  \n /-\\")
                                embed.add_field(
                                    name="Current word:", value="```"+progress+"```")

                                guessed_letters_string = ""
                                for letter in guessed_letters:
                                    guessed_letters_string = guessed_letters_string + letter + ", "

                                embed.add_field(
                                    name="Guessed letters:", value="```" + guessed_letters_string + "```",
                                    inline=False
                                )

                                await ctx.send(embed=embed)
                            else:
                                await ctx.send("Your current progress is: ```"+progress+"```")

                    else:
                        guessed_letters.append(msg.content.lower())
                        mistakes = mistakes + 1
                        if mistakes == 0:
                            embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃..............\n.┃.............. \n.┃.............. \n /-\\")
                            embed.add_field(
                                name="Current word:", value="```"+progress+"```")

                            guessed_letters_string = ""
                            for letter in guessed_letters:
                                guessed_letters_string = guessed_letters_string + letter + ", "

                            embed.add_field(
                                name="Guessed letters:", value="```" + guessed_letters_string + "```",
                                inline=False
                            )

                            await ctx.send(embed=embed)
                        elif mistakes == 1:
                            embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃.............😲\n.┃............. \n.┃.............. \n /-\\")
                            embed.add_field(
                                name="Current word:", value="```"+progress+"```")

                            guessed_letters_string = ""
                            for letter in guessed_letters:
                                guessed_letters_string = guessed_letters_string + letter + ", "

                            embed.add_field(
                                name="Guessed letters:", value="```" + guessed_letters_string + "```",
                                inline=False
                            )

                            await ctx.send(embed=embed)
                        elif mistakes == 2:
                            embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃.............😲\n.┃............./  \n.┃.............. \n /-\\")
                            embed.add_field(
                                name="Current word:", value="```"+progress+"```")

                            guessed_letters_string = ""
                            for letter in guessed_letters:
                                guessed_letters_string = guessed_letters_string + letter + ", "

                            embed.add_field(
                                name="Guessed letters:", value="```" + guessed_letters_string + "```",
                                inline=False
                            )

                            await ctx.send(embed=embed)
                        elif mistakes == 3:
                            embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃.............😲\n.┃............./ | \n.┃.............. \n /-\\")
                            embed.add_field(
                                name="Current word:", value="```"+progress+"```")

                            guessed_letters_string = ""
                            for letter in guessed_letters:
                                guessed_letters_string = guessed_letters_string + letter + ", "

                            embed.add_field(
                                name="Guessed letters:", value="```" + guessed_letters_string + "```",
                                inline=False
                            )

                            await ctx.send(embed=embed)
                        elif mistakes == 4:
                            embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃.............😲\n.┃............./ | \\ \n.┃.............. \n /-\\")
                            embed.add_field(
                                name="Current word:", value="```"+progress+"```")

                            guessed_letters_string = ""
                            for letter in guessed_letters:
                                guessed_letters_string = guessed_letters_string + letter + ", "

                            embed.add_field(
                                name="Guessed letters:", value="```" + guessed_letters_string + "```",
                                inline=False
                            )

                            await ctx.send(embed=embed)
                        elif mistakes == 5:
                            embed = discord.Embed(title="Hangman", colour=discord.Colour(
                                0x9de20e), description=". ┌─────┐\n.┃...............┋\n.┃...............┋\n.┃.............😲\n.┃............./ | \\ \n.┃............../  \n /-\\")
                            embed.add_field(
                                name="Current word:", value="```"+progress+"```")

                            guessed_letters_string = ""
                            for letter in guessed_letters:
                                guessed_letters_string = guessed_letters_string + letter + ", "

                            embed.add_field(
                                name="Guessed letters:", value="```" + guessed_letters_string + "```",
                                inline=False
                            )

                            await ctx.send(embed=embed)
                        else:
                            await ctx.send("Your current progress is: ```"+progress+"```")
                elif(msg.content.lower() == word.lower()):
                    await msg.add_reaction("\u2705")
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
