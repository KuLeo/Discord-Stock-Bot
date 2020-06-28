from discord.ext import commands


bot = commands.Bot(command_prefix='.')


@bot.event
async def on_ready():
    channel = bot.get_channel(726649005366575135)
    await channel.send('>> Bot is Online <<')
    print(">> Bot is Online")


@bot.event
async def on_member_join(member):
    print(f"{member} join!")


@bot.event
async def on_member_remove(member):
    print(f"{member} leave!")


@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000, 2)} (ms)')

bot.run('NzI2MzM3MzAzNDEyMzQyODI0.XvgFRg.QfZPXdWZF5VgKNe1_9_3wJll_ms')
