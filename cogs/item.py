import discord
from discord.ext import commands
import os
import datetime
import json

from discord.ext.commands.context import Context

class ItemCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(invoke_without_command=True)
    async def item(self, message):
        S = []
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)
        
        color = users[str(id)]['color']

        for i in users[str(id)]:
            if users[str(id)][i] == True:
                S.append(i)

        if "sage_spell" in S:
            spell = "Sage"
        elif "hunter_spell" in S:
            spell = "Hunter"
        else:
            spell = "Any spell you purchase will be displayed here"

        if "chameleon" in S:
            jutsu = "Chameleon"
        elif "transformation" in S:
            jutsu = "Transformation"
        else:
            jutsu = "Any jutsu you purchase will be displayed here"

        ability = "Any ability you purchase will be displayed here"
        
        embed = discord.Embed(title = f"*Inventory* 🛒", description= f"**Ability**🦸🏻 - *{ability}*\n**Spell**🧙🏻‍♂️ - *{spell}*\n**Jutsu**🥷🏻 - *{jutsu}*" , color = color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
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

        embed = discord.Embed(title = "Jutsu 🥷🏻",
        description= "*Chameleon Jutsu* 😶 *Cost* : `10,000 XP`\n*A ninjutsu to hide your name from the leaderboard*\n\n*Transformation Jutsu* 🥸 *Cost* : `12,000 XP`\n*A ninjutsu to replace your name with a text on the leaderboard*",
        color = color, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text = f"Buy : {get_prefix}buy justu   Note : A jutsu is forgotten when another jutsu is trained")
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        await message.channel.send(embed = embed)

    @item.command()
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

        embed = discord.Embed(title = "Spells 🧙🏻‍♂️",
        description="*Sage Spell* ✨ *Cost* : `50,000 XP`\n*Become an immortal and support your peers*\n\n*Hunter Spell* 🏹 *Cost* : `20,000 XP`\n*Become a predator that hunts the weak*\n\n*Wraith Spell* 👻 *Cost* : `70,000 XP`\n*Become a phantom that lives in the shadows*",
        color = color, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text = f"Buy : {get_prefix}buy spell  Note : A spell fades when another spell is brewed")

        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        await message.channel.send(embed = embed)

    @item.command()
    async def ability(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        embed = discord.Embed(color = color, timestamp=datetime.datetime.utcnow())
        embed.add_field(name = "`coming soon`  [Cost : 10 Levels]", value = "`???`", inline = False)
        embed.set_footer(text = "Note : An ability gets locked when another ability is unlocked!")

        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        await message.channel.send(embed = embed)

def setup(bot):
    bot.add_cog(ItemCog(bot))