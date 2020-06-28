import os
import json
import random

import discord
from discord.ext import commands


with open('setting.json', 'r', encoding='utf-8') as setting:
    jdata = json.load(setting)

bot = commands.Bot(command_prefix='.')

for file_name in os.listdir('./cmds'):
    try:
        if file_name.endswith('.py'):
            bot.load_extension(f'cmds.{file_name[:-3]}')
            print(f'Load {file_name} done.')
    except IOError as ioe:
        print(f'Load {file_name} IO Error, {str(ioe)}')
    except Exception as e:
        print(f'Load {file_name} fail, {str(e)}')


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
async def pic(ctx):
    pic_file = discord.File('E:\\20200516_102659.jpg')
    await ctx.send(file=pic_file)


@bot.command()
async def wpic(ctx):
    random_pic = random.choice(jdata['url_pic'])
    await ctx.send(random_pic)


if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
