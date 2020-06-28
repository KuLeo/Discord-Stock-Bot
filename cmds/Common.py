from core.CogExt import CogExtension

from discord.ext import commands


class Common(CogExtension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency * 1000, 2)} (ms)')


def setup(bot):
    bot.add_cog(Common(bot))
