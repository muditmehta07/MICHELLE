'''

Setup

'''

import discord
from discord.ext import commands
import os
import datetime
import json
from discord import message
from discord.ext.commands.context import Context

class SetupCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def prefix(self, message, pref : str = None):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as g:
            L = json.load(g)

        if pref == None:
            msg = "Server Prefix has not been changed since no prefix was provided."
        
        else:
            if message.channel.guild.id not in L:
                L[str(message.channel.guild.id)] = {}
                L[str(message.channel.guild.id)]["name"] = message.channel.guild.name
                L[str(message.channel.guild.id)]["prefix"] = f"{pref}"
                msg = f"Server Prefix has been updated to `{pref}`"

                with open("./local/prefix.json", "w") as h:
                    json.dump(L, h, indent=4)

            elif message.channel.guild.id in L:

                L[str(message.channel.guild.id)]["prefix"] = pref
                msg = f"Server Prefix has been updated to `{pref}`"

                with open("./local/prefix.json", 'w') as g:
                    json.dump(L, g, indent=4)

        embed = discord.Embed(
            description = msg,
            color = color,
            timestamp = datetime.datetime.utcnow()
        )

        embed.set_author(name = message.author, icon_url = message.author.avatar_url)

        await message.channel.send(embed=embed)


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        mstat = f'{str(len(self.bot.guilds))} servers | =help'
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=mstat))

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

            if guild.id not in L:
                L[str(guild.id)] = {}
                L[str(guild.id)]["name"] = guild.name
                L[str(guild.id)]["prefix"] = "="

        with open("./local/prefix.json", "w") as f:
            json.dump(L, f, indent=4)


    @commands.Cog.listener()
    async def on_guild_remove(self, guild):

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

            if guild.id not in L:
                L.pop(L[str(guild.id)])

        with open("./local/prefix.json", "w") as f:
            json.dump(L, f, indent=4)

        mstat = f'{str(len(self.bot.guilds))} servers | =help'
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=mstat))

def setup(bot):
    bot.add_cog(SetupCog(bot))
