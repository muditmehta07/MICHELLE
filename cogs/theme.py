import discord
from discord.ext import commands
import os
from discord import message
from discord.ext.commands.core import command
from discord.message import Message
import datetime
import json

from discord.ext.commands.context import Context
from discord.ext.commands.help import HelpCommand


class ThemeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="grey", aliases=["gray", "Gray", "Grey", "GRAY", "GREY"])
    async def grey(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        users[str(id)]['color'] = 0x95a5a6

        with open(guildid, 'w') as f:
            json.dump(users, f, indent=4)

        description = f'**Your theme has been updated to** `Default Grey`\n\n← This color will reflect on this sidebar, your Level Card and the top 5 Leaderboard'
        level_embed = discord.Embed(
            description=description, color=0x95a5a6, timestamp=datetime.datetime.utcnow())
        level_embed.set_author(name=message.author.name,
                               icon_url=message.author.avatar.url)
        await message.channel.send(embed=level_embed)

    @commands.command(name="gold", aliases=["Gold", "GOLD", "yellow", "YELLOW", "Yellow"])
    async def gold(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl) >= 5:
            users[str(id)]['color'] = 15844367

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'**Your theme has been updated to** `Gold`\n\n← This color will reflect on this sidebar, your Level Card and the top 5 Leaderboard'
            level_embed = discord.Embed(
                description=m, color=15844367, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(
                name=message.author.name, icon_url=message.author.avatar.url)
            await message.channel.send(embed=level_embed)

        else:
            m = f'**Your level seems to be too low**\nLevel required to use this command : `5`'
            c = users[str(id)]['color']
            level_embed = discord.Embed(
                description=m, color=c, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(
                name=message.author.name, icon_url=message.author.avatar.url)
            await message.channel.send(embed=level_embed)

    @commands.command(name="magenta", aliases=["Pink", "PINK", "pink", "MAGENTA", "Magenta"])
    async def magenta(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl) >= 5:
            users[str(id)]['color'] = 15277667

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'**Your theme has been updated to** `Magenta`\n\n← This color will reflect on this sidebar, your Level Card and the top 5 Leaderboard'
            level_embed = discord.Embed(
                description=m, color=15277667, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(
                name=message.author.name, icon_url=message.author.avatar.url)
            await message.channel.send(embed=level_embed)

        else:
            m = f'**Your level seems to be too low**\nLevel required to use this command : `5`'
            c = users[str(id)]['color']
            level_embed = discord.Embed(
                description=m, color=c, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(
                name=message.author.name, icon_url=message.author.avatar.url)
            await message.channel.send(embed=level_embed)

    @commands.command(name="teal", aliases=["Teal", "TEAL", "cyan", "Cyan", "CYAN"])
    async def teal(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl) >= 5:
            users[str(id)]['color'] = 1752220

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'**Your theme has been updated to** `Teal`\n\n← This color will reflect on this sidebar, your Level Card and the top 5 Leaderboard'
            level_embed = discord.Embed(
                description=m, color=1752220, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(
                name=message.author.name, icon_url=message.author.avatar.url)
            await message.channel.send(embed=level_embed)

        else:
            m = f'**Your level seems to be too low**\nLevel required to use this command : `5`'
            c = users[str(id)]['color']
            level_embed = discord.Embed(
                description=m, color=c, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(
                name=message.author.name, icon_url=message.author.avatar.url)
            await message.channel.send(embed=level_embed)

    @commands.command(name="orange", aliases=["Orange", "ORANGE"])
    async def orange(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl) >= 5:
            users[str(id)]['color'] = 15105570

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'**Your theme has been updated to** `Orange`\n\n← This color will reflect on this sidebar, your Level Card and the top 5 Leaderboard'
            level_embed = discord.Embed(
                description=m, color=15105570, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(
                name=message.author.name, icon_url=message.author.avatar.url)
            await message.channel.send(embed=level_embed)

        else:
            m = f'**Your level seems to be too low**\nLevel required to use this command : `5`'
            c = users[str(id)]['color']
            level_embed = discord.Embed(
                description=m, color=c, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(
                name=message.author.name, icon_url=message.author.avatar.url)
            await message.channel.send(embed=level_embed)

    @commands.command(name="red", aliases=["Red", "RED"])
    async def red(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl) >= 5:
            users[str(id)]['color'] = 15158332

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'**Your theme has been updated to** `Red`\n\n← This color will reflect on this sidebar, your Level Card and the top 5 Leaderboard'
            level_embed = discord.Embed(
                description=m, color=15158332, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(
                name=message.author.name, icon_url=message.author.avatar.url)
            await message.channel.send(embed=level_embed)

        else:
            m = f'**Your level seems to be too low**\nLevel required to use this command : `5`'
            c = users[str(id)]['color']
            level_embed = discord.Embed(
                description=m, color=c, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(
                name=message.author.name, icon_url=message.author.avatar.url)
            await message.channel.send(embed=level_embed)

    @commands.command(name="blue", aliases=["Blue", "BLUE", "blu", "Blu", "BLU"])
    async def blue(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl) >= 5:
            users[str(id)]['color'] = 3447003

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'**Your theme has been updated to** `Blue`\n\n← This color will reflect on this sidebar, your Level Card and the top 5 Leaderboard'
            level_embed = discord.Embed(
                description=m, color=3447003, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(
                name=message.author.name, icon_url=message.author.avatar.url)
            await message.channel.send(embed=level_embed)

        else:
            m = f'**Your level seems to be too low**\nLevel required to use this command : `5`'
            c = users[str(id)]['color']
            level_embed = discord.Embed(
                description=m, color=c, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(
                name=message.author.name, icon_url=message.author.avatar.url)
            await message.channel.send(embed=level_embed)

    @commands.command(name="green", aliases=["Green", "GREEN", "hulk", "HULK", "Hulk"])
    async def green(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl) >= 5:
            users[str(id)]['color'] = 3066993

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'**Your theme has been updated to** `Green`\n\n← This color will reflect on this sidebar, your Level Card and the top 5 Leaderboard'
            level_embed = discord.Embed(
                description=m, color=3066993, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(
                name=message.author.name, icon_url=message.author.avatar.url)
            await message.channel.send(embed=level_embed)

        else:
            m = f'**Your level seems to be too low**\nLevel required to use this command : `5`'
            c = users[str(id)]['color']
            level_embed = discord.Embed(
                description=m, color=c, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(
                name=message.author.name, icon_url=message.author.avatar.url)
            await message.channel.send(embed=level_embed)

    @commands.command(name="purple", aliases=["Purple", "PURPLE"])
    async def purple(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl) >= 5:
            users[str(id)]['color'] = 10181046

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'**Your theme has been updated to** `Purple`\n\n← This color will reflect on this sidebar, your Level Card and the top 5 Leaderboard'
            level_embed = discord.Embed(
                description=m, color=10181046, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(
                name=message.author.name, icon_url=message.author.avatar.url)
            await message.channel.send(embed=level_embed)

        else:
            m = f'**Your level seems to be too low**\nLevel required to use this command : `5`'
            c = users[str(id)]['color']
            level_embed = discord.Embed(
                description=m, color=c, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(
                name=message.author.name, icon_url=message.author.avatar.url)
            await message.channel.send(embed=level_embed)


async def setup(bot):
    await bot.add_cog(ThemeCog(bot))
