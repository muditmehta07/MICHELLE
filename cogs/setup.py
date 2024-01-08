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

            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(message.guild.id) in L:
                get_prefix = L[str(message.guild.id)]["prefix"]
            elif str(message.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Permissions** : Administartor\n\n**Description** : Change current server's command prefix\n\n**Usage** : `{get_prefix}prefix <new_prefix>`\n**Example** : `{get_prefix}prefix !`\n\n**Note** : Prefix cannot be more than 5 letters, @ and # signs cannot be used in the prefix" , 
                color = color, 
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Prefix Help ❓", icon_url=self.bot.user.avatar_url)
            await message.channel.send(embed = embed)
        
        else:
            count = 0
            for i in pref:
                count +=1

            if count>5:
                await message.channel.send("**Prefix cannot be more than 5 letters**")

            elif "@" in pref or "#" in pref:
                await message.channel.send("**Prefix cannot contain @ and # sign**")

            else:
                if message.channel.guild.id not in L:
                    L[str(message.channel.guild.id)] = {}
                    L[str(message.channel.guild.id)]["name"] = message.channel.guild.name
                    L[str(message.channel.guild.id)]["prefix"] = f"{pref}"
                    msg = f"Server Prefix has been updated to `{pref}`"

                    with open("./local/prefix.json", "w") as h:
                        json.dump(L, h, indent=4)

                    embed = discord.Embed(
                        description = msg,
                        color = color,
                        timestamp = datetime.datetime.utcnow()
                    )

                    embed.set_author(name = message.author.name, icon_url = message.author.avatar_url)

                    await message.channel.send(embed=embed)

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

                    embed.set_author(name = message.author.name, icon_url = message.author.avatar_url)

                    await message.channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(SetupCog(bot))