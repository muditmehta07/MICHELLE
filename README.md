# Michelle

__Website__ : https://top.gg/bot/840180379389263882

Okay so, this is a tutorial thingy, you can learn how to make a discord bot like Michelle here. I'll be explaining the code here in the easiest way.

# main.py

**Step 1 ** : Import all the necessary modules that we'll be using.

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
*Modules* : 1 - Discord, 2 - os (for removing new files that the bot creates), 3 - json (for reading and writing data), 4 - datetime (eh, self explanatory)

**Step 2 ** : Create the `bot` instance and configure discord

```Python

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix= get_the_prefix , intents=intents)
bot.remove_command('help')

```

*Note* : We remove the default `help` command to make a new one that looks prettier than the default one, cause default sucks.

**Step 3 ** : Get the server's prefix (if any) from `prefix.json`

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

*Note* : You can change the default prefix to anything you want, the default prefix is set to `=` in this code.

**Step 4 ** : Adding cog files (cog is basically a way of dividing code ito multiple files to make it presentable)

```Python

initial_extensions = ['cogs.setup', 'cogs.level', 'cogs.fun', 'cogs.help', 'cogs.about', 'cogs.general', 'cogs.item', 'cogs.shop', 'cogs.spells']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)
             
```

**Step 5 ** : Event when the bot starts and is online.

```Python

@bot.event
async def on_ready():
        mstat = f'{str(len(bot.guilds))} servers || =help'
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=mstat))
        
```

`@` is a command decorator
`bot` is the bot instance and `event` is method
`on_ready` is a predefined event which means when the bot is ready and is online
`mstat` is a string in which the number of servers that the bot is in is calculated using `guilds` method which returns a list of servers
`await` we use in asynchronous enviroments

**Step 6 ** : Event when a user joins a server

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

What the above code basically does is, add this user to the server's `json` file where their data will be stored. This code is not necessary but makes your life easier if you don't want any `dictionary key` or `file not found` errors

**Step 7 ** : Event when a user messages in a server.

```Python

@bot.event #again an event
async def on_message(message): #predefined event when a user messages
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
        users[f'{user.id}']['sage_spell'] = False
        users[f'{user.id}']['hunter_spell'] = False
        users[f'{user.id}']['wraith_spell'] = False
        users[f'{user.id}']['chameleon'] = False
        users[f'{user.id}']['transformation'] = False
        
        #creating the dictionary's where the data will be stored
        
        
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


**Step 8 ** : Last but not the least, running the bot

```Python

bot.run("token")

```

*Note* : replace `token` with your bot token

#level.py
