import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
import requests
from bs4 import BeautifulSoup

with open('setting.json', mode='r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    async def 圖片(selF, ctx):
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(random_pic)
        await ctx.send(file = pic)

    @commands.command()
    async def 虎斑貓(selF, ctx):
        random_pic = random.choice(jdata['url_pic'])
        # pic = discord.File(random_pic)
        await ctx.send(random_pic)

    @commands.command()
    async def ptt_joke(selF, ctx):
        url = 'https://www.ptt.cc/bbs/joke/index.html'
        userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
        headers = {'User-Agent': userAgent}
        list =[]
        res = requests.get(url, headers=headers)
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        ccc = soup.select('div[class="title"]')
        for each_article in ccc:
            title = each_article('a')[0].text
            articleUrl = 'https://www.ptt.cc' + each_article.select('a')[0]['href']
            list.append(articleUrl)
        await ctx.send(list)

def setup(bot):
    bot.add_cog(React(bot))