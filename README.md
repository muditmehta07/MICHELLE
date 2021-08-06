# Michelle

__Website__ : https://top.gg/bot/840180379389263882

Okay so, this is a tutorial thingy, you can learn how to make a discord bot like Michelle here. I'll be explaining the code here in the easiest way.

# main.py

__Step 1__ : Import all the necessary modules that we'll be using.

*Modules* : 1 - Discord, 2 - os (for removing new files that the bot creates), 3 - json (for reading and writing data), 4 - datetime (eh, self explanatory)

```Python

import discord
from discord import user
from discord import channel
from discord import message
from discord.colour import Color
from discord.enums import ActivityType
from discord.ext.commands.converter import _get_from_guilds
from discord.message import Message
from discord.utils import get
from discord.ext import commands,tasks
import os
import json
from itertools import cycle
import datetime

```

__Step 2__ : Create the `bot` instance and configure discord

*Note* : We remove the default `help` command to make a new one that looks prettier than the default one, cause default sucks.

```Python

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix= get_the_prefix , intents=intents)
bot.remove_command('help')

```

__Step 3__ : Get the server's prefix (if any) from `prefix.json`

If the `key` for the server is not found, the default prefix is given as `=`
*Note* : You can change the default prefix to anything you want, the default prefix is set to `=` in this code.

```Python

def get_the_prefix(client, message):
    with open("./local/prefix.json", "r") as f:
        L = json.load(f)

    if str(message.guild.id) in L:
        prefix = L[str(message.guild.id)]["prefix"]
    elif str(message.guild.id) not in L:
        prefix = "="

    return prefix
    
```

__Step 4__ : Adding cog files (cog is basically a way of dividing code ito multiple files to make it presentable)

We create a folder called `cogs` where we store all the extensions like `general.py`, `setup.py`, etc.
Here, `initial_extentions` is a list of cog files saved in a`folder.file` format.

```Python

initial_extensions = ['cogs.setup', 'cogs.level', 'cogs.fun', 'cogs.help', 'cogs.about', 'cogs.general']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)
             
```

__Step 5__ : Event when the bot starts and is online.

