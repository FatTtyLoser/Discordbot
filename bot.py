import discord
from discord.ext import commands
import json
import random

with open('setting.json', mode='r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='[', intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(f'{member} leave')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')

@bot.command()
async def 圖片(ctx):
    random_pic = random.choice(jdata['pic'])
    pic = discord.File(random_pic)
    await ctx.send(file = pic)

@bot.command()
async def 超腥拳婦白冰冰EX2(ctx):
    random_pic = random.choice(jdata['url_pic'])
    # pic = discord.File(random_pic)
    await ctx.send(random_pic)

bot.run(jdata['TOKEN'])