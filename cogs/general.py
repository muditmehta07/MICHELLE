import discord
from discord.ext import commands
import os
import datetime
import json
import asyncio

from discord.ext.commands.context import Context

class GenCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def autorole(self, ctx, role : discord.Role = None):
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid2 = './guild data/'+ str(guildid) +'.json'
        with open(guildid2, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if role == None:

            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(ctx.guild.id) in L:
                get_prefix = L[str(ctx.guild.id)]["prefix"]
            elif str(ctx.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Permissions** : `Administrator`\n\n__**Usage**__\n\n**{get_prefix}autorole <role>**\n> This command sets the auto-role as the provided `role`. This role will be assigned to new members when they join this server.\n\n__**Example**__\n\n**{get_prefix}autorole @Member**\n> To set autorole as `Member`." , 
                color=color,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Auto-Role Help ❓", icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = embed)


        else:
            roleId = role.id
            with open("./local/autorole.json", "r") as f:
                guilds = json.load(f)

            guilds[str(guildid)] = roleId

            with open("./local/autorole.json", "w") as f:
                json.dump(guilds, f, indent=4)

            await ctx.send(f"<@&{roleId}> **has been set as the** `Auto-Role`.\n> This role will now be assigned to new members")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def welcome(self, ctx, msg : str = None):
        user = ctx.author.id
        guildid = ctx.guild.id
        guildname = self.bot.get_guild(guildid).name
        channelid = ctx.channel.id

        with open("./local/welcome.json", 'r') as f:
            auth = json.load(f)

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        try:
            if not f'{guildid}' in auth:
                msg2 = ctx.message.content.replace(f"{get_prefix}welcome", "")
                auth[f'{guildid}'] = {}
                auth[f'{guildid}']['user'] = str(ctx.author.name)
                auth[f'{guildid}']['server'] = str(guildname)
                auth[f'{guildid}']['channel'] = channelid

                if msg != None:
                    embed = discord.Embed(description = f"{msg2}", timestamp=datetime.datetime.utcnow())
                    embed.set_author(name = f"Welcome {ctx.author}!", icon_url = ctx.author.avatar_url)

                elif msg == None:
                    msg2 = f'**Hello There!**\nWelcome to {str(guildname)}. We are happy to have you here!'
                    embed = discord.Embed(description = f"{msg2}", timestamp=datetime.datetime.utcnow())
                    embed.set_author(name = f"Welcome {ctx.author}!", icon_url = ctx.author.avatar_url)

                auth[f'{guildid}']['message'] = msg2

                with open("./local/welcome.json", 'w') as f:
                    json.dump(auth, f, indent=4)

                await ctx.send(content=f"> Use `{ctx.prefix}help welcome` for more info\n> **The following message will be sent to this channel on member join :**", embed=embed)

            elif f'{guildid}' in auth:
                msg2 = ctx.message.content.replace(f"{get_prefix}welcome", "")
                auth[f'{guildid}']['user'] = str(ctx.author.name)
                auth[f'{guildid}']['server'] = str(guildname)
                auth[f'{guildid}']['channel'] = channelid
                auth[f'{guildid}']['message'] = msg2

                with open("./local/welcome.json", 'w') as f:
                    json.dump(auth, f, indent=4)

                if msg != None:
                    embed = discord.Embed(description = f"{msg2}", timestamp=datetime.datetime.utcnow())
                    embed.set_author(name = f"Welcome {ctx.author}!", icon_url = ctx.author.avatar_url)

                elif msg == None:
                    msg2 = f'**Hello There!**\nWelcome to {str(guildname)}. We are happy to have you here!'
                    embed = discord.Embed(description = f"{msg2}", timestamp=datetime.datetime.utcnow())
                    embed.set_author(name = f"Welcome {ctx.author}!", icon_url = ctx.author.avatar_url)

                auth[f'{guildid}']['message'] = msg2

                with open("./local/welcome.json", 'w') as f:
                    json.dump(auth, f, indent=4)

                await ctx.send(content=f"> Use `{ctx.prefix}help welcome` for more info\n> **The following message will be sent to this channel on member join :**", embed=embed)

            else:
                return None

        except Exception as e:
            print(e)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def delwelcome(self, ctx):
        user = ctx.author.id
        guildid = ctx.guild.id

        with open("./local/welcome.json", 'r') as f:
            auth = json.load(f)

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        try:
            if f'{guildid}' in auth:
                del auth[f'{guildid}']

                with open("./local/welcome.json", 'w') as f:
                    json.dump(auth, f, indent=4)

                await ctx.send("> **Welcome Messages have been** `Deleted`.\n> I will not send any welcome messages from now")

            else:
                await ctx.send("> **Something went wrong.**\n> Looks like you don't have an active `welcome-channel`.")

        except:
            await ctx.send(f"> **An unexpected error occurred.**\n> Help us improve by reporting this error using `{ctx.prefix}feedback`")


    @commands.group(invoke_without_command=True)
    async def goodbye(self, message):
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
            description = f"**Permissions** : `Administrator`\n\n__**Usage**__\n**{get_prefix}goodbye set**\n> This command sets the channel as `goodbye-channel`. A default `goodbye-message` is provided.\n\n**{get_prefix}goodbye delete**\n> This command deletes the `goodbye-message` and will not send them again." , 
            color=color,
            timestamp=datetime.datetime.utcnow())

        embed.set_author(name = "Goodbye Help ❓", icon_url = self.bot.user.avatar_url)
        await message.channel.send(embed = embed)

    @goodbye.command()
    @commands.has_permissions(administrator=True)
    async def set(self, ctx):
        user = ctx.author.id
        guildid = ctx.guild.id
        guildname = self.bot.get_guild(guildid).name
        channelid = ctx.channel.id

        with open("./local/goodbye.json", 'r') as f:
            auth = json.load(f)

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        try:
            if not f'{guildid}' in auth:
                msg2 = None
                auth[f'{guildid}'] = {}
                auth[f'{guildid}']['user'] = str(ctx.author.name)
                auth[f'{guildid}']['server'] = str(guildname)
                auth[f'{guildid}']['channel'] = channelid
                auth[f'{guildid}']['message'] = msg2

                with open("./local/goodbye.json", 'w') as f:
                    json.dump(auth, f, indent=4)

                await ctx.send(content=f"> A `goodbye-message` will be sent here when a user leaves this server.")

            elif f'{guildid}' in auth:
                msg2 = None
                auth[f'{guildid}']['user'] = str(ctx.author.name)
                auth[f'{guildid}']['server'] = str(guildname)
                auth[f'{guildid}']['channel'] = channelid
                auth[f'{guildid}']['message'] = msg2

                with open("./local/goodbye.json", 'w') as f:
                    json.dump(auth, f, indent=4)

                await ctx.send(content=f"> A `goodbye-message` will be sent here when a user leaves this server.")

            else:
                return None

        except Exception as e:
            print(e)

    @goodbye.command()
    @commands.has_permissions(administrator=True)
    async def delete(self, ctx):
        user = ctx.author.id
        guildid = ctx.guild.id

        with open("./local/goodbye.json", 'r') as f:
            auth = json.load(f)

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        try:
            if f'{guildid}' in auth:
                del auth[f'{guildid}']

                with open("./local/goodbye.json", 'w') as f:
                    json.dump(auth, f, indent=4)

                await ctx.send("> **Goodbye Messages have been** `Deleted`.\n> I will not send any goodbye messages from now")

            else:
                await ctx.send("> **Something went wrong.**\n> Looks like you don't have an active `goodbye-channel`.")

        except:
            await ctx.send(f"> **An unexpected error occurred.**\n> Help us improve by reporting this error using `{ctx.prefix}feedback`")

    @commands.command()
    async def embed(self, message):
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

        if message.message.content == f"{get_prefix}embed":
            embed = discord.Embed(
                description = f"**Description** : Embed your text and make it presentable\n\n**Usage** : `{get_prefix}embed <text>`\n**Example** : `{get_prefix}embed hello, my name is michelle`\n\n**Note** : Your given text should be more than 5 words and must not contain the @ sign" , 
                color = color, 
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Embed Help ❓", icon_url=self.bot.user.avatar_url)
            await message.channel.send(embed = embed)

        else:
            msg = message.message.content.replace(f"{get_prefix}embed", "")
            wordList = msg.split()
            wordCount = len(wordList)

            if "@" in msg:
                mention = True
            else:
                mention = False

            if mention == True:
                await message.channel.send("**You cannot use @ sign in an Embed**\nNote : We use this to avoid mentions")

            elif wordCount >= 5:
                embed = discord.Embed(description = f"{msg}", color = color, timestamp=datetime.datetime.utcnow())
                embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                await message.channel.send(embed = embed)

            else:
                await message.channel.send("**An embed should contain atleast** `5 words`")

    '''

    Confession

    '''

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def confess(self, ctx):
        user = ctx.author.id
        guildid = ctx.guild.id
        guildname = self.bot.get_guild(guildid).name
        channelid = ctx.channel.id

        with open("./local/confess.json", 'r') as f:
            auth = json.load(f)

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        try:
            if not f'{guildid}' in auth:
                auth[f'{guildid}'] = {}
                auth[f'{guildid}']['user'] = str(ctx.author.name)
                auth[f'{guildid}']['server'] = str(guildname)
                auth[f'{guildid}']['channel'] = channelid

                with open("./local/confess.json", 'w') as f:
                    json.dump(auth, f, indent=4)

                embed = discord.Embed(
                    description = f"**Channel set as** `confession-channel`.\n**Confessions will now be sent here.**\n\n> Use command `{ctx.prefix}hi` to know more." , 
                    timestamp=datetime.datetime.utcnow())

                embed.set_author(name = "Confessions", icon_url = self.bot.user.avatar_url)
                await ctx.send(content=f"> Use `{ctx.prefix}help confess` for more info", embed = embed)

            elif f'{guildid}' in auth:
                auth[f'{guildid}']['user'] = str(ctx.author.name)
                auth[f'{guildid}']['server'] = str(guildname)
                auth[f'{guildid}']['channel'] = channelid

                with open("./local/confess.json", 'w') as f:
                    json.dump(auth, f, indent=4)

                embed = discord.Embed(
                    description = f"**Channel set as** `confession-channel`.\n**Confessions will now be sent here.**\n\n> Use command `{ctx.prefix}hi` to know more." , 
                    timestamp=datetime.datetime.utcnow())

                embed.set_author(name = "Confessions", icon_url = self.bot.user.avatar_url)
                await ctx.send(content=f"> Use `{ctx.prefix}help confess` for more info", embed = embed)

            else:
                await ctx.send(f"> **An unexpected error occurred.**\n> Help us improve by reporting this error using `{ctx.prefix}feedback`")

        except:
            await ctx.send(f"> **An unexpected error occurred.**\n> Help us improve by reporting this error using `{ctx.prefix}feedback`")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def delconfess(self, ctx):
        user = ctx.author.id
        guildid = ctx.guild.id

        with open("./local/confess.json", 'r') as f:
            auth = json.load(f)

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        try:
            if f'{guildid}' in auth:
                del auth[f'{guildid}']

                with open("./local/confess.json", 'w') as f:
                    json.dump(auth, f, indent=4)

                await ctx.send("> **Confession Channel has been** `Deleted`.\n> I will not send any confessions from now")

            else:
                await ctx.send("> **Something went wrong.**\n> Looks like you don't have an active `confession-channel`.")

        except:
            await ctx.send(f"> **An unexpected error occurred.**\n> Help us improve by reporting this error using `{ctx.prefix}feedback`")

    @commands.command(aliases = ["hello", "hey", "hii", "Hi", "HI"])
    async def hi(self, message):
        if message.guild:
            msg = message.message
            await msg.add_reaction("✅")

            embed = discord.Embed(
            description="__**=post <message>**__\n> Use this command to post an anonymous message to a server's confession channel. Replace `<message>` with a desired message you want to send",
            timestamp = datetime.datetime.utcnow())

            await message.author.send(embed=embed)

        else:
            embed = discord.Embed(
            description="__**=post <message>**__\n> Use this command to post an anonymous message to a server's confession channel. Replace `<message>` with a desired message you want to send",
            timestamp = datetime.datetime.utcnow())

            await message.author.send(embed=embed)

async def setup(bot):
    await bot.add_cog(GenCog(bot))