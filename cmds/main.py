from Fatiger_bot.core.classes import Cog_Extension
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import time


class Main(Cog_Extension):

    @commands.command()
    async def ping(selF, ctx):
        await ctx.send(f'{round(selF.bot.latency*1000)} (ms)')

    @commands.command()
    async def hi(selF, ctx):
        await ctx.send('3345678')

    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="Fatiger_bot", url="https://www.youtube.com/watch?v=072tU1tamd0&ab_channel=Majima", description="just a bot", color=0xdea1a1, timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Jefffery", url="https://www.youtube.com/watch?v=072tU1tamd0&ab_channel=Majima", icon_url="https://cdn.hk01.com/di/media/images/dw/20200831/377077163972759552.jpeg/V47dBJKbgpTNfW4-6pYOgzJ5Vl_PUCnkc3sM7XN7DO0?v=w1920")
        embed.set_thumbnail(url="https://cdn.hk01.com/di/media/images/dw/20200831/377077163972759552.jpeg/V47dBJKbgpTNfW4-6pYOgzJ5Vl_PUCnkc3sM7XN7DO0?v=w1920")
        embed.add_field(name="1", value="4", inline=True)
        embed.add_field(name="2", value="3", inline=False)
        embed.add_field(name="3", value="2", inline=True)
        embed.add_field(name="4", value="1", inline=False)
        embed.set_footer(text="test_text")
        await ctx.send(embed=embed)

    #刪除我所說的訊息、覆誦我所說的訊息。
    @commands.command()
    async def sayd(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    @commands.command()
    async def purge(self, ctx, num : int):
        await ctx.channel.purge(limit=num+1)

def setup(bot):
    bot.add_cog(Main(bot))