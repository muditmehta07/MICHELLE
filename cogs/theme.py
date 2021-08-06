'''

Theme

'''


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
    
    @commands.command()
    async def light(self, message):
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

        embed = discord.Embed(title = "LIGHT THEMES 🎡", description = f" ❤️ **Red** : `{get_prefix}red`\n💙 **Blue** : `{get_prefix}blue`\n💚 **Green** : `{get_prefix}green`\n💜 **Purple** : `{get_prefix}purple`\n🧡 **Orange** : `{get_prefix}orange`\n💙 **Teal** : `{get_prefix}teal`\n❤️ **Magenta** : `{get_prefix}magenta`\n💛 **Gold** : `{get_prefix}gold`", color = color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        await message.channel.send(embed = embed)

    @commands.command(name = "gold", aliases = ["Gold", "GOLD", "yellow", "YELLOW", "Yellow"])
    async def gold(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl)>=5:
            users[str(id)]['color'] = 15844367

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'{message.author.mention}, your theme has been updated to `Gold` '
            level_embed = discord.Embed(title = "Theme Updated 😄", description = m, color = 15844367, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

        else:
            m = f'{message.author.mention} Level required to use this command : `5`'
            c = users[str(id)]['color']
            level_embed = discord.Embed(title = "Sorry ☹️", description = m, color = c, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

    @commands.command(name = "magenta", aliases = ["Pink", "PINK", "pink", "MAGENTA", "Magenta"])
    async def magenta(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl)>=5:
            users[str(id)]['color'] = 15277667

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'{message.author.mention}, your theme has been updated to `Magenta` '
            level_embed = discord.Embed(title = "Theme Updated 😄", description = m, color = 15277667, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

        else:
            m = f'{message.author.mention} Level required to use this command : `5`'
            c = users[str(id)]['color']
            level_embed = discord.Embed(title = "Sorry ☹️", description = m, color = c, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

    @commands.command(name = "teal", aliases = ["Teal", "TEAL", "cyan", "Cyan", "CYAN"])
    async def teal(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl)>=5:
            users[str(id)]['color'] = 1752220

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'{message.author.mention}, your theme has been updated to `Teal` '
            level_embed = discord.Embed(title = "Theme Updated 😄", description = m, color = 1752220, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

        else:
            m = f'{message.author.mention} Level required to use this command : `5`'
            c = users[str(id)]['color']
            level_embed = discord.Embed(title = "Sorry ☹️", description = m, color = c, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

    @commands.command(name = "orange", aliases = ["Orange", "ORANGE"])
    async def orange(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl)>=5:
            users[str(id)]['color'] = 15105570

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'{message.author.mention}, your theme has been updated to `Orange` '
            level_embed = discord.Embed(title = "Theme Updated 😄", description = m, color = 15105570, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

        else:
            m = f'{message.author.mention} Level required to use this command : `5`'
            c = users[str(id)]['color']
            level_embed = discord.Embed(title = "Sorry ☹️", description = m, color = c, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

    @commands.command(name = "red", aliases = ["Red", "RED"])
    async def red(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl)>=5:
            users[str(id)]['color'] = 15158332

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'{message.author.mention}, your theme has been updated to `Red` '
            level_embed = discord.Embed(title = "Theme Updated 😄", description = m, color = 15158332, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

        else:
            m = f'{message.author.mention} Level required to use this command : `5`'
            c = users[str(id)]['color']
            level_embed = discord.Embed(title = "Sorry ☹️", description = m, color = c, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

    @commands.command(name = "blue", aliases = ["Blue", "BLUE", "blu", "Blu", "BLU"])
    async def blue(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl)>=5:
            users[str(id)]['color'] = 3447003

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'{message.author.mention}, your theme has been updated to `Blue` '
            level_embed = discord.Embed(title = "Theme Updated 😄", description = m, color = 3447003, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

        else:
            m = f'{message.author.mention} Level required to use this command : `5`'
            c = users[str(id)]['color']
            level_embed = discord.Embed(title = "Sorry ☹️", description = m, color = c, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

    @commands.command(name = "green", aliases = ["Green", "GREEN", "hulk", "HULK", "Hulk"])
    async def green(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl)>=5:
            users[str(id)]['color'] = 3066993

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'{message.author.mention}, your theme has been updated to `Green` '
            level_embed = discord.Embed(title = "Theme Updated 😄", description = m, color = 3066993, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

        else:
            m = f'{message.author.mention} Level required to use this command : `5`'
            c = users[str(id)]['color']
            level_embed = discord.Embed(title = "Sorry ☹️", description = m, color = c, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

    @commands.command(name = "purple", aliases = ["Purple", "PURPLE"])
    async def purple(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl)>=5:
            users[str(id)]['color'] = 10181046

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'{message.author.mention}, your theme has been updated to `Purple` '
            level_embed = discord.Embed(title = "Theme Updated 😄", description = m, color = 10181046, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

        else:
            m = f'{message.author.mention} Level required to use this command : `5`'
            c = users[str(id)]['color']
            level_embed = discord.Embed(title = "Sorry ☹️", description = m, color = c, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

    @commands.command()
    async def dark(self, message):
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

        embed = discord.Embed(title = "DARK THEMES 🎡", description = f" ❤️ **Dark Red** : `{get_prefix}dred`\n💙 **Dark Blue** : `{get_prefix}dblue`\n💚 **Dark Green** : `{get_prefix}dgreen`\n💜 **Dark Purple** : `{get_prefix}dpurple`\n🧡 **Dark Orange** : `{get_prefix}dorange`\n💙 **Dark Teal** : `{get_prefix}dteal`\n❤️ **Dark Magenta** : `{get_prefix}dmagenta`\n💛 **Dark Gold** : `{get_prefix}dgold`", color = color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        await message.channel.send(embed=embed)

    @commands.command()
    async def dgold(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl)>=5:
            users[str(id)]['color'] = 12745742

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'{message.author.mention}, your theme has been updated to `Dark Gold`'
            level_embed = discord.Embed(title = "Theme Updated 😄", description = m, color = 12745742, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

    @commands.command()
    async def dmagenta(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl)>=5:
            users[str(id)]['color'] = 11342935

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'{message.author.mention}, your theme has been updated to `Dark Magenta`'
            level_embed = discord.Embed(title = "Theme Updated 😄", description = m, color = 11342935, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

    @commands.command()
    async def dteal(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl)>=5:
            users[str(id)]['color'] = 1146986

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'{message.author.mention}, your theme has been updated to `Dark Teal`'
            level_embed = discord.Embed(title = "Theme Updated 😄", description = m, color = 1146986, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

    @commands.command()
    async def dorange(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl)>=5:
            users[str(id)]['color'] = 11027200

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'{message.author.mention}, your theme has been updated to `Dark Orange`'
            level_embed = discord.Embed(title = "Theme Updated 😄", description = m, color = 11027200, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

    @commands.command()
    async def dpurple(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl)>=5:
            users[str(id)]['color'] = 7419530

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'{message.author.mention}, your theme has been updated to `Dark Purple`'
            level_embed = discord.Embed(title = "Theme Updated 😄", description = m, color = 7419530, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

    @commands.command()
    async def dgreen(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl)>=5:
            users[str(id)]['color'] = 2067276

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'{message.author.mention}, your theme has been updated to `Dark Green`'
            level_embed = discord.Embed(title = "Theme Updated 😄", description = m, color = 2067276, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

    @commands.command()
    async def dblue(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl)>=5:
            users[str(id)]['color'] = 2123412

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'{message.author.mention}, your theme has been updated to `Dark Blue`'
            level_embed = discord.Embed(title = "Theme Updated 😄", description = m, color = 2123412, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

    @commands.command()
    async def dred(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']

        if int(lvl)>=5:
            users[str(id)]['color'] = 10038562

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)

            m = f'{message.author.mention}, your theme has been updated to `Dark Red` '
            level_embed = discord.Embed(title = "Theme Updated 😄", description = m, color = 10038562, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

        else:
            m = f'{message.author.mention} Level required to use this command : `5`'
            c = users[str(id)]['color']
            level_embed = discord.Embed(title = "Sorry ☹️", description = m, color = c, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)


def setup(bot):
    bot.add_cog(ThemeCog(bot))
