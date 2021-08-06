'''

Fun

'''

import discord
from discord.ext import commands
import os
import random
import datetime
import json
from discord import message
from discord.ext.commands.context import Context
from PIL import Image, ImageDraw, ImageFont
from discord.ext.commands.core import command

wom = ["with a pair of dirty flip flops.", "with a rusted knife.", "by feeding them cat biscuits.", "by hitting them with rotten eggs.", "with a lame joke.", "by tossing a rubbed duckie at them.", "with a glitchy boombot.", "by stabbing them with a banana.", "with smelly feet.", "with their dandruff."]
reason = [". What a noob", "because they slipped on a banana.", "because they fell asleep.", "because they were arrested for tax fraud.", "because of excessive sweating.", "because of constipation.", "because of low brain cells."]

class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def monster(self, ctx):
        id = ctx.author.id
        await ctx.message.author.avatar_url.save((f"{id}avatar.jpg"))
        background = Image.open("./meme/monster.png").convert("RGB").resize((800, 500))
        draw = ImageDraw.Draw(background, "RGB")

        try:
            logo = Image.open(f"{id}avatar.jpg").convert("RGB").resize((180, 180))
        except:
            logo = Image.open("./pictures/discord.png").convert("RGB").resize((180, 180))

        bigsize = (logo.size[0] * 3, logo.size[1] * 3)
        mask = Image.new("L", bigsize, 0)

        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, 255)

        draw.ellipse((140 * 3, 140 * 3, 140 * 3, 140 * 3), 0)

        mask = mask.resize(logo.size, Image.ANTIALIAS)
        logo.putalpha(mask)

        background.paste(logo, (320, 10), mask=logo)

        draw = ImageDraw.Draw(background, "RGB")

        background.save(f"{id}monster.jpg", quality = 100)

        embed = discord.Embed(
            title = f'You probably are, lol',
            timestamp = datetime.datetime.utcnow()
        )

        file = discord.File(f"{id}monster.jpg")
        embed.set_author(name = f'{ctx.author}', icon_url=f"{ctx.author.avatar_url}")
        embed.set_image(url = f"attachment://{id}monster.jpg")

        await ctx.send(file=file,embed=embed)
        os.remove(f"./{id}monster.jpg")
        os.remove(f"{id}avatar.jpg")

    @commands.command()
    async def hug(self, ctx, member : discord.Member):
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = './guild data/'+ str(guildid) +'.json'
        with open(guild, 'r') as g:
            users = json.load(g)

        color = users[str(id)]['color']

        memid = member.id
        user = await ctx.message.author.avatar_url.save((f"{id}avatar.jpg"))
        mem = await member.avatar_url.save((f"{memid}avatar.png"))
        background = Image.open("./meme/hug.png").convert("RGB").resize((800, 500))
        draw = ImageDraw.Draw(background, "RGB")

        try:
            logo = Image.open(f"{id}avatar.jpg").convert("RGB").resize((180, 180))
        except:
            logo = Image.open("./pictures/discord.png").convert("RGB").resize((180, 180))

        try:
            logo2 = Image.open(f"{memid}avatar.png").convert("RGB").resize((180, 180))
        except:
            logo2 = Image.open("./pictures/discord.png").convert("RGB").resize((180, 180))

        #User

        bigsize = (logo.size[0] * 3, logo.size[1] * 3)
        mask = Image.new("L", bigsize, 0)

        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, 255)

        draw.ellipse((140 * 3, 140 * 3, 140 * 3, 140 * 3), 0)

        mask = mask.resize(logo.size, Image.ANTIALIAS)
        logo.putalpha(mask)

        background.paste(logo, (400, 180), mask=logo)

        draw = ImageDraw.Draw(background, "RGB")

        #Member

        bigsize = (logo2.size[0] * 3, logo2.size[1] * 3)
        mask = Image.new("L", bigsize, 0)

        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, 255)

        draw.ellipse((140 * 3, 140 * 3, 140 * 3, 140 * 3), 0)

        mask = mask.resize(logo2.size, Image.ANTIALIAS)
        logo2.putalpha(mask)

        background.paste(logo2, (200, 140), mask=logo2)

        draw = ImageDraw.Draw(background, "RGB")

        background.save(f"{id}hug.jpg", quality = 100)

        if member == ctx.author:
            name = f"{ctx.author.display_name} hugged themself. What a narcissist!"
        else:
            name = f'{ctx.author.display_name} hugged {member.display_name}'

        embed = discord.Embed(
            title = f'{name}',
            color=color,
            timestamp = datetime.datetime.utcnow()
        )

        file = discord.File(f"{id}hug.jpg")
        embed.set_author(name = f'{ctx.author}', icon_url=f"{ctx.author.avatar_url}")
        embed.set_image(url = f"attachment://{id}hug.jpg")

        await ctx.send(file=file,embed=embed)
        os.remove(f"./{memid}avatar.png")
        os.remove(f"./{id}hug.jpg")
        os.remove(f"{id}avatar.jpg")

    @commands.command()
    async def kiss(self, ctx, member : discord.Member):
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = './guild data/'+ str(guildid) +'.json'
        with open(guild, 'r') as g:
            users = json.load(g)

        color = users[str(id)]['color']

        memid = member.id
        user = await ctx.message.author.avatar_url.save((f"{id}avatar.jpg"))
        mem = await member.avatar_url.save((f"{memid}avatar.png"))
        background = Image.open("./meme/kiss.jpg").convert("RGB").resize((800, 500))
        draw = ImageDraw.Draw(background, "RGB")

        try:
            logo = Image.open(f"{id}avatar.jpg").convert("RGB").resize((180, 180))
        except:
            logo = Image.open("./pictures/discord.png").convert("RGB").resize((180, 180))

        try:
            logo2 = Image.open(f"{memid}avatar.png").convert("RGB").resize((180, 180))
        except:
            logo2 = Image.open("./pictures/discord.png").convert("RGB").resize((180, 180))

        #User

        bigsize = (logo.size[0] * 3, logo.size[1] * 3)
        mask = Image.new("L", bigsize, 0)

        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, 255)

        draw.ellipse((140 * 3, 140 * 3, 140 * 3, 140 * 3), 0)

        mask = mask.resize(logo.size, Image.ANTIALIAS)
        logo.putalpha(mask)

        background.paste(logo, (200, 80), mask=logo)

        draw = ImageDraw.Draw(background, "RGB")

        #Member

        bigsize = (logo2.size[0] * 3, logo2.size[1] * 3)
        mask = Image.new("L", bigsize, 0)

        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, 255)

        draw.ellipse((140 * 3, 140 * 3, 140 * 3, 140 * 3), 0)

        mask = mask.resize(logo2.size, Image.ANTIALIAS)
        logo2.putalpha(mask)

        background.paste(logo2, (400, 40), mask=logo2)

        draw = ImageDraw.Draw(background, "RGB")

        background.save(f"{id}kiss.jpg", quality = 100)

        if member == ctx.author:
            name = f"{ctx.author.display_name} kissed themself. What a narcissist!"
        else:
            name = f'{ctx.author.display_name} kissed {member.display_name}'

        embed = discord.Embed(
            title = f'{name}',
            color=color,
            timestamp = datetime.datetime.utcnow()
        )

        file = discord.File(f"{id}kiss.jpg")
        embed.set_author(name = f'{ctx.author}', icon_url=f"{ctx.author.avatar_url}")
        embed.set_image(url = f"attachment://{id}kiss.jpg")

        await ctx.send(file=file,embed=embed)
        os.remove(f"./{memid}avatar.png")
        os.remove(f"./{id}kiss.jpg")
        os.remove(f"{id}avatar.jpg")

    @commands.command()
    async def slap(self, ctx, member : discord.Member):
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = './guild data/'+ str(guildid) +'.json'
        with open(guild, 'r') as g:
            users = json.load(g)

        color = users[str(id)]['color']

        memid = member.id
        user = await ctx.message.author.avatar_url.save((f"{id}avatar.jpg"))
        mem = await member.avatar_url.save((f"{memid}avatar.png"))
        background = Image.open("./meme/slap.jpg").convert("RGB").resize((800, 500))
        draw = ImageDraw.Draw(background, "RGB")

        try:
            logo = Image.open(f"{id}avatar.jpg").convert("RGB").resize((180, 180))
        except:
            logo = Image.open("./pictures/discord.png").convert("RGB").resize((180, 180))

        try:
            logo2 = Image.open(f"{memid}avatar.png").convert("RGB").resize((180, 180))
        except:
            logo2 = Image.open("./pictures/discord.png").convert("RGB").resize((180, 180))

        #User

        bigsize = (logo.size[0] * 3, logo.size[1] * 3)
        mask = Image.new("L", bigsize, 0)

        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, 255)

        draw.ellipse((140 * 3, 140 * 3, 140 * 3, 140 * 3), 0)

        mask = mask.resize(logo.size, Image.ANTIALIAS)
        logo.putalpha(mask)

        background.paste(logo, (390, 15), mask=logo)

        draw = ImageDraw.Draw(background, "RGB")

        #Member

        bigsize = (logo2.size[0] * 3, logo2.size[1] * 3)
        mask = Image.new("L", bigsize, 0)

        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, 255)

        draw.ellipse((140 * 3, 140 * 3, 140 * 3, 140 * 3), 0)

        mask = mask.resize(logo2.size, Image.ANTIALIAS)
        logo2.putalpha(mask)

        background.paste(logo2, (200, 80), mask=logo2)

        draw = ImageDraw.Draw(background, "RGB")

        background.save(f"{id}slap.jpg", quality = 100)

        if member == ctx.author:
            name = f"{ctx.author.display_name} slapped themself. What an idiot!"
        else:
            name = f'{ctx.author.display_name} slapped {member.display_name}'

        embed = discord.Embed(
            title = f'{name}',
            color=color,
            timestamp = datetime.datetime.utcnow()
        )

        file = discord.File(f"{id}slap.jpg")
        embed.set_author(name = f'{ctx.author}', icon_url=f"{ctx.author.avatar_url}")
        embed.set_image(url = f"attachment://{id}slap.jpg")

        await ctx.send(file=file,embed=embed)
        os.remove(f"./{memid}avatar.png")
        os.remove(f"./{id}slap.jpg")
        os.remove(f"{id}avatar.jpg")

    @commands.command(name = "kill", aliases = ["demolish", "destroy", "cancel", "KILL", "Kill"])
    async def kill(self, message, member : discord.Member):
        id = message.author.id
        memid = member.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        lvl = users[str(id)]['level']
        lvl2 = users[str(memid)]['level']
        c = users[str(id)]['color']

        if lvl>=10:
            if lvl2>=10:
                if users[str(memid)]['sage_spell'] == True:
                        m = f'{member.mention} is invulnerable because of `Sage Spell`'
                        level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                        level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                        await message.channel.send(embed=level_embed)
                elif users[str(id)]['sage_spell'] == True:
                        m = f'{message.author.mention} You own a `Sage Spell`, and cannot kill anyone'
                        level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                        level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                        await message.channel.send(embed=level_embed)
                elif member == message.author:
                    L = [1, 2]
                    x = random.choice(L)
                    if x == 1:
                        obj = random.choice(wom)
                        m = f'{message.author.mention} {obj}'
                        level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                        level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                        await message.channel.send(embed=level_embed)
                    else:
                        rsn = random.choice(reason)
                        m = f"{message.author.mention} {rsn}"
                        level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                        level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                        await message.channel.send(embed=level_embed)
                else:
                    L = [1, 2]
                    x = random.choice(L)
                    if x == 1:
                        with open(guildid, 'r') as f1:
                            users = json.load(f1)

                        u2 = users[str(memid)]['experience']

                        p = int((u2*5)/100)

                        u2 = u2 - p
                        users[str(memid)]['experience'] = int(u2)
                        lvl = int(u2 ** (1/4))
                        users[str(memid)]['level'] = lvl

                        u1 = users[str(id)]['experience']
                        u1 = u1 + p
                        users[str(id)]['experience'] = int(u1)
                        lvl = int(u1 ** (1/4))
                        users[str(id)]['level'] = lvl

                        with open(guildid, 'w') as f1:
                            json.dump(users, f1, indent=4)

                        obj = random.choice(wom)
                        m = f'{message.author.mention} killed {member.mention} {obj}'
                        level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                        level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                        level_embed.set_footer(text = f'{member.display_name} lost {p} XP')
                        await message.channel.send(embed=level_embed)
                    else:
                        with open(guildid, 'r') as f1:
                            users = json.load(f1)

                        u1 = users[str(id)]['experience']

                        p = int((u1*5)//100)

                        u1 = u1 - p
                        users[str(id)]['experience'] = int(u1)
                        lvl = int(u1 ** (1/4))
                        users[str(id)]['level'] = lvl

                        u2 = users[str(memid)]['experience']
                        u2 = u2 + p
                        users[str(memid)]['experience'] = int(u2)
                        lvl = int(u2 ** (1/4))
                        users[str(memid)]['level'] = lvl

                        with open(guildid, 'w') as f1:
                            json.dump(users, f1, indent=4)

                        rsn = random.choice(reason)
                        m = f"{message.author.mention} couldn't kill {member.mention} {rsn}"
                        level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                        level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                        level_embed.set_footer(text = f'{message.author.display_name} lost {p} XP')
                        await message.channel.send(embed=level_embed)
            else:
                m = f'{message.author.mention} User must be `Level 10` or +'
                level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                await message.channel.send(embed=level_embed)

        else:
            m = f'{message.author.mention} Requirements to use this command : `Level 10`'
            level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await message.channel.send(embed=level_embed)

    @commands.command()
    async def roast(self, message, member : discord.Member):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/roast.json", "r") as f:
            roasts = json.load(f)

        r = random.choice(roasts)

        embed = discord.Embed(title = "Roast 🔥",
        description = f"{member.mention} {r}",
        color = color,
        timestamp = datetime.datetime.utcnow())

        await message.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(FunCog(bot))
