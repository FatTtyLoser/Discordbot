# Discord_bot
###### tags: `Discord` `Python`

將一些 Function 記錄下來  
基本上 Linebot 跟 Discordbot 的部署方式並無太大差異

## Function and parameter list

### [Cogs](https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html)

**There comes a point in your bot’s development when you want to organize a collection of commands, listeners, and some state into one class. Cogs allow you to do just that.**

The gist:  
Each cog is a Python class that subclasses commands.Cog.  
Every command is marked with the commands.command() decorator.  
Every listener is marked with the commands.Cog.listener() decorator.  
* 透過官方說明文件，若要將python中class的方法利用於DisocordBot中，不同類別的function集中在一個class呼叫時，需使用Cogs方法來做，gist告訴我們decorator會有特殊寫法，所以一律套用在整個discordbot中的所有function mudole中。

### async

* async是協程(Coroutines)概念中python asyncio library的function name，Coroutine則是程式中子程式的一個通用概念與方法，用來宣告async中的function是有異步執行的功能。

### Cog_Extension

* Cog_Extension是commands.Cog.listener()伴隨的呼叫寫法，listener可以監聽指定的事件並透過接收使用者訊息來決定要啟用哪一個API，關於使用者的所在位置常使用ctx(context)
參數，而使用者傳送的訊息則使用msg去接收。

**commands.command()**

* 使用Cogs的command decorator的寫法。

>`on_member_join(self, member)`  
>`on_Member_remove(self, member)`  

* 成員加入與退出伺服器的指令，伺服器常用以紀錄，(self, member)參數表示bot選擇要接收的使用者訊息是什麼，self是call自己的bot，member是加入成員的預設名稱，由於是針對特定伺服器的特定頻道做join&leave所以需要指定頻道ID，故不能使用ctx來接收使用者位置。

> `on_message(self, msg)`

* 透過監聽使用者訊息，可設定關鍵字來做為觸發回應條件，然後回傳指定訊息到頻道中。

>`on_ready(None)`

* 必須透過協程的方式使用，方法是註冊一個額外的監聽器，譬如將on_ready置放在bot核心的.py中被啟用後，若是啟用成功順利運行時`print('BOT is working')`，來讓自己知道啟用狀況，同樣可以用在登入。
```
@bot.event
async def on_ready():
    print("BOT is working")
```
>setting.json


ctx(使用者,id,所在伺服器,所在頻道)
由於BOT可以被邀請進多數個頻道，必須使用ctx讓BOT知道要傳去哪一個伺服器與頻道。

---
## Tips

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

discord.bot 中的 command function  
使用 async 協程的概念 def 定義函數分為三個功能   
load = 載入自定義的擴充 function  
re-load = 重新載入(開發中可以在不停止 bot 的情況下 debug 後 re-load 即可將功能上線)  
unload = 卸載擴充函數  
放在 bot.py 本體會自動歸類為 no-category 由於功能是對擴充函數的操作，所以放在本體才有最大的權限。

概念：背景執行 異步執行 協程
異步執行 = = (作用) = => 模擬多執行序