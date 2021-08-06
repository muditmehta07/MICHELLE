'''

Shop

'''

import discord
from discord.ext import commands
import os
import datetime
import json

from discord.ext.commands.context import Context

class BuyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.group(invoke_without_command=True)
    async def buy(self, message):
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

        embed = discord.Embed(title = "Buy 🛍️", color = color, timestamp=datetime.datetime.utcnow())
        embed.add_field(name = "Spell 🧙🏻‍♂️", value = f"`{get_prefix}buy spell`")
        embed.add_field(name = "Jutsu 🥷🏻", value = f"`{get_prefix}buy jutsu`")
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)

        await message.channel.send(embed = embed)

    @buy.command()
    async def jutsu(self, message):
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

        embed = discord.Embed(title = "Buy Jutsu 🛍️", 
        description = f"`{get_prefix}buy chameleon` : *Chameleon Jutsu* 😶 **Cost : 10,000 XP**\n`{get_prefix}buy transformation` : *Transformation Jutsu* 🥸 **Cost : 12,000 XP**",
        color = color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)

        await message.channel.send(embed = embed)

    @buy.command()
    async def spell(self, message):
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

        embed = discord.Embed(title = "Buy Spell 🛍️",
        description=f"`{get_prefix}buy sage` : *Sage Spell* ✨ **Cost : 50,000 XP**\n`{get_prefix}buy hunter` : *Hunter Spell* 🏹 **Cost : 20,000 XP**\n*coming soon* : *Wraith Spell* 👻 **Cost : 70,000 X**",
        color = color, timestamp=datetime.datetime.utcnow())

        embed.set_author(name = message.author, icon_url = message.author.avatar_url)

        await message.channel.send(embed = embed)

    '''
    @buy.command()
    async def ability(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        embed = discord.Embed(title = "Buy Ability", color = color)
        embed.add_field(name = "??", value = "`=buy ??`")

        await message.channel.send(content = f'{message.author.mention}', embed = embed)
    '''

    '''

    Buy Spells Commands

    '''

    @buy.command()
    async def sage(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']
        color = users[str(id)]['color']

        if users[str(id)]['sage_spell'] == True:
            embed = discord.Embed(title = "Item already purchased", description = "`Sage Spell is Active`", color = color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed = embed)

        elif xp<50000:
            embed = discord.Embed(title = "Purchase Failed : Insufficient Balance", description = f"`Your XP : {xp}`\n\n`Required XP : 50,000`", color = color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed = embed)
        else:
            users[str(id)]['sage_spell'] = True
            xp = users[str(id)]['experience']
            xp = xp - 50000
            users[str(id)]['experience'] = int(xp)
            lvl = int(xp ** (1/4))
            users[str(id)]['level'] = lvl

            if users[str(id)]['wraith_spell'] == True:
                users[str(id)]['wraith_spell'] = False
                s = "Wraith Spell wore off\n"
            elif users[str(id)]['hunter_spell'] == True:
                users[str(id)]['hunter_spell'] = False
                s = "Hunter Spell wore off\n"
            else:
                s = "-"

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            embed = discord.Embed(title = "You purchased the Sage Spell", description = f"{s}`50,000 XP has been deducted`", color = color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed = embed)

    @buy.command()
    async def hunter(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']
        color = users[str(id)]['color']

        if users[str(id)]['hunter_spell'] == True:
            embed = discord.Embed(title = "Item already purchased", description = "`Hunter Spell is Active`", color = color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed = embed)

        elif xp<20000:
            embed = discord.Embed(title = "Purchase Failed : Insufficient Balance", description = f"`Your XP : {xp}`\n\n`Required XP : 20,000`", color = color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed = embed)
        else:
            users[str(id)]['hunter_spell'] = True
            xp = users[str(id)]['experience']
            xp = xp - 20000
            users[str(id)]['experience'] = int(xp)
            lvl = int(xp ** (1/4))
            users[str(id)]['level'] = lvl

            if users[str(id)]['sage_spell'] == True:
                users[str(id)]['sage_spell'] = False
                s = "Sage Spell wore off\n"
            elif users[str(id)]['wraith_spell'] == True:
                users[str(id)]['wraith_spell'] = False
                s = "Wraith Spell wore off\n"
            else:
                s = "-"

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            embed = discord.Embed(title = "You purchased the Hunter Spell", description = f"{s}`20,000 XP has been deducted`", color = color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed = embed)

    '''
    @buy.command()
    async def wraith(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']
        color = users[str(id)]['color']

        if users[str(id)]['wraith_spell'] == True:
            embed = discord.Embed(title = "Item already purchased", description = "`Wraith Spell is Active`", color = color)
            await message.channel.send(content = f'{message.author.mention}', embed = embed)

        elif xp<20000:
            embed = discord.Embed(title = "Purchase Failed : Insufficient Balance", description = f"`Your XP : {xp}`\n\n`Required XP : 70,000`", color = color)
            await message.channel.send(content = f'{message.author.mention}', embed = embed)
        else:
            users[str(id)]['wraith_spell'] = True
            xp = users[str(id)]['experience']
            xp = xp - 70000
            users[str(id)]['experience'] = int(xp)
            lvl = int(xp ** (1/4))
            users[str(id)]['level'] = lvl

            if users[str(id)]['sage_spell'] == True:
                users[str(id)]['sage_spell'] = False
                s = "Sage Spell wore off\n"
            elif users[str(id)]['hunter_spell'] == True:
                users[str(id)]['hunter_spell'] = False
                s = "Hunter Spell wore off\n"
            else:
                s = "-"

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            embed = discord.Embed(title = "You purchased the Wraith Spell", description = f"{s}`70,000 XP has been deducted`", color = color)
            await message.channel.send(content = f'{message.author.mention}', embed = embed)

    '''

    @buy.command()
    async def chameleon(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']
        color = users[str(id)]['color']

        if users[str(id)]['chameleon'] == True:
            embed = discord.Embed(title = "Jutsu Already Trained", description = "*You can't re-train a Jutsu*", color = color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed = embed)

        elif xp<10000:
            embed = discord.Embed(title = "Insufficient Balance", description = f"*Your XP* : `{xp}`\n\n*Required XP* : `10,000`", color = color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed = embed)
        else:
            users[str(id)]['chameleon'] = True
            xp = users[str(id)]['experience']
            xp = xp - 10000
            users[str(id)]['experience'] = int(xp)
            lvl = int(xp ** (1/4))
            users[str(id)]['level'] = lvl

            if users[str(id)]['transformation'] == True:
                users[str(id)]['transformation'] = False
                embed = discord.Embed(title = "Chameleon Jutsu Trained", description = "*You forgot Transformation Jutsu*\n`10,000 XP` *has been deducted*", color = color, timestamp=datetime.datetime.utcnow())
                embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                await message.channel.send(embed = embed)
            else:
                embed = discord.Embed(title = "Chameleon Jutsu Trained", description = "`10,000 XP` *has been deducted*", color = color, timestamp=datetime.datetime.utcnow())
                embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                await message.channel.send(embed = embed)
            
            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)



    @buy.command()
    async def transformation(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']
        color = users[str(id)]['color']

        if users[str(id)]['transformation'] == True:
            embed = discord.Embed(title = "Jutsu Already Trained", description = "*You can't re-train a Jutsu*", color = color, timestamp=datetime.datetime.utcnow())
            await message.channel.send(content = f'{message.author.mention}', embed = embed)
        elif xp<12000:
            embed = discord.Embed(title = "Insufficient Balance", description = f"*Your XP* : `{xp}`\n*Required XP* : `12,000`", color = color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed = embed)
        else:
            users[str(id)]['transformation'] = True
            xp = users[str(id)]['experience']
            xp = xp - 12000
            users[str(id)]['experience'] = int(xp)
            lvl = int(xp ** (1/4))
            users[str(id)]['level'] = lvl

            if users[str(id)]['chameleon'] == True:
                users[str(id)]['chameleon'] = False
                embed = discord.Embed(title = "Transformation Jutsu Trained", description = "*You forgot Chameleon Jutsu*\n`12,000 XP` *has been deducted*", color = color, timestamp=datetime.datetime.utcnow())
                embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                await message.channel.send(embed = embed)
            else:
                embed = discord.Embed(title = "Transformation Jutsu Trained", description = "`12,000 XP` *has been deducted*", color = color, timestamp=datetime.datetime.utcnow())
                embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                await message.channel.send(embed = embed)

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)


def setup(bot):
    bot.add_cog(BuyCog(bot))
