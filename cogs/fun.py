import discord
from discord.ext import commands
import os
import random
import datetime
import json
import praw
import asyncio
from discord import message
from discord.ext.commands import context
from discord.ext.commands.context import Context
from PIL import Image, ImageDraw, ImageFont
import requests

emoji_dict = {
    "A" : ":regional_indicator_a:",
    "B" : ":regional_indicator_b:",
    "C" : ":regional_indicator_c:",
    "D" : ":regional_indicator_d:",
    "E" : ":regional_indicator_e:",
    "F" : ":regional_indicator_f:",
    "G" : ":regional_indicator_g:",
    "H" : ":regional_indicator_h:",
    "I" : ":regional_indicator_i:",
    "J" : ":regional_indicator_j:",
    "K" : ":regional_indicator_k:",
    "L" : ":regional_indicator_l:",
    "M" : ":regional_indicator_m:",
    "N" : ":regional_indicator_n:",
    "O" : ":regional_indicator_o:",
    "P" : ":regional_indicator_p:",
    "Q" : ":regional_indicator_q:",
    "R" : ":regional_indicator_r:",
    "S" : ":regional_indicator_s:",
    "T" : ":regional_indicator_t:",
    "U" : ":regional_indicator_u:",
    "V" : ":regional_indicator_v:",
    "W" : ":regional_indicator_w:",
    "X" : ":regional_indicator_x:",
    "Y" : ":regional_indicator_y:",
    "Z" : ":regional_indicator_z:",
    "1" : ":one:",
    "2" : ":two:",
    "3" : ":three:",
    "4" : ":four:",
    "5" : ":five:",
    "6" : ":six:",
    "7" : ":seven:",
    "8" : ":eight:",
    "9" : ":nine:",
    "0" : ":zero:",
    "!" : ":grey_exclamation:",
    "?" : ":grey_question:"
    }

