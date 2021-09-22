import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='[', intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(890082452792565801)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(890082501383573555)
    await channel.send(f'{member} leave')

bot.run('Token')
