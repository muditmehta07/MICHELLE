import discord
from discord.ext import commands
import os
import random
import datetime
import json
from discord import message
from discord.ext.commands import context
from discord.ext.commands.context import Context
from PIL import Image, ImageDraw, ImageFont

wom = ["with a pair of dirty flip flops.", "with a rusted knife.", "by feeding them cat biscuits.", "by hitting them with rotten eggs.", "with a lame joke.", "by tossing a rubbed duckie at them.", "with a glitchy boombot.", "by stabbing them with a banana.", "with smelly feet.", "with their dandruff."]
reason = [". What a noob", "because they slipped on a banana.", "because they fell asleep.", "because they were arrested for tax fraud.", "because of excessive sweating.", "because of constipation.", "because of low brain cells."]

class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def convert(self, n):
        avg = str(datetime.timedelta(seconds = n))
        avgString = str(avg).split(".")[0]

        return avgString

    @commands.command()
    async def monster(self, ctx):
        await ctx.channel.trigger_typing()
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
    async def hug(self, ctx, member : discord.Member = None):
        await ctx.channel.trigger_typing()
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = './guild data/'+ str(guildid) +'.json'
        with open(guild, 'r') as g:
            users = json.load(g)

        color = users[str(id)]['color']

        if member == None:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(ctx.guild.id) in L:
                get_prefix = L[str(ctx.guild.id)]["prefix"]
            elif str(ctx.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Description** : Hugs the mentioned user by sending a custom image\n\n**Usage** : `{get_prefix}hug <user mention>`\n**Example** : `{get_prefix}hug @user` to hug a user" , 
                color = color, 
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Hug Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed = embed)

        else:
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
    async def kiss(self, ctx, member : discord.Member = None):
        await ctx.channel.trigger_typing()
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = './guild data/'+ str(guildid) +'.json'
        with open(guild, 'r') as g:
            users = json.load(g)

        color = users[str(id)]['color']

        if member == None:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(ctx.guild.id) in L:
                get_prefix = L[str(ctx.guild.id)]["prefix"]
            elif str(ctx.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Description** : Kisses the mentioned user by sending a custom image\n\n**Usage** : `{get_prefix}kiss <user mention>`\n**Example** : `{get_prefix}kiss @user` to kiss a user" , 
                color = color, 
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Kiss Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed = embed)
        
        else:
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
    async def slap(self, ctx, member : discord.Member = None):
        await ctx.channel.trigger_typing()
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = './guild data/'+ str(guildid) +'.json'
        with open(guild, 'r') as g:
            users = json.load(g)

        color = users[str(id)]['color']

        if member == None:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(ctx.guild.id) in L:
                get_prefix = L[str(ctx.guild.id)]["prefix"]
            elif str(ctx.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Description** : Slaps the mentioned user by sending a custom image\n\n**Usage** : `{get_prefix}slap <user mention>`\n**Example** : `{get_prefix}slap @user` to slap a user" , 
                color = color, 
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Slap Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed = embed)

        else:
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

    @commands.group(invoke_without_command = True)
    async def kill(self, message, member : discord.Member = None):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        c = users[str(id)]['color']

        if member == None:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(message.guild.id) in L:
                get_prefix = L[str(message.guild.id)]["prefix"]
            elif str(message.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Description** : Kills the mentioned user. Killing a user drops their XP and raises yours. You may also fail to kill them which would drop your XP and raise their's\n\n**Usage** : `{get_prefix}kill <weapon> <user mention>`\n**Example** : `{get_prefix}kill knife @user` to kill a user with a knife" , 
                color = c,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Kill Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await message.channel.send(embed = embed)

        else:
            memid = member.id
            lvl = users[str(id)]['level']
            lvl2 = users[str(memid)]['level']

            if lvl>=10:
                if lvl2>=10:
                    if users[str(memid)]['sage_spell'] == True:
                            m = f'{member.mention} owns a `Sage Spell` and is invulnerable of your mortal threats'
                            level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                            level_embed.set_author(name = message.author, icon_url = message.author.avatar_url)
                            await message.channel.send(embed=level_embed)

                    elif users[str(id)]['sage_spell'] == True:
                            m = f'{message.author.mention} You own a `Sage Spell`, you cannot kill anyone'
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

                            p = 20

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

                            p = 20

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

    @kill.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def knife(self, ctx, member : discord.Member = None):
        await ctx.channel.trigger_typing()
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        c = users[str(id)]['color']
        knife = self.bot.get_emoji(881474984193703999)

        if member == None:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(ctx.guild.id) in L:
                get_prefix = L[str(ctx.guild.id)]["prefix"]
            elif str(ctx.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Description** : Kills the mentioned user. Killing a user drops their XP and raises yours. You may also fail to kill them which would drop your XP and raise their's\n\n**Usage** : `{get_prefix}kill <weapon> <user mention>`\n**Example** : `{get_prefix}kill knife @user` to kill a user with a knife" , 
                color = c,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Kill Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed = embed)
            await ctx.command.reset_cooldown(ctx)

        else:
            memid = member.id
            lvl = users[str(id)]['level']
            lvl2 = users[str(memid)]['level']

            with open("./local/weapons.json", "r") as f:
                weapon = json.load(f)

            if str(ctx.author.id) in weapon:
                if weapon[f"{ctx.author.id}"]["knife"] == True:
                    if lvl>=10:
                        if lvl2>=10:
                            if users[str(memid)]['sage_spell'] == True:
                                    m = f'{member.mention} owns a `Sage Spell` and is invulnerable of your mortal threats'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif users[str(id)]['sage_spell'] == True:
                                    m = f'{ctx.author.mention} You own a `Sage Spell`, you cannot kill anyone'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif member == ctx.author:
                                L = [1, 2, 3]
                                x = random.choice(L)
                                if x == 1 or x == 3:
                                    m = f'{ctx.author.mention} stabbed themself with a Knife {knife}'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)
                                else:
                                    rsn = random.choice(reason)
                                    m = f"{ctx.author.mention} {rsn}"
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)
                            else:
                                L = [1, 2, 3]
                                x = random.choice(L)
                                if x == 1 or x == 3:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u2 = users[str(memid)]['experience']

                                    p = int((u2*0.25)//100)

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
                                    m = f'{ctx.author.mention} stabbed {member.mention} with a Knife {knife}\n\n{ctx.author.display_name} : `+{p} XP`  •  {member.display_name} : `-{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)

                                else:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u1 = users[str(id)]['experience']

                                    p = int((u1*0.25)//100)

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
                                    m = f'{ctx.author.mention} failed to stab {member.mention} with a Knife\n\n{ctx.author.display_name} : `-{p} XP`  •  {member.display_name} : `+{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                        else:
                            m = f'{ctx.author.mention} User must be `Level 10` or +'
                            level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                            level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                            await ctx.send(embed=level_embed)
                            await ctx.command.reset_cooldown(ctx)

                    else:
                        m = f'{ctx.author.mention} Requirements to use this command : `Level 10`'
                        level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                        level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                        await ctx.send(embed=level_embed)
                        await ctx.command.reset_cooldown(ctx)
                
                else:  
                    with open("./local/prefix.json", "r") as f:
                        L = json.load(f)

                    if str(ctx.guild.id) in L:
                        get_prefix = L[str(ctx.guild.id)]["prefix"]
                    elif str(ctx.guild.id) not in L:
                        get_prefix = "="

                    m = f'{ctx.author.mention} **You do not own a** {knife} `Knife`\nFor more info use `{get_prefix}help knife`'
                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                    await ctx.send(embed=level_embed)
                    await ctx.command.reset_cooldown(ctx)

            else:
                with open("./local/prefix.json", "r") as f:
                    L = json.load(f)

                if str(ctx.guild.id) in L:
                    get_prefix = L[str(ctx.guild.id)]["prefix"]
                elif str(ctx.guild.id) not in L:
                    get_prefix = "="

                m = f'{ctx.author.mention} **You do not own a** {knife} `Knife`\nFor more info use `{get_prefix}help knife`'
                level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                await ctx.send(embed=level_embed)
                await ctx.command.reset_cooldown(ctx)

    @knife.error
    async def knife_error(self, ctx, error):

        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = error.retry_after

            embed = discord.Embed(description = f"**Knife is being sharped** `{FunCog.convert(self, remaining_time)}`\nKnives have a Cooldown of **30 Seconds**", color=color, timestamp = datetime.datetime.utcnow())
            embed.set_author(name="Kill Cooldown", icon_url="https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed=embed)

    @kill.command()
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def machette(self, ctx, member : discord.Member = None):
        await ctx.channel.trigger_typing()
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        c = users[str(id)]['color']
        machette = self.bot.get_emoji(881478895503806464)

        if member == None:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(ctx.guild.id) in L:
                get_prefix = L[str(ctx.guild.id)]["prefix"]
            elif str(ctx.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Description** : Kills the mentioned user. Killing a user drops their XP and raises yours. You may also fail to kill them which would drop your XP and raise their's\n\n**Usage** : `{get_prefix}kill <weapon> <user mention>`\n**Example** : `{get_prefix}kill knife @user` to kill a user with a knife" , 
                color = c,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Kill Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed = embed)
            await ctx.command.reset_cooldown(ctx)

        else:
            memid = member.id
            lvl = users[str(id)]['level']
            lvl2 = users[str(memid)]['level']

            with open("./local/weapons.json", "r") as f:
                weapon = json.load(f)

            if str(ctx.author.id) in weapon:
                if weapon[f"{ctx.author.id}"]["machette"] == True:
                    if lvl>=10:
                        if lvl2>=10:
                            if users[str(memid)]['sage_spell'] == True:
                                    m = f'{member.mention} owns a `Sage Spell` and is invulnerable of your mortal threats'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif users[str(id)]['sage_spell'] == True:
                                    m = f'{ctx.author.mention} You own a `Sage Spell`, you cannot kill anyone'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif member == ctx.author:
                                L = [1, 2, 3]
                                x = random.choice(L)
                                if x == 1 or x == 3:
                                    m = f'{ctx.author.mention} stabbed themself with a Machette {machette}'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)
                                else:
                                    rsn = random.choice(reason)
                                    m = f"{ctx.author.mention} {rsn}"
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)
                            else:
                                L = [1, 2, 3]
                                x = random.choice(L)
                                if x == 1 or x==3:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u2 = users[str(memid)]['experience']

                                    p = int((u2*0.5)//100)

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
                                    m = f'{ctx.author.mention} stabbed {member.mention} with a Machette {machette}\n\n{ctx.author.display_name} : `+{p} XP`  •  {member.display_name} : `-{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)

                                else:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u1 = users[str(id)]['experience']

                                    p = int((u1*0.5)//100)

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
                                    m = f'{ctx.author.mention} failed to stab {member.mention} with a Machette {machette}\n\n{ctx.author.display_name} : `-{p} XP`  •  {member.display_name} : `+{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                        else:
                            m = f'{ctx.author.mention} User must be `Level 10` or +'
                            level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                            level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                            await ctx.send(embed=level_embed)
                            await ctx.command.reset_cooldown(ctx)

                    else:
                        m = f'{ctx.author.mention} Requirements to use this command : `Level 10`'
                        level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                        level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                        await ctx.send(embed=level_embed)
                        await ctx.command.reset_cooldown(ctx)

                else:  
                    with open("./local/prefix.json", "r") as f:
                        L = json.load(f)

                    if str(ctx.guild.id) in L:
                        get_prefix = L[str(ctx.guild.id)]["prefix"]
                    elif str(ctx.guild.id) not in L:
                        get_prefix = "="

                    m = f'{ctx.author.mention} **You do not own a** {machette} `Machette`\nFor more info use `{get_prefix}help machette`'
                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                    await ctx.send(embed=level_embed)
                    await ctx.command.reset_cooldown(ctx)

            else:
                with open("./local/prefix.json", "r") as f:
                    L = json.load(f)

                if str(ctx.guild.id) in L:
                    get_prefix = L[str(ctx.guild.id)]["prefix"]
                elif str(ctx.guild.id) not in L:
                    get_prefix = "="

                m = f'{ctx.author.mention} **You do not own a** {machette} `Machette`\nFor more info use `{get_prefix}help machette`'
                level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                await ctx.send(embed=level_embed)

    @machette.error
    async def machette_error(self, ctx, error):

        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = error.retry_after

            embed = discord.Embed(description = f"**Machette is being sharped** `{FunCog.convert(self, remaining_time)}`\nMachettes have a Cooldown of **2 Minutes**", color=color, timestamp = datetime.datetime.utcnow())
            embed.set_author(name="Kill Cooldown", icon_url="https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed=embed)

    @kill.command()
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def dagger(self, ctx, member : discord.Member = None):
        await ctx.channel.trigger_typing()
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        c = users[str(id)]['color']
        dagger = self.bot.get_emoji(881478895835164682)

        if member == None:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(ctx.guild.id) in L:
                get_prefix = L[str(ctx.guild.id)]["prefix"]
            elif str(ctx.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Description** : Kills the mentioned user. Killing a user drops their XP and raises yours. You may also fail to kill them which would drop your XP and raise their's\n\n**Usage** : `{get_prefix}kill <weapon> <user mention>`\n**Example** : `{get_prefix}kill knife @user` to kill a user with a knife" , 
                color = c,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Kill Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed = embed)
            await ctx.command.reset_cooldown(ctx)

        else:
            memid = member.id
            lvl = users[str(id)]['level']
            lvl2 = users[str(memid)]['level']

            with open("./local/weapons.json", "r") as f:
                weapon = json.load(f)

            if str(ctx.author.id) in weapon:
                if weapon[f"{ctx.author.id}"]["dagger"] == True:
                    if lvl>=10:
                        if lvl2>=10:
                            if users[str(memid)]['sage_spell'] == True:
                                    m = f'{member.mention} owns a `Sage Spell` and is invulnerable of your mortal threats'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif users[str(id)]['sage_spell'] == True:
                                    m = f'{ctx.author.mention} You own a `Sage Spell`, you cannot kill anyone'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif member == ctx.author:
                                L = [1, 2, 3]
                                x = random.choice(L)
                                if x == 1 or x == 3:
                                    m = f'{ctx.author.mention} stabbed themself with a Dagger {dagger}'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)
                                else:
                                    rsn = random.choice(reason)
                                    m = f"{ctx.author.mention} {rsn}"
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)
                            else:
                                L = [1, 2, 3]
                                x = random.choice(L)
                                if x == 1 or x==3:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u2 = users[str(memid)]['experience']

                                    p = int((u2*0.75)//100)

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
                                    m = f'{ctx.author.mention} stabbed {member.mention} with a Dagger {dagger}\n\n{ctx.author.display_name} : `+{p} XP`  •  {member.display_name} : `-{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)

                                else:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u1 = users[str(id)]['experience']

                                    p = int((u1*0.75)//100)

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
                                    m = f'{ctx.author.mention} failed to stab {member.mention} with a Dagger {dagger}\n\n{ctx.author.display_name} : `-{p} XP`  •  {member.display_name} : `+{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                        else:
                            m = f'{ctx.author.mention} User must be `Level 10` or +'
                            level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                            level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                            await ctx.send(embed=level_embed)
                            await ctx.command.reset_cooldown(ctx)

                    else:
                        m = f'{ctx.author.mention} Requirements to use this command : `Level 10`'
                        level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                        level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                        await ctx.send(embed=level_embed)
                        await ctx.command.reset_cooldown(ctx)

                else:  
                    with open("./local/prefix.json", "r") as f:
                        L = json.load(f)

                    if str(ctx.guild.id) in L:
                        get_prefix = L[str(ctx.guild.id)]["prefix"]
                    elif str(ctx.guild.id) not in L:
                        get_prefix = "="

                    m = f'{ctx.author.mention} **You do not own a** {dagger} `Dagger`\nFor more info use `{get_prefix}help dagger`'
                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                    await ctx.send(embed=level_embed)
                    await ctx.command.reset_cooldown(ctx)

            else:
                with open("./local/prefix.json", "r") as f:
                    L = json.load(f)

                if str(ctx.guild.id) in L:
                    get_prefix = L[str(ctx.guild.id)]["prefix"]
                elif str(ctx.guild.id) not in L:
                    get_prefix = "="

                m = f'{ctx.author.mention} **You do not own a** {dagger} `Dagger`\nFor more info use `{get_prefix}help dagger`'
                level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                await ctx.send(embed=level_embed)
                await ctx.command.reset_cooldown(ctx)

    @dagger.error
    async def dagger_error(self, ctx, error):

        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = error.retry_after

            embed = discord.Embed(description = f"**Dagger is being sharped** `{FunCog.convert(self, remaining_time)}`\nDaggers have a Cooldown of **5 Minutes**", color=color, timestamp = datetime.datetime.utcnow())
            embed.set_author(name="Kill Cooldown", icon_url="https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed=embed)

    @kill.command()
    @commands.cooldown(1, 480, commands.BucketType.user)
    async def sword(self, ctx, member : discord.Member = None):
        await ctx.channel.trigger_typing()
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        c = users[str(id)]['color']
        sword = self.bot.get_emoji(881478895247949887)

        if member == None:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(ctx.guild.id) in L:
                get_prefix = L[str(ctx.guild.id)]["prefix"]
            elif str(ctx.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Description** : Kills the mentioned user. Killing a user drops their XP and raises yours. You may also fail to kill them which would drop your XP and raise their's\n\n**Usage** : `{get_prefix}kill <weapon> <user mention>`\n**Example** : `{get_prefix}kill knife @user` to kill a user with a knife" , 
                color = c,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Kill Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed = embed)
            await ctx.command.reset_cooldown(ctx)

        else:
            memid = member.id
            lvl = users[str(id)]['level']
            lvl2 = users[str(memid)]['level']

            with open("./local/weapons.json", "r") as f:
                weapon = json.load(f)

            if str(ctx.author.id) in weapon:
                if weapon[f"{ctx.author.id}"]["sword"] == True:
                    if lvl>=10:
                        if lvl2>=10:
                            if users[str(memid)]['sage_spell'] == True:
                                    m = f'{member.mention} owns a `Sage Spell` and is invulnerable of your mortal threats'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif users[str(id)]['sage_spell'] == True:
                                    m = f'{ctx.author.mention} You own a `Sage Spell`, you cannot kill anyone'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif member == ctx.author:
                                L = [1, 2, 3]
                                x = random.choice(L)
                                if x == 1 or x == 3:
                                    m = f'{ctx.author.mention} slashed themself with a Sword {sword}'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)
                                else:
                                    rsn = random.choice(reason)
                                    m = f"{ctx.author.mention} {rsn}"
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)
                            else:
                                L = [1, 2, 3]
                                x = random.choice(L)
                                if x == 1 or x==3:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u2 = users[str(memid)]['experience']

                                    p = int((u2*1)//100)

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
                                    m = f'{ctx.author.mention} slashed {member.mention} with a Sword {sword}\n\n{ctx.author.display_name} : `+{p} XP`  •  {member.display_name} : `-{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)

                                else:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u1 = users[str(id)]['experience']

                                    p = int((u1*1)//100)

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
                                    m = f'{ctx.author.mention} failed to slash {member.mention} with a Sword {sword}\n\n{ctx.author.display_name} : `-{p} XP`  •  {member.display_name} : `+{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                        else:
                            m = f'{ctx.author.mention} User must be `Level 10` or +'
                            level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                            level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                            await ctx.send(embed=level_embed)
                            await ctx.command.reset_cooldown(ctx)

                    else:
                        m = f'{ctx.author.mention} Requirements to use this command : `Level 10`'
                        level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                        level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                        await ctx.send(embed=level_embed)
                        await ctx.command.reset_cooldown(ctx)

                else:  
                    with open("./local/prefix.json", "r") as f:
                        L = json.load(f)

                    if str(ctx.guild.id) in L:
                        get_prefix = L[str(ctx.guild.id)]["prefix"]
                    elif str(ctx.guild.id) not in L:
                        get_prefix = "="

                    m = f'{ctx.author.mention} **You do not own a** {sword} `Sword`\nFor more info use `{get_prefix}help sword`'
                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                    await ctx.send(embed=level_embed)
                    await ctx.command.reset_cooldown(ctx)

            else:
                with open("./local/prefix.json", "r") as f:
                    L = json.load(f)

                if str(ctx.guild.id) in L:
                    get_prefix = L[str(ctx.guild.id)]["prefix"]
                elif str(ctx.guild.id) not in L:
                    get_prefix = "="

                m = f'{ctx.author.mention} **You do not own a** {sword} `Sword`\nFor more info use `{get_prefix}help sword`'
                level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                await ctx.send(embed=level_embed)
                await ctx.command.reset_cooldown(ctx)

    @sword.error
    async def sword_error(self, ctx, error):

        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = error.retry_after

            embed = discord.Embed(description = f"**Sword is being sharped** `{FunCog.convert(self, remaining_time)}`\nSwords have a Cooldown of **8 Minutes**", color=color, timestamp = datetime.datetime.utcnow())
            embed.set_author(name="Kill Cooldown", icon_url="https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed=embed)

    @kill.command()
    @commands.cooldown(1, 900, commands.BucketType.user)
    async def scythe(self, ctx, member : discord.Member = None):
        await ctx.channel.trigger_typing()
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        c = users[str(id)]['color']
        scythe = self.bot.get_emoji(881478895604494376)

        if member == None:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(ctx.guild.id) in L:
                get_prefix = L[str(ctx.guild.id)]["prefix"]
            elif str(ctx.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Description** : Kills the mentioned user. Killing a user drops their XP and raises yours. You may also fail to kill them which would drop your XP and raise their's\n\n**Usage** : `{get_prefix}kill <weapon> <user mention>`\n**Example** : `{get_prefix}kill knife @user` to kill a user with a knife" , 
                color = c,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Kill Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed = embed)
            await ctx.command.reset_cooldown(ctx)

        else:
            memid = member.id
            lvl = users[str(id)]['level']
            lvl2 = users[str(memid)]['level']

            with open("./local/weapons.json", "r") as f:
                weapon = json.load(f)

            if str(ctx.author.id) in weapon:
                if weapon[f"{ctx.author.id}"]["scythe"] == True:
                    if lvl>=10:
                        if lvl2>=10:
                            if users[str(memid)]['sage_spell'] == True:
                                    m = f'{member.mention} owns a `Sage Spell` and is invulnerable of your mortal threats'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif users[str(id)]['sage_spell'] == True:
                                    m = f'{ctx.author.mention} You own a `Sage Spell`, you cannot kill anyone'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif member == ctx.author:
                                L = [1, 2, 3]
                                x = random.choice(L)
                                if x == 1 or x == 3:
                                    m = f'{ctx.author.mention} slashed themself with a Scythe {scythe}'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)
                                else:
                                    rsn = random.choice(reason)
                                    m = f"{ctx.author.mention} {rsn}"
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)
                            else:
                                L = [1, 2, 3]
                                x = random.choice(L)
                                if x == 1 or x==3:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u2 = users[str(memid)]['experience']

                                    p = int((u2*1.5)//100)

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
                                    m = f'{ctx.author.mention} slashed {member.mention} with a Scythe {scythe}\n\n{ctx.author.display_name} : `+{p} XP`  •  {member.display_name} : `-{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)

                                else:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u1 = users[str(id)]['experience']

                                    p = int((u1*1.5)//100)

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
                                    m = f'{ctx.author.mention} failed to slash {member.mention} with a Scythe {scythe}\n\n{ctx.author.display_name} : `-{p} XP`  •  {member.display_name} : `+{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                        else:
                            m = f'{ctx.author.mention} User must be `Level 10` or +'
                            level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                            level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                            await ctx.send(embed=level_embed)
                            await ctx.command.reset_cooldown(ctx)

                    else:
                        m = f'{ctx.author.mention} Requirements to use this command : `Level 10`'
                        level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                        level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                        await ctx.send(embed=level_embed)
                        await ctx.command.reset_cooldown(ctx)

                else:  
                    with open("./local/prefix.json", "r") as f:
                        L = json.load(f)

                    if str(ctx.guild.id) in L:
                        get_prefix = L[str(ctx.guild.id)]["prefix"]
                    elif str(ctx.guild.id) not in L:
                        get_prefix = "="

                    m = f'{ctx.author.mention} **You do not own a** {scythe} `Scythe`\nFor more info use `{get_prefix}help scythe`'
                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                    await ctx.send(embed=level_embed)
                    await ctx.command.reset_cooldown(ctx)

            else:
                with open("./local/prefix.json", "r") as f:
                    L = json.load(f)

                if str(ctx.guild.id) in L:
                    get_prefix = L[str(ctx.guild.id)]["prefix"]
                elif str(ctx.guild.id) not in L:
                    get_prefix = "="

                m = f'{ctx.author.mention} **You do not own a** {scythe} `Scythe`\nFor more info use `{get_prefix}help scythe`'
                level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                await ctx.send(embed=level_embed)
                await ctx.command.reset_cooldown(ctx)

    @scythe.error
    async def scythe_error(self, ctx, error):

        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = error.retry_after

            embed = discord.Embed(description = f"**Scythe is being sharped** `{FunCog.convert(self, remaining_time)}`\nScythes have a Cooldown of **15 Minutes**", color=color, timestamp = datetime.datetime.utcnow())
            embed.set_author(name="Kill Cooldown", icon_url="https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed=embed)

    @kill.command()
    @commands.cooldown(1, 1800, commands.BucketType.user)
    async def shuriken(self, ctx, member : discord.Member = None):
        await ctx.channel.trigger_typing()
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        c = users[str(id)]['color']
        shuriken = self.bot.get_emoji(881478895889690674)

        if member == None:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(ctx.guild.id) in L:
                get_prefix = L[str(ctx.guild.id)]["prefix"]
            elif str(ctx.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Description** : Kills the mentioned user. Killing a user drops their XP and raises yours. You may also fail to kill them which would drop your XP and raise their's\n\n**Usage** : `{get_prefix}kill <weapon> <user mention>`\n**Example** : `{get_prefix}kill knife @user` to kill a user with a knife" , 
                color = c,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Kill Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed = embed)
            await ctx.command.reset_cooldown(ctx)

        else:
            memid = member.id
            lvl = users[str(id)]['level']
            lvl2 = users[str(memid)]['level']

            with open("./local/weapons.json", "r") as f:
                weapon = json.load(f)

            if str(ctx.author.id) in weapon:
                if weapon[f"{ctx.author.id}"]["shuriken"] == True:
                    if lvl>=10:
                        if lvl2>=10:
                            if users[str(memid)]['sage_spell'] == True:
                                    m = f'{member.mention} owns a `Sage Spell` and is invulnerable of your mortal threats'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif users[str(id)]['sage_spell'] == True:
                                    m = f'{ctx.author.mention} You own a `Sage Spell`, you cannot kill anyone'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)

                            elif member == ctx.author:
                                L = [1, 2, 3]
                                x = random.choice(L)
                                if x == 1 or x == 3:
                                    m = f'{ctx.author.mention} pierced themself with a Shuriken {shuriken}'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)
                                else:
                                    rsn = random.choice(reason)
                                    m = f"{ctx.author.mention} {rsn}"
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                                    await ctx.command.reset_cooldown(ctx)
                            else:
                                L = [1, 2, 3]
                                x = random.choice(L)
                                if x == 1 or x==3:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u2 = users[str(memid)]['experience']

                                    p = int((u2*2)//100)

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
                                    m = f'{ctx.author.mention} pierced a Shuriken {shuriken} through {member.mention}\n\n{ctx.author.display_name} : `+{p} XP`  •  {member.display_name} : `-{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)

                                else:
                                    with open(guildid, 'r') as f1:
                                        users = json.load(f1)

                                    u1 = users[str(id)]['experience']

                                    p = int((u1*2)//100)

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
                                    m = f'{ctx.author.mention} failed to pierce a Shuriken {shuriken} through {member.mention}\n\n{ctx.author.display_name} : `-{p} XP`  •  {member.display_name} : `+{p} XP`'
                                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                                    await ctx.send(embed=level_embed)
                        else:
                            m = f'{ctx.author.mention} User must be `Level 10` or +'
                            level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                            level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                            await ctx.send(embed=level_embed)
                            await ctx.command.reset_cooldown(ctx)

                    else:
                        m = f'{ctx.author.mention} Requirements to use this command : `Level 10`'
                        level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                        level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                        await ctx.send(embed=level_embed)
                        await ctx.command.reset_cooldown(ctx)

                else:  
                    with open("./local/prefix.json", "r") as f:
                        L = json.load(f)

                    if str(ctx.guild.id) in L:
                        get_prefix = L[str(ctx.guild.id)]["prefix"]
                    elif str(ctx.guild.id) not in L:
                        get_prefix = "="

                    m = f'{ctx.author.mention} **You do not own a** {shuriken} `Shuriken`\nFor more info use `{get_prefix}help shuriken`'
                    level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                    level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                    await ctx.send(embed=level_embed)
                    await ctx.command.reset_cooldown(ctx)

            else:
                with open("./local/prefix.json", "r") as f:
                    L = json.load(f)

                if str(ctx.guild.id) in L:
                    get_prefix = L[str(ctx.guild.id)]["prefix"]
                elif str(ctx.guild.id) not in L:
                    get_prefix = "="

                m = f'{ctx.author.mention} **You do not own a** {shuriken} `Shuriken`\nFor more info use `{get_prefix}help shuriken`'
                level_embed = discord.Embed(description = m, color = c, timestamp=datetime.datetime.utcnow())
                level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                await ctx.send(embed=level_embed)
                await ctx.command.reset_cooldown(ctx)

    @shuriken.error
    async def shuriken_error(self, ctx, error):

        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if isinstance(error, commands.CommandOnCooldown):
            remaining_time = error.retry_after

            embed = discord.Embed(description = f"**Shuriken is being sharped** `{FunCog.convert(self, remaining_time)}`\nShuriken have a Cooldown of **30 Minutes**", color=color, timestamp = datetime.datetime.utcnow())
            embed.set_author(name="Kill Cooldown", icon_url="https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await ctx.send(embed=embed)

    @commands.command()
    async def roast(self, message, member : discord.Member = None):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if member == None:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(message.guild.id) in L:
                get_prefix = L[str(message.guild.id)]["prefix"]
            elif str(message.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description = f"**Description** : Roasts the mentioned user\n\n**Usage** : `{get_prefix}roast <user mention>`\n**Example** : `{get_prefix}roast @user` to roast a user" , 
                color = color, 
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Roast Help ❓", icon_url = "https://cdn.discordapp.com/emojis/880689402567884821.png?v=1")
            await message.channel.send(embed = embed)

        else:
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