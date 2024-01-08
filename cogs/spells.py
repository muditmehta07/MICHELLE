import discord
from discord.ext import commands
import os
import datetime
import json

from discord.ext.commands.context import Context

class SpellsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''

    Sage Commands

    '''

    @commands.command()
    async def gift(self, ctx, member : discord.Member, exp : int = 1):
        memid = member.id
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if users[str(id)]['sage_spell'] == True:
            if users[str(id)]['level'] > exp:
                user_level = users[str(id)]['level']
                user_level -= exp
                user_xp = user_level**4
                users[str(id)]['level'] = user_level
                users[str(id)]['experience'] = user_xp

                member_level = users[str(memid)]['level']
                member_level += exp
                member_xp = member_level**4
                users[str(memid)]['level'] = member_level
                users[str(memid)]['experience'] = member_xp

                with open(guildid, "w") as f:
                    json.dump(users, f, indent=4)

                embed = discord.Embed(title = "Level Gifted", description = f"{ctx.author.mention} gifted {exp} LVL to {member.mention}", color = color, timestamp=datetime.datetime.utcnow())
                embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
            else:
                text = f'Gift could not be sent'
                embed = discord.Embed(title = text, description="You do not have that many levels to gift", color = color, timestamp=datetime.datetime.utcnow())
                embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)

        else:
            text = f'Unable to use this command'
            embed = discord.Embed(title = text, description="You do not own the Sage Spell", color = color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)


    '''

    Hunter Commands

    '''

    @commands.command()
    async def seek(self, ctx):
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if users[str(id)]['hunter_spell'] == True:
            L = ""
            for i in users:
                if users[i]["sage_spell"] == True:
                    name = self.bot.get_user(int(i))
                    name = str(name)
                    L += "*"+name+"*"+"\n"
                elif users[i]["wraith_spell"] == True:
                    name = self.bot.get_user(int(i))
                    name = str(name)
                    L += "*"+name+"*"+"\n"

            if len(L) == 0:
                L = f"No Sage/Wraith Spell users found in Server : `{ctx.guild.name}`"

            await ctx.message.add_reaction("✅")

            embed = discord.Embed(title = "Seek Complete 🔍", description = f"{L}", color=color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.message.author.send(embed=embed)
        else:
            text = f'Unable to use this command'
            embed = discord.Embed(title = text, description="You do not own the Hunter Spell", color = color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)

    @commands.command()
    async def hunt(self, ctx, member : discord.Member):
        memid = member.id
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if users[str(id)]['hunter_spell'] == True:
            if users[str(id)]['level'] >=2:
                if users[str(memid)]['level'] >=10:
                    if users[str(memid)]["sage_spell"] == True or users[str(memid)]["wraith_spell"] == True:
                        user_level = users[str(id)]['level']
                        user_level -=1
                        user_xp = user_level**4
                        users[str(id)]['level'] = user_level
                        users[str(id)]['experience'] = user_xp

                        member_level = users[str(memid)]['level']
                        member_level -=2
                        member_xp = member_level**4
                        users[str(memid)]['level'] = member_level
                        users[str(memid)]['experience'] = member_xp

                        with open(guildid, "w") as f:
                            json.dump(users, f, indent=4)

                        embed = discord.Embed(title = "Hunt Complete 🏹", description = f"*{member.mention} was hunted by {ctx.author.mention}*", color=color,timestamp=datetime.datetime.utcnow())
                        embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                        await ctx.send(embed=embed)
                    else:
                        text = f'Unable to use this command'
                        embed = discord.Embed(title = text, description="Mentioned user does not own Sage or Wraith spells", color = color,timestamp=datetime.datetime.utcnow())
                        embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                        await ctx.send(embed = embed)
                else:
                    text = f'Hunt Cancelled'
                    embed = discord.Embed(title = text, description="Prey should always be level 10 or above", color = color,timestamp=datetime.datetime.utcnow())
                    embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                    await ctx.send(embed = embed)
            else:
                text = f'Hunt Cancelled'
                embed = discord.Embed(title = text, description="You must be atleast level 3 to hunt", color = color,timestamp=datetime.datetime.utcnow())
                embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
        else:
            text = f'Unable to use this command'
            embed = discord.Embed(title = text, description="You do not own the Hunter Spell", color = color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)

    '''
    
    Transformation Jutsu Command
    
    '''

    @commands.command()
    async def transform(self, message : discord.Message):
        id = message.author.id
        guildid = message.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        if str(id) in users:
            if users[str(id)]["transformation"] == True:

                name = message.message.content.replace(f"{get_prefix}transform", "")

                if name == None:
                    await message.message.channel.send(f"Usage : `{get_prefix}name <display name for leaderboard>`")

                elif name != None:
                    users[str(id)]["transform"] = name

                    with open(guildid, 'w') as e:
                        json.dump(users, e, indent=4)

                    await message.message.channel.send(f"You transformed into **{name}**, your name has been changed on the Leaderboard!")

        else:
            await message.message.channel.send("You don't know how to do the **Transformation Justu**!")

async def setup(bot):
    await bot.add_cog(SpellsCog(bot))