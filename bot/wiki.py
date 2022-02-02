import wikipedia
from discord.ext import commands


class Wiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lookup(self, ctx, query: str = None):
        """Looks up an article on wikipedia"""
        if(query is None):
            await ctx.send("The proper usage:\n```lookup <query>```")
            return
        else:
            try:
                summary = wikipedia.summary(query, sentences = 4)
                print(summary)
                await ctx.send(summary)
            except wikipedia.exceptions.DisambiguationError as err:
                limit = 5

                await ctx.send(err.options[:limit])


def setup(bot):
    bot.add_cog(Wiki(bot))