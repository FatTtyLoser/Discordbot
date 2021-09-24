# Discord_bot
###### tags: `Discord` `Python`

將一些 Function 記錄下來
基本上 Linebot 跟 Discordbot 的部署方式並無太大差異

functionname parameter_list

>on_Member_join

>on_Member_remove

@bot.commands 可以移到其他文件 利用Cog來啟用
@bot.event 同理也是可以使用Cog

>on_ready
```
@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run('token')
#token 需要是字串
```
>setting.json

@bot.command

ctx = context (上下文)

A: 嗨(使用者,id,所在伺服器,所在頻道)
B: 安安
#形成上下文
由於BOT可以被邀請進多數個頻道，必須使用ctx讓BOT知道要傳去哪一個伺服器與頻道。

---
**刪除我所說的訊息、覆誦我所說的訊息。**  
由於 sayd 參數中所帶的 msg 只有一個，所以只認訊息中的第一個 argument
如果訊息 print('[sayd 123 456') 時，discord bot 只會認定 123 為 mag  

```
@commands.command()
async def sayd(self, ctx, msg):
    await ctx.message.delete()
    await ctx.send(msg)
```

所以要在 sayd 參數中 ,msg 加上 * 代表複數 argument，讓 msg 參數可以接到所有使用者傳送的訊息。

```
@commands.command()
async def sayd(self, ctx, *,msg):
    await ctx.message.delete()
    await ctx.send(msg)
```

---

```
@commands.command()
async def purge(self, ctx, num : int):
    await ctx.channel.purge(limit=num+1)
```

Parameters
limit (Optional[int]) – The number of messages to search through. This is not the number of messages that will be deleted, though it can be.

check (Callable[[Message], bool]) – The function used to check if a message should be deleted. It must take a Message as its sole parameter.

before (Optional[Union[abc.Snowflake, datetime.datetime]]) – Same as before in history().

after (Optional[Union[abc.Snowflake, datetime.datetime]]) – Same as after in history().

around (Optional[Union[abc.Snowflake, datetime.datetime]]) – Same as around in history().

oldest_first (Optional[bool]) – Same as oldest_first in history().

bulk (bool) – If True, use bulk delete. Setting this to False is useful for mass-deleting a bot’s own messages without Permissions.manage_messages. When True, will fall back to single delete if current account is a user bot (now deprecated), or if messages are older than two weeks.

---

概念：背景執行 異步執行 協程
異步執行 = = (作用) = => 模擬多執行序