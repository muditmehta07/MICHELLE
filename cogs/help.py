'''

Help

'''

import discord
from discord.ext import commands
import os
import random
import datetime
import json
from discord import message
from discord.ext.commands.context import Context

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(color = color, timestamp=datetime.datetime.utcnow())
        embed.add_field(name = "General 🎄", value = f"`{get_prefix}help general`")
        embed.add_field(name = "Level 📈", value = f"`{get_prefix}help level`")
        embed.add_field(name = "Fun 😁", value = f"`{get_prefix}help fun`")
        embed.add_field(name = "Casual 🏠", value = f"`{get_prefix}help casual`")
        embed.add_field(name = "Image 🖼️", value = f"`{get_prefix}help image`")
        embed.add_field(name = "Translate 🔤", value = f"`{get_prefix}help translate`")
        embed.add_field(name = "Store 💰", value = f"`{get_prefix}help store`")
        embed.add_field(name = "Theme 🎡", value = f"`{get_prefix}help theme`")
        embed.add_field(name = "Info ℹ️", value = f"`{get_prefix}help info`")

        try:
            with open("./local/auth.json", 'r') as f:
                auth = json.load(f)

            if message.author.id == 488996680058798081:
                embed.add_field(name = "Developer 🧑🏻‍💻", value = f"`{get_prefix}help dev`")
            
            if auth[f"{id}"]["auth"] == True:
                embed.add_field(name = "Auth ✅", value = f"`{get_prefix}help auth`")
        except:
            print("")

        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(text = "For more info go to 'Info ℹ️'")
        embed.set_author(name = 'Michelle Help Commands', icon_url = self.bot.user.avatar_url)

        await message.channel.send(embed = embed)

    @help.command(aliases = ["INFO", "Info"])
    async def info(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(title = "Info ℹ️",
        description =f"**Invite 💌** : `{get_prefix}invite`\n**Change Prefix ❕** : `{get_prefix}prefix <new prefix>`\n**Server Info 🧾** : `{get_prefix}server`\n**User Info 🙎🏻** : `{get_prefix}user`\n**Feedback 🆘** : `{get_prefix}feedback`" ,
        color = color,
        timestamp=datetime.datetime.utcnow())
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)

        await message.channel.send(embed = embed)

    @help.command()
    async def dev(self, message):
        id = message.author.id

        if id == 488996680058798081:
            guildid = message.channel.guild.id
            guildid = './guild data/'+ str(guildid) +'.json'
            with open(guildid, 'r') as f:
                users = json.load(f)

            color = users[str(id)]['color']

            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(message.guild.id) in L:
                get_prefix = L[str(message.guild.id)]["prefix"]
            elif str(message.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(title = "Developer 🧑🏻‍💻",
            description =f"**List of Servers** : `{get_prefix}guilds`\n**Authorise/Deauthorise** : `{get_prefix}authorise <user>` `{get_prefix}deauthorise <user>`\n**Send and Update Report** : `{get_prefix}sendreport` `{get_prefix}updatereport`\n**Send and Update Auth** : `{get_prefix}sendauth` `{get_prefix}updateauth`\n**Send and Update Confess** : `{get_prefix}sendconfess` `{get_prefix}updateconfess`\n**Send and Update Welcome** : `{get_prefix}sendwelcome` `{get_prefix}updatewelcome`\n**Send and Update Prefix** : `{get_prefix}sendprefix` `{get_prefix}updateprefix`\n**Send and Update React** : `{get_prefix}sendreact` `{get_prefix}updatereact`\n**Send and Update Roast** : `{get_prefix}sendroast` `{get_prefix}updateroast`\n**Send and Update Guild** : `{get_prefix}sendguild` `{get_prefix}updateguild`\n",
            color = color,
            timestamp=datetime.datetime.utcnow())
            embed.set_author(name = message.author, icon_url = message.author.avatar_url)

            await message.channel.send(embed = embed)

    @help.command()
    async def auth(self, message):
        id = message.author.id

        with open("./local/auth.json", 'r') as f:
            auth = json.load(f)

        if str(id) in auth:
            guildid = message.channel.guild.id
            guildid = './guild data/'+ str(guildid) +'.json'
            with open(guildid, 'r') as f:
                users = json.load(f)

            color = users[str(id)]['color']

            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(message.guild.id) in L:
                get_prefix = L[str(message.guild.id)]["prefix"]
            elif str(message.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(title = "Auth ✅",
            description =f"**SetXP** : `{get_prefix}setxp <user> <xp>`\n**Listening** : `{get_prefix}listening <status>`\n**Playing** : `{get_prefix}playing <status>`\n**Watching** : `{get_prefix}watching <status>`\n**Default** : `{get_prefix}default <status>`\n",
            color = color,
            timestamp=datetime.datetime.utcnow())
            embed.set_author(name = message.author, icon_url = message.author.avatar_url)

            await message.channel.send(embed = embed)

    @help.command(aliases = ["General", "GENERAL", "normal"])
    async def general(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(title = "General 🎄", 
        description=f"`{get_prefix}reaction` : *Reaction Roles*\n`{get_prefix}welcome <custom msg>` : *Set the channel as 'welcome channel'*\n`{get_prefix}confess` : *Set the channel as 'confession channel'*\n`{get_prefix}delwelcome` : *Remove the set 'welcome channel'*\n`{get_prefix}delconfess` : *Remove the set 'confession channel'*\n`{get_prefix}embed <msg>` : *Embed your message*\n`{get_prefix}hi` : *Send me* __{get_prefix}hi__ *in DM for info*" , 
        color = color, 
        timestamp=datetime.datetime.utcnow())

        embed.set_footer(text = "`welcome` and `confess` needs admin permissions")
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        await message.channel.send(embed = embed)

    @help.command()
    async def casual(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(title = "Casual 🏠",
        color = color, 
        timestamp=datetime.datetime.utcnow())

        embed.add_field(name = "Wikipedia 🔍", value = f"`{get_prefix}help wiki`")
        embed.add_field(name = "Reddit 😜", value = f"`{get_prefix}help reddit`")
        embed.add_field(name = "YouTube 📺", value = f"`{get_prefix}help yt`")

        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        await message.channel.send(embed = embed)

    @help.command()
    async def translate(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(title = "Translate 🔤",
        description = f"`{get_prefix}lang` : *List of languages with codes*\n`{get_prefix}detect <text>` : *Detect the given text's language*\n`{get_prefix}tr <text> <to code>` : *Translate text to the given code's language*\n`{get_prefix}morse <text>` : *Convert text into morse*\n`{get_prefix}unmorse <text>` : *Convert morse into text*\n`{get_prefix}groot <text>` : *Convert text into groot*",
        color = color, 
        timestamp=datetime.datetime.utcnow())

        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        await message.channel.send(embed = embed)

    @help.command()
    async def reddit(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(title = "Reddit 😜", 
        description=f"`{get_prefix}reddit <subreddit>` : *Get a post from a specific Subreddit*\n`{get_prefix}meme <category>` : *Get a meme of a desired category*" , 
        color = color, 
        timestamp=datetime.datetime.utcnow())

        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        await message.channel.send(embed = embed)

    @help.command(name = "yt", aliases = ["youtube"])
    async def yt(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(title = "YouTube 📺", 
        description=f"`{get_prefix}yt <query>` : *Search a YouTube Video*" , 
        color = color, 
        timestamp=datetime.datetime.utcnow())

        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        await message.channel.send(embed = embed)

    @help.command()
    async def wiki(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(title = "Wikipedia 🔍", 
        description=f"`{get_prefix}wiki? <query>` : *Search on Wikipedia*\n`{get_prefix}wiki <query>` : *Get Wikipedia results*" , 
        color = color, 
        timestamp=datetime.datetime.utcnow())

        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        await message.channel.send(embed = embed)

    @help.command()
    async def fun(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(title = "Fun 😁", 
        description=f"`{get_prefix}meme <category>` : *Get a meme of desired category*\n`{get_prefix}roast <user>` : *Roast a user*\n`{get_prefix}kill <user>` : *Kill a user, drops their XP and raises yours*" ,
        color = color, 
        timestamp=datetime.datetime.utcnow())

        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        await message.channel.send(embed = embed)

    @help.command()
    async def image(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(title = "Image 🖼️", 
        description=f"`{get_prefix}hug <user>` : *Hug a user*\n`{get_prefix}kiss <user>` : *Kiss a user*\n`{get_prefix}slap <user>` : *Slap a user*\n`{get_prefix}monster` : *Sends the Vision meme*" ,
        color = color, 
        timestamp=datetime.datetime.utcnow())

        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        await message.channel.send(embed = embed)

    @help.command(aliases = ["Level", "LEVEL", "rank"])
    async def level(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(title = "Level 📈", 
        description=f"`{get_prefix}level` : *Your level card*\n`{get_prefix}level <user>` : *User's level*\n`{get_prefix}leader` : *Leaderboard (Rank 1-5)*\n`{get_prefix}leader2` : *Leaderboard (Rank 6-10)*",
        color = color, 
        timestamp=datetime.datetime.utcnow())

        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        await message.channel.send(embed = embed)

    @help.command(aliases = ["color", "colour"])
    async def theme(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(title = "Theme 🎡", 
        description = f"`{get_prefix}light` : *Light Themes* 🤍\n`{get_prefix}dark` : *Dark Themes* 🖤", 
        color = color, 
        timestamp=datetime.datetime.utcnow())

        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        await message.channel.send(embed = embed)

    @help.command(aliases = ["shop"])
    async def store(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(title = "Store Commands 💰", 
        description = f"`{get_prefix}item` : *Your Inventory*\n`{get_prefix}item spells` : *Spells*\n`{get_prefix}item jutsu` : *Jutsu*\n`{get_prefix}item ability` : *Abilities*\n`{get_prefix}buy` : *Buy an item*\n`{get_prefix}sell` : *Sell an item*" , 
        color = color, 
        timestamp=datetime.datetime.utcnow())

        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        await message.channel.send(embed = embed)

    @help.command()
    async def sage(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(title = "Sage Spell ✨", description = f"**Makes you invulnerable, you cannot be killed or robbed**\n\n`{get_prefix}gift <user> <lvl>` - *Gift your levels to someone*", timestamp=datetime.datetime.utcnow(), color = color)
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        await message.channel.send(content = f'{message.author.mention}', embed = embed)

    @help.command()
    async def hunter(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(title = "Hunter Spell 🏹", description = f"**become a predator and hunt other spell users**\n\n`{get_prefix}seek` - *get a list of sage and wraith spell users*\n`{get_prefix}hunt <user>` - *drop 2 levels of a sage/wraith spell user at the cost of your 1 level*", timestamp = datetime.datetime.utcnow(), color = color)
        await message.channel.send(content = f'{message.author.mention}', embed = embed)

def setup(bot):
    bot.add_cog(HelpCog(bot))
