import json

import discord
from discord.ext import commands


with open('setting.json', 'r', encoding='utf-8') as setting:
    jdata = json.load(setting)


bot = commands.Bot(command_prefix='.')


@bot.event
async def on_ready():
    channel = bot.get_channel(int(jdata['MAIN_CHANNEL']))
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


@bot.command()
async def pic(ctx):
    pic_file = discord.File('E:\\20200516_102659.jpg')
    await ctx.send(file=pic_file)


bot.run(jdata['TOKEN'])
