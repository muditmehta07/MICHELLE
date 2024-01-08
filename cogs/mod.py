import discord
from discord.ext import commands
import os
import datetime
import json

from discord.ext.commands.context import Context

class ModCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def int_check(s):
        try: 
            int(s)
            return True
        except ValueError:
            return False

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason=None):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if member == None:
            embed = discord.Embed(
                description = f"**Permissions** : `Kick Members`\n\n__**Usage**__\n\n**{ctx.prefix}kick <member> <reason>**\n> Do I really need to explain? This command kicks the mentioned user.\n\n__**Example**__\n\n**{ctx.prefix}kick @PastaEater**\n> To kick the user : `PastaEater`.\n\n**Note**: If the reason parameter is left blank, `Inappropriate Behaviour` will be set as the reason" , 
                color=color,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Kick Help ❓", icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = embed)

        elif member.id == ctx.author.id:
            await ctx.send("> **Nice try!** But you cannot kick yourself out.")

        else:
            if reason == None:
                reason = "Inappropriate Behaviour"

            else:
                content = ctx.message.content.replace(f"{ctx.prefix}kick ", " ")
                reason = content

            await member.kick(reason=reason)

            embed = discord.Embed(color=color, timestamp=datetime.datetime.utcnow())

            embed.add_field(name = f"User ID", value = f"`{member.id}`")
            embed.add_field(name = f"Kicked By", value = f"`{ctx.author}`")
            embed.add_field(name = f"Reason", value = f"> {reason}", inline=False)

            embed.set_thumbnail(url = f"{member.avatar_url}")
            embed.set_author(name = f"{member} Kicked")
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def masskick(self, ctx, member: int = None):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if member == None:
            embed = discord.Embed(
                description = f"**Permissions** : `Kick Members`\n\n__**Usage**__\n\n**{ctx.prefix}masskick <member1> <member2>...**\n> This command kicks multiple users by ID.\n\n__**Example**__\n\n**{ctx.prefix}masskick 123 456 789**\n> To masskick the users with IDs : `123`, `456`, `789`.\n\n**Note**: To get the ID of a user, enable `Discord Settings > Advanced > Developer Mode` and then right click a message sent by that user. A `copy-ID` option will now be visible." , 
                color=color,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Mass Kick Help ❓", icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = embed)

        else:
            reason = "Inappropriate Behaviour"
            users = ctx.message.content.split()

            ban_count = 0

            for i in users:
                if ModCog.int_check(i):
                    try:
                        i=int(i)
                        member = self.bot.get_user(i)
                        await member.kick(reason=reason)
                        ban_count += 1
                    except:
                        pass

            await ctx.send(f"> **{ban_count}** user(s) have been kicked.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.User = None, reason=None):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if member == None:
            embed = discord.Embed(
                description = f"**Permissions** : `Ban Members`\n\n__**Usage**__\n\n**{ctx.prefix}ban <member> <reason>**\n> Do I have to explain this one too? This command bans the mentioned user.\n\n__**Example**__\n\n**{ctx.prefix}ban @PastaEater**\n> To ban the user : `PastaEater`.\n\n**Note**: If the reason parameter is left blank, `Inappropriate Behaviour` will be set as the reason" , 
                color=color,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Ban Help ❓", icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = embed)

        elif member.id == ctx.author.id:
            await ctx.send("> **Nice try!** But you cannot ban yourself.")

        else:
            if reason == None:
                reason = "Inappropriate Behaviour"

            else:
                content = ctx.message.content.replace(f"{ctx.prefix}ban ", " ")
                reason = content

            await ctx.guild.ban(member, reason=reason)

            embed = discord.Embed(color=color, timestamp=datetime.datetime.utcnow())

            embed.add_field(name = f"User ID", value = f"`{member.id}`")
            embed.add_field(name = f"Banned By", value = f"`{ctx.author}`")
            embed.add_field(name = f"Reason", value = f"> {reason}", inline=False)

            embed.set_thumbnail(url = f"{member.avatar_url}")
            embed.set_author(name = f"{member} Banned")
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def massban(self, ctx, member: int = None):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if member == None:
            embed = discord.Embed(
                description = f"**Permissions** : `Ban Members`\n\n__**Usage**__\n\n**{ctx.prefix}massban <member1> <member2>...**\n> This command bans multiple users by ID.\n\n__**Example**__\n\n**{ctx.prefix}massban 123 456 789**\n> To massban the users with IDs : `123`, `456`, `789`.\n\n**Note**: To get the ID of a user, enable `Discord Settings > Advanced > Developer Mode` and then right click a message sent by that user. A `copy-ID` option will now be visible." , 
                color=color,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Mass Ban Help ❓", icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = embed)

        else:
            reason = "Inappropriate Behaviour"
            users = ctx.message.content.split()

            ban_count = 0

            for i in users:
                if ModCog.int_check(i):
                    try:
                        i=int(i)
                        member = self.bot.get_user(i)
                        await ctx.guild.ban(member, reason=reason)
                        ban_count += 1
                    except:
                        pass

            await ctx.send(f"> **{ban_count}** user(s) have been banned.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def warn(self, ctx, member: discord.Member = None):
        
        id = member.id
        guildid = ctx.guild.id

        if member == None:
            embed = discord.Embed(
                description = f"**Permissions** : `Administrator`\n\n__**Description**__\n Warn a user. Number of warnings a user has can be viewed by using command `{ctx.prefix}profile`\n\n> **Note**: Warnings can be reset by using command `{ctx.prefix}reset`" ,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Warn Help ❓", icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = embed)

        else:
            with open("./local/warn.json", "r") as f:
                warn = json.load(f)

            if str(guildid) in warn:
                if str(id) not in warn[str(guildid)]:
                    warn[str(guildid)][str(id)] = 1

                elif str(id) in warn[str(guildid)]:
                    warnings = warn[str(guildid)][str(id)]
                    warnings += 1
                    warn[str(guildid)][str(id)] = warnings

            elif str(guildid) not in warn:
                warn[str(guildid)] = {}
                warn[str(guildid)][str(id)] = 1

            with open("./local/warn.json", "w") as f:
                json.dump(warn, f, indent=4)

            warnings = warn[str(guildid)][str(id)]
            await ctx.send(f"> **{member}** has been warned `[Warnings: {warnings}]`")

    @commands.command(aliases = ["reset", "resetwarnings", "resetwarning"])
    @commands.has_permissions(administrator=True)
    async def resetwarn(self, ctx, member: discord.Member = None):
        
        id = member.id
        guildid = ctx.guild.id

        if member == None:
            embed = discord.Embed(
                description = f"**Permissions** : `Administrator`\n\n__**Description**__\n Warn a user. Number of warnings a user has can be viewed by using command `{ctx.prefix}profile`\n\n> **Note**: Warnings can be reset by using command `{ctx.prefix}reset`" ,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Warn Help ❓", icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = embed)

        else:
            with open("./local/warn.json", "r") as f:
                warn = json.load(f)

            if str(guildid) in warn:
                if str(id) not in warn[str(guildid)]:
                    warn[str(guildid)][str(id)] = 0

                elif str(id) in warn[str(guildid)]:
                    warn[str(guildid)][str(id)] = 0

            elif str(guildid) not in warn:
                warn[str(guildid)] = {}
                warn[str(guildid)][str(id)] = 0

            with open("./local/warn.json", "w") as f:
                json.dump(warn, f, indent=4)

            warnings = warn[str(guildid)][str(id)]
            await ctx.send(f"> **{member}**'s warnings were reset `[Warnings: {warnings}]`")

async def setup(bot):
    await bot.add_cog(ModCog(bot))