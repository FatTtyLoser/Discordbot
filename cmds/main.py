from Fatiger_bot.core.classes import Cog_Extension
import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):

    @commands.command()
    async def ping(selF, ctx):
        await ctx.send(f'{round(selF.bot.latency*1000)} (ms)')

    @commands.command()
    async def hi(selF, ctx):
        await ctx.send('3345678')

def setup(bot):
    bot.add_cog(Main(bot))