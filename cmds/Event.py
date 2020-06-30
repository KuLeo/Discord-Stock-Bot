from core.CogExt import CogExtension

from discord.ext import commands


class BasicEvent(CogExtension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(self.jdata['MAIN_CHANNEL']))
        await channel.send(f'{member} join here!')
        print(f"{member} join!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(self.jdata['MAIN_CHANNEL']))
        await channel.send(f'{member} leave!')
        print(f"{member} leave!")

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.upper() == 'HI' and msg.author != self.bot.user:
            await msg.channel.send(f'Hi, {msg.author}')


def setup(bot):
    bot.add_cog(BasicEvent(bot))
