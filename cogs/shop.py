import discord
from discord.ext import commands
import os
import datetime
import json
import asyncio

from discord.ext.commands.context import Context


class BuyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def convert(self, n):
        avg = str(datetime.timedelta(seconds=n))
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
    async def shopupdater(self, message):
        if message.author.id == 488996680058798081:
            await message.channel.send("**Shop updater has been initiated!**")

            while True:

                # Spell Update

                with open("./local/shop.json", "r") as f:
                    file = json.load(f)

                spellTime = file["spellTime"]

                while spellTime > 0:
                    spellTime -= 1
                    file["spellTime"] = spellTime

                    with open("./local/shop.json", "w") as f:
                        json.dump(file, f)

                    await asyncio.sleep(1)

                spell = file["spell"]

                if spell == "sage":
                    file["spell"] = "hunter"

                else:
                    file["spell"] = "sage"

                with open("./local/shop.json", "w") as f:
                    json.dump(file, f)

                # Jutsu Update

                with open("./local/shop.json", "r") as f:
                    file = json.load(f)

                jutsuTime = file["jutsuTime"]

                while jutsuTime > 0:
                    jutsuTime -= 1
                    file["jutsuTime"] = jutsuTime

                    with open("./local/shop.json", "w") as f:
                        json.dump(file, f)

                    await asyncio.sleep(1)

                jutsu = file["jutsu"]

                if jutsu == "transformation":
                    file["jutsu"] = "chameleon"

                else:
                    file["jutsu"] = "transformation"

                with open("./local/shop.json", "w") as f:
                    json.dump(file, f)

                # Weapon Update

                with open("./local/shop.json", "r") as f:
                    file = json.load(f)

                weaponTime = file["weaponTime"]

                while weaponTime > 0:
                    weaponTime -= 1
                    file["weaponTime"] = weaponTime

                    with open("./local/shop.json", "w") as f:
                        json.dump(file, f)

                    await asyncio.sleep(1)

                weapon = file["weapon"]

                if weapon == "knife":
                    file["weapon"] = "machette"

                elif weapon == "machette":
                    file["weapon"] = "dagger"

                elif weapon == "dagger":
                    file["weapon"] = "sword"

                elif weapon == "sword":
                    file["weapon"] = "scythe"

                elif weapon == "scythe":
                    file["weapon"] = "shuriken"

                file["spellTime"] = 151200
                file["jutsuTime"] = 151200
                file["weaponTime"] = 151200

                with open("./local/shop.json", "w") as f:
                    json.dump(file, f)

    @commands.group(invoke_without_command=True)
    async def buy(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
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
        chest = self.bot.get_emoji(955783898577661973)
        sage_emoji = self.bot.get_emoji(958255752156430336)
        hunter_emoji = self.bot.get_emoji(958255782112153600)

        replyEmoji = self.bot.get_emoji(929383454469128263)
        branchEmoji = self.bot.get_emoji(942824887666491426)

        with open("./local/shop.json", "r") as f:
            shopDict = json.load(f)

        spell, jutsu, weapon = shopDict["spell"], shopDict["jutsu"], shopDict["weapon"]

        spellTime = shopDict["spellTime"]
        jutsuTime = shopDict["jutsuTime"] + spellTime
        weaponTime = shopDict["weaponTime"] + jutsuTime

        spellTimeText = BuyCog.humanize(
            self, str(BuyCog.convert(self, spellTime)))
        jutsuTimeText = BuyCog.humanize(
            self, str(BuyCog.convert(self, jutsuTime)))
        weaponTimeText = BuyCog.humanize(
            self, str(BuyCog.convert(self, weaponTime)))

        if spell == "sage":
            if str(BuyCog.convert(self, spellTime)) != "0:00:00":
                spellString = f"{sage_emoji} **Sage Spell** — [50,000 XP](https://www.youtube.com/watch?v=1aRwM_QsqQI)\n{branchEmoji} **Available For :** {spellTimeText}\n{replyEmoji} **Help :** `{get_prefix}help sage spell`\n\n"

            else:
                spellString = f"{sage_emoji} **Sage Spell** — [50,000 XP](https://www.youtube.com/watch?v=1aRwM_QsqQI)\n{replyEmoji} **Help :** `{get_prefix}help sage spell`\n\n"

        elif spell == "hunter":
            if str(BuyCog.convert(self, spellTime)) != "0:00:00":
                spellString = f"{hunter_emoji} **Hunter Spell** — [20,000 XP](https://www.youtube.com/watch?v=OZ76UP-c8Ao)\n{branchEmoji} **Available For :** {spellTimeText}\n{replyEmoji} **Help :** `{get_prefix}help hunter spell`\n\n"

            else:
                spellString = f"{hunter_emoji} **Hunter Spell** — [20,000 XP](https://www.youtube.com/watch?v=OZ76UP-c8Ao)\n{replyEmoji} **Help :** `{get_prefix}help hunter spell`\n\n"

        if jutsu == "transformation":
            if str(BuyCog.convert(self, jutsuTime)) != "0:00:00":
                jutsuString = f":disguised_face: **Transformation Jutsu** — [12,000 XP](https://www.youtube.com/watch?v=T8sJXkb1OOc)\n{branchEmoji} **Available For :** {jutsuTimeText}\n{replyEmoji} **Help :** `{get_prefix}help transformation jutsu`\n\n"

            else:
                jutsuString = f":disguised_face: **Transformation Jutsu** — [12,000 XP](https://www.youtube.com/watch?v=T8sJXkb1OOc)\n{replyEmoji} **Help :** `{get_prefix}help transformation jutsu`\n\n"

        elif jutsu == "chameleon":
            if str(BuyCog.convert(self, jutsuTime)) != "0:00:00":
                jutsuString = f":face_in_clouds: **Chameleon Jutsu** — [10,000 XP](https://www.youtube.com/watch?v=v1-DI2yK8Wo)\n{branchEmoji} **Available For :** {jutsuTimeText}\n{replyEmoji} **Help :** `{get_prefix}help chameleon jutsu`\n\n"

            else:
                jutsuString = f":face_in_clouds: **Chameleon Jutsu** — [10,000 XP](https://www.youtube.com/watch?v=v1-DI2yK8Wo)\n{replyEmoji} **Help :** `{get_prefix}help chameleon jutsu`\n\n"

        if weapon == "knife":
            if str(BuyCog.convert(self, weaponTime)) != "0:00:00":
                weaponString = f"{knife} **Knife** — [3,000 XP](https://www.youtube.com/watch?v=K8M4KGedve8)\n{branchEmoji} **Available For :** {weaponTimeText}\n{replyEmoji} **Help :** `{get_prefix}help knife`\n\n"

            else:
                weaponString = f"{knife} **Knife** — [3,000 XP](https://www.youtube.com/watch?v=K8M4KGedve8)\n{replyEmoji} **Help :** `{get_prefix}help knife`\n\n"

        elif weapon == "machette":
            if str(BuyCog.convert(self, weaponTime)) != "0:00:00":
                weaponString = f"{machette} **Machette** — [12,000 XP](https://www.youtube.com/watch?v=DwbG64YC-vQ)\n{branchEmoji} **Available For :** {weaponTimeText}\n{replyEmoji} **Help :** `{get_prefix}help machette`\n\n"

            else:
                weaponString = f"{machette} **Machette** — [12,000 XP](https://www.youtube.com/watch?v=DwbG64YC-vQ)\n{replyEmoji} **Help :** `{get_prefix}help machette`\n\n"

        elif weapon == "dagger":
            if str(BuyCog.convert(self, weaponTime)) != "0:00:00":
                weaponString = f"{dagger} **Dagger** — [10,000 XP](https://www.youtube.com/watch?v=6y5trAiXdAQ)\n{branchEmoji} **Available For :** {weaponTimeText}\n{replyEmoji} **Help :** `{get_prefix}help dagger`\n\n"

            else:
                weaponString = f"{dagger} **Dagger** — [10,000 XP](https://www.youtube.com/watch?v=6y5trAiXdAQ)\n{replyEmoji} **Help :** `{get_prefix}help dagger`\n\n"

        elif weapon == "sword":
            if str(BuyCog.convert(self, weaponTime)) != "0:00:00":
                weaponString = f"{sword} **Sword** — [15,000 XP](https://www.youtube.com/watch?v=6ohYYtxfDCg)\n{branchEmoji} **Available For :** {weaponTimeText}\n{replyEmoji} **Help :** `{get_prefix}help sword`\n\n"

            else:
                weaponString = f"{sword} **Sword** — [15,000 XP](https://www.youtube.com/watch?v=6ohYYtxfDCg)\n{replyEmoji} **Help :** `{get_prefix}help sword`\n\n"

        elif weapon == "scythe":
            if str(BuyCog.convert(self, weaponTime)) != "0:00:00":
                weaponString = f"{scythe} **Scythe** — [17,000 XP](https://www.youtube.com/watch?v=OMrI9KhkSPg)\n{branchEmoji} **Available For :** {weaponTimeText}\n{replyEmoji} **Help :** `{get_prefix}help scythe`\n\n"

            else:
                weaponString = f"{scythe} **Scythe** — [17,000 XP](https://www.youtube.com/watch?v=OMrI9KhkSPg)\n{replyEmoji} **Help :** `{get_prefix}help scythe`\n\n"

        elif weapon == "shuriken":
            if str(BuyCog.convert(self, weaponTime)) != "0:00:00":
                weaponString = f"{shuriken} **Shuriken** — [23,000 XP](https://www.youtube.com/watch?v=ktLR-WjB_C8)\n{branchEmoji} **Available For :** {weaponTimeText}\n{replyEmoji} **Help :** `{get_prefix}help shuriken`\n\n"

            else:
                weaponString = f"{shuriken} **Shuriken** — [23,000 XP](https://www.youtube.com/watch?v=ktLR-WjB_C8)\n{replyEmoji} **Help :** `{get_prefix}help shuriken`\n\n"

        chestString = f"{chest} **Chest** — [12,000 XP](https://www.youtube.com/shorts/37nHCjyGhUY)\n{replyEmoji} **Help :** `{get_prefix}help chest`"

        embed = discord.Embed(
            description=f"{spellString} {jutsuString} {weaponString} {chestString}",
            color=color,
            timestamp=datetime.datetime.utcnow()
        )

        embed.set_author(name="Buy", icon_url=self.bot.user.avatar)
        embed.set_footer(text=f"use {get_prefix}help <item> for more info")

        await message.channel.send(embed=embed)

    @buy.command()
    async def sage(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']
        color = users[str(id)]['color']

        with open("./local/shop.json", "r") as f:
            shopDict = json.load(f)

        if shopDict["spell"] != "sage":
            await message.channel.send("**`Sage Spell` is not available in the shop at the moment**")

        elif users[str(id)]['sage_spell'] == True:
            await message.channel.send("**You already own a Sage Spell**")

        elif xp < 50000:
            await message.channel.send("**Insufficient Balance. You do not have** `50,000` **XP**")

        else:
            users[str(id)]['sage_spell'] = True
            xp = users[str(id)]['experience']
            xp = xp - 50000
            users[str(id)]['experience'] = int(xp)
            lvl = int(xp ** (1/4))
            users[str(id)]['level'] = lvl

            if users[str(id)]['wraith_spell'] == True:
                users[str(id)]['wraith_spell'] = False
                s = "Wraith Spell wore off"

            elif users[str(id)]['hunter_spell'] == True:
                users[str(id)]['hunter_spell'] = False
                s = "Hunter Spell wore off"
            else:
                s = "-"

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            await message.channel.send(f"**Sage Spell was purchased. [50,000 XP Deducted] [{s}]**")

    @buy.command()
    async def hunter(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']
        color = users[str(id)]['color']

        with open("./local/shop.json", "r") as f:
            shopDict = json.load(f)

        if shopDict["spell"] != "hunter":
            await message.channel.send("**`Hunter Spell` is not available in the shop at the moment**")

        elif users[str(id)]['hunter_spell'] == True:
            await message.channel.send("**You already own a Hunter Spell**")

        elif xp < 20000:
            await message.channel.send("**Insufficient Balance. You do not have** `20,000` **XP**")

        else:
            users[str(id)]['hunter_spell'] = True
            xp = users[str(id)]['experience']
            xp = xp - 20000
            users[str(id)]['experience'] = int(xp)
            lvl = int(xp ** (1/4))
            users[str(id)]['level'] = lvl

            if users[str(id)]['sage_spell'] == True:
                users[str(id)]['sage_spell'] = False
                s = "Sage Spell wore off"

            elif users[str(id)]['wraith_spell'] == True:
                users[str(id)]['wraith_spell'] = False
                s = "Wraith Spell wore off"
            else:
                s = "-"

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            await message.channel.send(f"**Hunter Spell was purchased. [20,000 XP Deducted] [{s}]**")

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
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']
        color = users[str(id)]['color']

        with open("./local/shop.json", "r") as f:
            shopDict = json.load(f)

        if shopDict["jutsu"] != "chameleon":
            await message.channel.send("**`Chameleon Jutsu` is not available in the shop at the moment**")

        elif users[str(id)]['chameleon'] == True:
            await message.channel.send("**You already trained the Chameleon Jutsu**")

        elif xp < 10000:
            await message.channel.send("**Insufficient Balance. You do not have** `10,000` **XP**")

        else:
            users[str(id)]['chameleon'] = True
            xp = users[str(id)]['experience']
            xp = xp - 10000
            users[str(id)]['experience'] = int(xp)
            lvl = int(xp ** (1/4))
            users[str(id)]['level'] = lvl

            if users[str(id)]['transformation'] == True:
                users[str(id)]['transformation'] = False
                await message.channel.send("**Chameleon Jutsu was trained. [10,000 XP Deducted] [You forgot Transformation Jutsu]**")

            else:
                await message.channel.send("**Chameleon Jutsu was trained. [10,000 XP Deducted]**")

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

    @buy.command()
    async def transformation(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']
        color = users[str(id)]['color']

        with open("./local/shop.json", "r") as f:
            shopDict = json.load(f)

        if shopDict["jutsu"] != "transformation":
            await message.channel.send("**`Transformation Jutsu` is not available in the shop at the moment**")

        elif users[str(id)]['transformation'] == True:
            await message.channel.send("**You already trained the Transformation Jutsu**")

        elif xp < 12000:
            await message.channel.send("**Insufficient Balance. You do not have** `12,000` **XP**")

        else:
            users[str(id)]['transformation'] = True
            xp = users[str(id)]['experience']
            xp = xp - 12000
            users[str(id)]['experience'] = int(xp)
            lvl = int(xp ** (1/4))
            users[str(id)]['level'] = lvl

            if users[str(id)]['chameleon'] == True:
                users[str(id)]['chameleon'] = False
                await message.channel.send("**Transformation Jutsu was trained. [12,000 XP Deducted] [You forgot Chameleon Jutsu]**")

            else:
                await message.channel.send("**Transformation Jutsu was trained. [12,000 XP Deducted]**")

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

    @buy.command()
    async def knife(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        with open("./local/weapons.json", 'r') as f:
            weapon = json.load(f)

        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']
        color = users[str(id)]['color']
        knife = self.bot.get_emoji(881474984193703999)

        if lvl >= 10:
            with open("./local/shop.json", "r") as f:
                shopDict = json.load(f)

            if shopDict["weapon"] != "knife":
                await message.channel.send("**`Knife` is not available in the shop at the moment**")

            elif xp < 3000:
                await message.channel.send("**Insufficient Balance. You do not have** `3,000` **XP**")

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

                await message.channel.send("**Knife was successfully purchased. [3,000 XP Deducted]**")

                with open("./local/weapons.json", 'w') as f:
                    json.dump(weapon, f, indent=4)

                with open(guildid, 'w') as f:
                    json.dump(users, f, indent=4)

            elif str(id) in weapon:
                if weapon[str(id)]['knife'] == True:
                    await message.channel.send("**You already own a Knife**")

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

                    await message.channel.send("**Knife was successfully purchased. [3,000 XP Deducted]**")

                    with open("./local/weapons.json", 'w') as f:
                        json.dump(weapon, f, indent=4)

                    with open(guildid, 'w') as f:
                        json.dump(users, f, indent=4)

        else:
            await message.channel.send("**Weapons are :lock: locked. [Level Required - 10]**")

    @buy.command()
    async def machette(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        with open("./local/weapons.json", 'r') as f:
            weapon = json.load(f)

        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']
        color = users[str(id)]['color']
        machette = self.bot.get_emoji(881478895503806464)

        if lvl >= 10:
            with open("./local/shop.json", "r") as f:
                shopDict = json.load(f)

            if shopDict["weapon"] != "machette":
                await message.channel.send("**`Machette` is not available in the shop at the moment**")

            elif xp < 12000:
                await message.channel.send("**Insufficient Balance. You do not have** `12,000` **XP**")

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

                await message.channel.send("**Machette was successfully purchased. [12,000 XP Deducted]**")

                with open("./local/weapons.json", 'w') as f:
                    json.dump(weapon, f, indent=4)

                with open(guildid, 'w') as f:
                    json.dump(users, f, indent=4)

            elif str(id) in weapon:
                if weapon[str(id)]['machette'] == True:
                    await message.channel.send("**You already own a Machette**")

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

                    await message.channel.send("**Machette was successfully purchased. [12,000 XP Deducted]**")

                    with open("./local/weapons.json", 'w') as f:
                        json.dump(weapon, f, indent=4)

                    with open(guildid, 'w') as f:
                        json.dump(users, f, indent=4)

        else:
            await message.channel.send("**Weapons are :lock: locked. [Level Required - 10]**")

    @buy.command()
    async def dagger(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        with open("./local/weapons.json", 'r') as f:
            weapon = json.load(f)

        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']
        color = users[str(id)]['color']
        dagger = self.bot.get_emoji(881478895835164682)

        if lvl >= 10:
            with open("./local/shop.json", "r") as f:
                shopDict = json.load(f)

            if shopDict["weapon"] != "dagger":
                await message.channel.send("**`Dagger` is not available in the shop at the moment**")

            elif xp < 10000:
                await message.channel.send("**Insufficient Balance. You do not have** `10,000` **XP**")

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

                await message.channel.send("**Dagger was successfully purchased. [10,000 XP Deducted]**")

                with open("./local/weapons.json", 'w') as f:
                    json.dump(weapon, f, indent=4)

                with open(guildid, 'w') as f:
                    json.dump(users, f, indent=4)

            elif str(id) in weapon:
                if weapon[str(id)]['dagger'] == True:
                    await message.channel.send("**You already own a Dagger**")

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

                    await message.channel.send("**Dagger was successfully purchased. [10,000 XP Deducted]**")

                    with open("./local/weapons.json", 'w') as f:
                        json.dump(weapon, f, indent=4)

                    with open(guildid, 'w') as f:
                        json.dump(users, f, indent=4)

        else:
            await message.channel.send("**Weapons are :lock: locked. [Level Required - 10]**")

    @buy.command()
    async def sword(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        with open("./local/weapons.json", 'r') as f:
            weapon = json.load(f)

        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']
        color = users[str(id)]['color']
        sword = self.bot.get_emoji(881478895247949887)

        if lvl >= 10:
            with open("./local/shop.json", "r") as f:
                shopDict = json.load(f)

            if shopDict["weapon"] != "sword":
                await message.channel.send("**`Sword` is not available in the shop at the moment**")

            elif xp < 15000:
                await message.channel.send("**Insufficient Balance. You do not have** `15,000` **XP**")

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

                await message.channel.send("**Sword was successfully purchased. [15,000 XP Deducted]**")

                with open("./local/weapons.json", 'w') as f:
                    json.dump(weapon, f, indent=4)

                with open(guildid, 'w') as f:
                    json.dump(users, f, indent=4)

            elif str(id) in weapon:
                if weapon[str(id)]['sword'] == True:
                    await message.channel.send("**You already own a Sword**")

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

                    await message.channel.send("**Sword was successfully purchased. [15,000 XP Deducted]**")

                    with open("./local/weapons.json", 'w') as f:
                        json.dump(weapon, f, indent=4)

                    with open(guildid, 'w') as f:
                        json.dump(users, f, indent=4)

        else:
            await message.channel.send("**Weapons are :lock: locked. [Level Required - 10]**")

    @buy.command()
    async def scythe(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        with open("./local/weapons.json", 'r') as f:
            weapon = json.load(f)

        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']
        color = users[str(id)]['color']
        scythe = self.bot.get_emoji(881478895604494376)

        if lvl >= 10:
            with open("./local/shop.json", "r") as f:
                shopDict = json.load(f)

            if shopDict["weapon"] != "scythe":
                await message.channel.send("**`Scythe` is not available in the shop at the moment**")

            elif xp < 17000:
                await message.channel.send("**Insufficient Balance. You do not have** `17,000` **XP**")

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

                await message.channel.send("**Scythe was successfully purchased. [17,000 XP Deducted]**")

                with open("./local/weapons.json", 'w') as f:
                    json.dump(weapon, f, indent=4)

                with open(guildid, 'w') as f:
                    json.dump(users, f, indent=4)

            elif str(id) in weapon:
                if weapon[str(id)]['scythe'] == True:
                    await message.channel.send("**You already own a Scythe**")

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

                    await message.channel.send("**Scythe was successfully purchased. [17,000 XP Deducted]**")

                    with open("./local/weapons.json", 'w') as f:
                        json.dump(weapon, f, indent=4)

                    with open(guildid, 'w') as f:
                        json.dump(users, f, indent=4)

        else:
            await message.channel.send("**Weapons are :lock: locked. [Level Required - 10]**")

    @buy.command()
    async def shuriken(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        with open("./local/weapons.json", 'r') as f:
            weapon = json.load(f)

        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']
        color = users[str(id)]['color']
        shuriken = self.bot.get_emoji(881478895889690674)

        if lvl >= 10:
            with open("./local/shop.json", "r") as f:
                shopDict = json.load(f)

            if shopDict["weapon"] != "shuriken":
                await message.channel.send("**`Shuriken` is not available in the shop at the moment**")

            elif xp < 23000:
                await message.channel.send("**Insufficient Balance. You do not have** `23,000` **XP**")

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

                await message.channel.send("**Shuriken was successfully purchased. [23,000 XP Deducted]**")

                with open("./local/weapons.json", 'w') as f:
                    json.dump(weapon, f, indent=4)

                with open(guildid, 'w') as f:
                    json.dump(users, f, indent=4)

            elif str(id) in weapon:
                if weapon[str(id)]['shuriken'] == True:
                    await message.channel.send("**You already own a Shuriken**")

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

                    await message.channel.send("**Shuriken was successfully purchased. [23,000 XP Deducted]**")

                    with open("./local/weapons.json", 'w') as f:
                        json.dump(weapon, f, indent=4)

                    with open(guildid, 'w') as f:
                        json.dump(users, f, indent=4)

        else:
            await message.channel.send("**Weapons are :lock: locked. [Level Required - 10]**")

    @commands.group(invoke_without_command=True)
    async def sell(self, message):
        S = []
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']
        sage_emoji = self.bot.get_emoji(958255752156430336)
        hunter_emoji = self.bot.get_emoji(958255782112153600)

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="
        else:
            get_prefix = "="

        for i in users[str(id)]:
            if users[str(id)][i] == True:
                S.append(i)

        if "sage_spell" in S:
            spell = f"{sage_emoji} Sage"

        elif "hunter_spell" in S:
            spell = f"{hunter_emoji} Hunter"

        else:
            spell = "None"

        if "chameleon" in S:
            jutsu = ":face_in_clouds: Chameleon"

        elif "transformation" in S:
            jutsu = ":disguised_face: Transformation"

        else:
            jutsu = "None"

        ability = "None"

        with open("./local/weapons.json", "r") as f:
            weapons = json.load(f)

        if str(id) in weapons:
            if weapons[f"{id}"]["knife"] == True:
                knife = self.bot.get_emoji(881474984193703999)
                w = f"{knife} Knife"

            elif weapons[f"{id}"]["machette"] == True:
                machette = self.bot.get_emoji(881478895503806464)
                w = f"{machette} Machette"

            elif weapons[f"{id}"]["dagger"] == True:
                dagger = self.bot.get_emoji(881478895835164682)
                w = f"{dagger} Dagger"

            elif weapons[f"{id}"]["sword"] == True:
                sword = self.bot.get_emoji(881478895247949887)
                w = f"{sword} Sword"

            elif weapons[f"{id}"]["scythe"] == True:
                scythe = self.bot.get_emoji(881478895604494376)
                w = f"{scythe} Scythe"

            elif weapons[f"{id}"]["shuriken"] == True:
                shuriken = self.bot.get_emoji(881478895889690674)
                w = f"{shuriken} Shuriken"

            else:
                w = "None"

        else:
            w = "None"

        embed = discord.Embed(
            color=color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Sell 🪙", icon_url=self.bot.user.avatar)
        #embed.add_field(name = "🦸🏻 Ability", value = f"`{ability}`")
        embed.add_field(name="Spell", value=f"{spell}\n"
                        f"`{get_prefix}sell spell`", inline=False)
        embed.add_field(name="Jutsu", value=f"{jutsu}\n"
                        f"`{get_prefix}sell jutsu`", inline=False)
        embed.add_field(name="Weapon", value=f"{w}\n"
                        f"`{get_prefix}sell weapon`\n\n"
                        f"**Note** that the selling price of Spells and Jutsu\nwill be 50% of its cost price", inline=False)
        await message.channel.send(embed=embed)

    @sell.command()
    async def spell(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        sage = users[str(id)]['sage_spell']
        hunter = users[str(id)]['hunter_spell']
        wraith = users[str(id)]['wraith_spell']

        if sage == True:
            users[str(id)]['sage_spell'] = False
            xp = users[str(id)]['experience']
            xp = xp + 25000
            users[str(id)]['experience'] = int(xp)
            lvl = int(xp ** (1/4))
            users[str(id)]['level'] = lvl

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            await message.channel.send("**Sage Spell ✨ sold for** `25,000` **XP**")

        elif hunter == True:
            users[str(id)]['hunter_spell'] = False
            xp = users[str(id)]['experience']
            xp = xp + 10000
            users[str(id)]['experience'] = int(xp)
            lvl = int(xp ** (1/4))
            users[str(id)]['level'] = lvl

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            await message.channel.send("**Hunter Spell 🏹 sold for** `10,000` **XP**")

        else:
            await message.channel.send("**You do not own any spells.**")

    @sell.command()
    async def jutsu(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        cham = users[str(id)]['chameleon']
        trans = users[str(id)]['transformation']

        if cham == True:
            users[str(id)]['chameleon'] = False
            xp = users[str(id)]['experience']
            xp = xp + 3000
            users[str(id)]['experience'] = int(xp)
            lvl = int(xp ** (1/4))
            users[str(id)]['level'] = lvl

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            await message.channel.send("**Chameleon Jutsu 🥷🏻 forgotten, acquired** `3,000` **XP**")

        elif trans == True:
            users[str(id)]['transformation'] = False
            xp = users[str(id)]['experience']
            xp = xp + 10000
            users[str(id)]['experience'] = int(xp)
            lvl = int(xp ** (1/4))
            users[str(id)]['level'] = lvl

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            await message.channel.send("**Transformation Jutsu 🥷🏻 forgotten, acquired** `5,000` **XP**")

        else:
            await message.channel.send("**You do not know any jutsu.**")

    @sell.command()
    async def weapon(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/weapons.json", 'r') as f:
            weapon = json.load(f)

        if str(id) not in weapon:
            await message.channel.send("**You do not own any weapons.**")

        elif str(id) in weapon:

            if weapon[str(id)]['knife'] == True:
                weapon.pop(str(id))
                wstr = "Knife was sold for `500 XP`"
                xp = users[str(id)]['experience']
                xp = xp + 500
                users[str(id)]['experience'] = int(xp)
                lvl = int(xp ** (1/4))
                users[str(id)]['level'] = lvl

            elif weapon[str(id)]['machette'] == True:
                weapon.pop(str(id))
                wstr = "Machette was sold for `2K XP`"
                xp = users[str(id)]['experience']
                xp = xp + 2000
                users[str(id)]['experience'] = int(xp)
                lvl = int(xp ** (1/4))
                users[str(id)]['level'] = lvl

            elif weapon[str(id)]['dagger'] == True:
                weapon.pop(str(id))
                wstr = "Dagger was sold for `2K XP`"
                xp = users[str(id)]['experience']
                xp = xp + 2000
                users[str(id)]['experience'] = int(xp)
                lvl = int(xp ** (1/4))
                users[str(id)]['level'] = lvl

            elif weapon[str(id)]['sword'] == True:
                weapon.pop(str(id))
                wstr = "Sword was sold for `2.5K XP`"
                xp = users[str(id)]['experience']
                xp = xp + 2500
                users[str(id)]['experience'] = int(xp)
                lvl = int(xp ** (1/4))
                users[str(id)]['level'] = lvl

            elif weapon[str(id)]['scythe'] == True:
                weapon.pop(str(id))
                wstr = "Scythe was sold for `3K XP`"
                xp = users[str(id)]['experience']
                xp = xp + 3000
                users[str(id)]['experience'] = int(xp)
                lvl = int(xp ** (1/4))
                users[str(id)]['level'] = lvl

            elif weapon[str(id)]['shuriken'] == True:
                weapon.pop(str(id))
                wstr = "Shuriken was sold for `5K XP`"
                xp = users[str(id)]['experience']
                xp = xp + 5000
                users[str(id)]['experience'] = int(xp)
                lvl = int(xp ** (1/4))
                users[str(id)]['level'] = lvl

            else:
                await message.channel.send("**You do not own any weapons.**")

            with open("./local/weapons.json", 'w') as f:
                json.dump(weapon, f, indent=4)

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            await message.channel.send(f"{wstr}")

        else:
            await message.channel.send("**You do not own any weapons.**")

    @sell.command()
    async def chest(self, message):
        await message.channel.send("**Chests cannot be sold.**")

    @buy.command()
    async def chest(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/chest.json", "r") as f:
            chest = json.load(f)

        if str(id) not in chest:
            user_xp = users[str(id)]["experience"]

            if user_xp >= 12000:
                user_xp = user_xp - 12000
                users[str(id)]["experience"] = int(user_xp)
                user_lvl = int(user_xp ** (1/4))
                users[str(id)]['level'] = user_lvl

                chest[str(id)] = {}
                chest[str(id)][str(message.channel.guild.id)] = {}
                chest[str(id)][str(message.channel.guild.id)]["level"] = 1
                chest[str(id)][str(message.channel.guild.id)]["xp"] = 0

                await message.channel.send("**Purchase Successful. You bought a chest! `12,000 XP` has been deducted**")

                with open("./local/chest.json", "w") as f:
                    json.dump(chest, f, indent=4)

                with open(guildid, "w") as f:
                    json.dump(users, f, indent=4)

            elif user_xp < 12000:
                await message.channel.send("**Insufficient Balance. `12,000 XP` is required to buy a chest**")

        elif str(id) in chest:
            user_data = chest[str(id)]
            user_data = list(user_data)

            if str(message.channel.guild.id) in user_data:
                await message.channel.send("**You have already purchased a chest from this server. Only 1 chest per server is allowed**")

            elif str(message.channel.guild.id) not in user_data:
                user_xp = users[str(id)]["experience"]

                if user_xp >= 12000:
                    user_xp = user_xp - 12000
                    users[str(id)]["experience"] = int(user_xp)
                    user_lvl = int(user_xp ** (1/4))
                    users[str(id)]['level'] = user_lvl

                    chest[str(id)][str(message.channel.guild.id)] = {}
                    chest[str(id)][str(message.channel.guild.id)]["level"] = 1
                    chest[str(id)][str(message.channel.guild.id)]["xp"] = 0

                    await message.channel.send("**Purchase Successful. You bought a chest! `12,000 XP` has been deducted**")

                    with open("./local/chest.json", "w") as f:
                        json.dump(chest, f, indent=4)

                    with open(guildid, "w") as f:
                        json.dump(users, f, indent=4)

                elif user_xp < 12000:
                    await message.channel.send("**Insufficient Balance. `12,000 XP` is required to buy a chest**")


async def setup(bot):
    await bot.add_cog(BuyCog(bot))
