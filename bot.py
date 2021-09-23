import discord
from discord.ext import commands
import json
import random
import os

intents = discord.Intents.default()
intents.members = True

with open('setting.json', mode='r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='[', intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(F'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])