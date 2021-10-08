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

        embed = discord.Embed(color = color, timestamp=datetime.datetime.utcnow())
        embed.add_field(name = "🧙🏻‍♂️ Spell", value = f"`{get_prefix}buy spell`")
        embed.add_field(name = "🥷🏻 Jutsu", value = f"`{get_prefix}buy jutsu`")
        embed.add_field(name = "⚔️ Weapons", value = f"`{get_prefix}weapons`")
        embed.set_author(name = "Buy 🛍️", icon_url = self.bot.user.avatar_url)

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

        embed = discord.Embed(
        description = f"`{get_prefix}buy chameleon` : *Chameleon Jutsu* 😶 **Cost : 10,000 XP**\n`{get_prefix}buy transformation` : *Transformation Jutsu* 🥸 **Cost : 12,000 XP**",
        color = color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name = "Buy Jutsu 🛍️", icon_url = self.bot.user.avatar_url)

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

        embed = discord.Embed(
        description=f"`{get_prefix}buy sage` : **Sage Spell** ✨ **Cost : 50,000 XP**\n`{get_prefix}buy hunter` : **Hunter Spell** 🏹 **Cost : 20,000 XP**\n*Coming Soon* : *Wraith Spell* 👻 **Cost : 70,000 XP**",
        color = color, timestamp=datetime.datetime.utcnow())

        embed.set_author(name = "Buy Spell 🛍️", icon_url = self.bot.user.avatar_url)

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

            embed = discord.Embed(title = "You purchased the Sage Spell", description = f"`50,000 XP has been deducted`", color = color, timestamp=datetime.datetime.utcnow())
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

            embed = discord.Embed(title = "You purchased the Hunter Spell", description = f"`20,000 XP has been deducted`", color = color, timestamp=datetime.datetime.utcnow())
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
            await message.channel.send(embed = embed)
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

    @buy.command()
    async def knife(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        with open("./local/weapons.json", 'r') as f:
            weapon = json.load(f)


        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']
        color = users[str(id)]['color']
        knife = self.bot.get_emoji(881474984193703999)

        if lvl >= 10:
            if xp < 3000:
                embed = discord.Embed(title = "Insufficient Balance", description = f"*Your XP* : `{xp}`\n*Required XP* : `3,000`", color = color, timestamp=datetime.datetime.utcnow())
                embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                await message.channel.send(embed = embed)

            elif not str(id) in weapon:
                weapon[f"{id}"] = {}
                weapon[f"{id}"]["knife"] = True
                weapon[f"{id}"]["machette"] = False
                weapon[f"{id}"]["dagger"] = False
                weapon[f"{id}"]["sword"] = False
                weapon[f"{id}"]["scythe"] = False
                weapon[f"{id}"]["shuriken"] = False


                xp = users[str(id)]['experience']
                xp = xp - 3000
                users[str(id)]['experience'] = int(xp)
                lvl = int(xp ** (1/4))
                users[str(id)]['level'] = lvl

                embed = discord.Embed(title = f"Knife {knife} was successfully purchased", description = "`3,000 XP` *has been deducted*", color = color, timestamp=datetime.datetime.utcnow())
                embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                await message.channel.send(embed = embed)

                with open("./local/weapons.json", 'w') as f:
                    json.dump(weapon, f, indent=4)

                with open(guildid, 'w') as f:
                    json.dump(users, f, indent=4)

            elif str(id) in weapon:
                if weapon[str(id)]['knife'] == True:
                    embed = discord.Embed(description = f"{message.author.mention} You already own a Knife {knife}", color = color, timestamp=datetime.datetime.utcnow())
                    await message.channel.send(embed = embed)

                else:
                    weapon[str(id)]['knife'] = True
                    xp = users[str(id)]['experience']
                    xp = xp - 3000
                    users[str(id)]['experience'] = int(xp)
                    lvl = int(xp ** (1/4))
                    users[str(id)]['level'] = lvl

                    if weapon[str(id)]['machette'] == True:
                        weapon[str(id)]['machette'] = False
                        wstr = "Machette was sold for `2K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 2000
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['dagger'] == True:
                        weapon[str(id)]['dagger'] = False
                        wstr = "Dagger was sold for `2K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 2000
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['sword'] == True:
                        weapon[str(id)]['sword'] = False
                        wstr = "Sword was sold for `2.5K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 2500
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['scythe'] == True:
                        weapon[str(id)]['scythe'] = False
                        wstr = "Scythe was sold for `3K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 3000
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['shuriken'] == True:
                        weapon[str(id)]['shuriken'] = False
                        wstr = "Shuriken was sold for `5K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 5000
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl

                    embed = discord.Embed(title = f"Knife {knife} was successfully purchased", description = f"`3,000 XP` *has been deducted*\n{wstr}", color = color, timestamp=datetime.datetime.utcnow())
                    embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                    await message.channel.send(embed = embed)

                    with open("./local/weapons.json", 'w') as f:
                        json.dump(weapon, f, indent=4)

                    with open(guildid, 'w') as f:
                        json.dump(users, f, indent=4)

        else:
            embed = discord.Embed(title = "Weapons Unavailable", description = f'{message.author.mention} Level required to use this command : `10`', color = color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed = embed)

    @buy.command()
    async def machette(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        with open("./local/weapons.json", 'r') as f:
            weapon = json.load(f)


        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']
        color = users[str(id)]['color']
        machette = self.bot.get_emoji(881478895503806464)

        if lvl >= 10:
            if xp < 12000:
                embed = discord.Embed(title = "Insufficient Balance", description = f"*Your XP* : `{xp}`\n*Required XP* : `12,000`", color = color, timestamp=datetime.datetime.utcnow())
                embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                await message.channel.send(embed = embed)

            elif not str(id) in weapon:
                weapon[f"{id}"] = {}
                weapon[f"{id}"]["knife"] = False
                weapon[f"{id}"]["machette"] = True
                weapon[f"{id}"]["dagger"] = False
                weapon[f"{id}"]["sword"] = False
                weapon[f"{id}"]["scythe"] = False
                weapon[f"{id}"]["shuriken"] = False

                xp = users[str(id)]['experience']
                xp = xp - 12000
                users[str(id)]['experience'] = int(xp)
                lvl = int(xp ** (1/4))
                users[str(id)]['level'] = lvl

                embed = discord.Embed(title = f"Machette {machette} was successfully purchased", description = "`12,000 XP` *has been deducted*", color = color, timestamp=datetime.datetime.utcnow())
                embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                await message.channel.send(embed = embed)

                with open("./local/weapons.json", 'w') as f:
                    json.dump(weapon, f, indent=4)

                with open(guildid, 'w') as f:
                    json.dump(users, f, indent=4)

            elif str(id) in weapon:
                if weapon[str(id)]['machette'] == True:
                    embed = discord.Embed(description = f"{message.author.mention} You already own a Machette {machette}", color = color, timestamp=datetime.datetime.utcnow())
                    await message.channel.send(embed = embed)

                else:
                    weapon[str(id)]['machette'] = True
                    xp = users[str(id)]['experience']
                    xp = xp - 12000
                    users[str(id)]['experience'] = int(xp)
                    lvl = int(xp ** (1/4))
                    users[str(id)]['level'] = lvl

                    if weapon[str(id)]['knife'] == True:
                        weapon[str(id)]['knife'] = False
                        wstr = "Knife was sold for `500 XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 500
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['dagger'] == True:
                        weapon[str(id)]['dagger'] = False
                        wstr = "Dagger was sold for `2K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 2000
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['sword'] == True:
                        weapon[str(id)]['sword'] = False
                        wstr = "Sword was sold for `2.5K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 2500
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['scythe'] == True:
                        weapon[str(id)]['scythe'] = False
                        wstr = "Scythe was sold for `3K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 3000
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['shuriken'] == True:
                        weapon[str(id)]['shuriken'] = False
                        wstr = "Shuriken was sold for `5K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 5000
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl

                    embed = discord.Embed(title = f"Machette {machette} was successfully purchased", description = f"`12,000 XP` *has been deducted*\n{wstr}", color = color, timestamp=datetime.datetime.utcnow())
                    embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                    await message.channel.send(embed = embed)

                    with open("./local/weapons.json", 'w') as f:
                        json.dump(weapon, f, indent=4)

                    with open(guildid, 'w') as f:
                        json.dump(users, f, indent=4)

        else:
            embed = discord.Embed(title = "Weapons Unavailable", description = f'{message.author.mention} Level required to use this command : `10`', color = color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed = embed)

    @buy.command()
    async def dagger(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        with open("./local/weapons.json", 'r') as f:
            weapon = json.load(f)


        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']
        color = users[str(id)]['color']
        dagger = self.bot.get_emoji(881478895835164682)

        if lvl >= 10:
            if xp < 10000:
                embed = discord.Embed(title = "Insufficient Balance", description = f"*Your XP* : `{xp}`\n*Required XP* : `10,000`", color = color, timestamp=datetime.datetime.utcnow())
                embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                await message.channel.send(embed = embed)

            elif not str(id) in weapon:
                weapon[f"{id}"] = {}
                weapon[f"{id}"]["knife"] = False
                weapon[f"{id}"]["machette"] = False
                weapon[f"{id}"]["dagger"] = True
                weapon[f"{id}"]["sword"] = False
                weapon[f"{id}"]["scythe"] = False
                weapon[f"{id}"]["shuriken"] = False

                xp = users[str(id)]['experience']
                xp = xp - 10000
                users[str(id)]['experience'] = int(xp)
                lvl = int(xp ** (1/4))
                users[str(id)]['level'] = lvl

                embed = discord.Embed(title = f"Dagger {dagger} was successfully purchased", description = "`10,000 XP` *has been deducted*", color = color, timestamp=datetime.datetime.utcnow())
                embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                await message.channel.send(embed = embed)

                with open("./local/weapons.json", 'w') as f:
                    json.dump(weapon, f, indent=4)

                with open(guildid, 'w') as f:
                    json.dump(users, f, indent=4)

            elif str(id) in weapon:
                if weapon[str(id)]['dagger'] == True:
                    embed = discord.Embed(description = f"{message.author.mention} You already own a Dagger {dagger}", color = color, timestamp=datetime.datetime.utcnow())
                    await message.channel.send(embed = embed)

                else:
                    weapon[str(id)]['dagger'] = True
                    xp = users[str(id)]['experience']
                    xp = xp - 10000
                    users[str(id)]['experience'] = int(xp)
                    lvl = int(xp ** (1/4))
                    users[str(id)]['level'] = lvl

                    if weapon[str(id)]['knife'] == True:
                        weapon[str(id)]['knife'] = False
                        wstr = "Knife was sold for `500 XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 500
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['machette'] == True:
                        weapon[str(id)]['machette'] = False
                        wstr = "Machette was sold for `2K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 2000
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['sword'] == True:
                        weapon[str(id)]['sword'] = False
                        wstr = "Sword was sold for `2.5K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 2500
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['scythe'] == True:
                        weapon[str(id)]['scythe'] = False
                        wstr = "Scythe was sold for `3K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 3000
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['shuriken'] == True:
                        weapon[str(id)]['shuriken'] = False
                        wstr = "Shuriken was sold for `5K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 5000
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl

                    embed = discord.Embed(title = f"Dagger {dagger} was successfully purchased", description = f"`10,000 XP` *has been deducted*\n{wstr}", color = color, timestamp=datetime.datetime.utcnow())
                    embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                    await message.channel.send(embed = embed)

                    with open("./local/weapons.json", 'w') as f:
                        json.dump(weapon, f, indent=4)

                    with open(guildid, 'w') as f:
                        json.dump(users, f, indent=4)

        else:
            embed = discord.Embed(title = "Weapons Unavailable", description = f'{message.author.mention} Level required to use this command : `10`', color = color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed = embed)

    @buy.command()
    async def sword(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        with open("./local/weapons.json", 'r') as f:
            weapon = json.load(f)


        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']
        color = users[str(id)]['color']
        sword = self.bot.get_emoji(881478895247949887)

        if lvl >= 10:
            if xp < 15000:
                embed = discord.Embed(title = "Insufficient Balance", description = f"*Your XP* : `{xp}`\n*Required XP* : `15,000`", color = color, timestamp=datetime.datetime.utcnow())
                embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                await message.channel.send(embed = embed)

            elif not str(id) in weapon:
                weapon[f"{id}"] = {}
                weapon[f"{id}"]["knife"] = False
                weapon[f"{id}"]["machette"] = False
                weapon[f"{id}"]["dagger"] = False
                weapon[f"{id}"]["sword"] = True
                weapon[f"{id}"]["scythe"] = False
                weapon[f"{id}"]["shuriken"] = False

                xp = users[str(id)]['experience']
                xp = xp - 15000
                users[str(id)]['experience'] = int(xp)
                lvl = int(xp ** (1/4))
                users[str(id)]['level'] = lvl

                embed = discord.Embed(title = f"Sword {sword} was successfully purchased", description = "`15,000 XP` *has been deducted*", color = color, timestamp=datetime.datetime.utcnow())
                embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                await message.channel.send(embed = embed)

                with open("./local/weapons.json", 'w') as f:
                    json.dump(weapon, f, indent=4)

                with open(guildid, 'w') as f:
                    json.dump(users, f, indent=4)

            elif str(id) in weapon:
                if weapon[str(id)]['sword'] == True:
                    embed = discord.Embed(description = f"{message.author.mention} You already own a Sword {sword}", color = color, timestamp=datetime.datetime.utcnow())
                    await message.channel.send(embed = embed)

                else:
                    weapon[str(id)]['sword'] = True
                    xp = users[str(id)]['experience']
                    xp = xp - 15000
                    users[str(id)]['experience'] = int(xp)
                    lvl = int(xp ** (1/4))
                    users[str(id)]['level'] = lvl

                    if weapon[str(id)]['knife'] == True:
                        weapon[str(id)]['knife'] = False
                        wstr = "Knife was sold for `500 XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 500
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['machette'] == True:
                        weapon[str(id)]['machette'] = False
                        wstr = "Machette was sold for `2K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 2000
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['dagger'] == True:
                        weapon[str(id)]['dagger'] = False
                        wstr = "Dagger was sold for `2K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 2000
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['scythe'] == True:
                        weapon[str(id)]['scythe'] = False
                        wstr = "Scythe was sold for `3K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 3000
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['shuriken'] == True:
                        weapon[str(id)]['shuriken'] = False
                        wstr = "Shuriken was sold for `5K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 5000
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl

                    embed = discord.Embed(title = f"Sword {sword} was successfully purchased", description = f"`15,000 XP` *has been deducted*\n{wstr}", color = color, timestamp=datetime.datetime.utcnow())
                    embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                    await message.channel.send(embed = embed)

                    with open("./local/weapons.json", 'w') as f:
                        json.dump(weapon, f, indent=4)

                    with open(guildid, 'w') as f:
                        json.dump(users, f, indent=4)

        else:
            embed = discord.Embed(title = "Weapons Unavailable", description = f'{message.author.mention} Level required to use this command : `10`', color = color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed = embed)

    @buy.command()
    async def scythe(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        with open("./local/weapons.json", 'r') as f:
            weapon = json.load(f)


        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']
        color = users[str(id)]['color']
        scythe = self.bot.get_emoji(881478895604494376)

        if lvl >= 10:
            if xp < 17000:
                embed = discord.Embed(title = "Insufficient Balance", description = f"*Your XP* : `{xp}`\n*Required XP* : `17,000`", color = color, timestamp=datetime.datetime.utcnow())
                embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                await message.channel.send(embed = embed)

            elif not str(id) in weapon:
                weapon[f"{id}"] = {}
                weapon[f"{id}"]["knife"] = False
                weapon[f"{id}"]["machette"] = False
                weapon[f"{id}"]["dagger"] = False
                weapon[f"{id}"]["sword"] = False
                weapon[f"{id}"]["scythe"] = True
                weapon[f"{id}"]["shuriken"] = False

                xp = users[str(id)]['experience']
                xp = xp - 17000
                users[str(id)]['experience'] = int(xp)
                lvl = int(xp ** (1/4))
                users[str(id)]['level'] = lvl

                embed = discord.Embed(title = f"Scythe {scythe} was successfully purchased", description = "`17,000 XP` *has been deducted*", color = color, timestamp=datetime.datetime.utcnow())
                embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                await message.channel.send(embed = embed)

                with open("./local/weapons.json", 'w') as f:
                    json.dump(weapon, f, indent=4)

                with open(guildid, 'w') as f:
                    json.dump(users, f, indent=4)

            elif str(id) in weapon:
                if weapon[str(id)]['scythe'] == True:
                    embed = discord.Embed(description = f"{message.author.mention} You already own a Scythe {scythe}", color = color, timestamp=datetime.datetime.utcnow())
                    await message.channel.send(embed = embed)

                else:
                    weapon[str(id)]['scythe'] = True
                    xp = users[str(id)]['experience']
                    xp = xp - 17000
                    users[str(id)]['experience'] = int(xp)
                    lvl = int(xp ** (1/4))
                    users[str(id)]['level'] = lvl

                    if weapon[str(id)]['knife'] == True:
                        weapon[str(id)]['knife'] = False
                        wstr = "Knife was sold for `500 XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 500
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['machette'] == True:
                        weapon[str(id)]['machette'] = False
                        wstr = "Machette was sold for `2K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 2000
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['dagger'] == True:
                        weapon[str(id)]['dagger'] = False
                        wstr = "Dagger was sold for `2K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 2000
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['sword'] == True:
                        weapon[str(id)]['sword'] = False
                        wstr = "Sword was sold for `2.5K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 2500
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['shuriken'] == True:
                        weapon[str(id)]['shuriken'] = False
                        wstr = "Shuriken was sold for `5K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 5000
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl

                    embed = discord.Embed(title = f"Scythe {scythe} was successfully purchased", description = f"`17,000 XP` *has been deducted*\n{wstr}", color = color, timestamp=datetime.datetime.utcnow())
                    embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                    await message.channel.send(embed = embed)

                    with open("./local/weapons.json", 'w') as f:
                        json.dump(weapon, f, indent=4)

                    with open(guildid, 'w') as f:
                        json.dump(users, f, indent=4)

        else:
            embed = discord.Embed(title = "Weapons Unavailable", description = f'{message.author.mention} Level required to use this command : `10`', color = color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed = embed)

    @buy.command()
    async def shuriken(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        with open("./local/weapons.json", 'r') as f:
            weapon = json.load(f)


        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']
        color = users[str(id)]['color']
        shuriken = self.bot.get_emoji(881478895889690674)

        if lvl >= 10:
            if xp < 23000:
                embed = discord.Embed(title = "Insufficient Balance", description = f"*Your XP* : `{xp}`\n*Required XP* : `23,000`", color = color, timestamp=datetime.datetime.utcnow())
                embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                await message.channel.send(embed = embed)

            elif not str(id) in weapon:
                weapon[f"{id}"] = {}
                weapon[f"{id}"]["knife"] = False
                weapon[f"{id}"]["machette"] = False
                weapon[f"{id}"]["dagger"] = False
                weapon[f"{id}"]["sword"] = False
                weapon[f"{id}"]["scythe"] = False
                weapon[f"{id}"]["shuriken"] = True

                xp = users[str(id)]['experience']
                xp = xp - 23000
                users[str(id)]['experience'] = int(xp)
                lvl = int(xp ** (1/4))
                users[str(id)]['level'] = lvl

                embed = discord.Embed(title = f"Shuriken {shuriken} was successfully purchased", description = "`23,000 XP` *has been deducted*", color = color, timestamp=datetime.datetime.utcnow())
                embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                await message.channel.send(embed = embed)

                with open("./local/weapons.json", 'w') as f:
                    json.dump(weapon, f, indent=4)

                with open(guildid, 'w') as f:
                    json.dump(users, f, indent=4)

            elif str(id) in weapon:
                if weapon[str(id)]['shuriken'] == True:
                    embed = discord.Embed(description = f"{message.author.mention} You already own a Shuriken {shuriken}", color = color, timestamp=datetime.datetime.utcnow())
                    await message.channel.send(embed = embed)

                else:
                    weapon[str(id)]['shuriken'] = True
                    xp = users[str(id)]['experience']
                    xp = xp - 23000
                    users[str(id)]['experience'] = int(xp)
                    lvl = int(xp ** (1/4))
                    users[str(id)]['level'] = lvl

                    if weapon[str(id)]['knife'] == True:
                        weapon[str(id)]['knife'] = False
                        wstr = "Knife was sold for `500 XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 500
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['machette'] == True:
                        weapon[str(id)]['machette'] = False
                        wstr = "Machette was sold for `2K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 2000
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['dagger'] == True:
                        weapon[str(id)]['dagger'] = False
                        wstr = "Dagger was sold for `2K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 2000
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['sword'] == True:
                        weapon[str(id)]['sword'] = False
                        wstr = "Sword was sold for `2.5K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 2500
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl


                    if weapon[str(id)]['scythe'] == True:
                        weapon[str(id)]['scythe'] = False
                        wstr = "Scythe was sold for `3K XP`"
                        xp = users[str(id)]['experience']
                        xp = xp + 3000
                        users[str(id)]['experience'] = int(xp)
                        lvl = int(xp ** (1/4))
                        users[str(id)]['level'] = lvl

                    embed = discord.Embed(title = f"Shuriken {shuriken} was successfully purchased", description = f"`23,000 XP` *has been deducted*\n{wstr}", color = color, timestamp=datetime.datetime.utcnow())
                    embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                    await message.channel.send(embed = embed)

                    with open("./local/weapons.json", 'w') as f:
                        json.dump(weapon, f, indent=4)

                    with open(guildid, 'w') as f:
                        json.dump(users, f, indent=4)

        else:
            embed = discord.Embed(title = "Weapons Unavailable", description = f'{message.author.mention} Level required to use this command : `10`', color = color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed = embed)

    @commands.group(invoke_without_command=True)
    async def sell(self, message):
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

        embed = discord.Embed(description="Coming in Patch 1.0 🔜", color = color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name = "Sell 🪙", icon_url = self.bot.user.avatar_url)

        await message.channel.send(embed = embed)


def setup(bot):
    bot.add_cog(BuyCog(bot))