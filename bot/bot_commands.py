from discord.ext import commands
import discord


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


def setup(bot):
    bot.add_cog(Greetings(bot))