import os
import json

from discord.ext import commands


with open('setting.json', 'r', encoding='utf-8') as setting:
    jdata = json.load(setting)

bot = commands.Bot(command_prefix='.')

# load cmds
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


if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
