from discord.ext import commands
import discord
import string
import random
import json
import requests

class Calculation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, left: int, right:int):
        """Adds two numbers together!"""
        await ctx.send(left + right)

    @commands.command()
    async def subtract(self, ctx, left: int, right: int):
        """Subtracts two numbers!"""
        await ctx.send(left - right)

class RandomLibraryStuff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def generate_password(self, ctx, length: int = None):
        """Generates a random password with input number of chars"""
        try:
            if(length is None):
                await ctx.send("The proper usage is: \n```generate_password <int>```")
            elif(isinstance(length, int)):
                chars = string.ascii_letters
                digits = string.digits
                punct = string.punctuation

                all = chars + digits + punct

                temp = random.sample(all, length)
                password = "".join(temp)

                await ctx.send("The generated password is:\n" + "```" + password + "```")
            else:
                await ctx.send("The proper usage is: \n```generate_password <int>```")
        except Exception as err:
            await ctx.send(err)

    @commands.command()
    async def roll(self, ctx, dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    
    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self, ctx, *choices: str):
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))


    @commands.command(description="Repeats content n times")
    async def repeat(self, ctx, times: int, content: str):
        for x in range(times):
            await ctx.send(content)

    @commands.command()
    async def guess(self, ctx, number: int):
        """ Guess a random number from 1 to 6. """
        value = random.randint(1, 6)
        
        async def tick(ctx, value):
            emoji = '\N{WHITE HEAVY CHECK MARK}' if value else '\N{CROSS MARK}'
            try:
                # this will react to the command author's message
                await ctx.message.add_reaction(emoji)
            except discord.HTTPException:
                # sometimes errors occur during this, for example
                # maybe you dont have permission to do that
                # we dont mind, so we can just ignore them
                pass

        await tick(ctx, number == value)


class ActivityCheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def check_spotify_activity(self, ctx, *, member: discord.Member = None):
        """Checks user's current Spotify activity!"""
        if(member is None):
            await ctx.send("Please @ someone!")
            return

        listening = member.activities
        if not listening: 
            await ctx.send("The user is not listening to anything!")
        else:
            try:
                if listening == None:
                    await ctx.send("The user is currently not listening to anything!")
                else:
                    new_embed = discord.Embed()
                    message = member.display_name + " is listening to " + listening[0].title + " by " + listening[0].artist
                    
                    artists = listening[0].artist.split("; ")

                    response = requests.get("https://api.lyrics.ovh/v1/" + artists[0] + "/" + listening[0].title)
                    lyrics_json = json.dumps(response.json(), sort_keys=True, indent=4)
                    lyrics = json.loads(lyrics_json)

                    new_embed.set_image(url = listening[0].album_cover_url)
                    new_embed.add_field(name="Activity", value=message)

                    await ctx.send(embed=new_embed)

                    if "error" in lyrics.keys():
                        await ctx.send("Error trying to find lyrics!")
                    else:
                        await ctx.send("Lyrics:\n```"+lyrics["lyrics"] + "```")
            except Exception as err:
                await ctx.send(err)

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        if(member is None):
            await ctx.send("You have to tag someone!")
        else:
            await ctx.send('Hello {0.display_name}. Welcome to the server!'.format(member))

    @commands.command()
    async def joined(self, ctx, *, member: discord.Member):
        await ctx.send('{0} joined on {0.joined_at}'.format(member))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))



def setup(bot):
    bot.add_cog(Greetings(bot))
    bot.add_cog(ActivityCheck(bot))
    bot.add_cog(RandomLibraryStuff(bot))
    bot.add_cog(Calculation(bot))