`@` is a command decorator
`bot` is the bot instance and `event` is method
`on_ready` is a predefined event which means when the bot is ready and is online
`mstat` is a string in which the number of servers that the bot is in is calculated using `guilds` method which returns a list of servers
`await` we use in asynchronous enviroments, asynchronous env is defined with `async` keyword (more about `async` : https://docs.python.org/3/library/asyncio-task.html)

```Python

@bot.event
async def on_ready():
        mstat = f'{str(len(bot.guilds))} servers || =help'
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=mstat))
        
```

__Step 6__ : Event when a user joins a server

`on_member_join` : event called when a user joins a server, this is predefined.

What the above code basically does is, add this user to the server's `json` file where their data will be stored. This code is not necessary but makes your life easier if you don't want any `dictionary key` or `file not found` errors


```Python

@bot.event
async def on_member_join(member):
    guildid = member.guild.id
    guildid = './guild data/'+ str(guildid) +'.json'
    if member.bot == False:
        if os.path.exists(guildid):
            with open(guildid, 'r') as f:
                users = json.load(f)

            await update_data(users, member)

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)
        elif not os.path.exists(guildid):
            with open(guildid, "x") as f:
                print("")
            with open(guildid, 'w') as f:
                d = {

                }
                json.dump(d, f, indent=4)
            with open(guildid, 'r') as f:
                users = json.load(f)

            await update_data(users, member)

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)
                
```

__Step 7__ : Event when a user messages

`on_message` : predefined event for when a user messages in a server, this may or may not be called in a DM channel, depends on your code. In this case it won't be called when a user messages in DMs.

`update_data` : a function that we define so that when a user messages, it updates their data that was created when they joined the server, it adds fields like `experience`, `level` and `color` to their server data

`add_experience` : a function that we define which adds 5 experience per text a user sends

`level_up` : a fucntion that we define which sends a message when a user levels up


```Python

@bot.event #again an event
async def on_message(message): 
    if message.author.bot == False: #so that bot doesn't add itself to any of the data files, we do not wanna track the bot's level lol
        if message.guild:
            guildid = message.channel.guild.id
            guildid = './guild data/'+ str(guildid) +'.json'
            if os.path.exists(guildid):
                with open(guildid, 'r') as f:
                    users = json.load(f)

                await update_data(users, message.author)
                await add_experience(users, message.author, 5)
                await level_up(users, message.author, message)

                with open(guildid, 'w') as f:
                    json.dump(users, f, indent=4)
            elif not os.path.exists(guildid):
                with open(guildid, 'x') as f:
                    print("")
                with open(guildid, 'w') as f:
                    d = {

                    }
                    json.dump(d, f, indent=4)
                with open(guildid, 'r') as f:
                    users = json.load(f)
                await update_data(users, message.author)
                await add_experience(users, message.author, 5)
                await level_up(users, message.author, message)

                with open(guildid, 'w') as f:
                    json.dump(users, f, indent=4)

            await bot.process_commands(message)
        else:
            await bot.process_commands(message)

async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['name'] = str(user.name)
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['rank'] = 0
        users[f'{user.id}']['level'] = 1
        users[f'{user.id}']['color'] = 0x95a5a6
        
        
async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp

async def level_up(users, user, message):
    with open('levels.json', 'r') as g:
        levels = json.load(g)
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1 / 4))
    if lvl_start < lvl_end:
        users[f'{user.id}']['level'] = lvl_end
        l1 = users[f'{user.id}']['level']
        color = users[f'{user.id}']['color']
        if l1==10:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(message.guild.id) in L:
                prefix = L[str(message.guild.id)]["prefix"]
            elif str(message.guild.id) not in L:
                prefix = "="
            up_message = f'{user.mention} *leveled up to* `Level {lvl_end}` ⏫'
            up_description = f'Unlocked *{prefix}kill* 🔓'
            level_embed = discord.Embed(description = up_message, color = color, timestamp=datetime.datetime.utcnow())
            level_embed.set_footer(text = up_description)
            level_embed.set_author(name = user, icon_url= user.avatar_url)
            await message.channel.send(embed=level_embed)
        elif l1==5:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(message.guild.id) in L:
                prefix = L[str(message.guild.id)]["prefix"]
            elif str(message.guild.id) not in L:
                prefix = "="
            up_message = f'{user.mention} *leveled up to* `Level {lvl_end}` ⏫'
            up_description = f'Unlocked *{prefix}theme* 🔓'
            level_embed = discord.Embed(description = up_message, color = color, timestamp=datetime.datetime.utcnow())
            level_embed.set_footer(text = up_description)
            level_embed.set_author(name = user, icon_url= user.avatar_url)
            await message.channel.send(embed=level_embed)
        else:
            up_message = f'{user.mention} leveled up to `Level {lvl_end}` ⏫ '
            level_embed = discord.Embed(description = up_message, color = color, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = user, icon_url= user.avatar_url)
            await message.channel.send(embed=level_embed)
```

__Step 8__ : Last but not the least, running the bot

*Note* : replace `token` with your bot token


```Python

bot.run("token")

```

# level.py


From here it's get a bit complicated, cause here we are gonna make a *level card* using the Python module `PIL` or `pillow`. We create this file in a folder named `cogs` in the same directory as `main.py`

__Step 1__ : import pillow

```Python

from PIL import Image, ImageDraw, ImageFont

```
__Step 2__ : create a class


```Python

class LevelCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

```        

Because we are using cogs, we won't be defining the bot instance again. 
__Step 3__ : creating a function that converts numbers into readable format. Example : 5000 will be converted to 5K

```Python
    def human_format(self, num):
        num = float('{:.3g}'.format(num))
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num /= 1000.0
        return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])
   
```

__Step 4__ : Now the real fun begins with this step, we start writing the code for the level card

```Python
    @commands.command(name = "level", aliases = ["rank", "Level", "LEVEL", "Rank", "RANK"])
    async def level(self, ctx, member: discord.Member = None):
        guildid = ctx.message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        if not member:
            id = ctx.message.author.id
            with open(guildid, 'r') as f:
                users = json.load(f)

            R={}
            for i in users:
                user = i
                exp = users[i]['experience']
                R[user]=exp
            R = dict(sorted(R.items(), key=lambda item: item[1], reverse=True))
            L= list(R)
            theme = users[str(id)]['color']
            rank = L.index(str(id))+1
            level = users[str(id)]['level']
            currentxp = users[str(id)]['experience']
            xp = currentxp
            final_xp = (int(level)+1) ** 4
            user_name = ctx.author.name
            discriminator = "#"+ctx.author.discriminator
            await ctx.message.author.avatar_url.save(("logo.jpg"))

            level = LevelCog.human_format(self, level)
          
            if theme == 9807270: #gray
                full_image = Image.open("./pictures/bg.jpg").convert("RGB").resize((1060, 320))
            elif theme == 15158332 or theme == 10038562: #red
                full_image = Image.open("./pictures/red.jpg").convert("RGB").resize((1060, 320))
            elif theme == 3447003 or theme == 2123412: #blue
                full_image = Image.open("./pictures/blue.jpg").convert("RGB").resize((1060, 320))
            elif theme == 3066993 or theme == 2067276: #green
                full_image = Image.open("./pictures/green.jpg").convert("RGB").resize((1060, 320))
            elif theme == 10181046 or theme == 7419530: #purple
                full_image = Image.open("./pictures/purple.jpg").convert("RGB").resize((1060, 320))
            elif theme == 15844367 or theme == 12745742: #gold
                full_image = Image.open("./pictures/gold.jpg").convert("RGB").resize((1060, 320))
            elif theme == 1752220 or theme == 1146986: #teal
                full_image = Image.open("./pictures/teal.png").convert("RGB").resize((1060, 320))
            elif theme == 15105570 or theme == 11027200: #orange
                full_image = Image.open("./pictures/orange.jpg").convert("RGB").resize((1060, 320))
            elif theme == 15277667 or theme == 11342935: #magenta
                full_image = Image.open("./pictures/magenta.jpg").convert("RGB").resize((1060, 320))
            else: #gray
                full_image = Image.open("./pictures/bg.jpg").convert("RGB").resize((1060, 320))

            background = Image.new("RGB", (1000, 240))

            theme = hex(theme).split('x')[-1]

            try:
                logo = Image.open("logo.jpg").convert("RGB").resize((180, 180))
            except:
                logo = Image.open("./pictures/discord.png").convert("RGB").resize((180, 180))
            bigsize = (logo.size[0] * 3, logo.size[1] * 3)
            mask = Image.new("L", bigsize, 0)

            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + bigsize, 255)

            draw.ellipse((140 * 3, 140 * 3, 189 * 3, 189 * 3), 0)

            mask = mask.resize(logo.size, Image.ANTIALIAS)
            logo.putalpha(mask)

            background.paste(logo, (40, 30), mask=logo)

            draw = ImageDraw.Draw(background, "RGB")

            if ctx.message.author.status == discord.Status.online:
                draw.ellipse((180, 165, 230, 215), fill="#47d147")
            elif ctx.message.author.status == discord.Status.idle:
                draw.ellipse((180, 165, 230, 215), fill="#ffff99")
            elif ctx.message.author.status == discord.Status.dnd:
                draw.ellipse((180, 165, 230, 215), fill="#b34f5a")
            else:
                draw.ellipse((180, 165, 230, 215), fill="#d9d9d9")

            big_font = ImageFont.FreeTypeFont("ABeeZee-Regular.otf", 60)
            medium_font = ImageFont.FreeTypeFont("ABeeZee-Regular.otf", 40)
            small_font = ImageFont.FreeTypeFont("ABeeZee-Regular.otf", 30)

            text_size = draw.textsize(str(level), font=big_font)
            offset_x = 1000 - 15 - text_size[0]
            offset_y = 10
            draw.text((offset_x, offset_y), str(level), font=big_font, fill=f"#{theme}")

            text_size = draw.textsize("LEVEL", font=small_font)
            offset_x -= text_size[0] + 5
            draw.text((offset_x, offset_y + 27), "LEVEL", font=small_font, fill=f"#{theme}")

            text_size = draw.textsize(f"#{rank}", font=big_font)
            offset_x -= text_size[0] + 15
            draw.text((offset_x, offset_y), f"#{rank}", font=big_font, fill="#fff")

            text_size = draw.textsize("RANK", font=small_font)
            offset_x -= text_size[0] + 5
            draw.text((offset_x, offset_y + 27), "RANK", font=small_font, fill="#fff")

            bar_offset_x = 320
            bar_offset_y = 160
            bar_offset_x_1 = 950
            bar_offset_y_1 = 200
            circle_size = bar_offset_y_1 - bar_offset_y

            draw.rectangle((bar_offset_x, bar_offset_y, bar_offset_x_1, bar_offset_y_1), fill="#727175")

            draw.ellipse(
                (bar_offset_x - circle_size // 2, bar_offset_y, bar_offset_x + circle_size // 2, bar_offset_y_1), fill="#727175"
            )

            draw.ellipse(
                (bar_offset_x_1 - circle_size // 2, bar_offset_y, bar_offset_x_1 + circle_size // 2, bar_offset_y_1), fill="#727175"
            )

            bar_length = bar_offset_x_1 - bar_offset_x
            progress = (xp) * 100 / final_xp
            progress = 100 - progress
            progress_bar_length = round(bar_length * progress / 100)
            bar_offset_x_1 = bar_offset_x + progress_bar_length

            draw.rectangle((bar_offset_x, bar_offset_y, bar_offset_x_1, bar_offset_y_1), fill=f"#{theme}")

            draw.ellipse(
                (bar_offset_x - circle_size // 2, bar_offset_y, bar_offset_x + circle_size // 2, bar_offset_y_1), fill=f"#{theme}"
            )

            draw.ellipse(
                (bar_offset_x_1 - circle_size // 2, bar_offset_y, bar_offset_x_1 + circle_size // 2, bar_offset_y_1), fill=f"#{theme}"
            )

            text_size = draw.textsize(f"/ {LevelCog.human_format(self, final_xp)} XP", font=small_font)

            offset_x = 950 - text_size[0]
            offset_y = bar_offset_y - text_size[1] - 14

            draw.text((offset_x, offset_y), f"/ {LevelCog.human_format(self, final_xp)} XP", font=small_font, fill="#727175")

            text_size = draw.textsize(f"{LevelCog.human_format(self, xp)}", font=small_font)
            offset_x -= text_size[0] + 8
            draw.text((offset_x, offset_y), f"{LevelCog.human_format(self, xp)}", font=small_font, fill="#fff")

            text_size = draw.textsize(user_name, font=medium_font)

            offset_x = bar_offset_x
            offset_y = bar_offset_y - text_size[1] - 14
            draw.text((offset_x, offset_y), user_name, font=medium_font, fill="#fff")

            offset_x += text_size[0] + 5
            offset_y += 10

            draw.text((offset_x, offset_y), discriminator, font=small_font, fill="#727175")

            img_w, img_h = background.size
            bg_w, bg_h = full_image.size
            offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)

            full_image.paste(background, offset)

            full_image.save("image.jpg", quality=100)
            file = discord.File("image.jpg")
            await ctx.send(file=file)
            os.remove("image.jpg")
            os.remove("logo.jpg")

        else:
            id = member.id
            with open(guildid, 'r') as f:
                users = json.load(f)
            lvl = users[str(id)]['level']
            exp = users[str(id)]['experience']
            color = users[str(id)]['color']
            m = f'{member.mention} is Level {lvl}'
            level_embed = discord.Embed(description = m, color = color, timestamp = datetime.datetime.utcnow())
            level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            await ctx.send(embed=level_embed)
```
            
 
__Step 5__ :  Add the cog to the main code

```Python

 def setup(bot):
    bot.add_cog(LevelCog(bot))

```
