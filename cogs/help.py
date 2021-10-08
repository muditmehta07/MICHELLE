import discord
from discord.ext import commands
import os
import random
import datetime
import json
from discord import message
from discord.ext.commands.context import Context

from discord.ext import commands
from discord.ext.commands.core import command
from discord.utils import get

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Help Command
    @commands.group(invoke_without_command=True)
    async def help(self, message):
        await message.channel.trigger_typing()
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

        tips = [f"Use `{get_prefix}michelle` to know about me", f"Use `{get_prefix}daily` to get Daily Reward", f"[Invite Me](https://discordapp.com/oauth2/authorize?client_id=840180379389263882&permissions=4228906231&scope=bot%20applications.commands) to get 1M XP", f"Use `{get_prefix}feedback` to give a review", f"[Vote Me](https://top.gg/bot/840180379389263882/vote) to make me popular", f"Use `{get_prefix}prefix` to set server prefix"]
        protip = random.choice(tips)

        with open("./local/settings.json") as s:
            set = json.load(s)

        emojigeneral = self.bot.get_emoji(880688858445013032)
        emojilevel = self.bot.get_emoji(880689068613189653)
        emojifun = self.bot.get_emoji(880689402567884821)
        emojishop = self.bot.get_emoji(880689176268374037)
        emojiimage = self.bot.get_emoji(880689143359868999)
        emojicasual = self.bot.get_emoji(880689293226557470)
        emojitheme = self.bot.get_emoji(880689337853947966)
        emojiinfo = self.bot.get_emoji(880689203179036672)
        emojisettings = self.bot.get_emoji(880689241724686346)
        emojidev = self.bot.get_emoji(880689362721972224)
        emojiauth = self.bot.get_emoji(880689269000241212)
        emojistatus = self.bot.get_emoji(880689107276296223)

        if str(message.author.id) in set:
            if set[f"{message.author.id}"]["tips"] == True:
                embed = discord.Embed(description = f"**PROTIP** : {protip}", color = color, timestamp=datetime.datetime.utcnow())
                embed.add_field(name = f"{emojigeneral} General", value = f"`{get_prefix}general`")
                embed.add_field(name = f"{emojilevel} Level", value = f"`{get_prefix}leveling`")
                embed.add_field(name = f"{emojifun} Fun", value = f"`{get_prefix}fun`")
                embed.add_field(name = f"{emojishop} Store", value = f"`{get_prefix}store`")
                embed.add_field(name = f"{emojiimage} Image", value = f"`{get_prefix}image`")
                embed.add_field(name = f"{emojicasual} Casual", value = f"`{get_prefix}casual`")
                embed.add_field(name = f"{emojitheme} Theme", value = f"`{get_prefix}theme`")
                embed.add_field(name = f"{emojiinfo} Info", value = f"`{get_prefix}info`")
                embed.add_field(name = f"{emojisettings} Settings", value = f"`{get_prefix}settings`")

                try:
                    with open("./local/auth.json", 'r') as f:
                        auth = json.load(f)

                    if message.author.id == 488996680058798081:
                        embed.add_field(name = f"{emojidev} Developer", value = f"`{get_prefix}dev`")
                    
                    if auth[f"{id}"]["auth"] == True:
                        embed.add_field(name = f"{emojiauth} Auth", value = f"`{get_prefix}auth`")
                        embed.add_field(name = f"{emojistatus} Status", value = f"`{get_prefix}status`")
                except:
                    print("")

                embed.set_thumbnail(url=self.bot.user.avatar_url)
                embed.set_author(name = 'Michelle Help Commands', icon_url = self.bot.user.avatar_url)

                await message.channel.send(embed = embed)

            else:
                embed = discord.Embed(color = color, timestamp=datetime.datetime.utcnow())

                embed.add_field(name = f"{emojigeneral} General", value = f"`{get_prefix}general`")
                embed.add_field(name = f"{emojilevel} Level", value = f"`{get_prefix}leveling`")
                embed.add_field(name = f"{emojifun} Fun", value = f"`{get_prefix}fun`")
                embed.add_field(name = f"{emojishop} Store", value = f"`{get_prefix}store`")
                embed.add_field(name = f"{emojiimage} Image", value = f"`{get_prefix}image`")
                embed.add_field(name = f"{emojicasual} Casual", value = f"`{get_prefix}casual`")
                embed.add_field(name = f"{emojitheme} Theme", value = f"`{get_prefix}theme`")
                embed.add_field(name = f"{emojiinfo} Info", value = f"`{get_prefix}info`")
                embed.add_field(name = f"{emojisettings} Settings", value = f"`{get_prefix}settings`")

                try:
                    with open("./local/auth.json", 'r') as f:
                        auth = json.load(f)

                    if message.author.id == 488996680058798081:
                        embed.add_field(name = f"{emojidev} Developer", value = f"`{get_prefix}dev`")
                    
                    if auth[f"{id}"]["auth"] == True:
                        embed.add_field(name = f"{emojiauth} Auth", value = f"`{get_prefix}auth`")
                        embed.add_field(name = f"{emojistatus} Status", value = f"`{get_prefix}status`")
                except:
                    print("")

                embed.set_thumbnail(url=self.bot.user.avatar_url)
                embed.set_author(name = 'Michelle Help Commands', icon_url = self.bot.user.avatar_url)

                await message.channel.send(embed = embed)

        else:
            embed = discord.Embed(description = f"**PROTIP** : {protip}", color = color, timestamp=datetime.datetime.utcnow())
            embed.add_field(name = f"{emojigeneral} General", value = f"`{get_prefix}general`")
            embed.add_field(name = f"{emojilevel} Level", value = f"`{get_prefix}leveling`")
            embed.add_field(name = f"{emojifun} Fun", value = f"`{get_prefix}fun`")
            embed.add_field(name = f"{emojishop} Store", value = f"`{get_prefix}store`")
            embed.add_field(name = f"{emojiimage} Image", value = f"`{get_prefix}image`")
            embed.add_field(name = f"{emojicasual} Casual", value = f"`{get_prefix}casual`")
            embed.add_field(name = f"{emojitheme} Theme", value = f"`{get_prefix}theme`")
            embed.add_field(name = f"{emojiinfo} Info", value = f"`{get_prefix}info`")
            embed.add_field(name = f"{emojisettings} Settings", value = f"`{get_prefix}settings`")

            try:
                with open("./local/auth.json", 'r') as f:
                    auth = json.load(f)

                if message.author.id == 488996680058798081:
                    embed.add_field(name = f"{emojidev} Developer", value = f"`{get_prefix}dev`")
                
                if auth[f"{id}"]["auth"] == True:
                    embed.add_field(name = f"{emojiauth} Auth", value = f"`{get_prefix}auth`")
                    embed.add_field(name = f"{emojistatus} Status", value = f"`{get_prefix}status`")
            except:
                print("")

            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_author(name = 'Michelle Help Commands', icon_url = self.bot.user.avatar_url)

            await message.channel.send(embed = embed)

    @commands.command()
    async def casual(self, message):
        await message.channel.trigger_typing()
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

        embed = discord.Embed(
            color = color,
            timestamp=datetime.datetime.utcnow())

        embed.add_field(name = "🔤 Translate", value = f"`{get_prefix}translate`")
        embed.add_field(name = "🔍 Wikipedia", value = f"`{get_prefix}help wiki`")
        embed.add_field(name = "😜 Reddit", value = f"`{get_prefix}help reddit`")
        embed.add_field(name = "📺 YouTube", value = f"`{get_prefix}help yt`")

        embed.set_author(name = f"Casual", icon_url = "https://cdn.discordapp.com/emojis/880689293226557470.png?v=1")

        await message.channel.send(embed = embed)


    #General
    @commands.command(aliases = ["General", "GENERAL"])
    async def general(self, message):
        await message.channel.trigger_typing()
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

        tips = [f"Use `{get_prefix}hi` for DM Commands"]
        protip = random.choice(tips)

        with open("./local/settings.json") as s:
            set = json.load(s)

        if str(message.author.id) in set:
            if set[f"{message.author.id}"]["tips"] == True:
                embed = discord.Embed(description = f"**PROTIP** : {protip}", color = color, timestamp=datetime.datetime.utcnow())
                embed.add_field(name = "🥷🏻 Confession", value = f"`{get_prefix}help confess`")
                embed.add_field(name = "❣️ Custom Pings", value = f"`{get_prefix}ping`")
                embed.add_field(name = "📱 DM", value = f"`{get_prefix}hi`")
                embed.add_field(name = "📥 Embed", value = f"`{get_prefix}embed`")
                embed.add_field(name = "👆🏻 Reaction Roles", value = f"`{get_prefix}reaction`")
                embed.add_field(name = "🙏🏻 Welcome", value = f"`{get_prefix}help welcome`")
                
                embed.set_author(name = f"General", icon_url = "https://cdn.discordapp.com/emojis/880688858445013032.png?v=1")
                await message.channel.send(embed = embed)

            else:
                embed = discord.Embed(color = color, timestamp=datetime.datetime.utcnow())

                embed.add_field(name = "🥷🏻 Confession", value = f"`{get_prefix}help confess`")
                embed.add_field(name = "❣️ Custom Pings", value = f"`{get_prefix}ping`")
                embed.add_field(name = "📱 DM", value = f"`{get_prefix}hi`")
                embed.add_field(name = "📥 Embed", value = f"`{get_prefix}embed`")
                embed.add_field(name = "👆🏻 Reaction Roles", value = f"`{get_prefix}reaction`")
                embed.add_field(name = "🙏🏻 Welcome", value = f"`{get_prefix}help welcome`")
                
                embed.set_author(name = f"General", icon_url = "https://cdn.discordapp.com/emojis/880688858445013032.png?v=1")
                await message.channel.send(embed = embed)

        else:
            embed = discord.Embed(description = f"**PROTIP** : {protip}", color = color, timestamp=datetime.datetime.utcnow())
            embed.add_field(name = "🥷🏻 Confession", value = f"`{get_prefix}help confess`")
            embed.add_field(name = "❣️ Custom Pings", value = f"`{get_prefix}ping`")
            embed.add_field(name = "📱 DM", value = f"`{get_prefix}hi`")
            embed.add_field(name = "📥 Embed", value = f"`{get_prefix}embed`")
            embed.add_field(name = "👆🏻 Reaction Roles", value = f"`{get_prefix}reaction`")
            embed.add_field(name = "🙏🏻 Welcome", value = f"`{get_prefix}help welcome`")
            
            embed.set_author(name = f"General", icon_url = "https://cdn.discordapp.com/emojis/880688858445013032.png?v=1")
            await message.channel.send(embed = embed)


    #Welcome
    @help.command()
    async def welcome(self, message):
        await message.channel.trigger_typing()
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

        embed = discord.Embed(
            description = f"**Permissions** : `Administrator`\n\n**Usage** :\n`{get_prefix}welcome <optional message>` : Use this command in a channel that you want to set as your *welcome channel*. If the *optional message* is left blank, the default message will be used instead. The optional message replaces the default messsage if provided.\n\n`{get_prefix}delwelcome` : Use this command in your *welcome channel* so that I stop sending *welcome messages*" , 
            color = color, 
            timestamp=datetime.datetime.utcnow())

        embed.set_author(name = "Welcome Help ❓", icon_url = self.bot.user.avatar_url)
        await message.channel.send(embed = embed)


    #Confession
    @help.command()
    async def confess(self, message):
        await message.channel.trigger_typing()
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

        embed = discord.Embed(
            description = f"**Permissions** : `Administrator`\n\n**Usage** :\n`{get_prefix}confess` : Use this command in a channel that you want to set as your *confession channel*. \n\n`{get_prefix}delconfess` : Use this command in your *confess channel* so that I stop sending *confession messages*\n\n`{get_prefix}hi` : I will send you a DM with instructions about how to create a *confession message*" , 
            color = color, 
            timestamp=datetime.datetime.utcnow())

        embed.set_author(name = "Confession Help ❓", icon_url = self.bot.user.avatar_url)
        await message.channel.send(embed = embed)


    #Info
    @commands.command(aliases = ["INFO", "Info"])
    async def info(self, message):
        await message.channel.trigger_typing()
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

        embed = discord.Embed(
            description = f"About Michelle : `{get_prefix}michelle`",
            color = color,
            timestamp=datetime.datetime.utcnow())

        embed.add_field(name = "🙎🏻 Profile", value = f"`{get_prefix}profile`")
        embed.add_field(name = "📃 Server", value = f"`{get_prefix}server`")
        embed.add_field(name = "💌 Invite", value = f"`{get_prefix}invite`")
        embed.add_field(name = "☝🏻 Vote", value = f"`{get_prefix}vote`")
        embed.add_field(name = "❕ Prefix", value = f"`{get_prefix}prefix`")
        embed.add_field(name = "📟 Feedback", value = f"`{get_prefix}feedback`")

        embed.set_author(name = f"Info", icon_url = "https://cdn.discordapp.com/emojis/880689203179036672.png?v=1")

        await message.channel.send(embed = embed)


    #Developer
    @commands.command()
    async def dev(self, message):
        await message.channel.trigger_typing()
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

            embed = discord.Embed(
                description =f"**Auth Users** : `{get_prefix}authlist`\n**Authorise/Deauthorise** : `{get_prefix}authorise <user>` `{get_prefix}deauthorise <user>`\n**Send and Update Report** : `{get_prefix}sendreport` `{get_prefix}updatereport`\n**Send and Update Auth** : `{get_prefix}sendauth` `{get_prefix}updateauth`\n**Send and Update Confess** : `{get_prefix}sendconfess` `{get_prefix}updateconfess`\n**Send and Update Welcome** : `{get_prefix}sendwelcome` `{get_prefix}updatewelcome`\n**Send and Update Prefix** : `{get_prefix}sendprefix` `{get_prefix}updateprefix`\n**Send and Update React** : `{get_prefix}sendreact` `{get_prefix}updatereact`\n**Send and Update Roast** : `{get_prefix}sendroast` `{get_prefix}updateroast`\n**Send and Update Guild** : `{get_prefix}sendguild` `{get_prefix}updateguild`\n**Send and Update P Ping** : `{get_prefix}sendping` `{get_prefix}updateping`\n**Send and Update S Pings** : `{get_prefix}sendpings` `{get_prefix}updatepings`\n**Send and Update Pings** : `{get_prefix}sendstatus` `{get_prefix}updatestatus`\n**Send and Update Invite** : `{get_prefix}sendinvite` `{get_prefix}updateinvite`\n**Send and Update Items** : `{get_prefix}senditems` `{get_prefix}updateitems`",
                color = color,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = f"Developer", icon_url = "https://cdn.discordapp.com/emojis/880689362721972224.png?v=1")

            await message.channel.send(embed = embed)


    #Status
    @commands.command()
    async def status(self, message):
        await message.channel.trigger_typing()
        id = message.author.id

        with open("./local/auth.json", 'r') as f:
            auth = json.load(f)

        if str(id) in auth:
            if auth[f"{id}"]["auth"] == True:
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

                embed = discord.Embed(
                    description =f"**Listening** : `{get_prefix}listening`\n**Playing** : `{get_prefix}playing`\n**Watching** : `{get_prefix}watching`\n**Default** : `{get_prefix}default`",
                    color = color,
                    timestamp=datetime.datetime.utcnow())
        
                embed.set_author(name = f"Status", icon_url = "https://cdn.discordapp.com/emojis/880689107276296223.png?v=1")

                await message.channel.send(embed = embed)


    #Auth
    @commands.command()
    async def auth(self, message):
        await message.channel.trigger_typing()
        id = message.author.id

        with open("./local/auth.json", 'r') as f:
            auth = json.load(f)

        if str(id) in auth:
            if auth[f"{id}"]["auth"] == True:
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

                embed = discord.Embed(
                    description =f"**SetXP** : `{get_prefix}setxp <user> <xp>`",
                    color = color,
                    timestamp=datetime.datetime.utcnow())

                embed.set_author(name = f"Auth", icon_url = "https://cdn.discordapp.com/emojis/880689269000241212.png?v=1")

                await message.channel.send(embed = embed)


    #Translate
    @commands.command()
    async def translate(self, message):
        await message.channel.trigger_typing()
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

        embed = discord.Embed(
            description = f"`{get_prefix}lang` : *List of languages with codes*\n`{get_prefix}detect <text>` : *Detect the given text's language*\n`{get_prefix}tr <text> <to code>` : *Translate text to the given code's language*\n`{get_prefix}morse <text>` : *Convert text into morse*\n`{get_prefix}unmorse <text>` : *Convert morse into text*\n`{get_prefix}groot <text>` : *Convert text into groot*",
            color = color, 
            timestamp=datetime.datetime.utcnow())

        embed.set_author(name = "Translate 🔤", icon_url = "https://cdn.discordapp.com/emojis/880689293226557470.png?v=1")
        await message.channel.send(embed = embed)


    #Reddit
    @help.command()
    async def reddit(self, message):
        await message.channel.trigger_typing()
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

        embed = discord.Embed(
            description=f"`{get_prefix}reddit <subreddit>` : *Get a post from a specific Subreddit*\n`{get_prefix}meme <category>` : *Get a meme of a desired category*" , 
            color = color, 
            timestamp=datetime.datetime.utcnow())

        embed.set_author(name = "Reddit 😜", icon_url = "https://cdn.discordapp.com/emojis/880689293226557470.png?v=1")
        await message.channel.send(embed = embed)


    #YouTube
    @help.command(name = "yt", aliases = ["youtube"])
    async def yt(self, message):
        await message.channel.trigger_typing()
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

        embed = discord.Embed(
            description=f"`{get_prefix}yt <query>` : *Search a YouTube Video*" , 
            color = color, 
            timestamp=datetime.datetime.utcnow())

        embed.set_author(name = "YouTube 📺", icon_url = "https://cdn.discordapp.com/emojis/880689293226557470.png?v=1")
        await message.channel.send(embed = embed)


    #Wikipedia
    @help.command()
    async def wiki(self, message):
        await message.channel.trigger_typing()
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

        embed = discord.Embed(
            description=f"`{get_prefix}wiki? <query>` : *Search on Wikipedia*\n`{get_prefix}wiki <query>` : *Get Wikipedia results*" , 
            color = color, 
            timestamp=datetime.datetime.utcnow())

        embed.set_author(name = "Wikipedia 🔍", icon_url = "https://cdn.discordapp.com/emojis/880689293226557470.png?v=1")
        await message.channel.send(embed = embed)


    #Fun
    @commands.command()
    async def fun(self, message):
        await message.channel.trigger_typing()
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

        with open("./local/settings.json") as s:
            set = json.load(s)

        if str(message.author.id) in set:
            if set[f"{message.author.id}"]["tips"] == True:
                embed = discord.Embed(description = f"**PROTIP** : Use `{get_prefix}help <command>` for info", color = color, timestamp=datetime.datetime.utcnow())

                embed.add_field(name="😂 Meme", value=f"`{get_prefix}meme`")
                embed.add_field(name="🔥 Roast", value=f"`{get_prefix}roast`")
                embed.add_field(name="🔪 Kill", value=f"`{get_prefix}kill`")
                embed.add_field(name="🎲 Dice", value=f"`{get_prefix}dice`")
                embed.add_field(name="🎱 8 Ball", value=f"`{get_prefix}8ball`")
                embed.add_field(name="🪙 Coin Flip", value=f"`{get_prefix}flip`")

                embed.set_author(name = f"Fun", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
                await message.channel.send(embed = embed)

            else:
                embed = discord.Embed(color = color, timestamp=datetime.datetime.utcnow())

                embed.add_field(name="😂 Meme", value=f"`{get_prefix}meme`")
                embed.add_field(name="🔥 Roast", value=f"`{get_prefix}roast`")
                embed.add_field(name="🔪 Kill", value=f"`{get_prefix}kill`")
                embed.add_field(name="🎲 Dice", value=f"`{get_prefix}dice`")
                embed.add_field(name="🎱 8 Ball", value=f"`{get_prefix}8ball`")
                embed.add_field(name="🪙 Coin Flip", value=f"`{get_prefix}flip`")

                embed.set_author(name = f"Fun", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
                await message.channel.send(embed = embed)

        else:
            embed = discord.Embed(description = f"**PROTIP** : Use `{get_prefix}help <command>` for info", color = color, timestamp=datetime.datetime.utcnow())

            embed.add_field(name="😂 Meme", value=f"`{get_prefix}meme`")
            embed.add_field(name="🔥 Roast", value=f"`{get_prefix}roast`")
            embed.add_field(name="🔪 Kill", value=f"`{get_prefix}kill`")
            embed.add_field(name="🎲 Dice", value=f"`{get_prefix}dice`")
            embed.add_field(name="🎱 8 Ball", value=f"`{get_prefix}8ball`")
            embed.add_field(name="🪙 Coin Flip", value=f"`{get_prefix}flip`")

            embed.set_author(name = f"Fun", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await message.channel.send(embed = embed)


    #Meme
    @help.command()
    async def meme(self, message):
        await message.channel.trigger_typing()
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

        embed = discord.Embed(
            description = f"**Description** : Sends a meme of the desired category using Reddit's API. If category is not specified, it uses `meme` subreddit\n\n**Usage** : `{get_prefix}meme <optional category>`\n**Example** : `{get_prefix}meme marvel` to get a Marvel Meme" , 
            color = color, 
            timestamp=datetime.datetime.utcnow())

        embed.set_author(name = "Meme Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
        await message.channel.send(embed = embed)


    #Roast
    @help.command()
    async def roast(self, message):
        await message.channel.trigger_typing()
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

        embed = discord.Embed(
            description = f"**Description** : Roasts the mentioned user\n\n**Usage** : `{get_prefix}roast <user mention>`\n**Example** : `{get_prefix}roast @user` to roast a user" , 
            color = color, 
            timestamp=datetime.datetime.utcnow())

        embed.set_author(name = "Roast Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
        await message.channel.send(embed = embed)


    #Kill
    @help.command()
    async def kill(self, message):
        await message.channel.trigger_typing()
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

        embed = discord.Embed(
            description = f"**Description** : Kills the mentioned user. Killing a user drops their XP and raises yours. You may also fail to kill them which would drop your XP and raise their's\n\n**Usage** : `{get_prefix}kill <user mention>`\n**Example** : `{get_prefix}kill @user` to kill a user" , 
            color = color, 
            timestamp=datetime.datetime.utcnow())

        embed.set_author(name = "Kill Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
        await message.channel.send(embed = embed)


    #Image
    @commands.command(aliases = ["images"])
    async def image(self, message):
        await message.channel.trigger_typing()
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

        with open("./local/settings.json") as s:
            set = json.load(s)

        if str(message.author.id) in set:
            if set[f"{message.author.id}"]["tips"] == True:
                embed = discord.Embed(description = f"**PROTIP** : Use `{get_prefix}help <command>` for info", color = color, timestamp=datetime.datetime.utcnow())

                embed.add_field(name="🫂 Hug", value=f"`{get_prefix}hug`")
                embed.add_field(name="👩‍❤️‍💋‍👨 Kiss", value=f"`{get_prefix}kiss`")
                embed.add_field(name="🤚🏻 Slap", value=f"`{get_prefix}slap`")

                embed.set_author(name = f"Image", icon_url = "https://cdn.discordapp.com/emojis/880689143359868999.png?v=1")
                await message.channel.send(embed = embed)

            else:
                embed = discord.Embed(color = color, timestamp=datetime.datetime.utcnow())

                embed.add_field(name="🫂 Hug", value=f"`{get_prefix}hug`")
                embed.add_field(name="👩‍❤️‍💋‍👨 Kiss", value=f"`{get_prefix}kiss`")
                embed.add_field(name="🤚🏻 Slap", value=f"`{get_prefix}slap`")

                embed.set_author(name = f"Image", icon_url = "https://cdn.discordapp.com/emojis/880689143359868999.png?v=1")
                await message.channel.send(embed = embed)
        else:
            embed = discord.Embed(description = f"**PROTIP** : Use `{get_prefix}help <command>` for info", color = color, timestamp=datetime.datetime.utcnow())

            embed.add_field(name="🫂 Hug", value=f"`{get_prefix}hug`")
            embed.add_field(name="👩‍❤️‍💋‍👨 Kiss", value=f"`{get_prefix}kiss`")
            embed.add_field(name="🤚🏻 Slap", value=f"`{get_prefix}slap`")

            embed.set_author(name = f"Image", icon_url = "https://cdn.discordapp.com/emojis/880689143359868999.png?v=1")
            await message.channel.send(embed = embed)


    #Hug
    @help.command()
    async def hug(self, message):
        await message.channel.trigger_typing()
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

        embed = discord.Embed(
            description = f"**Description** : Hugs the mentioned user by sending a custom image\n\n**Usage** : `{get_prefix}hug <user mention>`\n**Example** : `{get_prefix}hug @user` to hug a user" , 
            color = color, 
            timestamp=datetime.datetime.utcnow())

        embed.set_author(name = "Hug Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689143359868999.png?v=1")
        await message.channel.send(embed = embed)


    #Kiss
    @help.command()
    async def kiss(self, message):
        await message.channel.trigger_typing()
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

        embed = discord.Embed(
            description = f"**Description** : Kisses the mentioned user by sending a custom image\n\n**Usage** : `{get_prefix}kiss <user mention>`\n**Example** : `{get_prefix}kiss @user` to kiss a user" , 
            color = color, 
            timestamp=datetime.datetime.utcnow())

        embed.set_author(name = "Kiss Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689143359868999.png?v=1")
        await message.channel.send(embed = embed)


    #Slap
    @help.command()
    async def slap(self, message):
        await message.channel.trigger_typing()
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

        embed = discord.Embed(
            description = f"**Description** : Slaps the mentioned user by sending a custom image\n\n**Usage** : `{get_prefix}slap <user mention>`\n**Example** : `{get_prefix}slap @user` to slap a user" , 
            color = color, 
            timestamp=datetime.datetime.utcnow())

        embed.set_author(name = "Slap Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689143359868999.png?v=1")
        await message.channel.send(embed = embed)


    #Leveling
    @commands.command(aliases = ["Leveling", "LEVELING"])
    async def leveling(self, message):
        await message.channel.trigger_typing()
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

        with open("./local/settings.json") as s:
            set = json.load(s)

        if str(message.author.id) in set:
            if set[f"{message.author.id}"]["tips"] == True:
                embed = discord.Embed(description = f"**PROTIP** : Use `{get_prefix}help <command>` for info", color = color, timestamp=datetime.datetime.utcnow())

                embed.add_field(name = "⏫ Level", value=f"`{get_prefix}level`")
                embed.add_field(name = "📃 Leaderboard", value=f"`{get_prefix}leader`")

                embed.set_author(name = f"Leveling", icon_url = "https://cdn.discordapp.com/emojis/880689068613189653.png?v=1")
                await message.channel.send(embed = embed)

            else:
                embed = discord.Embed(color = color, timestamp=datetime.datetime.utcnow())

                embed.add_field(name = "⏫ Level", value=f"`{get_prefix}level`")
                embed.add_field(name = "📃 Leaderboard", value=f"`{get_prefix}leader`")

                embed.set_author(name = f"Leveling", icon_url = "https://cdn.discordapp.com/emojis/880689068613189653.png?v=1")
                await message.channel.send(embed = embed)

        else:
            embed = discord.Embed(description = f"**PROTIP** : Use `{get_prefix}help <command>` for info", color = color, timestamp=datetime.datetime.utcnow())

            embed.add_field(name = "⏫ Level", value=f"`{get_prefix}level`")
            embed.add_field(name = "📃 Leaderboard", value=f"`{get_prefix}leader`")

            embed.set_author(name = f"Leveling", icon_url = "https://cdn.discordapp.com/emojis/880689068613189653.png?v=1")
            await message.channel.send(embed = embed)


    #Level
    @help.command()
    async def level(self, message):
        await message.channel.trigger_typing()
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

        embed = discord.Embed(
            description = f"**Description** : Returns the level of a user\n\n**Usage** : `{get_prefix}level` to get your Level Card\n**Example** : `{get_prefix}level @user` to get user's level" , 
            color = color, 
            timestamp=datetime.datetime.utcnow())

        embed.set_author(name = "Level Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689068613189653.png?v=1")
        await message.channel.send(embed = embed)


    #Leader
    @help.command()
    async def leader(self, message):
        await message.channel.trigger_typing()
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

        embed = discord.Embed(
            description = f"**Description** : Returns the leaderboard of a guild\n\n**Usage** : `{get_prefix}leader` to get Leaderboard" , 
            color = color, 
            timestamp=datetime.datetime.utcnow())

        embed.set_author(name = "Leaderboard Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689068613189653.png?v=1")
        await message.channel.send(embed = embed)


    #Theme
    @commands.command(aliases = ["color", "colour"])
    async def theme(self, message):
        await message.channel.trigger_typing()
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

        embed = discord.Embed(
            color = color, 
            timestamp=datetime.datetime.utcnow())

        embed.add_field(name = "◻️ Light Themes", value=f"{get_prefix}light")
        embed.add_field(name = "◼️ Dark Themes", value=f"{get_prefix}dark")

        embed.set_author(name = f"Theme", icon_url = "https://cdn.discordapp.com/emojis/880689337853947966.png?v=1")
        await message.channel.send(embed = embed)


    #Store
    @commands.command(aliases = ["shop"])
    async def store(self, message):
        await message.channel.trigger_typing()
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

        embed = discord.Embed(
            color = color, 
            timestamp=datetime.datetime.utcnow())

        embed.add_field(name = "🎒 Inventory", value = f"`{get_prefix}item`")
        embed.add_field(name = "🛒 Buy", value = f"`{get_prefix}buy`")
        embed.add_field(name = "🪙 Sell", value = f"`{get_prefix}sell`")
        embed.add_field(name = "✨ Spell", value = f"`{get_prefix}item spells`")
        embed.add_field(name = "🥷🏻 Jutsu", value = f"`{get_prefix}item jutsu`")
        embed.add_field(name = "🦸🏻 Ability", value = f"`{get_prefix}item ability`")

        embed.set_author(name = f"Store", icon_url = "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
        await message.channel.send(embed = embed)


    #Michelle
    @commands.command(aliases = ["help michelle", "Michelle", "help Michelle", "MICHELLE"])
    async def michelle(self, message):
        await message.channel.trigger_typing()
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

        embed = discord.Embed(
            description = f"**Michelle is a multipurpose bot with a Leveling System, Fun and much more!**\nUse `{get_prefix}help` for a list of all commands.",
            color = color, 
            timestamp=datetime.datetime.utcnow())

        embed.add_field(name = "__Patch Notes 0.8__", value = f"• **Feature** : Weapons added to kill command\n"
        f"• **Bug Fix** : Profile info displayed incorrectly.\n\n"
        f"[Website](https://top.gg/bot/840180379389263882)  •  [Invite](https://discordapp.com/oauth2/authorize?client_id=840180379389263882&permissions=4228906231&scope=bot%20applications.commands)  •  [Beta](https://discordapp.com/oauth2/authorize?client_id=840521197699072020&permissions=4228906231&scope=bot%20applications.commands)  •  [Vote](https://top.gg/bot/840180379389263882/vote)", inline=False)

        embed.set_author(name ="About Michelle", icon_url = self.bot.user.avatar_url)
        await message.channel.send(embed = embed)


    #Sage
    @help.command()
    async def sage(self, message):
        await message.channel.trigger_typing()
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

        file = discord.File("./pictures/sage.png")

        embed = discord.Embed(description = f"Makes you invulnerable, you cannot be killed or kill a user. But you can be hunted by a **Hunter Spell** user\n**Price** : `50,000 XP` • **Buy** : `{get_prefix}buy sage`\n\n__**Exclusive Command**__\n`{get_prefix}gift <user> <level>` - Gift your levels to a user", timestamp=datetime.datetime.utcnow(), color = color)
        embed.set_author(name =  "Sage Spell", icon_url = "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
        embed.set_thumbnail(url="attachment://sage.png")
        await message.channel.send(file=file, embed = embed)


    #Hunter
    @help.command()
    async def hunter(self, message):
        await message.channel.trigger_typing()
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

        file = discord.File("./pictures/hunter.png")
        embed = discord.Embed(description = f"Become a predator and hunt other spell users\n**Price** : `20,000 XP` • **Buy** : `{get_prefix}buy hunter`\n\n__**Exclusive Commands**__\n`{get_prefix}seek` - Get a list of Sage & Wraith spell users\n`{get_prefix}hunt <user>` - Can only be used on Sage/Wraith Spell users\nDrops a user's 2 levels at the cost of your 1 level", timestamp = datetime.datetime.utcnow(), color = color)
        embed.set_thumbnail(url="attachment://hunter.png")
        embed.set_author(name = "Hunter Spell", icon_url = "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
        await message.channel.send(file=file, embed = embed)


    #Chameleon
    @help.command()
    async def chameleon(self, message):
        await message.channel.trigger_typing()
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

        file = discord.File("./pictures/chameleon.jpg")
        embed = discord.Embed(description = f"This Ninjutsu will hide your name from the Leaderboard\n**Price** : `10,000 XP`\n**Buy** : `{get_prefix}buy chameleon`", timestamp = datetime.datetime.utcnow(), color = color)
        embed.set_thumbnail(url="attachment://chameleon.jpg")
        embed.set_author(name = "Chameleon Jutsu", icon_url = "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
        await message.channel.send(file=file, embed = embed)


    #Transform
    @help.command(aliases = ["transformation"])
    async def transform(self, message):
        await message.channel.trigger_typing()
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

        file = discord.File("./pictures/transformation.jpg")
        embed = discord.Embed(description = f"This Ninjutsu will disguise your name on the Leaderboard\n**Price** : `12,000 XP`\n**Buy** : `{get_prefix}buy transformation`", timestamp = datetime.datetime.utcnow(), color = color)
        embed.set_thumbnail(url="attachment://transformation.jpg")
        embed.set_author(name = "Transformation Jutsu", icon_url = "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
        await message.channel.send(file=file, embed = embed)

    @commands.group(aliases = ["weapon"], invoke_without_command=True)
    async def weapons(self, ctx):
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(
            color=color, timestamp=datetime.datetime.utcnow()
        )

        embed.add_field(name="Bladed 🔪", value=f"`{get_prefix}weapons bladed`")
        #embed.add_field(name="Fictional 📺", value=f"`{get_prefix}help fictional`")
        #embed.add_field(name="Godly 😇", value=f"`{get_prefix}help godly`")
        #embed.add_field(name="Legendary 👽", value=f"`{get_prefix}help legendary`")
        embed.set_author(name="Weapon Categories ⚔️", icon_url = "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")

        await ctx.send(embed=embed)

    @weapons.command()
    async def bladed(self, message):
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

        knife = self.bot.get_emoji(881474984193703999)
        machette = self.bot.get_emoji(881478895503806464)
        dagger = self.bot.get_emoji(881478895835164682)
        sword = self.bot.get_emoji(881478895247949887)
        scythe = self.bot.get_emoji(881478895604494376)
        shuriken = self.bot.get_emoji(881478895889690674)

        embed = discord.Embed(
        color = color, timestamp=datetime.datetime.utcnow())
        embed.add_field(name=f"{knife} Knife", value=f"`{get_prefix}help knife`")
        embed.add_field(name=f"{machette} Machette", value=f"`{get_prefix}help machette`")
        embed.add_field(name=f"{dagger} Dagger", value=f"`{get_prefix}help dagger`")
        embed.add_field(name=f"{sword} Sword", value=f"`{get_prefix}help sword`")
        embed.add_field(name=f"{scythe} Scythe", value=f"`{get_prefix}help scythe`")
        embed.add_field(name=f"{shuriken} Shuriken", value=f"`{get_prefix}help shuriken`")

        embed.set_author(name = "Bladed Weapons 🔪", icon_url = "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
        await message.channel.send(embed = embed)

    '''
    @weapons.command()
    async def fictional(self, message):
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

        embed = discord.Embed(
        description=f"**Light Saber** : `{get_prefix}help lightsaber`\n\n**Riptide** : `{get_prefix}help riptide`\n\n**Elderwand** : `{get_prefix}help elderwand`\n\n**Death Note** : `{get_prefix}help deathnote`\n\n**Infinity Gauntlet** : `{get_prefix}help gauntlet`",
        color = color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name = "Fictional Weapons 📺", icon_url =  "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
        await message.channel.send(embed = embed)

    @weapons.command()
    async def godly(self, message):
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

        embed = discord.Embed(
        description=f"**Spear of Lugh** : `{get_prefix}help lugh`\n\n**Magical Katana** : `{get_prefix}help murasame`\n\n**King Arthur's Sword** : `{get_prefix}help excalibur`\n\n**Thor's Hammer** : `{get_prefix}help mjolnir`\n\n**Shiva's Trident** : `{get_prefix}help trishula`\n\n**Zeus' Bolt** : `{get_prefix}help astrape`",
        color = color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name = "Godly Weapons 😇", icon_url =  "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
        await message.channel.send(embed = embed)

    @weapons.command()
    async def legendary(self, message):
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

        embed = discord.Embed(
        description=f"🍌 **Banana** : `{get_prefix}help banana`\n\n🦶🏻 **Smelly Feet** : `{get_prefix}help feet`\n\n💉 **Cough Syrup** : `{get_prefix}help syrup`",
        color = color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name = "Legendary Weapons 👽", icon_url = "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
        await message.channel.send(embed = embed)
    '''

    @help.command()
    async def knife(self, message):
        await message.channel.trigger_typing()
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

        file = discord.File("./pictures/weapon/knife.png")
        embed = discord.Embed(description = f"**A weapon to kill**\n\nXP Drop : `0.25% XP` • Cooldown : `30sec`\nPrice : `3,000 XP` • Buy : `{get_prefix}buy knife`\n\n**Usage** : `{get_prefix}kill knife @user`", timestamp = datetime.datetime.utcnow(), color = color)
        embed.set_thumbnail(url="attachment://knife.png")
        embed.set_author(name = "Knife", icon_url = "https://cdn.discordapp.com/emojis/881474984193703999.png?v=1")
        await message.channel.send(file=file, embed = embed)

    @help.command()
    async def machette(self, message):
        await message.channel.trigger_typing()
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

        file = discord.File("./pictures/weapon/machette.png")
        embed = discord.Embed(description = f"**A weapon to kill**\n\nXP Drop : `0.5% XP` • Cooldown : `2min`\nPrice : `12,000 XP` • Buy : `{get_prefix}buy machette`\n\n**Usage** : `{get_prefix}kill machette @user`", timestamp = datetime.datetime.utcnow(), color = color)
        embed.set_thumbnail(url="attachment://machette.png")
        embed.set_author(name = "Machette", icon_url = "https://cdn.discordapp.com/emojis/881478895503806464.png?v=1")
        await message.channel.send(file=file, embed = embed)

    @help.command()
    async def dagger(self, message):
        await message.channel.trigger_typing()
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

        file = discord.File("./pictures/weapon/dagger.png")
        embed = discord.Embed(description = f"**A weapon to kill**\n\nXP Drop : `0.75% XP` • Cooldown : `5min`\nPrice : `10,000 XP` • Buy : `{get_prefix}buy dagger`", timestamp = datetime.datetime.utcnow(), color = color)
        embed.set_thumbnail(url="attachment://dagger.png")
        embed.set_author(name = "Dagger", icon_url = "https://cdn.discordapp.com/emojis/881478895835164682.png?v=1")
        await message.channel.send(file=file, embed = embed)

    @help.command()
    async def sword(self, message):
        await message.channel.trigger_typing()
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

        file = discord.File("./pictures/weapon/sword.png")
        embed = discord.Embed(description = f"**A weapon to kill**\n\nXP Drop : `1% XP` • Cooldown : `8min`\nPrice : `15,000 XP` • Buy : `{get_prefix}buy sword`", timestamp = datetime.datetime.utcnow(), color = color)
        embed.set_thumbnail(url="attachment://sword.png")
        embed.set_author(name = "Sword", icon_url = "https://cdn.discordapp.com/emojis/881478895247949887.png?v=1")
        await message.channel.send(file=file, embed = embed)

    @help.command()
    async def scythe(self, message):
        await message.channel.trigger_typing()
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

        file = discord.File("./pictures/weapon/scythe.png")
        embed = discord.Embed(description = f"**A weapon to kill**\n\nXP Drop : `1.5% XP` • Cooldown : `15min`\nPrice : `17,000 XP` • Buy : `{get_prefix}buy scythe`", timestamp = datetime.datetime.utcnow(), color = color)
        embed.set_thumbnail(url="attachment://scythe.png")
        embed.set_author(name = "Scythe", icon_url = "https://cdn.discordapp.com/emojis/881478895604494376.png?v=1")
        await message.channel.send(file=file, embed = embed)

    @help.command()
    async def shuriken(self, message):
        await message.channel.trigger_typing()
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

        file = discord.File("./pictures/weapon/shuriken.png")
        embed = discord.Embed(description = f"**A weapon to kill**\n\nXP Drop : `2% XP` • Cooldown : `30min`\nPrice : `23,000 XP` • Buy : `{get_prefix}buy shuriken`", timestamp = datetime.datetime.utcnow(), color = color)
        embed.set_thumbnail(url="attachment://shuriken.png")
        embed.set_author(name = "Shuriken", icon_url = "https://cdn.discordapp.com/emojis/881478895889690674.png?v=1")
        await message.channel.send(file=file, embed = embed)

def setup(bot):
    bot.add_cog(HelpCog(bot))