class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def convert(self, n):
        avg = str(datetime.timedelta(seconds = n))
        avgString = str(avg).split(".")[0]

        return avgString

    def humanize(self, n):
        if "days" in n or "day" in n:
            L = n.split()
            days = L[0] + " " + L[1]
            time = L[2]
            time = time.split(":")
            hours = time[0]

            return f"{days} {hours} hours"

        else:
            L = n.split(":")
            hours = L[0]
            minutes = L[1]
            seconds = L[2]

            if hours == "0" and minutes != "00":
                return f"{minutes} minutes, {seconds} seconds"

            elif hours == "0" and minutes == "00":
                return f"{seconds} seconds"

            else:
                return f"{hours} hours, {minutes} minutes"

    @commands.command()
    async def pat(self, ctx, member : discord.Member = None):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = './guild data/'+ str(guildid) +'.json'
        with open(guild, 'r') as g:
            users = json.load(g)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        if member == None:

            embed = discord.Embed(
                description = f"**Description** : Pat the mentioned user by sending a GIF\n\n**Usage** : `{get_prefix}pat <user mention>`\n**Example** : `{get_prefix}pat @user` to punch a user" , 
                color = color, 
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Pat Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed = embed)

        else:
            memid = member.id

            embed = discord.Embed(
                description = f"**{ctx.author.display_name} comforted {member.display_name}**",
                color = color, 
                timestamp=datetime.datetime.utcnow())

            L = ["https://media.giphy.com/media/109ltuoSQT212w/giphy.gif",
            "https://media.giphy.com/media/L2z7dnOduqEow/giphy.gif",
            "https://media.giphy.com/media/osYdfUptPqV0s/giphy.gif",
            "https://media.giphy.com/media/3oz8xDLT82QiURnPS8/giphy.gif",
            "https://media.giphy.com/media/SSPW60F2Uul8OyRvQ0/giphy.gif"]

            url = random.choice(L)

            embed.set_image(url=url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)

            await ctx.send(embed=embed)

    @commands.command(aliases = ["high5"])
    async def highfive(self, ctx, member : discord.Member = None):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = './guild data/'+ str(guildid) +'.json'
        with open(guild, 'r') as g:
            users = json.load(g)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        if member == None:

            embed = discord.Embed(
                description = f"**Description** : Highfive the mentioned user by sending a GIF\n\n**Usage** : `{get_prefix}high5 <user mention>`\n**Example** : `{get_prefix}high5 @user` to punch a user" , 
                color = color, 
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Highfive Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed = embed)

        else:
            memid = member.id

            embed = discord.Embed(
                description = f"**{ctx.author.display_name} gave {member.display_name} a highfive**",
                color = color, 
                timestamp=datetime.datetime.utcnow())

            L = ["https://media.giphy.com/media/yZWsMXuXP9e5a/giphy.gif",
            "https://media.giphy.com/media/3oEjHV0z8S7WM4MwnK/giphy.gif",
            "https://media.giphy.com/media/xT8qBkXehPSstbhfWM/giphy.gif",
            "https://media.giphy.com/media/HozURFRL6mT2o/giphy.gif",
            "https://media.giphy.com/media/65HR2UL6nn6XMSUoRA/giphy.gif"]

            url = random.choice(L)

            embed.set_image(url=url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)

            await ctx.send(embed=embed)

    @commands.command()
    async def punch(self, ctx, member : discord.Member = None):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = './guild data/'+ str(guildid) +'.json'
        with open(guild, 'r') as g:
            users = json.load(g)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        if member == None:

            embed = discord.Embed(
                description = f"**Description** : Punch the mentioned user by sending a GIF\n\n**Usage** : `{get_prefix}punch <user mention>`\n**Example** : `{get_prefix}punch @user` to punch a user" , 
                color = color, 
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Punch Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed = embed)

        else:
            memid = member.id

            embed = discord.Embed(
                description = f"**{ctx.author.display_name} punched {member.display_name}**",
                color = color, 
                timestamp=datetime.datetime.utcnow())

            L = ["https://media.giphy.com/media/Z5zuypybI5dYc/giphy.gif",
            "https://media.giphy.com/media/xUO4t2gkWBxDi/giphy.gif",
            "https://media.giphy.com/media/DuVRadBbaX6A8/giphy.gif",
            "https://media.giphy.com/media/XbV2eCHp0mHthRjdJP/giphy.gif",
            "https://media.giphy.com/media/11HeubLHnQJSAU/giphy.gif"]

            url = random.choice(L)

            embed.set_image(url=url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)

            await ctx.send(embed=embed)

    @commands.command()
    async def hug(self, ctx, member : discord.Member = None):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = './guild data/'+ str(guildid) +'.json'
        with open(guild, 'r') as g:
            users = json.load(g)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        if member == None:

            embed = discord.Embed(
                description = f"**Description** : Hugs the mentioned user by sending a GIF\n\n**Usage** : `{get_prefix}hug <user mention>`\n**Example** : `{get_prefix}hug @user` to hug a user" , 
                color = color, 
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Hug Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed = embed)

        else:
            memid = member.id

            embed = discord.Embed(
                description = f"**{ctx.author.display_name} hugged {member.display_name}**",
                color = color, 
                timestamp=datetime.datetime.utcnow())

            L = ["https://media.giphy.com/media/du8yT5dStTeMg/giphy.gif",
            "https://media.giphy.com/media/lrr9rHuoJOE0w/giphy.gif",
            "https://media.giphy.com/media/wnsgren9NtITS/giphy.gif",
            "https://media.giphy.com/media/49mdjsMrH7oze/giphy.gif",
            "https://media.giphy.com/media/u9BxQbM5bxvwY/giphy.gif"]

            url = random.choice(L)

            embed.set_image(url=url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)

            await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self, ctx, member : discord.Member = None):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = './guild data/'+ str(guildid) +'.json'
        with open(guild, 'r') as g:
            users = json.load(g)

        color = users[str(id)]['color']

        if member == None:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(ctx.guild.id) in L:
                get_prefix = L[str(ctx.guild.id)]["prefix"]
            elif str(ctx.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Description** : Kisses the mentioned user by sending a custom image\n\n**Usage** : `{get_prefix}kiss <user mention>`\n**Example** : `{get_prefix}kiss @user` to kiss a user" , 
                color = color, 
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Kiss Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed = embed)
        
        else:
            memid = member.id

            embed = discord.Embed(
                description = f"**{ctx.author.display_name} kissed {member.display_name}**",
                color = color, 
                timestamp=datetime.datetime.utcnow())

            L = ["https://media.giphy.com/media/bGm9FuBCGg4SY/giphy.gif",
            "https://media.giphy.com/media/G3va31oEEnIkM/giphy.gif",
            "https://media.giphy.com/media/FqBTvSNjNzeZG/giphy.gif",
            "https://media.giphy.com/media/zkppEMFvRX5FC/giphy.gif",
            "https://media.giphy.com/media/bm2O3nXTcKJeU/giphy.gif",
            "https://media.giphy.com/media/nyGFcsP0kAobm/giphy.gif"]

            url = random.choice(L)

            embed.set_image(url=url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)

            await ctx.send(embed=embed)

    @commands.command()
    async def slap(self, ctx, member : discord.Member = None):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = './guild data/'+ str(guildid) +'.json'
        with open(guild, 'r') as g:
            users = json.load(g)

        color = users[str(id)]['color']

        if member == None:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(ctx.guild.id) in L:
                get_prefix = L[str(ctx.guild.id)]["prefix"]
            elif str(ctx.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Description** : Slaps the mentioned user by sending a custom image\n\n**Usage** : `{get_prefix}slap <user mention>`\n**Example** : `{get_prefix}slap @user` to slap a user" , 
                color = color, 
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Slap Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed = embed)

        else:
            memid = member.id

            embed = discord.Embed(
                description = f"**{ctx.author.display_name} slapped {member.display_name}**",
                color = color, 
                timestamp=datetime.datetime.utcnow())

            L = ["https://media.giphy.com/media/Gf3AUz3eBNbTW/giphy.gif",
            "https://media.giphy.com/media/Zau0yrl17uzdK/giphy.gif",
            "https://media.giphy.com/media/9U5J7JpaYBr68/giphy.gif",
            "https://media.giphy.com/media/10DRaO76k9sgHC/giphy.gif",
            "https://media.giphy.com/media/m6etefcEsTANa/giphy.gif",
            "https://media.giphy.com/media/6Fad0loHc6Cbe/giphy.gif"]

            url = random.choice(L)

            embed.set_image(url=url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)

            await ctx.send(embed=embed)

    @commands.group(invoke_without_command = True)
    async def kill(self, message, member : discord.Member = None):
        
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        c = users[str(id)]['color']

        if member == None:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(message.guild.id) in L:
                get_prefix = L[str(message.guild.id)]["prefix"]
            elif str(message.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Description** : Kills the mentioned user. Killing a user drops their XP and raises yours. You may also fail to kill them which would drop your XP and raise their's\n\n**Usage** : `{get_prefix}kill <weapon> <user mention>`\n**Example** : `{get_prefix}kill knife @user` to kill a user with a knife" , 
                color = c,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Kill Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await message.channel.send(embed = embed)

        else:
            memid = member.id
            lvl = users[str(id)]['level']
            lvl2 = users[str(memid)]['level']

            if lvl>=10:
                if lvl2>=10:
                    if users[str(memid)]['sage_spell'] == True:
                            m = f'{member.name} owns a `Sage Spell` and is invulnerable to your mortal threats'
                            level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                            level_embed.set_author(name = message.author, icon_url = message.author.avatar)
                            await message.channel.send(embed=level_embed)

                    elif users[str(id)]['sage_spell'] == True:
                            m = f'{message.author.name}, you own a `Sage Spell` and cannot kill anyone'
                            level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                            level_embed.set_author(name = message.author, icon_url = message.author.avatar)
                            await message.channel.send(embed=level_embed)

                    elif member == message.author:
                        embed = discord.Embed(
                            description = f"**{message.author.display_name} committed alt+f4**",
                            color = c, 
                            timestamp=datetime.datetime.utcnow())

                        L = [
                            "https://media.giphy.com/media/4XOfvSkkxchHy/giphy.gif",
                            "https://media.giphy.com/media/OorbbcMrkiJ8c/giphy.gif",
                            "https://media.giphy.com/media/J1cBEFZp00lJC/giphy.gif",
                            "https://media.giphy.com/media/vkwAeqMEUSaoU/giphy.gif",
                            "https://media.giphy.com/media/krMpiV41eo264/giphy.gif",
                            "https://media.giphy.com/media/yZf5WeLUsi0JG/giphy.gif"
                            ]

                        url = random.choice(L)

                        embed.set_image(url=url)
                        embed.set_author(name=message.author.name, icon_url=message.author.avatar)

                        await message.channel.send(embed=embed)
                        
                    else:
                        L = [1, 2]
                        x = random.choice(L)
                        if x == 1:
                            with open(guildid, 'r') as f1:
                                users = json.load(f1)

                            u2 = users[str(memid)]['experience']

                            p = 20

                            u2 = u2 - p
                            users[str(memid)]['experience'] = int(u2)
                            lvl = int(u2 ** (1/4))
                            users[str(memid)]['level'] = lvl

                            u1 = users[str(id)]['experience']
                            u1 = u1 + p
                            users[str(id)]['experience'] = int(u1)
                            lvl = int(u1 ** (1/4))
                            users[str(id)]['level'] = lvl

                            with open(guildid, 'w') as f1:
                                json.dump(users, f1, indent=4)

                            embed = discord.Embed(
                                description = f"**{message.author.display_name} killed {member.display_name}**",
                                color = c, 
                                timestamp=datetime.datetime.utcnow())

                            L = [
                                "https://media.giphy.com/media/PkQFrCxsgL3Mc/giphy.gif",
                                "https://media.giphy.com/media/S7nF0HAVEBxUu76pxR/giphy.gif"
                                "https://media.giphy.com/media/YmZOBDYBcmWK4/giphy.gif"
                                ]

                            url = random.choice(L)

                            embed.set_image(url=url)
                            embed.set_author(name=message.author.name, icon_url=message.author.avatar)
                            embed.set_footer(text = f'{member.display_name} lost {p} XP')
                            await message.channel.send(embed=embed)

                        else:
                            with open(guildid, 'r') as f1:
                                users = json.load(f1)

                            u1 = users[str(id)]['experience']

                            p = 20

                            u1 = u1 - p
                            users[str(id)]['experience'] = int(u1)
                            lvl = int(u1 ** (1/4))
                            users[str(id)]['level'] = lvl

                            u2 = users[str(memid)]['experience']
                            u2 = u2 + p
                            users[str(memid)]['experience'] = int(u2)
                            lvl = int(u2 ** (1/4))
                            users[str(memid)]['level'] = lvl

                            with open(guildid, 'w') as f1:
                                json.dump(users, f1, indent=4)

                            embed = discord.Embed(
                                description = f"**{message.author.display_name} failed to kill {member.display_name}**",
                                color = c, 
                                timestamp=datetime.datetime.utcnow())

                            L = [
                                "https://media.giphy.com/media/3orieV4J8MNjklR3aw/giphy.gif",
                                "https://media.giphy.com/media/VJ5WsYvjzATmXksHQt/giphy.gif",
                                "https://media.giphy.com/media/RapC4KegCTwYQHDHof/giphy.gif",
                                "https://media.giphy.com/media/26xBC0xYwcSWzTL2g/giphy.gif",
                                "https://media.giphy.com/media/aGCfToZLs8PW7lHDCc/giphy.gif",
                                "https://media.giphy.com/media/XN5yQdKrK3v4A/giphy.gif",
                                "https://c.tenor.com/sAdlyyKDxogAAAAC/bart-simpson-the-simpsons.gif"
                                ]

                            url = random.choice(L)

                            embed.set_image(url=url)
                            embed.set_author(name=message.author.name, icon_url=message.author.avatar)
                            embed.set_footer(text = f'{message.author.display_name} lost {p} XP')
                            await message.channel.send(embed=embed)
                else:
                    m = f'{message.author.mention} User must be `Level 10` or +'
                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                    level_embed.set_author(name = message.author, icon_url = message.author.avatar)
                    await message.channel.send(embed=level_embed)

            else:
                m = f'{message.author.mention} Requirements to use this command : `Level 10`'
                level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                level_embed.set_author(name = message.author, icon_url = message.author.avatar)
                await message.channel.send(embed=level_embed)

    @kill.command(aliases=["Knife"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def knife(self, ctx, member : discord.Member = None):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        c = users[str(id)]['color']
        knife = self.bot.get_emoji(881474984193703999)

        if member == None:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(ctx.guild.id) in L:
                get_prefix = L[str(ctx.guild.id)]["prefix"]
            elif str(ctx.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Description** : Kills the mentioned user. Killing a user drops their XP and raises yours. You may also fail to kill them which would drop your XP and raise their's\n\n**Usage** : `{get_prefix}kill <weapon> <user mention>`\n**Example** : `{get_prefix}kill knife @user` to kill a user with a knife" , 
                color = c,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Kill Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed = embed)
            await ctx.command.reset_cooldown(ctx)

        else:
            memid = member.id
            lvl = users[str(id)]['level']
            lvl2 = users[str(memid)]['level']

            with open("./local/weapons.json", "r") as f:
                weapon = json.load(f)

            if str(ctx.author.id) in weapon:
                if weapon[f"{ctx.author.id}"]["knife"] == True:
                    if lvl>=10:
                        if lvl2>=10:
                            if users[str(memid)]['sage_spell'] == True:
                                    m = f'{member.mention} owns a `Sage Spell` and is invulnerable of your mortal threats'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif users[str(id)]['sage_spell'] == True:
                                    m = f'{ctx.author.mention} You own a `Sage Spell`, you cannot kill anyone'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif member == ctx.author:
                                m = f'{ctx.author.mention} stabbed themself with a Knife {knife}'
                                level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                await ctx.send(embed=level_embed)
                                await ctx.command.reset_cooldown(ctx)

                            else:
                                L = [1, 2, 3]
                                x = random.choice(L)
                                if x == 1 or x == 3:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u2 = users[str(memid)]['experience']

                                    p = int((u2*0.25)//100)

                                    u2 = u2 - p
                                    users[str(memid)]['experience'] = int(u2)
                                    lvl = int(u2 ** (1/4))
                                    users[str(memid)]['level'] = lvl

                                    u1 = users[str(id)]['experience']
                                    u1 = u1 + p
                                    users[str(id)]['experience'] = int(u1)
                                    lvl = int(u1 ** (1/4))
                                    users[str(id)]['level'] = lvl

                                    with open(guildid, 'w') as f1:
                                        json.dump(users, f1, indent=4)

                                    m = f'{ctx.author.mention} stabbed {member.mention} with a Knife {knife}\n\n{ctx.author.display_name} : `+{p} XP`  •  {member.display_name} : `-{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)

                                else:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u1 = users[str(id)]['experience']

                                    p = int((u1*0.25)//100)

                                    u1 = u1 - p
                                    users[str(id)]['experience'] = int(u1)
                                    lvl = int(u1 ** (1/4))
                                    users[str(id)]['level'] = lvl

                                    u2 = users[str(memid)]['experience']
                                    u2 = u2 + p
                                    users[str(memid)]['experience'] = int(u2)
                                    lvl = int(u2 ** (1/4))
                                    users[str(memid)]['level'] = lvl

                                    with open(guildid, 'w') as f1:
                                        json.dump(users, f1, indent=4)

                                    m = f'{ctx.author.mention} failed to stab {member.mention} with a Knife\n\n{ctx.author.display_name} : `-{p} XP`  •  {member.display_name} : `+{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)
                        else:
                            m = f'{ctx.author.mention} User must be `Level 10` or +'
                            level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                            level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                            await ctx.send(embed=level_embed)
                            await ctx.command.reset_cooldown(ctx)

                    else:
                        m = f'{ctx.author.mention} Requirements to use this command : `Level 10`'
                        level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                        level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                        await ctx.send(embed=level_embed)
                        await ctx.command.reset_cooldown(ctx)
                
                else:  
                    with open("./local/prefix.json", "r") as f:
                        L = json.load(f)

                    if str(ctx.guild.id) in L:
                        get_prefix = L[str(ctx.guild.id)]["prefix"]
                    elif str(ctx.guild.id) not in L:
                        get_prefix = "="

                    m = f'{ctx.author.mention} **You do not own a** {knife} `Knife`\nFor more info use `{get_prefix}help knife`'
                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                    await ctx.send(embed=level_embed)
                    await ctx.command.reset_cooldown(ctx)

            else:
                with open("./local/prefix.json", "r") as f:
                    L = json.load(f)

                if str(ctx.guild.id) in L:
                    get_prefix = L[str(ctx.guild.id)]["prefix"]
                elif str(ctx.guild.id) not in L:
                    get_prefix = "="

                m = f'{ctx.author.mention} **You do not own a** {knife} `Knife`\nFor more info use `{get_prefix}help knife`'
                level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                await ctx.send(embed=level_embed)
                await ctx.command.reset_cooldown(ctx)

    @knife.error
    async def knife_error(self, ctx, error):

        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = error.retry_after

            embed = discord.Embed(description = f"**Knife is being sharped** `{FunCog.convert(self, remaining_time)}`\nKnives have a Cooldown of **30 Seconds**", color=color, timestamp = datetime.datetime.utcnow())
            embed.set_author(name="Kill Cooldown", icon_url="https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed=embed)

    @kill.command(aliases=["Machette"])
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def machette(self, ctx, member : discord.Member = None):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        c = users[str(id)]['color']
        machette = self.bot.get_emoji(881478895503806464)

        if member == None:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(ctx.guild.id) in L:
                get_prefix = L[str(ctx.guild.id)]["prefix"]
            elif str(ctx.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Description** : Kills the mentioned user. Killing a user drops their XP and raises yours. You may also fail to kill them which would drop your XP and raise their's\n\n**Usage** : `{get_prefix}kill <weapon> <user mention>`\n**Example** : `{get_prefix}kill knife @user` to kill a user with a knife" , 
                color = c,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Kill Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed = embed)
            await ctx.command.reset_cooldown(ctx)

        else:
            memid = member.id
            lvl = users[str(id)]['level']
            lvl2 = users[str(memid)]['level']

            with open("./local/weapons.json", "r") as f:
                weapon = json.load(f)

            if str(ctx.author.id) in weapon:
                if weapon[f"{ctx.author.id}"]["machette"] == True:
                    if lvl>=10:
                        if lvl2>=10:
                            if users[str(memid)]['sage_spell'] == True:
                                    m = f'{member.mention} owns a `Sage Spell` and is invulnerable of your mortal threats'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif users[str(id)]['sage_spell'] == True:
                                    m = f'{ctx.author.mention} You own a `Sage Spell`, you cannot kill anyone'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif member == ctx.author:
                                m = f'{ctx.author.mention} stabbed themself with a Machette {machette}'
                                level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                await ctx.send(embed=level_embed)
                                await ctx.command.reset_cooldown(ctx)

                            else:
                                L = [1, 2, 3]
                                x = random.choice(L)
                                if x == 1 or x==3:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u2 = users[str(memid)]['experience']

                                    p = int((u2*0.5)//100)

                                    u2 = u2 - p
                                    users[str(memid)]['experience'] = int(u2)
                                    lvl = int(u2 ** (1/4))
                                    users[str(memid)]['level'] = lvl

                                    u1 = users[str(id)]['experience']
                                    u1 = u1 + p
                                    users[str(id)]['experience'] = int(u1)
                                    lvl = int(u1 ** (1/4))
                                    users[str(id)]['level'] = lvl

                                    with open(guildid, 'w') as f1:
                                        json.dump(users, f1, indent=4)

                                    m = f'{ctx.author.mention} stabbed {member.mention} with a Machette {machette}\n\n{ctx.author.display_name} : `+{p} XP`  •  {member.display_name} : `-{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)

                                else:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u1 = users[str(id)]['experience']

                                    p = int((u1*0.5)//100)

                                    u1 = u1 - p
                                    users[str(id)]['experience'] = int(u1)
                                    lvl = int(u1 ** (1/4))
                                    users[str(id)]['level'] = lvl

                                    u2 = users[str(memid)]['experience']
                                    u2 = u2 + p
                                    users[str(memid)]['experience'] = int(u2)
                                    lvl = int(u2 ** (1/4))
                                    users[str(memid)]['level'] = lvl

                                    with open(guildid, 'w') as f1:
                                        json.dump(users, f1, indent=4)

                                    m = f'{ctx.author.mention} failed to stab {member.mention} with a Machette {machette}\n\n{ctx.author.display_name} : `-{p} XP`  •  {member.display_name} : `+{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)
                        else:
                            m = f'{ctx.author.mention} User must be `Level 10` or +'
                            level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                            level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                            await ctx.send(embed=level_embed)
                            await ctx.command.reset_cooldown(ctx)

                    else:
                        m = f'{ctx.author.mention} Requirements to use this command : `Level 10`'
                        level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                        level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                        await ctx.send(embed=level_embed)
                        await ctx.command.reset_cooldown(ctx)

                else:  
                    with open("./local/prefix.json", "r") as f:
                        L = json.load(f)

                    if str(ctx.guild.id) in L:
                        get_prefix = L[str(ctx.guild.id)]["prefix"]
                    elif str(ctx.guild.id) not in L:
                        get_prefix = "="

                    m = f'{ctx.author.mention} **You do not own a** {machette} `Machette`\nFor more info use `{get_prefix}help machette`'
                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                    await ctx.send(embed=level_embed)
                    await ctx.command.reset_cooldown(ctx)

            else:
                with open("./local/prefix.json", "r") as f:
                    L = json.load(f)

                if str(ctx.guild.id) in L:
                    get_prefix = L[str(ctx.guild.id)]["prefix"]
                elif str(ctx.guild.id) not in L:
                    get_prefix = "="

                m = f'{ctx.author.mention} **You do not own a** {machette} `Machette`\nFor more info use `{get_prefix}help machette`'
                level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                await ctx.send(embed=level_embed)

    @machette.error
    async def machette_error(self, ctx, error):

        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = error.retry_after

            embed = discord.Embed(description = f"**Machette is being sharped** `{FunCog.convert(self, remaining_time)}`\nMachettes have a Cooldown of **2 Minutes**", color=color, timestamp = datetime.datetime.utcnow())
            embed.set_author(name="Kill Cooldown", icon_url="https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed=embed)

    @kill.command(aliases=["Dagger"])
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def dagger(self, ctx, member : discord.Member = None):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        c = users[str(id)]['color']
        dagger = self.bot.get_emoji(881478895835164682)

        if member == None:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(ctx.guild.id) in L:
                get_prefix = L[str(ctx.guild.id)]["prefix"]
            elif str(ctx.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Description** : Kills the mentioned user. Killing a user drops their XP and raises yours. You may also fail to kill them which would drop your XP and raise their's\n\n**Usage** : `{get_prefix}kill <weapon> <user mention>`\n**Example** : `{get_prefix}kill knife @user` to kill a user with a knife" , 
                color = c,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Kill Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed = embed)
            await ctx.command.reset_cooldown(ctx)

        else:
            memid = member.id
            lvl = users[str(id)]['level']
            lvl2 = users[str(memid)]['level']

            with open("./local/weapons.json", "r") as f:
                weapon = json.load(f)

            if str(ctx.author.id) in weapon:
                if weapon[f"{ctx.author.id}"]["dagger"] == True:
                    if lvl>=10:
                        if lvl2>=10:
                            if users[str(memid)]['sage_spell'] == True:
                                    m = f'{member.mention} owns a `Sage Spell` and is invulnerable of your mortal threats'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif users[str(id)]['sage_spell'] == True:
                                    m = f'{ctx.author.mention} You own a `Sage Spell`, you cannot kill anyone'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif member == ctx.author:
                                m = f'{ctx.author.mention} stabbed themself with a Dagger {dagger}'
                                level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                await ctx.send(embed=level_embed)
                                await ctx.command.reset_cooldown(ctx)

                            else:
                                L = [1, 2, 3]
                                x = random.choice(L)
                                if x == 1 or x==3:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u2 = users[str(memid)]['experience']

                                    p = int((u2*0.75)//100)

                                    u2 = u2 - p
                                    users[str(memid)]['experience'] = int(u2)
                                    lvl = int(u2 ** (1/4))
                                    users[str(memid)]['level'] = lvl

                                    u1 = users[str(id)]['experience']
                                    u1 = u1 + p
                                    users[str(id)]['experience'] = int(u1)
                                    lvl = int(u1 ** (1/4))
                                    users[str(id)]['level'] = lvl

                                    with open(guildid, 'w') as f1:
                                        json.dump(users, f1, indent=4)

                                    m = f'{ctx.author.mention} stabbed {member.mention} with a Dagger {dagger}\n\n{ctx.author.display_name} : `+{p} XP`  •  {member.display_name} : `-{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)

                                else:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u1 = users[str(id)]['experience']

                                    p = int((u1*0.75)//100)

                                    u1 = u1 - p
                                    users[str(id)]['experience'] = int(u1)
                                    lvl = int(u1 ** (1/4))
                                    users[str(id)]['level'] = lvl

                                    u2 = users[str(memid)]['experience']
                                    u2 = u2 + p
                                    users[str(memid)]['experience'] = int(u2)
                                    lvl = int(u2 ** (1/4))
                                    users[str(memid)]['level'] = lvl

                                    with open(guildid, 'w') as f1:
                                        json.dump(users, f1, indent=4)

                                    m = f'{ctx.author.mention} failed to stab {member.mention} with a Dagger {dagger}\n\n{ctx.author.display_name} : `-{p} XP`  •  {member.display_name} : `+{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)
                        else:
                            m = f'{ctx.author.mention} User must be `Level 10` or +'
                            level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                            level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                            await ctx.send(embed=level_embed)
                            await ctx.command.reset_cooldown(ctx)

                    else:
                        m = f'{ctx.author.mention} Requirements to use this command : `Level 10`'
                        level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                        level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                        await ctx.send(embed=level_embed)
                        await ctx.command.reset_cooldown(ctx)

                else:  
                    with open("./local/prefix.json", "r") as f:
                        L = json.load(f)

                    if str(ctx.guild.id) in L:
                        get_prefix = L[str(ctx.guild.id)]["prefix"]
                    elif str(ctx.guild.id) not in L:
                        get_prefix = "="

                    m = f'{ctx.author.mention} **You do not own a** {dagger} `Dagger`\nFor more info use `{get_prefix}help dagger`'
                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                    await ctx.send(embed=level_embed)
                    await ctx.command.reset_cooldown(ctx)

            else:
                with open("./local/prefix.json", "r") as f:
                    L = json.load(f)

                if str(ctx.guild.id) in L:
                    get_prefix = L[str(ctx.guild.id)]["prefix"]
                elif str(ctx.guild.id) not in L:
                    get_prefix = "="

                m = f'{ctx.author.mention} **You do not own a** {dagger} `Dagger`\nFor more info use `{get_prefix}help dagger`'
                level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                await ctx.send(embed=level_embed)
                await ctx.command.reset_cooldown(ctx)

    @dagger.error
    async def dagger_error(self, ctx, error):

        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = error.retry_after

            embed = discord.Embed(description = f"**Dagger is being sharped** `{FunCog.convert(self, remaining_time)}`\nDaggers have a Cooldown of **5 Minutes**", color=color, timestamp = datetime.datetime.utcnow())
            embed.set_author(name="Kill Cooldown", icon_url="https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed=embed)

    @kill.command(aliases=["Sword"])
    @commands.cooldown(1, 480, commands.BucketType.user)
    async def sword(self, ctx, member : discord.Member = None):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        c = users[str(id)]['color']
        sword = self.bot.get_emoji(881478895247949887)

        if member == None:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(ctx.guild.id) in L:
                get_prefix = L[str(ctx.guild.id)]["prefix"]
            elif str(ctx.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Description** : Kills the mentioned user. Killing a user drops their XP and raises yours. You may also fail to kill them which would drop your XP and raise their's\n\n**Usage** : `{get_prefix}kill <weapon> <user mention>`\n**Example** : `{get_prefix}kill knife @user` to kill a user with a knife" , 
                color = c,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Kill Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed = embed)
            await ctx.command.reset_cooldown(ctx)

        else:
            memid = member.id
            lvl = users[str(id)]['level']
            lvl2 = users[str(memid)]['level']

            with open("./local/weapons.json", "r") as f:
                weapon = json.load(f)

            if str(ctx.author.id) in weapon:
                if weapon[f"{ctx.author.id}"]["sword"] == True:
                    if lvl>=10:
                        if lvl2>=10:
                            if users[str(memid)]['sage_spell'] == True:
                                    m = f'{member.mention} owns a `Sage Spell` and is invulnerable of your mortal threats'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif users[str(id)]['sage_spell'] == True:
                                    m = f'{ctx.author.mention} You own a `Sage Spell`, you cannot kill anyone'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif member == ctx.author:
                                m = f'{ctx.author.mention} slashed themself with a Sword {sword}'
                                level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                await ctx.send(embed=level_embed)
                                await ctx.command.reset_cooldown(ctx)

                            else:
                                L = [1, 2, 3]
                                x = random.choice(L)
                                if x == 1 or x==3:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u2 = users[str(memid)]['experience']

                                    p = int((u2*1)//100)

                                    u2 = u2 - p
                                    users[str(memid)]['experience'] = int(u2)
                                    lvl = int(u2 ** (1/4))
                                    users[str(memid)]['level'] = lvl

                                    u1 = users[str(id)]['experience']
                                    u1 = u1 + p
                                    users[str(id)]['experience'] = int(u1)
                                    lvl = int(u1 ** (1/4))
                                    users[str(id)]['level'] = lvl

                                    with open(guildid, 'w') as f1:
                                        json.dump(users, f1, indent=4)

                                    m = f'{ctx.author.mention} slashed {member.mention} with a Sword {sword}\n\n{ctx.author.display_name} : `+{p} XP`  •  {member.display_name} : `-{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)

                                else:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u1 = users[str(id)]['experience']

                                    p = int((u1*1)//100)

                                    u1 = u1 - p
                                    users[str(id)]['experience'] = int(u1)
                                    lvl = int(u1 ** (1/4))
                                    users[str(id)]['level'] = lvl

                                    u2 = users[str(memid)]['experience']
                                    u2 = u2 + p
                                    users[str(memid)]['experience'] = int(u2)
                                    lvl = int(u2 ** (1/4))
                                    users[str(memid)]['level'] = lvl

                                    with open(guildid, 'w') as f1:
                                        json.dump(users, f1, indent=4)

                                    m = f'{ctx.author.mention} failed to slash {member.mention} with a Sword {sword}\n\n{ctx.author.display_name} : `-{p} XP`  •  {member.display_name} : `+{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)
                        else:
                            m = f'{ctx.author.mention} User must be `Level 10` or +'
                            level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                            level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                            await ctx.send(embed=level_embed)
                            await ctx.command.reset_cooldown(ctx)

                    else:
                        m = f'{ctx.author.mention} Requirements to use this command : `Level 10`'
                        level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                        level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                        await ctx.send(embed=level_embed)
                        await ctx.command.reset_cooldown(ctx)

                else:  
                    with open("./local/prefix.json", "r") as f:
                        L = json.load(f)

                    if str(ctx.guild.id) in L:
                        get_prefix = L[str(ctx.guild.id)]["prefix"]
                    elif str(ctx.guild.id) not in L:
                        get_prefix = "="

                    m = f'{ctx.author.mention} **You do not own a** {sword} `Sword`\nFor more info use `{get_prefix}help sword`'
                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                    await ctx.send(embed=level_embed)
                    await ctx.command.reset_cooldown(ctx)

            else:
                with open("./local/prefix.json", "r") as f:
                    L = json.load(f)

                if str(ctx.guild.id) in L:
                    get_prefix = L[str(ctx.guild.id)]["prefix"]
                elif str(ctx.guild.id) not in L:
                    get_prefix = "="

                m = f'{ctx.author.mention} **You do not own a** {sword} `Sword`\nFor more info use `{get_prefix}help sword`'
                level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                await ctx.send(embed=level_embed)
                await ctx.command.reset_cooldown(ctx)

    @sword.error
    async def sword_error(self, ctx, error):

        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = error.retry_after

            embed = discord.Embed(description = f"**Sword is being sharped** `{FunCog.convert(self, remaining_time)}`\nSwords have a Cooldown of **8 Minutes**", color=color, timestamp = datetime.datetime.utcnow())
            embed.set_author(name="Kill Cooldown", icon_url="https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed=embed)

    @kill.command(aliases=["Scythe"])
    @commands.cooldown(1, 900, commands.BucketType.user)
    async def scythe(self, ctx, member : discord.Member = None):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        c = users[str(id)]['color']
        scythe = self.bot.get_emoji(881478895604494376)

        if member == None:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(ctx.guild.id) in L:
                get_prefix = L[str(ctx.guild.id)]["prefix"]
            elif str(ctx.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Description** : Kills the mentioned user. Killing a user drops their XP and raises yours. You may also fail to kill them which would drop your XP and raise their's\n\n**Usage** : `{get_prefix}kill <weapon> <user mention>`\n**Example** : `{get_prefix}kill knife @user` to kill a user with a knife" , 
                color = c,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Kill Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed = embed)
            await ctx.command.reset_cooldown(ctx)

        else:
            memid = member.id
            lvl = users[str(id)]['level']
            lvl2 = users[str(memid)]['level']

            with open("./local/weapons.json", "r") as f:
                weapon = json.load(f)

            if str(ctx.author.id) in weapon:
                if weapon[f"{ctx.author.id}"]["scythe"] == True:
                    if lvl>=10:
                        if lvl2>=10:
                            if users[str(memid)]['sage_spell'] == True:
                                    m = f'{member.mention} owns a `Sage Spell` and is invulnerable of your mortal threats'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif users[str(id)]['sage_spell'] == True:
                                    m = f'{ctx.author.mention} You own a `Sage Spell`, you cannot kill anyone'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif member == ctx.author:
                                m = f'{ctx.author.mention} slashed themself with a Scythe {scythe}'
                                level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                await ctx.send(embed=level_embed)
                                await ctx.command.reset_cooldown(ctx)

                            else:
                                L = [1, 2, 3]
                                x = random.choice(L)
                                if x == 1 or x==3:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u2 = users[str(memid)]['experience']

                                    p = int((u2*1.5)//100)

                                    u2 = u2 - p
                                    users[str(memid)]['experience'] = int(u2)
                                    lvl = int(u2 ** (1/4))
                                    users[str(memid)]['level'] = lvl

                                    u1 = users[str(id)]['experience']
                                    u1 = u1 + p
                                    users[str(id)]['experience'] = int(u1)
                                    lvl = int(u1 ** (1/4))
                                    users[str(id)]['level'] = lvl

                                    with open(guildid, 'w') as f1:
                                        json.dump(users, f1, indent=4)

                                    m = f'{ctx.author.mention} slashed {member.mention} with a Scythe {scythe}\n\n{ctx.author.display_name} : `+{p} XP`  •  {member.display_name} : `-{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)

                                else:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u1 = users[str(id)]['experience']

                                    p = int((u1*1.5)//100)

                                    u1 = u1 - p
                                    users[str(id)]['experience'] = int(u1)
                                    lvl = int(u1 ** (1/4))
                                    users[str(id)]['level'] = lvl

                                    u2 = users[str(memid)]['experience']
                                    u2 = u2 + p
                                    users[str(memid)]['experience'] = int(u2)
                                    lvl = int(u2 ** (1/4))
                                    users[str(memid)]['level'] = lvl

                                    with open(guildid, 'w') as f1:
                                        json.dump(users, f1, indent=4)

                                    m = f'{ctx.author.mention} failed to slash {member.mention} with a Scythe {scythe}\n\n{ctx.author.display_name} : `-{p} XP`  •  {member.display_name} : `+{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)
                        else:
                            m = f'{ctx.author.mention} User must be `Level 10` or +'
                            level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                            level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                            await ctx.send(embed=level_embed)
                            await ctx.command.reset_cooldown(ctx)

                    else:
                        m = f'{ctx.author.mention} Requirements to use this command : `Level 10`'
                        level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                        level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                        await ctx.send(embed=level_embed)
                        await ctx.command.reset_cooldown(ctx)

                else:  
                    with open("./local/prefix.json", "r") as f:
                        L = json.load(f)

                    if str(ctx.guild.id) in L:
                        get_prefix = L[str(ctx.guild.id)]["prefix"]
                    elif str(ctx.guild.id) not in L:
                        get_prefix = "="

                    m = f'{ctx.author.mention} **You do not own a** {scythe} `Scythe`\nFor more info use `{get_prefix}help scythe`'
                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                    await ctx.send(embed=level_embed)
                    await ctx.command.reset_cooldown(ctx)

            else:
                with open("./local/prefix.json", "r") as f:
                    L = json.load(f)

                if str(ctx.guild.id) in L:
                    get_prefix = L[str(ctx.guild.id)]["prefix"]
                elif str(ctx.guild.id) not in L:
                    get_prefix = "="

                m = f'{ctx.author.mention} **You do not own a** {scythe} `Scythe`\nFor more info use `{get_prefix}help scythe`'
                level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                await ctx.send(embed=level_embed)
                await ctx.command.reset_cooldown(ctx)

    @scythe.error
    async def scythe_error(self, ctx, error):

        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = error.retry_after

            embed = discord.Embed(description = f"**Scythe is being sharped** `{FunCog.convert(self, remaining_time)}`\nScythes have a Cooldown of **15 Minutes**", color=color, timestamp = datetime.datetime.utcnow())
            embed.set_author(name="Kill Cooldown", icon_url="https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed=embed)

    @kill.command(aliases=["Shuriken"])
    @commands.cooldown(1, 1800, commands.BucketType.user)
    async def shuriken(self, ctx, member : discord.Member = None):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        c = users[str(id)]['color']
        shuriken = self.bot.get_emoji(881478895889690674)

        if member == None:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(ctx.guild.id) in L:
                get_prefix = L[str(ctx.guild.id)]["prefix"]
            elif str(ctx.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Description** : Kills the mentioned user. Killing a user drops their XP and raises yours. You may also fail to kill them which would drop your XP and raise their's\n\n**Usage** : `{get_prefix}kill <weapon> <user mention>`\n**Example** : `{get_prefix}kill knife @user` to kill a user with a knife" , 
                color = c,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Kill Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed = embed)
            await ctx.command.reset_cooldown(ctx)

        else:
            memid = member.id
            lvl = users[str(id)]['level']
            lvl2 = users[str(memid)]['level']

            with open("./local/weapons.json", "r") as f:
                weapon = json.load(f)

            if str(ctx.author.id) in weapon:
                if weapon[f"{ctx.author.id}"]["shuriken"] == True:
                    if lvl>=10:
                        if lvl2>=10:
                            if users[str(memid)]['sage_spell'] == True:
                                    m = f'{member.mention} owns a `Sage Spell` and is invulnerable of your mortal threats'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif users[str(id)]['sage_spell'] == True:
                                    m = f'{ctx.author.mention} You own a `Sage Spell`, you cannot kill anyone'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif member == ctx.author:
                                m = f'{ctx.author.mention} pierced themself with a Shuriken {shuriken}'
                                level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                await ctx.send(embed=level_embed)
                                await ctx.command.reset_cooldown(ctx)

                            else:
                                L = [1, 2, 3]
                                x = random.choice(L)
                                if x == 1 or x==3:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u2 = users[str(memid)]['experience']

                                    p = int((u2*2)//100)

                                    u2 = u2 - p
                                    users[str(memid)]['experience'] = int(u2)
                                    lvl = int(u2 ** (1/4))
                                    users[str(memid)]['level'] = lvl

                                    u1 = users[str(id)]['experience']
                                    u1 = u1 + p
                                    users[str(id)]['experience'] = int(u1)
                                    lvl = int(u1 ** (1/4))
                                    users[str(id)]['level'] = lvl

                                    with open(guildid, 'w') as f1:
                                        json.dump(users, f1, indent=4)

                                    m = f'{ctx.author.mention} pierced a Shuriken {shuriken} through {member.mention}\n\n{ctx.author.display_name} : `+{p} XP`  •  {member.display_name} : `-{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)

                                else:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u1 = users[str(id)]['experience']

                                    p = int((u1*2)//100)

                                    u1 = u1 - p
                                    users[str(id)]['experience'] = int(u1)
                                    lvl = int(u1 ** (1/4))
                                    users[str(id)]['level'] = lvl

                                    u2 = users[str(memid)]['experience']
                                    u2 = u2 + p
                                    users[str(memid)]['experience'] = int(u2)
                                    lvl = int(u2 ** (1/4))
                                    users[str(memid)]['level'] = lvl

                                    with open(guildid, 'w') as f1:
                                        json.dump(users, f1, indent=4)

                                    m = f'{ctx.author.mention} failed to pierce a Shuriken {shuriken} through {member.mention}\n\n{ctx.author.display_name} : `-{p} XP`  •  {member.display_name} : `+{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                                    await ctx.send(embed=level_embed)
                        else:
                            m = f'{ctx.author.mention} User must be `Level 10` or +'
                            level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                            level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                            await ctx.send(embed=level_embed)
                            await ctx.command.reset_cooldown(ctx)

                    else:
                        m = f'{ctx.author.mention} Requirements to use this command : `Level 10`'
                        level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                        level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                        await ctx.send(embed=level_embed)
                        await ctx.command.reset_cooldown(ctx)

                else:  
                    with open("./local/prefix.json", "r") as f:
                        L = json.load(f)

                    if str(ctx.guild.id) in L:
                        get_prefix = L[str(ctx.guild.id)]["prefix"]
                    elif str(ctx.guild.id) not in L:
                        get_prefix = "="

                    m = f'{ctx.author.mention} **You do not own a** {shuriken} `Shuriken`\nFor more info use `{get_prefix}help shuriken`'
                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                    await ctx.send(embed=level_embed)
                    await ctx.command.reset_cooldown(ctx)

            else:
                with open("./local/prefix.json", "r") as f:
                    L = json.load(f)

                if str(ctx.guild.id) in L:
                    get_prefix = L[str(ctx.guild.id)]["prefix"]
                elif str(ctx.guild.id) not in L:
                    get_prefix = "="

                m = f'{ctx.author.mention} **You do not own a** {shuriken} `Shuriken`\nFor more info use `{get_prefix}help shuriken`'
                level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
                await ctx.send(embed=level_embed)
                await ctx.command.reset_cooldown(ctx)

    @shuriken.error
    async def shuriken_error(self, ctx, error):

        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = error.retry_after

            embed = discord.Embed(description = f"**Shuriken is being sharped** `{FunCog.convert(self, remaining_time)}`\nShuriken have a Cooldown of **30 Minutes**", color=color, timestamp = datetime.datetime.utcnow())
            embed.set_author(name="Kill Cooldown", icon_url="https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed=embed)

    @commands.command()
    async def roast(self, message, member : discord.Member = None):
        
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if member == None:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(message.guild.id) in L:
                get_prefix = L[str(message.guild.id)]["prefix"]
            elif str(message.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Description** : Roasts the mentioned user\n\n**Usage** : `{get_prefix}roast <user-mention>`\n**Example** : `{get_prefix}roast @user` to roast a user" , 
                color = color, 
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Roast Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await message.channel.send(embed = embed)

        else:
            with open("./local/roast.json", "r") as f:
                roasts = json.load(f)

            r = random.choice(roasts)
            await message.channel.send(f"{member.mention} {r}")

    @commands.command()
    async def hack(self, message, member: discord.Member = None):
        
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if member == None or member.id == message.author.id:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(message.guild.id) in L:
                get_prefix = L[str(message.guild.id)]["prefix"]
            elif str(message.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Description** : Hacks a user, 100% real.\n\n**Usage** : `{get_prefix}hack <user mention>`\n**Example** : `{get_prefix}hack @user`" , 
                color = color, 
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Hack Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await message.channel.send(embed = embed)

        elif member.id == 840180379389263882:
            heckmsg = await message.channel.send("Setting up linux...")
            await asyncio.sleep(2)
            await heckmsg.edit("Loading")
            await asyncio.sleep(1)
            await heckmsg.edit("Loading •")
            await asyncio.sleep(1)
            await heckmsg.edit("Loading • •")
            await asyncio.sleep(1)
            await heckmsg.edit("Loading • • •")
            await asyncio.sleep(1)
            await heckmsg.edit("System failed! I cannot be hacked") 

        else:
            heckmsg = await message.channel.send("Setting up linux...")
            await asyncio.sleep(2)
            await heckmsg.edit("Loading")
            await asyncio.sleep(1)
            await heckmsg.edit("Loading •")
            await asyncio.sleep(1)
            await heckmsg.edit("Loading • •")
            await asyncio.sleep(1)
            await heckmsg.edit("Loading • • •")
            await asyncio.sleep(1)
            await heckmsg.edit("System loaded successfully!")
            await asyncio.sleep(1)
            await heckmsg.edit(f"[▖] Sending malicious data to {member.name}")
            await asyncio.sleep(1)
            await heckmsg.edit(f"[▘] Reading Instagram DMs : `i look like a horse`")
            await asyncio.sleep(1)
            await heckmsg.edit(f"[▝] Private images downloaded : `holy-poop.jpg`")
            await asyncio.sleep(1)
            await heckmsg.edit(f"[▗] input('obtain passwords')")
            await asyncio.sleep(1)
            await heckmsg.edit(f"[▖] print('passwords recieved')")
            await asyncio.sleep(1)
            await heckmsg.edit(f"[▘] Selling browsing history to friends")
            await asyncio.sleep(1)
            await heckmsg.edit(f"[▝] Browsing history sold : `cute armpits`")
            await asyncio.sleep(1)
            await heckmsg.edit(f"[▗] Transaction history sold : `butt lotion $12`")
            await asyncio.sleep(1)
            await heckmsg.edit(f"[▖] Attacking devices using matrix...")
            await asyncio.sleep(1)
            await heckmsg.edit(f"[▘] Starting the matrix...")
            await asyncio.sleep(1)
            await heckmsg.edit(f"0 1 1 0 1 0 1 0 0 1 1 0 1 0 1\n"
            f" 1 0 1 1 0 1 1 1 0 1 0 0 1 0 1\n"
            f"1 0 0 1 1 0 1 0 1 0 1 1 0 1 0\n"
            f" 0 1 0 0 1 1 0 1 0 1 0 0 1 1 1")
            await asyncio.sleep(0.2)
            await heckmsg.edit(f" 0 1 0 0 1 1 0 1 0 1 0 0 1 1 1\n"
            f"0 1 1 0 1 0 1 0 0 1 1 0 1 0 1\n"
            f" 1 0 1 1 0 1 1 1 0 1 0 0 1 0 1\n"
            f"1 0 0 1 1 0 1 0 1 0 1 1 0 1 0\n")
            await asyncio.sleep(0.2)
            await heckmsg.edit(f"0 1 1 0 1 0 1 0 0 1 1 0 1 0 1\n"
            f" 1 0 1 1 0 1 1 1 0 1 0 0 1 0 1\n"
            f"1 0 0 1 1 0 1 0 1 0 1 1 0 1 0\n"
            f" 0 1 0 0 1 1 0 1 0 1 0 0 1 1 1")
            await asyncio.sleep(0.2)
            await heckmsg.edit(f" 0 1 0 0 1 1 0 1 0 1 0 0 1 1 1\n"
            f"0 1 1 0 1 0 1 0 0 1 1 0 1 0 1\n"
            f" 1 0 1 1 0 1 1 1 0 1 0 0 1 0 1\n"
            f"1 0 0 1 1 0 1 0 1 0 1 1 0 1 0\n")
            await asyncio.sleep(0.2)
            await heckmsg.edit(f"0 1 1 0 1 0 1 0 0 1 1 0 1 0 1\n"
            f" 1 0 1 1 0 1 1 1 0 1 0 0 1 0 1\n"
            f"1 0 0 1 1 0 1 0 1 0 1 1 0 1 0\n"
            f" 0 1 0 0 1 1 0 1 0 1 0 0 1 1 1")
            await asyncio.sleep(0.2)
            await heckmsg.edit(f" 0 1 0 0 1 1 0 1 0 1 0 0 1 1 1\n"
            f"0 1 1 0 1 0 1 0 0 1 1 0 1 0 1\n"
            f" 1 0 1 1 0 1 1 1 0 1 0 0 1 0 1\n"
            f"1 0 0 1 1 0 1 0 1 0 1 1 0 1 0\n")
            await asyncio.sleep(0.2)
            await heckmsg.edit(f"0 1 1 0 1 0 1 0 0 1 1 0 1 0 1\n"
            f" 1 0 1 1 0 1 1 1 0 1 0 0 1 0 1\n"
            f"1 0 0 1 1 0 1 0 1 0 1 1 0 1 0\n"
            f" 0 1 0 0 1 1 0 1 0 1 0 0 1 1 1")
            await asyncio.sleep(0.2)
            await heckmsg.edit(f" 0 1 0 0 1 1 0 1 0 1 0 0 1 1 1\n"
            f"0 1 1 0 1 0 1 0 0 1 1 0 1 0 1\n"
            f" 1 0 1 1 0 1 1 1 0 1 0 0 1 0 1\n"
            f"1 0 0 1 1 0 1 0 1 0 1 1 0 1 0\n")
            await asyncio.sleep(0.2)
            await heckmsg.edit(f"0 1 1 0 1 0 1 0 0 1 1 0 1 0 1\n"
            f" 1 0 1 1 0 1 1 1 0 1 0 0 1 0 1\n"
            f"1 0 0 1 1 0 1 0 1 0 1 1 0 1 0\n"
            f" 0 1 0 0 1 1 0 1 0 1 0 0 1 1 1")
            await asyncio.sleep(0.2)
            await heckmsg.edit(f" 0 1 0 0 1 1 0 1 0 1 0 0 1 1 1\n"
            f"0 1 1 0 1 0 1 0 0 1 1 0 1 0 1\n"
            f" 1 0 1 1 0 1 1 1 0 1 0 0 1 0 1\n"
            f"1 0 0 1 1 0 1 0 1 0 1 1 0 1 0\n")
            await asyncio.sleep(0.2)
            await heckmsg.edit(f"0 1 1 0 1 0 1 0 0 1 1 0 1 0 1\n"
            f" 1 0 1 1 0 1 1 1 0 1 0 0 1 0 1\n"
            f"1 0 0 1 1 0 1 0 1 0 1 1 0 1 0\n"
            f" 0 1 0 0 1 1 0 1 0 1 0 0 1 1 1")
            await heckmsg.edit(f"{member.name} hacked!\nData has been sent to you via dm!")
            await message.author.send(f"Download {member.name}'s private information here : https://michelle-bot.co/9bZkp7q19f0.html")

    @commands.command()
    async def dumbrate(self, message, member: discord.Member = None):
        
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        dumbRate = str(random.randint(0, 100))

        if member == None or member.id == message.author.id:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(message.guild.id) in L:
                get_prefix = L[str(message.guild.id)]["prefix"]
            elif str(message.guild.id) not in L:
                get_prefix = "="

            dumbmsg = await message.channel.send("Calculating your dumb rate")
            await asyncio.sleep(2)
            await dumbmsg.edit("Calculating")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating •")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating • •")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating • • •")
            await asyncio.sleep(1)
            await dumbmsg.edit(f"You are **{dumbRate}%** dumb")

        elif member.id == 840180379389263882:
            dumbmsg = await message.channel.send(f"Calculating my dumb rate")
            await asyncio.sleep(2)
            await dumbmsg.edit("Calculating")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating •")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating • •")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating • • •")
            await asyncio.sleep(1)
            await dumbmsg.edit(f"I am **0%** dumb")   

        else:
            dumbmsg = await message.channel.send(f"Calculating {member.name}'s dumb rate")
            await asyncio.sleep(2)
            await dumbmsg.edit("Calculating")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating •")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating • •")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating • • •")
            await asyncio.sleep(1)
            await dumbmsg.edit(f"{member.name} is **{dumbRate}%** dumb")

    @commands.command()
    async def simprate(self, message, member: discord.Member = None):
        
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        dumbRate = str(random.randint(0, 100))

        if member == None or member.id == message.author.id:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(message.guild.id) in L:
                get_prefix = L[str(message.guild.id)]["prefix"]
            elif str(message.guild.id) not in L:
                get_prefix = "="

            dumbmsg = await message.channel.send("Calculating your simp rate")
            await asyncio.sleep(2)
            await dumbmsg.edit("Calculating")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating •")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating • •")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating • • •")
            await asyncio.sleep(1)
            await dumbmsg.edit(f"You are **{dumbRate}%** simp")

        elif member.id == 840180379389263882:
            dumbmsg = await message.channel.send(f"Calculating my simp rate")
            await asyncio.sleep(2)
            await dumbmsg.edit("Calculating")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating •")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating • •")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating • • •")
            await asyncio.sleep(1)
            await dumbmsg.edit(f"I am **100%** simp 4u")   

        else:
            dumbmsg = await message.channel.send(f"Calculating {member.name}'s simp rate")
            await asyncio.sleep(2)
            await dumbmsg.edit("Calculating")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating •")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating • •")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating • • •")
            await asyncio.sleep(1)
            await dumbmsg.edit(f"{member.name} is **{dumbRate}%** simp")

    @commands.command()
    async def simprate(self, message, member: discord.Member = None):
        
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        dumbRate = str(random.randint(0, 100))

        if member == None or member.id == message.author.id:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(message.guild.id) in L:
                get_prefix = L[str(message.guild.id)]["prefix"]
            elif str(message.guild.id) not in L:
                get_prefix = "="

            dumbmsg = await message.channel.send("Calculating your simp rate")
            await asyncio.sleep(2)
            await dumbmsg.edit("Calculating")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating •")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating • •")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating • • •")
            await asyncio.sleep(1)
            await dumbmsg.edit(f"You are **{dumbRate}%** simp")

        elif member.id == 840180379389263882:
            dumbmsg = await message.channel.send(f"Calculating my simp rate")
            await asyncio.sleep(2)
            await dumbmsg.edit("Calculating")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating •")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating • •")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating • • •")
            await asyncio.sleep(1)
            await dumbmsg.edit(f"I am **100%** simp 4u")   

        else:
            dumbmsg = await message.channel.send(f"Calculating {member.name}'s simp rate")
            await asyncio.sleep(2)
            await dumbmsg.edit("Calculating")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating •")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating • •")
            await asyncio.sleep(1)
            await dumbmsg.edit("Calculating • • •")
            await asyncio.sleep(1)
            await dumbmsg.edit(f"{member.name} is **{dumbRate}%** simp")

    @commands.command(name = "aww", aliases = ["aw", "awww", "Aw", "AW", "Aww", "AWW"])
    async def aww(self, ctx):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = self.bot.get_guild(guildid)
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        try:

            reddit = praw.Reddit(client_id = 'vOtMxaMzhnpD9A', client_secret = 'NIzr13jWXE8MPVsIxtRVe_HqftPAOQ', user_agent = 'Olivia')
            memes_submissions = reddit.subreddit("wholesomememes").hot()
            post = random.randint(1, 100)
            for i in range(0, post):
                submission = next(x for x in memes_submissions if not x.stickied)

            if submission.url.endswith('.png') or submission.url.endswith('.jpg') or submission.url.endswith('.gif'):
                embed = discord.Embed(description = f"{submission.title}",
                timestamp=datetime.datetime.utcnow(),
                color=color)

                embed.set_footer(text=ctx.author)
                embed.set_image(url=f"{submission.url}")

                await ctx.send(embed=embed)

            else:
                await ctx.send(f'Called by : {ctx.author}\nTitle : {submission.title}\n{submission.url}')

        except:

            await ctx.author.send(f"We've encountered an error! ☹️\nError from : `{guild.name}`")

    @commands.command()
    async def kitty(self, ctx):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = self.bot.get_guild(guildid)
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        try:

            reddit = praw.Reddit(client_id = 'vOtMxaMzhnpD9A', client_secret = 'NIzr13jWXE8MPVsIxtRVe_HqftPAOQ', user_agent = 'Olivia')
            memes_submissions = reddit.subreddit("catpics").hot()
            post = random.randint(1, 100)
            for i in range(0, post):
                submission = next(x for x in memes_submissions if not x.stickied)

            if submission.url.endswith('.png') or submission.url.endswith('.jpg') or submission.url.endswith('.gif'):
                embed = discord.Embed(title = "Meow 🐈",
                timestamp=datetime.datetime.utcnow(),
                color=color)

                embed.set_footer(text=ctx.author)
                embed.set_image(url=f"{submission.url}")

                await ctx.send(embed=embed)

            else:
                await ctx.send(f'Called by : {ctx.author}\nTitle : {submission.title}\n{submission.url}')

        except:

            await ctx.author.send(f"We've encountered an error! ☹️\nError from : `{guild.name}`")

    @commands.command()
    async def doggo(self, ctx):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = self.bot.get_guild(guildid)
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        try:

            reddit = praw.Reddit(client_id = 'vOtMxaMzhnpD9A', client_secret = 'NIzr13jWXE8MPVsIxtRVe_HqftPAOQ', user_agent = 'Olivia')
            memes_submissions = reddit.subreddit("dogpics").hot()
            post = random.randint(1, 100)
            for i in range(0, post):
                submission = next(x for x in memes_submissions if not x.stickied)

            if submission.url.endswith('.png') or submission.url.endswith('.jpg') or submission.url.endswith('.gif'):
                embed = discord.Embed(title = "Bow bow 🐕",
                timestamp=datetime.datetime.utcnow(),
                color=color)

                embed.set_footer(text=ctx.author)
                embed.set_image(url=f"{submission.url}")

                await ctx.send(embed=embed)

            else:
                await ctx.send(f'Called by : {ctx.author}\nTitle : {submission.title}\n{submission.url}')

        except:

            await ctx.author.send(f"We've encountered an error! ☹️\nError from : `{guild.name}`")

    @commands.command(aliases = ["shower", "showerthought"])
    async def showerthoughts(self, ctx):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = self.bot.get_guild(guildid)
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        try:

            reddit = praw.Reddit(client_id = 'vOtMxaMzhnpD9A', client_secret = 'NIzr13jWXE8MPVsIxtRVe_HqftPAOQ', user_agent = 'Olivia')
            memes_submissions = reddit.subreddit("showerthoughts").hot()
            post = random.randint(1, 100)
            for i in range(0, post):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title = f"{submission.title}",
            url = f"{submission.url}",
            timestamp=datetime.datetime.utcnow(),
            color=color)

            embed.set_author(name = "Shower Thoughts", icon_url= self.bot.user.avatar)
            embed.set_footer(text=ctx.author)

            await ctx.send(embed=embed)

        except:

            await ctx.author.send(f"We've encountered an error! ☹️\nError from : `{guild.name}`")

    @commands.command(aliases = ["dadjoke"])
    async def dadjokes(self, ctx):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = self.bot.get_guild(guildid)
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        try:

            reddit = praw.Reddit(client_id = 'vOtMxaMzhnpD9A', client_secret = 'NIzr13jWXE8MPVsIxtRVe_HqftPAOQ', user_agent = 'Olivia')
            memes_submissions = reddit.subreddit("dadjokes").hot()
            post = random.randint(1, 100)
            for i in range(0, post):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title = f"{submission.title}", description = f"{submission.selftext}",
            url = f"{submission.url}",
            timestamp=datetime.datetime.utcnow(),
            color=color)

            embed.set_author(name = "Dad Jokes", icon_url= self.bot.user.avatar)
            embed.set_footer(text=ctx.author)

            await ctx.send(embed=embed)

        except:

            await ctx.author.send(f"We've encountered an error! ☹️\nError from : `{guild.name}`")

    @commands.command()
    async def emojify(self, ctx, text : str = None):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = self.bot.get_guild(guildid)
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        c = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        if text == None:
            embed = discord.Embed(
                description = f"**Description** : Emojify any given text\n\n**Usage** : `{get_prefix}emojify <text>`\n**Example** : `{get_prefix}emojify hello there` to Emojify the phrase - *Hello There* " , 
                color = c,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Emojify Help ❓")
            await ctx.send(embed = embed)

        else:
            text = ctx.message.content.replace(f"{get_prefix}emojify ", "")
            text = text.upper()
            text = list(text)
            emojify = ""

            for i in text:
                if i in emoji_dict:
                    index = text.index(i)
                    text[index] = emoji_dict[i]

            for i in text:
                emojify += f"{i} "

            await ctx.send(f"> {emojify}")

    @commands.command(aliases = ["guessthepokemon", "gtp", "pokemon"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def guess(self, ctx, difficulty: str = "easy"):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = self.bot.get_guild(guildid)
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if difficulty == "easy":
            id = random.randint(1, 251)

            photo = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{id}.png"
            link = f"https://pokeapi.co/api/v2/pokemon/{id}"
            response = requests.get(link)
            data = response.json()

            name = data["name"]

            embed = discord.Embed(description = f"**Guess the Pokemon**\nType the name of this Pokemon to guess",color=color, timestamp=datetime.datetime.utcnow())
            embed.set_image(url=photo)
            embed.set_author(name=f"{ctx.author}", icon_url=self.bot.user.avatar)

            botmsg = await ctx.send(embed=embed)

            cross = self.bot.get_emoji(880679527200735273)
            mark = self.bot.get_emoji(880679486205620234)

            try:
                def check(message):
                    message.content = message.content.lower()
                    return f"{name}" in message.content and ctx.author.id == message.author.id

                msg = ping = await self.bot.wait_for("message", check=check, timeout=60)
                ping = ping.content

                if f"{name}" in ping:
                    await botmsg.add_reaction(f"{mark}")
                    await msg.add_reaction(f"{mark}")

                    id = msg.author.id

                    guildid = ctx.guild.id

                    guildid = './guild data/'+ str(guildid) +'.json'
                    with open(guildid, 'r') as f:
                        users = json.load(f)

                    xp = users[str(id)]['experience']
                    initial_level = users[str(id)]['level']

                    daily = random.randint(20, 50)
                    daily = daily*5
                    xp += daily
                    users[str(id)]['experience'] = int(xp)
                    lvl = int(xp ** (1/4))
                    users[str(id)]['level'] = lvl

                    with open(guildid, 'w') as f:
                        json.dump(users, f, indent=4)


                    if lvl > initial_level:
                        with open("./local/settings.json") as s:
                            set = json.load(s)

                        if str(ctx.author.id) in set:
                            if set[f"{ctx.author.id}"]["level_ups"] == True:
                                if initial_level < 10 and lvl >= 10:
                                    
                                    stonks = self.bot.get_emoji(896752212749983774)
                                    await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}** and unlocked the ability to `Kill`! {stonks}")

                                elif initial_level < 5 and lvl >= 5:

                                    stonks = self.bot.get_emoji(896752212749983774)
                                    await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}** and unlocked `Themes`! {stonks}")

                                elif lvl > initial_level:
                                    stonks = self.bot.get_emoji(896752212749983774)
                                    await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}**! {stonks}")

                        elif str(ctx.author.id) not in set:
                            if initial_level < 10 and lvl >= 10:
                                
                                stonks = self.bot.get_emoji(896752212749983774)
                                await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}** and unlocked the ability to `Kill`! {stonks}")

                            elif initial_level < 5 and lvl >= 5:

                                stonks = self.bot.get_emoji(896752212749983774)
                                await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}** and unlocked `Themes`! {stonks}")

                            elif lvl > initial_level:
                                stonks = self.bot.get_emoji(896752212749983774)
                                await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}**! {stonks}")

                    await msg.reply(f"**Correct!** You recieved **{daily} XP**")

            except asyncio.TimeoutError:
                await botmsg.add_reaction(f"{cross}")

        elif difficulty == "medium":
            id = random.randint(252, 655)

            photo = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{id}.png"
            link = f"https://pokeapi.co/api/v2/pokemon/{id}"
            response = requests.get(link)
            data = response.json()

            name = data["name"]

            embed = discord.Embed(description = f"**Guess the Pokemon**\nType the name of this Pokemon to guess", color=color, timestamp=datetime.datetime.utcnow())
            embed.set_image(url=photo)
            embed.set_author(name=f"{ctx.author}", icon_url=self.bot.user.avatar)

            botmsg = await ctx.send(embed=embed)

            cross = self.bot.get_emoji(880679527200735273)
            mark = self.bot.get_emoji(880679486205620234)

            try:
                def check(message):
                    message.content = message.content.lower()
                    return f"{name}" in message.content and ctx.author.id == message.author.id

                msg = ping = await self.bot.wait_for("message", check=check, timeout=60)
                ping = ping.content

                if f"{name}" in ping:
                    await botmsg.add_reaction(f"{mark}")
                    await msg.add_reaction(f"{mark}")

                    id = msg.author.id

                    guildid = ctx.guild.id

                    guildid = './guild data/'+ str(guildid) +'.json'
                    with open(guildid, 'r') as f:
                        users = json.load(f)

                    xp = users[str(id)]['experience']
                    initial_level = users[str(id)]['level']

                    daily = random.randint(50, 70)
                    daily = daily*5
                    xp += daily
                    users[str(id)]['experience'] = int(xp)
                    lvl = int(xp ** (1/4))
                    users[str(id)]['level'] = lvl

                    with open(guildid, 'w') as f:
                        json.dump(users, f, indent=4)


                    if lvl > initial_level:
                        with open("./local/settings.json") as s:
                            set = json.load(s)

                        if str(ctx.author.id) in set:
                            if set[f"{ctx.author.id}"]["level_ups"] == True:
                                if initial_level < 10 and lvl >= 10:
                                    
                                    stonks = self.bot.get_emoji(896752212749983774)
                                    await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}** and unlocked the ability to `Kill`! {stonks}")

                                elif initial_level < 5 and lvl >= 5:

                                    stonks = self.bot.get_emoji(896752212749983774)
                                    await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}** and unlocked `Themes`! {stonks}")

                                elif lvl > initial_level:
                                    stonks = self.bot.get_emoji(896752212749983774)
                                    await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}**! {stonks}")

                        elif str(ctx.author.id) not in set:
                            if initial_level < 10 and lvl >= 10:
                                
                                stonks = self.bot.get_emoji(896752212749983774)
                                await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}** and unlocked the ability to `Kill`! {stonks}")

                            elif initial_level < 5 and lvl >= 5:

                                stonks = self.bot.get_emoji(896752212749983774)
                                await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}** and unlocked `Themes`! {stonks}")

                            elif lvl > initial_level:
                                stonks = self.bot.get_emoji(896752212749983774)
                                await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}**! {stonks}")

                    await msg.reply(f"**Correct!** You recieved **{daily} XP**")

            except asyncio.TimeoutError:
                await botmsg.add_reaction(f"{cross}")

        elif difficulty == "hard":
            id = random.randint(656, 898)

            photo = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{id}.png"
            link = f"https://pokeapi.co/api/v2/pokemon/{id}"
            response = requests.get(link)
            data = response.json()

            name = data["name"]

            embed = discord.Embed(description = f"**Guess the Pokemon**\nType the name of this Pokemon to guess",color=color, timestamp=datetime.datetime.utcnow())
            embed.set_image(url=photo)
            embed.set_author(name=f"{ctx.author}", icon_url=self.bot.user.avatar)

            botmsg = await ctx.send(embed=embed)

            cross = self.bot.get_emoji(880679527200735273)
            mark = self.bot.get_emoji(880679486205620234)

            try:
                def check(message):
                    message.content = message.content.lower()
                    return f"{name}" in message.content and ctx.author.id == message.author.id

                msg = ping = await self.bot.wait_for("message", check=check, timeout=60)
                ping = ping.content

                if f"{name}" in ping:
                    await botmsg.add_reaction(f"{mark}")
                    await msg.add_reaction(f"{mark}")

                    id = msg.author.id

                    guildid = ctx.guild.id

                    guildid = './guild data/'+ str(guildid) +'.json'
                    with open(guildid, 'r') as f:
                        users = json.load(f)

                    xp = users[str(id)]['experience']
                    initial_level = users[str(id)]['level']

                    daily = random.randint(70, 100)
                    daily = daily*5
                    xp += daily
                    users[str(id)]['experience'] = int(xp)
                    lvl = int(xp ** (1/4))
                    users[str(id)]['level'] = lvl

                    with open(guildid, 'w') as f:
                        json.dump(users, f, indent=4)

                    if lvl > initial_level:
                        with open("./local/settings.json") as s:
                            set = json.load(s)

                        if str(ctx.author.id) in set:
                            if set[f"{ctx.author.id}"]["level_ups"] == True:
                                if initial_level < 10 and lvl >= 10:
                                    
                                    stonks = self.bot.get_emoji(896752212749983774)
                                    await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}** and unlocked the ability to `Kill`! {stonks}")

                                elif initial_level < 5 and lvl >= 5:

                                    stonks = self.bot.get_emoji(896752212749983774)
                                    await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}** and unlocked `Themes`! {stonks}")

                                elif lvl > initial_level:
                                    stonks = self.bot.get_emoji(896752212749983774)
                                    await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}**! {stonks}")

                        elif str(ctx.author.id) not in set:
                            if initial_level < 10 and lvl >= 10:
                                
                                stonks = self.bot.get_emoji(896752212749983774)
                                await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}** and unlocked the ability to `Kill`! {stonks}")

                            elif initial_level < 5 and lvl >= 5:

                                stonks = self.bot.get_emoji(896752212749983774)
                                await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}** and unlocked `Themes`! {stonks}")

                            elif lvl > initial_level:
                                stonks = self.bot.get_emoji(896752212749983774)
                                await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}**! {stonks}")

                    await msg.reply(f"**Correct!** You recieved **{daily} XP**")

            except asyncio.TimeoutError:
                await botmsg.add_reaction(f"{cross}")

        else:
            embed = discord.Embed(title="Guess the Pokemon", description = f"**Description :** Sends an image of a Pokemon, try to guess it by typing its name and earns XP if your guess is correct.\n\n**Usage :** `{ctx.prefix}guess <difficulty>`\n**Difficulty :** `easy` | `medium` | `hard`",color=0x1abc9c, timestamp=datetime.datetime.utcnow())
            await ctx.send(embed=embed)

    @guess.error
    async def guess_error(self, ctx, error):

        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = error.retry_after

            embed = discord.Embed(description = f"**Command On Cooldown**\nYou're trying to use this command too many times.\n\nTry again in **{FunCog.humanize(self, str(FunCog.convert(self, remaining_time)))}**", color=color, timestamp = datetime.datetime.utcnow())
            embed.set_author(name=f"{ctx.author}", icon_url=self.bot.user.avatar)
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(FunCog(bot))