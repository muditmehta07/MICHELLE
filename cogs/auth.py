from audioop import cross
import discord
from discord.ext import commands
import os
import datetime
import json

from discord.ext.commands.context import Context

class AuthCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def authorise(self, message, member : discord.Member):
        id = message.author.id
        user = member.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if message.author.id == 488996680058798081 or message.author.id == 840129213968941096:
            with open("./local/auth.json", 'r') as f:
                auth = json.load(f)

            if not f'{user}' in auth:
                auth[f'{user}'] = {}
                auth[f'{user}']['name'] = str(member.name)
                auth[f'{user}']['auth'] = True

                with open("./local/auth.json", 'w') as f:
                    json.dump(auth, f, indent=4)
                embed = discord.Embed(description = f"{member.name} was authorised.", color = color)
                await message.channel.send(embed = embed)

            elif f'{user}' in auth:
                auth[f'{user}']['auth'] = True

                with open("./local/auth.json", 'w') as f:
                    json.dump(auth, f, indent=4)
                embed = discord.Embed(description = f"{member.name} was authorised.", color = color)
                await message.channel.send(embed = embed)

        else:
            await message.author.send(content = f'Oh! You are not authorised to use that')

    @commands.command()
    async def deauthorise(self, message, member : discord.Member):
        user = member.id
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if message.author.id == 488996680058798081 or message.author.id == 840129213968941096:
            with open("./local/auth.json", 'r') as f:
                auth = json.load(f)

            if f'{user}' in auth:
                auth[f'{user}']['auth'] = False

            with open("./local/auth.json", 'w') as f:
                json.dump(auth, f, indent=4)
            embed = discord.Embed(description = f"{member.name} was deauthorised.", color = color)
            await message.channel.send(embed = embed)

        else:
            await message.author.send(content = f'Oh! You are not authorised to use that')

    @commands.command()
    async def playing(self, ctx):
        with open("./local/auth.json", 'r') as f:
            auth = json.load(f)
        userid = ctx.author.id

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        try:
            if auth[str(userid)]['auth'] == True:

                with open("./bot/status.json", "r") as f:
                    D = json.load(f)

                status = D["status"]
                text = D["text"]
                D["activity"] = "playing"

                if status == "online":
                    if text == None:
                        await self.bot.change_presence(activity = discord.Game(name="VALORANT"))
                        D["text"] = "VALORANT"

                    else:
                        await self.bot.change_presence(activity = discord.Game(name=text))

                elif status == "idle":
                    if text == None:
                        await self.bot.change_presence(status=discord.Status.idle, activity = discord.Game(name="VALORANT"))
                        D["text"] = "VALORANT"

                    else:
                        await self.bot.change_presence(status=discord.Status.idle, activity = discord.Game(name=text))

                with open("./bot/status.json", "w") as f:
                    json.dump(D, f, indent=4)

            else:
                await ctx.author.send(content = f'Oh! You are not authorised to use that')
        except:
            await ctx.author.send(content = f'Oh! You are not authorised to use that')

    @commands.command()
    async def watching(self, ctx):
        with open("./local/auth.json", 'r') as f:
            auth = json.load(f)
        userid = ctx.author.id

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="


        try:
            if auth[str(userid)]['auth'] == True:
                
                with open("./bot/status.json", "r") as f:
                    D = json.load(f)

                status = D["status"]
                text = D["text"]
                D["activity"] = "watching"

                if status == "online":
                    if text == None:
                        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Avengers Endgame"))
                        D["text"] = "Avengers Endgame"

                    else:
                        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=text))

                elif status == "idle":
                    if text == None:
                        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="Avengers Endgame"))
                        D["text"] = "Avengers Endgame"

                    else:
                        await self.bot.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching, name=text))

                with open("./bot/status.json", "w") as f:
                    json.dump(D, f, indent=4)

            else:
                await ctx.author.send(content = f'Oh! You are not authorised to use that')
        except:
            await ctx.author.send(content = f'Oh! You are not authorised to use that')

    @commands.command()
    async def listening(self, ctx):
        with open("./local/auth.json", 'r') as f:
            auth = json.load(f)
        userid = ctx.author.id

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        try:
            if auth[str(userid)]['auth'] == True:
                with open("./bot/status.json", "r") as f:
                    D = json.load(f)

                status = D["status"]
                text = D["text"]
                D["activity"] = "listening"

                if status == "online":
                    if text == None:
                        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Spotify"))
                        D["text"] = "Spotify"

                    else:
                        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=text))

                elif status == "idle":
                    if text == None:
                        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name="Spotify"))
                        D["text"] = "Spotify"

                    else:
                        await self.bot.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.listening, name=text))

                with open("./bot/status.json", "w") as f:
                    json.dump(D, f, indent=4)

            else:
                await ctx.author.send(content = f'Oh! You are not authorised to use that')
        except:
            await ctx.author.send(content = f'Oh! You are not authorised to use that')

    @commands.command()
    async def default(self, ctx, stat : str = "online"):
        with open("./local/auth.json", 'r') as f:
            auth = json.load(f)
        userid = ctx.author.id

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        try:
            if auth[str(userid)]['auth'] == True:
                mstat = f'{str(len(self.bot.guilds))} Servers'

                with open("./bot/status.json", "r") as f:
                    D = json.load(f)

                D["activity"] = "watching"
                D["text"] = mstat

                if stat == "idle":
                    await self.bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=mstat))
                    D["status"] = "idle"

                else:
                    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=mstat))
                    D["status"] = "online"

                with open("./bot/status.json", "w") as f:
                    json.dump(D, f, indent=4)

        except:
            await ctx.author.send(content = f'Oh! You are not authorised to use that')

    @commands.command()
    async def text(self, ctx):
        with open("./local/auth.json", 'r') as f:
            auth = json.load(f)
        userid = ctx.author.id

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        cross = self.bot.get_emoji(880679527200735273)
        mark = self.bot.get_emoji(880679486205620234)

        try:
            if auth[str(userid)]['auth'] == True:
                text = ctx.message.content.replace(f"{get_prefix}text ", "")
                with open("./bot/status.json", "r") as f:
                    D = json.load(f)

                status = D["status"]
                activity = D["activity"]
                D["text"] = text

                if status == "online":
                    if activity == None:
                        await self.bot.change_presence(activity = discord.Game(name=text))
                    elif activity == "playing":
                        await self.bot.change_presence(activity = discord.Game(name=text))
                    elif activity == "watching":
                        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=text))
                    elif activity == "listening":
                        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=text))
                if status == "idle":
                    if activity == None:
                        await self.bot.change_presence(status=discord.Status.idle, activity = discord.Game(name=text))
                    elif activity == "playing":
                        await self.bot.change_presence(status=discord.Status.idle, activity = discord.Game(name=text))
                    elif activity == "watching":
                        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=text))
                    elif activity == "listening":
                        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name=text))

                await ctx.message.add_reaction(mark)

        except:
            await ctx.message.add_reaction(cross)

    @commands.command()
    async def clear(self, ctx):
        with open("./local/auth.json", 'r') as f:
            auth = json.load(f)
        userid = ctx.author.id

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        cross = self.bot.get_emoji(880679527200735273)
        mark = self.bot.get_emoji(880679486205620234)

        try:
            if auth[str(userid)]['auth'] == True:
                text = ctx.message.content.replace(f"{get_prefix}text ", "")
                with open("./bot/status.json", "r") as f:
                    D = json.load(f)

                status = D["status"]
                D["activity"] = None
                D["text"] = None

                if status == "online":
                    await self.bot.change_presence(status=discord.Status.online)
                elif status == "idle":
                    await self.bot.change_presence(status=discord.Status.idle)

                with open("./bot/status.json", "w") as f:
                    json.dump(D, f, indent=4)

                await ctx.message.add_reaction(mark)

        except:
            await ctx.message.add_reaction(cross)


    @commands.command(name = "setxp", aliases = ["changexp", "altxp", "xpchange"])
    async def setxp(self, ctx, member : discord.Member, new : int = 5):
        with open("./local/auth.json", 'r') as f:
            auth = json.load(f)

        userid = ctx.author.id

        cross = self.bot.get_emoji(880679527200735273)
        mark = self.bot.get_emoji(880679486205620234)

        try:
            if auth[str(userid)]['auth'] == True:
                id = member.id
                guildid = ctx.guild.id
                guildid = './guild data/'+ str(guildid) +'.json'
                with open(guildid, 'r') as f:
                    users = json.load(f)

                xp = new
                users[str(id)]['experience'] = int(xp)
                lvl = int(xp ** (1/4))
                users[str(id)]['level'] = lvl

                with open(guildid, 'w') as f:
                    json.dump(users, f, indent=4)

                await ctx.message.add_reaction(mark)

        except:
            await ctx.message.add_reaction(cross)

    @commands.command()
    async def addgiftbox(self, ctx, user : discord.Member):
        with open("./local/auth.json", 'r') as f:
            auth = json.load(f)

        cross = self.bot.get_emoji(880679527200735273)
        mark = self.bot.get_emoji(880679486205620234)

        try:
            if auth[str(ctx.author.id)]['auth'] == True:
                with open("./local/items.json", "r") as g:
                    i = json.load(g)

                if not str(user.id) in i:
                    i[f"{user.id}"] = {}
                    i[f"{user.id}"]["items"] = ["gift_box"]

                    await ctx.message.add_reaction(mark)
                    await user.send(f"You just recieved a **Gift Box**🎁 from **{ctx.author}**. Go to a server and use command `=giftbox` to open it and recieve **1 Million XP**")

                elif str(user.id) in i:
                    item_list = i[f"{user.id}"]["items"]
                    item_list.append("gift_box")
                    i[f"{user.id}"]["items"] = item_list

                    await ctx.message.add_reaction(mark)
                    await user.send(f"You just recieved a **Gift Box**🎁 from **{ctx.author}**. Go to a server and use command `=giftbox` to open it and recieve **1 Million XP**")

                with open("./local/items.json", "w") as g:
                    json.dump(i, g, indent=4)

        except Exception as e:
            await ctx.message.add_reaction(cross)

async def setup(bot):
    await bot.add_cog(AuthCog(bot))