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

# Command-line 訊息留在 bot.py 本體，容易識別 bot 啟動狀況。
@bot.event
async def on_ready():
    print(">> Bot is online <<")

''' 
discord.bot 中的 command function
使用 async 協程的概念 def 定義函數分為三個功能 
load = 載入自定義的擴充 function
re-load = 重新載入(開發中可以在不停止 bot 的情況下 debug 後 re-load 即可將功能上線)
unload = 卸載擴充函數
放在 bot.py 本體會自動歸類為 no-category 由於功能是對擴充函數的操作，所以放在本體才有最大的權限。
'''
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un - Loaded {extension} done.')
@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re - Loaded {extension} done.')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(F'cmds.{filename[:-3]}')


if __name__ == "__main__":
    bot.run(jdata['TOKEN'])