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
                await message.channel.send(content = f'{member.mention}', embed = embed)

            elif f'{user}' in auth:
                auth[f'{user}']['auth'] = True

                with open("./local/auth.json", 'w') as f:
                    json.dump(auth, f, indent=4)
                embed = discord.Embed(description = f"{member.name} was authorised.", color = color)
                await message.channel.send(content = f'{member.mention}', embed = embed)

        else:
            embed = discord.Embed(description = "This is a dev only command. 😬", color = color)
            await message.channel.send(content = f'{message.author.mention}', embed = embed)

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
            await message.channel.send(content = f'{member.mention}', embed = embed)

        else:
            embed = discord.Embed(description = "This is a dev only command. 😬", color = color)
            await message.channel.send(content = f'{message.author.mention}', embed = embed)

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
                stat = ctx.message.content.replace(f"{get_prefix}playing ", "")
                await self.bot.change_presence(activity = discord.Game(stat))
            else:
                embed = discord.Embed(description = "This is an auth user only command. 😬")
                await ctx.send(content = f'{ctx.author.mention}', embed = embed)
        except:
            embed = discord.Embed(description = "This is an auth user only command. 😬")
            await ctx.send(content = f'{ctx.author.mention}', embed = embed)

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
                wstat = ctx.message.content.replace(f"{get_prefix}watching ", "")
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=wstat))
            else:
                embed = discord.Embed(description = "This is an auth user only command. 😬")
                await ctx.send(content = f'{ctx.author.mention}', embed = embed)
        except:
            embed = discord.Embed(description = "This is an auth user only command. 😬")
            await ctx.send(content = f'{ctx.author.mention}', embed = embed)

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
                mstat = ctx.message.content.replace(f"{get_prefix}listening ", "")
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=mstat))
            else:
                embed = discord.Embed(description = "This is an auth user only command. 😬")
                await ctx.send(content = f'{ctx.author.mention}', embed = embed)
        except:
            embed = discord.Embed(description = "This is an auth user only command. 😬")
            await ctx.send(content = f'{ctx.author.mention}', embed = embed)

    @commands.command()
    async def default(self, ctx):
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
                mstat = f'{str(len(self.bot.guilds))} servers || =help'
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=mstat))
            else:
                embed = discord.Embed(description = "This is an auth user only command. 😬")
                await ctx.send(content = f'{ctx.author.mention}', embed = embed)
        except:
            embed = discord.Embed(description = "This is an auth user only command. 😬")
            await ctx.send(content = f'{ctx.author.mention}', embed = embed)

    @commands.command()
    async def pfp1(self, ctx):
        with open("./local/auth.json", 'r') as f:
            auth = json.load(f)
        userid = ctx.author.id

        try:
            if auth[str(userid)]['auth'] == True:
                with open("./pictures/1.png", 'rb') as f:
                    image = f.read()
                await self.bot.user.edit(avatar=image)

            else:
                embed = discord.Embed(description = "This is an auth user only command. 😬")
                await ctx.send(content = f'{ctx.author.mention}', embed = embed)
        except:
            embed = discord.Embed(description = "You've used the command alot, try again later. 😬")
            await ctx.send(content = f'{ctx.author.mention}', embed = embed)

    @commands.command()
    async def pfp2(self, ctx):
        with open("./local/auth.json", 'r') as f:
            auth = json.load(f)
        userid = ctx.author.id

        try:
            if auth[str(userid)]['auth'] == True:
                with open("./pictures/2.png", 'rb') as f:
                    image = f.read()
                await self.bot.user.edit(avatar=image)

            else:
                embed = discord.Embed(description = "This is an auth user only command. 😬")
                await ctx.send(content = f'{ctx.author.mention}', embed = embed)
        except:
            embed = discord.Embed(description = "You've used the command alot, try again later. 😬")
            await ctx.send(content = f'{ctx.author.mention}', embed = embed)

    @commands.command()
    async def pfp3(self, ctx):
        with open("./local/auth.json", 'r') as f:
            auth = json.load(f)
        userid = ctx.author.id

        try:
            if auth[str(userid)]['auth'] == True:
                with open("./pictures/3.png", 'rb') as f:
                    image = f.read()
                await self.botot.user.edit(avatar=image)

            else:
                embed = discord.Embed(description = "This is an auth user only command. 😬")
                await ctx.send(content = f'{ctx.author.mention}', embed = embed)
        except:
            embed = discord.Embed(description = "You've used the command alot, try again later. 😬")
            await ctx.send(content = f'{ctx.author.mention}', embed = embed)


    @commands.command(name = "setxp", aliases = ["changexp", "altxp", "xpchange"])
    async def setxp(self, message, member : discord.Member, new : int = 5):
        with open("./local/auth.json", 'r') as f:
            auth = json.load(f)
        userid = message.author.id
        try:
            if auth[str(userid)]['auth'] == True:
                id = member.id
                guildid = message.channel.guild.id
                guildid = './guild data/'+ str(guildid) +'.json'
                with open(guildid, 'r') as f:
                    users = json.load(f)

                xp = new
                users[str(id)]['experience'] = int(xp)
                lvl = int(xp ** (1/4))
                users[str(id)]['level'] = lvl

                with open(guildid, 'w') as f:
                    json.dump(users, f, indent=4)
            else:
                embed = discord.Embed(title = "You are not Authorised. 😬", description = "Only users authorised by my developer can use this command.", timestamp=datetime.datetime.utcnow())
                await message.channel.send(content = f'{message.author.mention}', embed = embed)
        except:
            embed = discord.Embed(title = "You are not Authorised. 😬", description = "Only users authorised by my developer can use this command.", timestamp=datetime.datetime.utcnow())
            await message.channel.send(content = f'{message.author.mention}', embed = embed)


def setup(bot):
    bot.add_cog(AuthCog(bot))