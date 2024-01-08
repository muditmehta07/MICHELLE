import discord
from discord.ext import commands
import os
import pickle
import random
import datetime
import json
from discord.ext.commands import cooldowns


class ItemCog(commands.Cog):
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

    @commands.command(aliases=["inv"])
    async def inventory(self, message):
        S = []
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        chest_emoji = self.bot.get_emoji(955783898577661973)
        sage_emoji = self.bot.get_emoji(958255752156430336)
        hunter_emoji = self.bot.get_emoji(958255782112153600)

        embed = discord.Embed(description="",
                              color=color, timestamp=datetime.datetime.utcnow())

        embed.set_author(
            name=f"{message.author.name}'s Inventory", icon_url=message.author.avatar)

        for i in users[str(id)]:
            if users[str(id)][i] == True:
                S.append(i)

        if "sage_spell" in S:
            giftbox = f"{sage_emoji} **Sage Spell**\n**ID :** `sage` - *Item*\n\n"
            description = embed.description + giftbox
            embed.description = description

        elif "hunter_spell" in S:
            giftbox = f"{hunter_emoji} **Hunter Spell**\n**ID :** `hunter` - *Item*\n\n"
            description = embed.description + giftbox
            embed.description = description

        if "chameleon" in S:
            giftbox = f":face_in_clouds: **Chameleon Jutsu**\n**ID :** `chameleon` - *Skill*\n\n"
            description = embed.description + giftbox
            embed.description = description

        elif "transformation" in S:
            giftbox = f":disguised_face: **Chameleon Jutsu**\n**ID :** `transformation` - *Skill*\n\n"
            description = embed.description + giftbox
            embed.description = description

        with open("./local/weapons.json", "r") as f:
            weapons = json.load(f)

        if str(id) in weapons:
            if weapons[f"{id}"]["knife"] == True:
                i = self.bot.get_emoji(881474984193703999)
                giftbox = f"{i} **Knife**\n**ID :** `knife` - *Weapon*\n\n"
                description = embed.description + giftbox
                embed.description = description

            elif weapons[f"{id}"]["machette"] == True:
                i = self.bot.get_emoji(881478895503806464)
                giftbox = f"{i} **Machette**\n**ID :** `machette` - *Weapon*\n\n"
                description = embed.description + giftbox
                embed.description = description

            elif weapons[f"{id}"]["dagger"] == True:
                i = self.bot.get_emoji(881478895835164682)
                giftbox = f"{i} **Dagger**\n**ID :** `dagger` - *Weapon*\n\n"
                description = embed.description + giftbox
                embed.description = description

            elif weapons[f"{id}"]["sword"] == True:
                i = self.bot.get_emoji(881478895247949887)
                giftbox = f"{i} **Sword**\n**ID :** `sword` - *Weapon*\n\n"
                description = embed.description + giftbox
                embed.description = description

            elif weapons[f"{id}"]["scythe"] == True:
                i = self.bot.get_emoji(881478895604494376)
                giftbox = f"{i} **Scythe**\n**ID :** `scythe` - *Weapon*\n\n"
                description = embed.description + giftbox
                embed.description = description

            elif weapons[f"{id}"]["shuriken"] == True:
                i = self.bot.get_emoji(881478895889690674)
                giftbox = f"{i} **Shuriken**\n**ID :** `shuriken` - *Weapon*\n\n"
                description = embed.description + giftbox
                embed.description = description

        with open("./local/items.json", "r") as g:
            auth = json.load(g)

        if str(message.author.id) in auth:
            item_list = auth[f"{message.author.id}"]["items"]

            count = 0
            for i in item_list:
                if i == "gift_box":
                    count += 1

            if count >= 1:
                giftbox = f"🎁 **Gift Box** - {count}\n**ID :** `giftbox` - *Power Up*\n\n"
                description = embed.description + giftbox
                embed.description = description

        with open("./local/chest.json", "r") as f:
            chest = json.load(f)

        if str(id) in chest:
            user_data = chest[str(id)]
            user_data = list(user_data)

            if len(user_data) >= 1:
                chest_text = ""
                for i in user_data:
                    chest_lvl = chest[str(message.author.id)][str(i)]["level"]

                    if chest_lvl == 1:
                        chest_name = "Common Chest"
                    elif chest_lvl == 2:
                        chest_name = "Amazing Chest"
                    elif chest_lvl == 3:
                        chest_name = "Brilliant Chest"
                    elif chest_lvl == 4:
                        chest_name = "Divine Chest"
                    elif chest_lvl == 5:
                        chest_name = "Exquisite Chest"
                    elif chest_lvl == 6:
                        chest_name = "Legendary Chest"

                    chest_text += f"{chest_emoji} **{chest_name}**\n**ID :** `{i}` - *Storage*\n\n"

                description = embed.description + chest_text
                embed.description = description

        len_description = len(embed.description)
        if len_description == 0:
            await message.reply(f"**Your inventory is empty (0 items)**")

        else:
            await message.channel.send(embed=embed)

    @commands.command(aliases=["weapon"])
    async def weapons(self, message):
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

        theme = users[str(id)]['color']
        if theme == 9807270:  # gray
            url = "https://cdn.discordapp.com/emojis/909410043630333982.png?v=1"

        elif theme == 15158332 or theme == 10038562:  # red
            url = "https://cdn.discordapp.com/emojis/909411551906234378.png?v=1"

        elif theme == 3447003 or theme == 2123412:  # blue
            url = "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1"

        elif theme == 3066993 or theme == 2067276:  # green
            url = "https://cdn.discordapp.com/emojis/909410753960902718.png?v=1"

        elif theme == 10181046 or theme == 7419530:  # purple
            url = "https://cdn.discordapp.com/emojis/909411520373477406.png?v=1"

        elif theme == 15844367 or theme == 12745742:  # gold
            url = "https://cdn.discordapp.com/emojis/909411582465949746.png?v=1"

        elif theme == 1752220 or theme == 1146986:  # teal
            url = "https://cdn.discordapp.com/emojis/909410348480733244.png?v=1"

        elif theme == 15105570 or theme == 11027200:  # orange
            url = "https://cdn.discordapp.com/emojis/909411487632744509.png?v=1"

        elif theme == 15277667 or theme == 11342935:  # magenta
            url = "https://cdn.discordapp.com/emojis/909410987285827655.png?v=1"

        else:  # gray
            url = "https://cdn.discordapp.com/emojis/909410043630333982.png?v=1"

        knife = self.bot.get_emoji(881474984193703999)
        machette = self.bot.get_emoji(881478895503806464)
        dagger = self.bot.get_emoji(881478895835164682)
        sword = self.bot.get_emoji(881478895247949887)
        scythe = self.bot.get_emoji(881478895604494376)
        shuriken = self.bot.get_emoji(881478895889690674)
        replyEmoji = self.bot.get_emoji(929383454469128263)

        embed = discord.Embed(description=f"{knife}**knife**\n{replyEmoji}A kitchen knife\n"
                              f"{machette}**machette**\n{replyEmoji}An old machette\n"
                              f"{dagger}**dagger**\n{replyEmoji}A faulty dagger\n"
                              f"{sword}**sword**\n{replyEmoji}A sword from minecraft\n"
                              f"{shuriken}**shuriken**\n{replyEmoji}A manji shuriken",
                              color=color, timestamp=datetime.datetime.utcnow())

        embed.set_footer(
            text=f"use '{get_prefix}help <weapon name>' for more info")
        embed.set_author(name="Weapons", icon_url=url)
        await message.channel.send(embed=embed)

    @commands.command(aliases=["spells"])
    async def spell(self, message):
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

        replyEmoji = self.bot.get_emoji(929383454469128263)

        embed = discord.Embed(
            description=f"**sage**\n{replyEmoji}Become an immortal and support your peers\n"
            f"**hunter**\n{replyEmoji}Become a predator that hunts the weak",
            color=color, timestamp=datetime.datetime.utcnow())
        embed.set_footer(
            text=f"use '{get_prefix}help <spell name>' for more info")
        embed.set_author(
            name="Spells", icon_url="https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
        await message.channel.send(embed=embed)

    @commands.command(aliases=["jutsus"])
    async def jutsu(self, message):
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

        replyEmoji = self.bot.get_emoji(929383454469128263)

        embed = discord.Embed(
            description=f"**chameleon**\n{replyEmoji}A Ninjutsu to hide yourself\n"
            f"**transformation**\n{replyEmoji}A Ninjutsu to transform yourself",
            color=color, timestamp=datetime.datetime.utcnow())
        embed.set_footer(
            text=f"use '{get_prefix}help <jutsu name>' for more info")
        embed.set_author(
            name="Jutsu", icon_url="https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
        await message.channel.send(embed=embed)

    @commands.command()
    async def giftbox(self, ctx):
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/items.json", "r") as g:
            auth = json.load(g)

        if not str(ctx.author.id) in auth:

            embed = discord.Embed(description="You own **0** Gift Boxes\n\nGift Boxes contain **XP**, currently the only way to obtain a Gift Box is to join the offical [Michelle's Community](https://discord.gg/EfHrMURtnA) Server",
                                  color=color, timestamp=datetime.datetime.utcnow())
            embed.set_author(
                name="Gift Box 🎁", icon_url="https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
            await ctx.send(embed=embed)

        elif str(ctx.author.id) in auth:

            item_list = auth[f"{ctx.author.id}"]["items"]

            count = 0
            for i in item_list:
                if i == "gift_box":
                    count += 1

            if count == 0:
                embed = discord.Embed(description="You own **0** Gift Boxes\n\nGift Boxes contain **XP**, currently the only way to obtain a Gift Box is to join the offical [Michelle's Community](https://discord.gg/EfHrMURtnA) Server",
                                      color=color, timestamp=datetime.datetime.utcnow())
                embed.set_author(
                    name="Gift Box 🎁", icon_url="https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
                await ctx.send(embed=embed)

            elif count > 0:
                item_list.remove("gift_box")
                auth[f"{ctx.author.id}"]["items"] = item_list

                with open("./local/items.json", "w") as g:
                    json.dump(auth, g, indent=4)

                initial_level = users[str(id)]['level']
                xp = users[str(id)]['experience']
                xp += 100000
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

                embed = discord.Embed(description=f"You found **100K XP** in the Gift Box. **{count-1}** Gift Boxes Remaining",
                                      color=color, timestamp=datetime.datetime.utcnow())
                embed.set_author(
                    name="Gift Box 🎁", icon_url="https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
                await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def daily(self, ctx):
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']
        xp = users[str(id)]['experience']
        initial_level = int(users[str(id)]['level'])

        daily = random.randint(250, 750)
        daily = daily*5
        xp += daily
        users[str(id)]['experience'] = int(xp)
        lvl = int(xp ** (1/4))
        users[str(id)]['level'] = lvl

        with open(guildid, 'w') as f:
            json.dump(users, f, indent=4)

        embed = discord.Embed(description=f"**You recieved** `{daily} XP`\n----------\n"
                              f"Next daily reward in **24 hours**",
                              color=color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Daily Rewards")

        await ctx.send(embed=embed)

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

                    else:
                        stonks = self.bot.get_emoji(896752212749983774)
                        await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}**! {stonks}")

            elif str(ctx.author.id) not in set:
                if 10 > initial_level and lvl >= 10:

                    stonks = self.bot.get_emoji(896752212749983774)
                    await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}** and unlocked the ability to `Kill`! {stonks}")

                elif 5 > initial_level and lvl >= 5:

                    stonks = self.bot.get_emoji(896752212749983774)
                    await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}** and unlocked `Themes`! {stonks}")

                else:
                    stonks = self.bot.get_emoji(896752212749983774)
                    await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}**! {stonks}")

            else:
                if 10 > initial_level and lvl >= 10:

                    stonks = self.bot.get_emoji(896752212749983774)
                    await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}** and unlocked the ability to `Kill`! {stonks}")

                elif 5 > initial_level and lvl >= 5:

                    stonks = self.bot.get_emoji(896752212749983774)
                    await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}** and unlocked `Themes`! {stonks}")

                else:
                    stonks = self.bot.get_emoji(896752212749983774)
                    await ctx.send(f"{ctx.author.mention} Stonks! You elevated to **Level {lvl}**! {stonks}")

    @daily.error
    async def daily_error(self, ctx, error):

        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = error.retry_after

            with open("./local/settings.json") as s:
                set = json.load(s)

            if str(ctx.author.id) in set:
                if set[f"{ctx.author.id}"]["tips"] == True:
                    embed = discord.Embed(
                        description=f"**You already recieved your daily reward**\n\n**PROTIP** : You can get more XP by killing server members using weapons\nWeapons are now available in shop.\n\nCome back in **{ItemCog.humanize(self, str(ItemCog.convert(self, remaining_time)))}**", color=color, timestamp=datetime.datetime.utcnow())
                    embed.set_author(name="Daily Rewards On Cooldown")
                    await ctx.send(embed=embed)

                else:
                    embed = discord.Embed(
                        description=f"**You already recieved your daily reward**\n----------\nCome back in **{ItemCog.humanize(self, str(ItemCog.convert(self, remaining_time)))}**", color=color, timestamp=datetime.datetime.utcnow())
                    embed.set_author(name="Daily Rewards On Cooldown")
                    await ctx.send(embed=embed)

            else:
                embed = discord.Embed(
                    description=f"**You already recieved your daily reward**\n----------\nCome back in **{ItemCog.humanize(self, str(ItemCog.convert(self, remaining_time)))}**", color=color, timestamp=datetime.datetime.utcnow())
                embed.set_author(name="Daily Rewards On Cooldown")
                await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 21600, commands.BucketType.user)
    async def beg(self, ctx):
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']
        xp = users[str(id)]['experience']
        initial_level = int(users[str(id)]['level'])

        daily1 = random.randint(2, 80)
        daily1 = daily1*5
        xp += daily1
        users[str(id)]['experience'] = int(xp)
        lvl = int(xp ** (1/4))
        users[str(id)]['level'] = lvl

        with open(guildid, 'w') as f:
            json.dump(users, f, indent=4)

        A = {
            'Kazuto Kirigaya': ["You can be an excellent swordsman. **{daily} XP**, that's all I have", 'Sword Art Online'],
            'Asuna Yuuki': ["Hm, my guild won't help you, but here, take **{daily} XP**", 'Sword Art Online'],
            'Naruto Uzumaki': ["Here, take **{daily} XP**. I'm there for you anytime. Believe it!", 'Naruto'],
            'Sakura Harano': ["Don't hurt me, take **{daily} XP**. SASUKE HELP!", 'Naruto'],
            'Sasuke Uchiha': ["Take **{daily} XP** and help me find my brother", 'Naruto'],
            'Itachi Uchiha': ["Genjutsu of that level doesn't work on me", 'Naruto'],
            'Kakashi Hatake': ["Alright, take **{daily} XP**. Won't be able to buy that book today then", 'Naruto'],
            'Light Yagami': ["Worship me as the God of this new world", 'Death Note'],
            'Misa Amane': ["I guess you don't have the eyes. Take **{daily} XP** though", 'Death Note'],
            'Kurisu Makise': ["I'll give you **{daily} XP** to get away from that microwave", 'Steins;Gate'],
            'Killua Zoldyck': ["When I say, take 1 Million XP, it means you take **{daily} XP**", 'Hunter x Hunter'],
            'Rintarou Okabe': ["My lab members have **{daily} XP**, and my enemies have none", 'Steins;Gate'],
            'Edward Elric': ["Like I always say - Can't find a door? Make your own with **{daily} XP**", 'Fullmetal Alchemist'],
            'Levi Ackerman': ["If you don't want to die, take **{daily} XP**", 'Attack on Titan'],
            'Monkey D. Luffy': ["**{daily} XP**? What is that? What are you blabbering about?", 'One Piece'],
            'L': ["**{daily} XP**? It appears to be some code only Kira can understand", 'Death Note'],
            'Izuku Midoriya': ["**{daily} XP** will make you many times stronger than you already are!", 'My Hero Academia'],
            'Ichigo Kurosaki': ["I drop **{daily} XP** everytime I see dead people. Oops", 'Bleach'],
            'Saitama': ["Ok. Take **{daily} XP**", 'One Punch Man'],
            'Naho Takamiya': ["The letter told me to give you **{daily} XP**", 'Orange'],
            'Satoru Fujinuma': ["I never stopped believing! And I believe you'll get **{daily} XP**", 'Erased'],
            'Airi Katagiri': ["*Snip, Snip.* Take **{daily} XP**", 'Erased'],
            'Arata Kaizaki': ["Yeah sure. Take **{daily} XP**, that's all I have right now", 'ReLife'],
            'Chizuru Hishiro': ["/*drops **{daily} XP** and runs away/*", 'ReLife']
        }

        B = ['https://www.youtube.com/watch?v=BnhMFj4DKY0', 'https://www.youtube.com/watch?v=nYzkPMZPUCI', 'https://www.youtube.com/watch?v=-Bl-RL59ick', 'https://www.youtube.com/watch?v=3llgfBhLp3A', 'https://www.youtube.com/watch?v=n8aurcpEQhM', 'https://www.youtube.com/watch?v=Dshc0vdq3iM',
             'https://www.youtube.com/watch?v=vJKnksy99RE', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'https://www.youtube.com/watch?v=L_jWHffIx5E', 'https://www.youtube.com/watch?v=aJ9usrpAPao', 'https://www.youtube.com/watch?v=-DUV2oAL11A', 'https://www.youtube.com/watch?v=T78nq62aQgM']

        i = list(A.keys())
        r = random.randint(0, 22)
        i = i[r]
        character = i
        line = A[i][0]
        anime = A[i][1]
        link = random.choice(B)

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

        if i == "Itachi Uchiha" or i == "Light Yagami":
            embed = discord.Embed(title=f"{character}",
                                  description=line,
                                  url=f"{link}",
                                  color=color, timestamp=datetime.datetime.utcnow())

            embed.set_footer(text=f"{anime}")
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(title=f"{character}",
                                  description=line.format(daily=daily1),
                                  url=f"{link}",
                                  color=color, timestamp=datetime.datetime.utcnow())

            embed.set_footer(text=f"{anime}")
            await ctx.send(embed=embed)

    @beg.error
    async def beg_error(self, ctx, error):

        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = error.retry_after

            embed = discord.Embed(
                description=f"You're begging too much, stop it, doesn't look good\n\nYou can beg again in **{ItemCog.humanize(self, str(ItemCog.convert(self, remaining_time)))}**", color=color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name="Beg On Cooldown")
            await ctx.send(embed=embed)

    @commands.group(invoke_without_command=True)
    async def chest(self, ctx, chest_id: str = None):
        user_id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(user_id)]['color']
        chest_emoji = "https://cdn.discordapp.com/emojis/955783898577661973.webp?size=96&quality=lossless"

        with open("./local/chest.json", "r") as f:
            chest = json.load(f)

        if chest_id == None:
            embed = discord.Embed(
                description=f"**Description** : Chests are used to store XP and keep it safe.\n\n**Usage**: `{ctx.prefix}chest <chest id>`\n**Example**: `{ctx.prefix}chest 1234 <chest id>` to view Chest with ID - 1234\n\n**Note**: To check your chest IDs, use command `=inv`",
                color=color,
                timestamp=datetime.datetime.utcnow()
            )

            embed.set_author(name="Chest Help ❓")
            await ctx.send(embed=embed)

        elif str(user_id) not in chest:
            await ctx.reply("**Whoops. Looks like you don't own a chest**")

        elif str(user_id) in chest:
            user_data = chest[str(user_id)]
            user_data = list(user_data)

            if len(user_data) == 0:
                await ctx.reply("**Whoops. Looks like you don't own a chest**")

            elif len(user_data) >= 1:
                if chest_id in user_data:
                    chest_level = chest[str(user_id)][str(chest_id)]["level"]
                    chest_xp = chest[str(user_id)][str(chest_id)]["xp"]

                    if chest_level == 1:
                        chest_xp = int(chest_xp)
                        percentage = int((chest_xp//20000) * 100)

                        embed = discord.Embed(
                            description=f"**Description**: A regular chest made out of wood from the `Enchanted Forest`. It is said that the `Dark Queen` used to summon her `Minions` in that forest.\n\n**{chest_xp} / 20,000 XP** ({percentage}% used)",
                            color=color,
                            timestamp=datetime.datetime.utcnow()
                        )

                        embed.set_author(name="Common Chest",
                                         icon_url=chest_emoji)
                        embed.set_footer(text="Upgrade for more storage")

                        await ctx.send(embed=embed)

                    elif chest_level == 2:
                        chest_xp = int(chest_xp)
                        percentage = int((chest_xp//100000) * 100)

                        embed = discord.Embed(
                            description=f"**Description**: A chest made out of silver obtained from the silver mines of `Underworld`. The mines were guarded by `Goblins`.\n\n**{chest_xp} / 100,000 XP** ({percentage}% used)",
                            color=color,
                            timestamp=datetime.datetime.utcnow()
                        )

                        embed.set_author(name="Amazing Chest",
                                         icon_url=chest_emoji)
                        embed.set_footer(text="Upgrade for more storage")

                        await ctx.send(embed=embed)

                    elif chest_level == 3:
                        chest_xp = int(chest_xp)
                        percentage = int((chest_xp//175000) * 100)

                        embed = discord.Embed(
                            description=f"**Description**: A chest made out of gold obtained from the gold mines of `Underworld`. The mines were heavily guarded by `Hobgoblins`.\n\n**{chest_xp} / 175,000 XP** ({percentage}% used)",
                            color=color,
                            timestamp=datetime.datetime.utcnow()
                        )

                        embed.set_author(name="Brilliant Chest",
                                         icon_url=chest_emoji)
                        embed.set_footer(text="Upgrade for more storage")

                        await ctx.send(embed=embed)

                    elif chest_level == 4:
                        chest_xp = int(chest_xp)
                        percentage = int((chest_xp//500000) * 100)

                        embed = discord.Embed(
                            description=f"**Description**: A chest made out of `Celestial Bronze` obtained from the bottom of `Mount Olympus`. `Golems` are often found there.\n\n**{chest_xp} / 500,000 XP** ({percentage}% used)",
                            color=color,
                            timestamp=datetime.datetime.utcnow()
                        )

                        embed.set_author(name="Divine Chest",
                                         icon_url=chest_emoji)
                        embed.set_footer(text="Upgrade for more storage")

                        await ctx.send(embed=embed)

                    elif chest_level == 5:
                        chest_xp = int(chest_xp)
                        percentage = int((chest_xp//1000000) * 100)

                        embed = discord.Embed(
                            description=f"**Description**: A chest made out of `Terrestrial Obsidian` obtained from the depths of the `Underworld`. The `Obsidian` is protected by `Dracula`.\n\n**{chest_xp} / 1,000,000 XP**",
                            color=color,
                            timestamp=datetime.datetime.utcnow()
                        )

                        embed.set_author(name="Exquisite Chest",
                                         icon_url=chest_emoji)
                        embed.set_footer(text="Upgrade for more storage")

                        await ctx.send(embed=embed)

                    elif chest_level == 6:
                        embed = discord.Embed(
                            description=f"**Description**: A chest made out of `Imperial Gold` obtained from the top of `Mount Olympus`. The material is extremely difficult to obtain as it is limited and guarded by the `Imperial Dragon`.\n\n**{chest_xp} XP** stored",
                            color=color,
                            timestamp=datetime.datetime.utcnow()
                        )

                        embed.set_author(name="Legendary Chest",
                                         icon_url=chest_emoji)

                        await ctx.send(embed=embed)

                elif chest_id not in user_data:
                    await ctx.send("**Whoops. Looks like you don't own a chest with that ID**")

                else:
                    await ctx.send("**Whoops. Looks like you don't own a chest with that ID**")

    @chest.command()
    async def deposit(self, ctx):
        user_id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(user_id)]['color']

        user_xp = users[str(user_id)]['experience']

        content = ctx.message.content
        content = content.split()

        if len(content) < 4:
            embed = discord.Embed(
                description=f"**Description** : Chests are used to store XP and keep it safe.\n\n**Usage**: `{ctx.prefix}chest deposit <XP to deposit> <chest id>`\n**Example**: `{ctx.prefix}chest deposit 100 1234` to deposit 100 XP to a Chest with ID - 1234\n\n**Note**: To check your chest IDs, use command `=inv`",
                color=color,
                timestamp=datetime.datetime.utcnow()
            )

            embed.set_author(name="Chest Deposit Help ❓")
            await ctx.send(embed=embed)

        else:
            deposit_xp = str(content[-2])
            chest_id = str(content[-1])

        if int(deposit_xp) > int(user_xp):
            await ctx.reply(f"**Insufficient Funds. You don't have that much XP**")

        elif int(user_xp) >= int(deposit_xp):

            with open("./local/chest.json", "r") as f:
                chest = json.load(f)

            if chest_id == None:
                await ctx.reply(f"**Usage:** `{ctx.prefix}chest deposit <xp> <chest id>` to view chest of specific ID")

            elif str(user_id) not in chest:
                await ctx.reply("**Whoops. Looks like you don't own a chest**")

            elif str(user_id) in chest:
                user_data = chest[str(user_id)]
                user_data = list(user_data)

                if len(user_data) == 0:
                    await ctx.reply("**Whoops. Looks like you don't own a chest**")

                elif len(user_data) >= 1:
                    if chest_id in user_data:
                        chest_level = chest[str(
                            user_id)][str(chest_id)]["level"]
                        chest_xp = chest[str(user_id)][str(chest_id)]["xp"]

                        if chest_level == 1:
                            if (int(chest_xp) + int(deposit_xp)) > 20000:
                                await ctx.reply("**Insufficient Storage. Chest ran out of storage, upgrade it to get more**")

                            elif (int(chest_xp) + int(deposit_xp)) <= 20000:
                                users[str(user_id)]['experience'] = user_xp - \
                                    int(deposit_xp)
                                user_xp = users[str(user_id)]['experience']
                                lvl = int(user_xp ** (1/4))
                                users[str(user_id)]['level'] = lvl
                                chest[str(user_id)][str(chest_id)
                                                    ]["xp"] = chest_xp + int(deposit_xp)

                                with open("./local/chest.json", "w") as f:
                                    json.dump(chest, f, indent=4)

                                with open(guildid, "w") as f:
                                    json.dump(users, f, indent=4)

                                await ctx.reply(f"`{deposit_xp} XP` **has been deposited in your chest!**")

                        elif chest_level == 2:
                            if (chest_xp + int(deposit_xp)) > 100000:
                                await ctx.reply("**Insufficient Storage. Chest ran out of storage, upgrade it to get more**")

                            elif (chest_xp + int(deposit_xp)) <= 100000:
                                users[str(user_id)]['experience'] = user_xp - \
                                    int(deposit_xp)
                                user_xp = users[str(user_id)]['experience']
                                lvl = int(user_xp ** (1/4))
                                users[str(user_id)]['level'] = lvl
                                chest[str(user_id)][str(chest_id)
                                                    ]["xp"] = chest_xp + int(deposit_xp)

                                with open("./local/chest.json", "w") as f:
                                    json.dump(chest, f, indent=4)

                                with open(guildid, "w") as f:
                                    json.dump(users, f, indent=4)

                                await ctx.reply(f"`{deposit_xp} XP` **has been deposited in your chest!**")

                        elif chest_level == 3:
                            if (chest_xp + int(deposit_xp)) > 175000:
                                await ctx.reply("**Insufficient Storage. Chest ran out of storage, upgrade it to get more**")

                            elif (chest_xp + int(deposit_xp)) <= 175000:
                                users[str(user_id)]['experience'] = user_xp - \
                                    int(deposit_xp)
                                user_xp = users[str(user_id)]['experience']
                                lvl = int(user_xp ** (1/4))
                                users[str(user_id)]['level'] = lvl
                                chest[str(user_id)][str(chest_id)
                                                    ]["xp"] = chest_xp + int(deposit_xp)

                                with open("./local/chest.json", "w") as f:
                                    json.dump(chest, f, indent=4)

                                with open(guildid, "w") as f:
                                    json.dump(users, f, indent=4)

                                await ctx.reply(f"`{deposit_xp} XP` **has been deposited in your chest!**")

                        elif chest_level == 4:
                            if (chest_xp + int(deposit_xp)) > 500000:
                                await ctx.reply("**Insufficient Storage. Chest ran out of storage, upgrade it to get more**")

                            elif (chest_xp + int(deposit_xp)) <= 500000:
                                users[str(user_id)]['experience'] = user_xp - \
                                    int(deposit_xp)
                                user_xp = users[str(user_id)]['experience']
                                lvl = int(user_xp ** (1/4))
                                users[str(user_id)]['level'] = lvl
                                chest[str(user_id)][str(chest_id)
                                                    ]["xp"] = chest_xp + int(deposit_xp)

                                with open("./local/chest.json", "w") as f:
                                    json.dump(chest, f, indent=4)

                                with open(guildid, "w") as f:
                                    json.dump(users, f, indent=4)

                                await ctx.reply(f"`{deposit_xp} XP` **has been deposited in your chest!**")

                        elif chest_level == 5:
                            if (chest_xp + int(deposit_xp)) > 1000000:
                                await ctx.reply("**Insufficient Storage. Chest ran out of storage, upgrade it to get more**")

                            elif (chest_xp + int(deposit_xp)) <= 1000000:
                                users[str(user_id)]['experience'] = user_xp - \
                                    int(deposit_xp)
                                user_xp = users[str(user_id)]['experience']
                                lvl = int(user_xp ** (1/4))
                                users[str(user_id)]['level'] = lvl
                                chest[str(user_id)][str(chest_id)
                                                    ]["xp"] = chest_xp + int(deposit_xp)

                                with open("./local/chest.json", "w") as f:
                                    json.dump(chest, f, indent=4)

                                with open(guildid, "w") as f:
                                    json.dump(users, f, indent=4)

                                await ctx.reply(f"`{deposit_xp} XP` **has been deposited in your chest!**")

                        elif chest_level == 6:
                            users[str(user_id)]['experience'] = user_xp - \
                                int(deposit_xp)
                            user_xp = users[str(user_id)]['experience']
                            lvl = int(user_xp ** (1/4))
                            users[str(user_id)]['level'] = lvl
                            chest[str(user_id)][str(chest_id)
                                                ]["xp"] = chest_xp + int(deposit_xp)

                            with open("./local/chest.json", "w") as f:
                                json.dump(chest, f, indent=4)

                            with open(guildid, "w") as f:
                                json.dump(users, f, indent=4)

                            await ctx.reply(f"`{deposit_xp} XP` **has been deposited in your chest!**")

                    elif chest_id not in user_data:
                        await ctx.reply("**Whoops. Looks like you don't own a chest with that ID**")

    @chest.command()
    async def withdraw(self, ctx):
        user_id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(user_id)]['color']

        user_xp = users[str(user_id)]['experience']

        content = ctx.message.content
        content = content.split()

        if len(content) < 4:
            embed = discord.Embed(
                description=f"**Description** : Chests are used to store XP and keep it safe.\n\n**Usage**: `{ctx.prefix}chest withdraw <XP to withdraw> <chest id>`\n**Example**: `{ctx.prefix}chest withdraw 100 1234` to withdraw 100 XP from a Chest with ID - 1234\n\n**Note**: To check your chest IDs, use command `=inv`",
                color=color,
                timestamp=datetime.datetime.utcnow()
            )

            embed.set_author(name="Chest Withdraw Help ❓")
            await ctx.send(embed=embed)

        else:
            withdraw_xp = str(content[-2])
            chest_id = str(content[-1])

        with open("./local/chest.json", "r") as f:
            chest = json.load(f)

        if chest_id == None:
            await ctx.reply(f"**Usage:** `{ctx.prefix}chest deposit <xp> <chest id>` to view chest of specific ID")

        elif str(user_id) not in chest:
            await ctx.reply("**Whoops. Looks like you don't own a chest**")

        elif str(user_id) in chest:
            user_data = chest[str(user_id)]
            user_data = list(user_data)

            if len(user_data) == 0:
                await ctx.reply("**Whoops. Looks like you don't own a chest**")

            elif len(user_data) >= 1:
                if chest_id in user_data:
                    chest_level = chest[str(user_id)][str(chest_id)]["level"]
                    chest_xp = chest[str(user_id)][str(chest_id)]["xp"]

                    if int(withdraw_xp) > chest_xp:
                        await ctx.reply(f"**Insufficient Funds. You don't have that much XP in this chest**")

                    elif chest_xp >= int(withdraw_xp):

                        users[str(user_id)]['experience'] = user_xp + \
                            int(withdraw_xp)
                        user_xp = users[str(user_id)]['experience']
                        lvl = int(user_xp ** (1/4))
                        users[str(user_id)]['level'] = lvl
                        chest[str(user_id)][str(chest_id)
                                            ]["xp"] = chest_xp - int(withdraw_xp)

                        with open("./local/chest.json", "w") as f:
                            json.dump(chest, f, indent=4)

                        with open(guildid, "w") as f:
                            json.dump(users, f, indent=4)

                        await ctx.reply(f"`{withdraw_xp} XP` **has been withdrawn from your chest!**")

                elif chest_id not in user_data:
                    await ctx.reply("**Whoops. Looks like you don't own a chest with that ID**")

                else:
                    await ctx.reply("**Whoops. Looks like you don't own a chest with that ID**")

    @chest.command()
    async def upgrade(self, ctx, chest_id: str = None):
        user_id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(user_id)]['color']

        user_xp = users[str(user_id)]['experience']

        chest_id = str(chest_id)

        with open("./local/chest.json", "r") as f:
            chest = json.load(f)

        if chest_id == None:
            embed = discord.Embed(
                description=f"**Description** : Chests are used to store XP and keep it safe.\n\n**Usage**: `{ctx.prefix}chest upgrade <chest id>`\n**Example**: `{ctx.prefix}chest upgrade 1234` to upgrade a Chest with ID - 1234\n\n**Note**: To check your chest IDs, use command `=inv`",
                color=color,
                timestamp=datetime.datetime.utcnow()
            )

            embed.set_author(name="Chest Upgrade Help ❓")
            await ctx.send(embed=embed)

        elif str(user_id) not in chest:
            await ctx.reply("**Whoops. Looks like you don't own a chest**")

        elif str(user_id) in chest:
            user_data = chest[str(user_id)]
            user_data = list(user_data)

            if len(user_data) == 0:
                await ctx.reply("**Whoops. Looks like you don't own a chest**")

            elif len(user_data) >= 1:
                if chest_id in user_data:
                    chest_level = chest[str(user_id)][str(chest_id)]["level"]

                    if chest_level == 1:

                        if user_xp >= 50000:
                            users[str(user_id)]['experience'] = user_xp - 50000
                            user_xp = users[str(user_id)]['experience']
                            lvl = int(user_xp ** (1/4))
                            users[str(user_id)]['level'] = lvl
                            chest[str(user_id)][str(chest_id)]["level"] = 2

                            with open("./local/chest.json", "w") as f:
                                json.dump(chest, f, indent=4)

                            with open(guildid, "w") as f:
                                json.dump(users, f, indent=4)

                            await ctx.reply(f"**Chest upgraded to Level 2.** `50,000 XP` **has been deducted**")

                        elif 50000 > user_xp:
                            await ctx.reply("**Insufficient Funds. You don't have 50,000 XP**")

                    elif chest_level == 2:

                        if user_xp >= 75000:
                            users[str(user_id)]['experience'] = user_xp - 75000
                            user_xp = users[str(user_id)]['experience']
                            lvl = int(user_xp ** (1/4))
                            users[str(user_id)]['level'] = lvl
                            chest[str(user_id)][str(chest_id)]["level"] = 3

                            with open("./local/chest.json", "w") as f:
                                json.dump(chest, f, indent=4)

                            with open(guildid, "w") as f:
                                json.dump(users, f, indent=4)

                            await ctx.send(f"**Chest upgraded to Level 3.** `75,000 XP` **has been deducted**")

                        elif 75000 > user_xp:
                            await ctx.send("**Insufficient Funds. You don't have 75,000 XP**")

                    elif chest_level == 3:

                        if user_xp >= 100000:
                            users[str(user_id)]['experience'] = user_xp - 100000
                            user_xp = users[str(user_id)]['experience']
                            lvl = int(user_xp ** (1/4))
                            users[str(user_id)]['level'] = lvl
                            chest[str(user_id)][str(chest_id)]["level"] = 4

                            with open("./local/chest.json", "w") as f:
                                json.dump(chest, f, indent=4)

                            with open(guildid, "w") as f:
                                json.dump(users, f, indent=4)

                            await ctx.send(f"**Chest upgraded to Level 4.** `100,000 XP` **has been deducted**")

                        elif 100000 > user_xp:
                            await ctx.send("**Insufficient Funds. You don't have 100,000 XP**")

                    elif chest_level == 4:

                        if user_xp >= 250000:
                            users[str(user_id)]['experience'] = user_xp - 250000
                            user_xp = users[str(user_id)]['experience']
                            lvl = int(user_xp ** (1/4))
                            users[str(user_id)]['level'] = lvl
                            chest[str(user_id)][str(chest_id)]["level"] = 5

                            with open("./local/chest.json", "w") as f:
                                json.dump(chest, f, indent=4)

                            with open(guildid, "w") as f:
                                json.dump(users, f, indent=4)

                            await ctx.send(f"**Chest upgraded to Level 5.** `250,000 XP` **has been deducted**")

                        elif 250000 > user_xp:
                            await ctx.send("**Insufficient Funds. You don't have 250,000 XP**")

                    elif chest_level == 5:

                        if user_xp >= 500000:
                            users[str(user_id)]['experience'] = user_xp - 500000
                            user_xp = users[str(user_id)]['experience']
                            lvl = int(user_xp ** (1/4))
                            users[str(user_id)]['level'] = lvl
                            chest[str(user_id)][str(chest_id)]["level"] = 6

                            with open("./local/chest.json", "w") as f:
                                json.dump(chest, f, indent=4)

                            with open(guildid, "w") as f:
                                json.dump(users, f, indent=4)

                            await ctx.send(f"**Chest upgraded to Level 6.** `500,000 XP` **has been deducted**")

                        elif 500000 > user_xp:
                            await ctx.send("**Insufficient Funds. You don't have 500,000 XP**")

                    elif chest_level == 6:
                        await ctx.send(f"**Chest maxed out! This chest is at** `Level 6`")

                elif chest_id not in user_data:
                    await ctx.send("**Whoops. Looks like you don't own a chest with that ID**")

                else:
                    await ctx.send("**Whoops. Looks like you don't own a chest with that ID**")

    '''    
    @chest.command()
    async def gift(self, ctx, chest_id : str = None):
        pass
    '''


async def setup(bot):
    await bot.add_cog(ItemCog(bot))
