from core.CogExt import CogExtension

from discord.ext import commands


class AdminCommand(CogExtension):
    @commands.command()
    async def load(self, ctx, extension):
        self.bot.load_extension(f'cmds.{extension}')
        await ctx.send(f'Loaded {extension} done.')

    @commands.command()
    async def unload(self, ctx, extension):
        """[summary]

        Args:
            ctx ([type]): [description]
            extension ([type]): [description]
        """
        if extension != "AdminCommand":
            self.bot.unload_extension(f'cmds.{extension}')
            await ctx.send(f'Unloaded {extension} done.')

    @commands.command()
    async def reload(self, ctx, extension):
        if str(ctx.message.author.id) in self.jdata["Admin"]:
            self.bot.reload_extension(f'cmds.{extension}')
            await ctx.send(f'Reloaded {extension} done.')


def setup(bot):
    bot.add_cog(AdminCommand(bot))
