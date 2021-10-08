import discord
from discord.ext import commands
import os, pickle
import random
import datetime
import json
from discord.ext.commands import cooldowns

from discord.ext.commands.context import Context
from discord.ext.commands.core import command
from discord.flags import alias_flag_value

class ItemCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def convert(self, n):
        avg = str(datetime.timedelta(seconds = n))
        avgString = str(avg).split(".")[0]

        return avgString
    
    @commands.group(invoke_without_command=True)
    async def item(self, message):
        S = []
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
        else:
            get_prefix = "="

        for i in users[str(id)]:
            if users[str(id)][i] == True:
                S.append(i)

        if "sage_spell" in S:
            spell = "Sage"

        elif "hunter_spell" in S:
            spell = "Hunter"

        else:
            spell = "No Spell"

        if "chameleon" in S:
            jutsu = "Chameleon"

        elif "transformation" in S:
            jutsu = "Transformation"

        else:
            jutsu = "No Justu"

        ability = "No Ability"
        
        embed = discord.Embed(color = color, timestamp=datetime.datetime.utcnow())

        embed.set_author(name = "Inventory", icon_url = "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
        embed.add_field(name = "🦸🏻 Ability", value = f"`{ability}`")
        embed.add_field(name = "🧙🏻‍♂️ Spell", value = f"`{spell}`")
        embed.add_field(name = "🥷🏻 Jutsu", value = f"`{jutsu}`")
        embed.add_field(name = "⚔️ Weapons", value = f"`{get_prefix}weapons`")
        embed.add_field(name = "🎁 Gift Box", value = f"`{get_prefix}item giftbox`")
        embed.add_field(name = "🏆 Daily", value = f"`{get_prefix}daily`")
        await message.channel.send(embed = embed)

    @item.command()
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
        description= f"**Chameleon Jutsu** 😶  `{get_prefix}help chameleon`\nA Ninjutsu to hide yourself\n\n**Transformation Jutsu** 🥸  `{get_prefix}help transform`\nA Ninjutsu to transform yourself",
        color = color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name = "Jutsu 🥷🏻", icon_url = "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
        await message.channel.send(embed = embed)

    @item.command(aliases = ["spell"])
    async def spells(self, message):
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
        description=f"**Sage Spell** ✨  `{get_prefix}help sage`\nBecome an immortal and support your peers\n\n**Hunter Spell** 🏹  `{get_prefix}help hunter`\nBecome a predator that hunts the weak\n\n**Wraith Spell** 👻  `SOLD OUT`\nBecome a phantom that lives in the shadows",
        color = color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name = "Spells 🧙🏻‍♂️", icon_url = "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
        await message.channel.send(embed = embed)

    @item.command()
    async def ability(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        embed = discord.Embed(description = "**Abilities Coming Soon!**",
        color = color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name = "Ability 🦸🏻", icon_url = "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
        await message.channel.send(embed = embed)

    @item.command()
    async def giftbox(self, ctx):
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/items.json", "r") as g:
            auth = json.load(g)

        if not str(ctx.author.id) in auth:

            embed = discord.Embed(description = "You own **0** Gift Boxes\n[Invite Me](https://discordapp.com/oauth2/authorize?client_id=840180379389263882&scope=bot&permissions=4228906231) to recieve one!",
            color = color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name = "Gift Box 🎁", icon_url = "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
            await ctx.send(embed = embed)

        elif str(ctx.author.id) in auth:

            item_list = auth[f"{ctx.author.id}"]["items"]

            count = 0
            for i in item_list:
                if i == "gift_box":
                    count +=1

            if count == 0:
                embed = discord.Embed(description = "You own **0** Gift Boxes\n[Invite Me](https://discordapp.com/oauth2/authorize?client_id=840180379389263882&scope=bot&permissions=4228906231) to recieve one!",
                color = color, timestamp=datetime.datetime.utcnow())
                embed.set_author(name = "Gift Box 🎁", icon_url = "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
                await ctx.send(embed = embed)

            elif count>0:
                item_list.remove("gift_box")
                auth[f"{ctx.author.id}"]["items"] = item_list

                with open("./local/items.json", "w") as g:
                    json.dump(auth, g, indent=4)

                xp = users[str(id)]['experience']
                xp += 1000000
                users[str(id)]['experience'] = int(xp)
                lvl = int(xp ** (1/4))
                users[str(id)]['level'] = lvl

                with open(guildid, 'w') as f:
                    json.dump(users, f, indent=4)

                embed = discord.Embed(description = f"You found **1 Million XP** in the Gift Box\n**{count-1}** Gift Boxes Left",
                color = color, timestamp=datetime.datetime.utcnow())
                embed.set_author(name = "Gift Box 🎁", icon_url = "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
                await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.member)
    async def daily(self, ctx):
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']
        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']

        daily = random.randint(100, 8000)
        daily = daily*5
        xp += daily
        users[str(id)]['experience'] = int(xp)
        lvl = int(xp ** (1/4))
        users[str(id)]['level'] = lvl

        with open(guildid, 'w') as f:
            json.dump(users, f, indent=4)

        if daily < 1000:
            msg = "Sheesh, even your bad luck is rotten"
        elif daily >=1001 and daily <=15000:
            msg = "Eh, not bad mate"
        elif daily>=15001 and daily <=30000:
            msg = "Good job!"
        elif daily>=30001 and daily <=50000:
            msg = "JACKPOT!!! YOU ARE INSANE!"
        else:
            msg = "Hmm, okay"

        embed = discord.Embed(description = f"**Recieved {daily} XP**\n{msg}", color=color, timestamp = datetime.datetime.utcnow())
        embed.set_author(name="Daily Rewards 🏆", icon_url="https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")

        await ctx.send(embed=embed)

    @daily.error
    async def daily_error(self, ctx, error):

        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = error.retry_after

            embed = discord.Embed(description = f"**You already claimed your daily**\nCome back in `{ItemCog.convert(self, remaining_time)}`", color=color, timestamp = datetime.datetime.utcnow())
            embed.set_author(name="Daily Rewards 🏆", icon_url="https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ItemCog(bot))