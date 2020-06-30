import json

from discord.ext import commands


class CogExtension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open('setting.json', 'r', encoding='utf-8') as setting:
            jdata = json.load(setting)
        self.jdata = jdata
