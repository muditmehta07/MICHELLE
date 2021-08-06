'''

Level

'''

import discord
from discord.ext import commands
import os
import datetime
import json
import names
from discord import message
from discord.ext.commands.context import Context
from PIL import Image, ImageDraw, ImageFont

class LevelCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def human_format(self, num):
        num = float('{:.3g}'.format(num))
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num /= 1000.0
        return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])

    @commands.command(name = "level", aliases = ["rank", "Level", "LEVEL", "Rank", "RANK"])
    async def level(self, ctx, member: discord.Member = None):
        guildid = ctx.message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        if not member:
            id = ctx.message.author.id
            with open(guildid, 'r') as f:
                users = json.load(f)

            R={}
            for i in users:
                user = i
                exp = users[i]['experience']
                R[user]=exp
            R = dict(sorted(R.items(), key=lambda item: item[1], reverse=True))
            L= list(R)
            theme = users[str(id)]['color']
            rank = L.index(str(id))+1
            level = users[str(id)]['level']
            currentxp = users[str(id)]['experience']
            xp = currentxp
            final_xp = (int(level)+1) ** 4
            user_name = ctx.author.name
            discriminator = "#"+ctx.author.discriminator
            await ctx.message.author.avatar_url.save(("logo.jpg"))

            level = LevelCog.human_format(self, level)
            
            if theme == 9807270: #gray
                full_image = Image.open("./pictures/bg.jpg").convert("RGB").resize((1060, 320))
            elif theme == 15158332 or theme == 10038562: #red
                full_image = Image.open("./pictures/red.jpg").convert("RGB").resize((1060, 320))
            elif theme == 3447003 or theme == 2123412: #blue
                full_image = Image.open("./pictures/blue.jpg").convert("RGB").resize((1060, 320))
            elif theme == 3066993 or theme == 2067276: #green
                full_image = Image.open("./pictures/green.jpg").convert("RGB").resize((1060, 320))
            elif theme == 10181046 or theme == 7419530: #purple
                full_image = Image.open("./pictures/purple.jpg").convert("RGB").resize((1060, 320))
            elif theme == 15844367 or theme == 12745742: #gold
                full_image = Image.open("./pictures/gold.jpg").convert("RGB").resize((1060, 320))
            elif theme == 1752220 or theme == 1146986: #teal
                full_image = Image.open("./pictures/teal.png").convert("RGB").resize((1060, 320))
            elif theme == 15105570 or theme == 11027200: #orange
                full_image = Image.open("./pictures/orange.jpg").convert("RGB").resize((1060, 320))
            elif theme == 15277667 or theme == 11342935: #magenta
                full_image = Image.open("./pictures/magenta.jpg").convert("RGB").resize((1060, 320))
            else: #gray
                full_image = Image.open("./pictures/bg.jpg").convert("RGB").resize((1060, 320))

            background = Image.new("RGB", (1000, 240))

            theme = hex(theme).split('x')[-1]

            try:
                logo = Image.open("logo.jpg").convert("RGB").resize((180, 180))
            except:
                logo = Image.open("./pictures/discord.png").convert("RGB").resize((180, 180))
            bigsize = (logo.size[0] * 3, logo.size[1] * 3)
            mask = Image.new("L", bigsize, 0)

            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + bigsize, 255)

            draw.ellipse((140 * 3, 140 * 3, 189 * 3, 189 * 3), 0)

            mask = mask.resize(logo.size, Image.ANTIALIAS)
            logo.putalpha(mask)

            background.paste(logo, (40, 30), mask=logo)

            draw = ImageDraw.Draw(background, "RGB")

            if ctx.message.author.status == discord.Status.online:
                draw.ellipse((180, 165, 230, 215), fill="#47d147")
            elif ctx.message.author.status == discord.Status.idle:
                draw.ellipse((180, 165, 230, 215), fill="#ffff99")
            elif ctx.message.author.status == discord.Status.dnd:
                draw.ellipse((180, 165, 230, 215), fill="#b34f5a")
            else:
                draw.ellipse((180, 165, 230, 215), fill="#d9d9d9")

            big_font = ImageFont.FreeTypeFont("ABeeZee-Regular.otf", 60)
            medium_font = ImageFont.FreeTypeFont("ABeeZee-Regular.otf", 40)
            small_font = ImageFont.FreeTypeFont("ABeeZee-Regular.otf", 30)

            text_size = draw.textsize(str(level), font=big_font)
            offset_x = 1000 - 15 - text_size[0]
            offset_y = 10
            draw.text((offset_x, offset_y), str(level), font=big_font, fill=f"#{theme}")

            text_size = draw.textsize("LEVEL", font=small_font)
            offset_x -= text_size[0] + 5
            draw.text((offset_x, offset_y + 27), "LEVEL", font=small_font, fill=f"#{theme}")

            text_size = draw.textsize(f"#{rank}", font=big_font)
            offset_x -= text_size[0] + 15
            draw.text((offset_x, offset_y), f"#{rank}", font=big_font, fill="#fff")

            text_size = draw.textsize("RANK", font=small_font)
            offset_x -= text_size[0] + 5
            draw.text((offset_x, offset_y + 27), "RANK", font=small_font, fill="#fff")

            bar_offset_x = 320
            bar_offset_y = 160
            bar_offset_x_1 = 950
            bar_offset_y_1 = 200
            circle_size = bar_offset_y_1 - bar_offset_y

            draw.rectangle((bar_offset_x, bar_offset_y, bar_offset_x_1, bar_offset_y_1), fill="#727175")

            draw.ellipse(
                (bar_offset_x - circle_size // 2, bar_offset_y, bar_offset_x + circle_size // 2, bar_offset_y_1), fill="#727175"
            )

            draw.ellipse(
                (bar_offset_x_1 - circle_size // 2, bar_offset_y, bar_offset_x_1 + circle_size // 2, bar_offset_y_1), fill="#727175"
            )

            bar_length = bar_offset_x_1 - bar_offset_x
            progress = (xp) * 100 / final_xp
            progress = 100 - progress
            progress_bar_length = round(bar_length * progress / 100)
            bar_offset_x_1 = bar_offset_x + progress_bar_length

            draw.rectangle((bar_offset_x, bar_offset_y, bar_offset_x_1, bar_offset_y_1), fill=f"#{theme}")

            draw.ellipse(
                (bar_offset_x - circle_size // 2, bar_offset_y, bar_offset_x + circle_size // 2, bar_offset_y_1), fill=f"#{theme}"
            )

            draw.ellipse(
                (bar_offset_x_1 - circle_size // 2, bar_offset_y, bar_offset_x_1 + circle_size // 2, bar_offset_y_1), fill=f"#{theme}"
            )

            text_size = draw.textsize(f"/ {LevelCog.human_format(self, final_xp)} XP", font=small_font)

            offset_x = 950 - text_size[0]
            offset_y = bar_offset_y - text_size[1] - 14

            draw.text((offset_x, offset_y), f"/ {LevelCog.human_format(self, final_xp)} XP", font=small_font, fill="#727175")

            text_size = draw.textsize(f"{LevelCog.human_format(self, xp)}", font=small_font)
            offset_x -= text_size[0] + 8
            draw.text((offset_x, offset_y), f"{LevelCog.human_format(self, xp)}", font=small_font, fill="#fff")

            text_size = draw.textsize(user_name, font=medium_font)

            offset_x = bar_offset_x
            offset_y = bar_offset_y - text_size[1] - 14
            draw.text((offset_x, offset_y), user_name, font=medium_font, fill="#fff")

            offset_x += text_size[0] + 5
            offset_y += 10

            draw.text((offset_x, offset_y), discriminator, font=small_font, fill="#727175")

            img_w, img_h = background.size
            bg_w, bg_h = full_image.size
            offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)

            full_image.paste(background, offset)

            full_image.save("image.jpg", quality=100)
            file = discord.File("image.jpg")
            await ctx.send(file=file)
            os.remove("image.jpg")
            os.remove("logo.jpg")

        else:
            id = member.id
            with open(guildid, 'r') as f:
                users = json.load(f)
            lvl = users[str(id)]['level']
            exp = users[str(id)]['experience']
            color = users[str(id)]['color']
            m = f'{member.mention} is Level {lvl}'
            level_embed = discord.Embed(description = m, color = color, timestamp = datetime.datetime.utcnow())
            level_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            await ctx.send(embed=level_embed)


    @commands.command(name = "leader", aliases = ["leaderboard", "Leaderboard", "LEADERBOARD", "Leader", "LEADER", "lb", "LB", "Lb"])
    async def leader(self, message : discord.Message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        R={}
        for i in users:
            user = i
            exp = users[i]['experience']
            R[user]=exp
        R = dict(sorted(R.items(), key=lambda item: item[1], reverse=True))
        L= list(R)
        
        for i in L:
            if users[str(i)]['chameleon'] == True:
                L.remove(i)

        try:
            one = int(L[0])
            if users[str(one)]['transformation'] == True:
                user1 = names.get_full_name()
                rank1 = str(user1)
                xp = R[str(one)]
                msg1 = int(xp/5)
                lvl1 = int(xp**(1/4))
            else:
                user1 = self.bot.get_user(one)
                rank1 = str(user1)
                xp = R[str(one)]
                msg1 = int(xp/5)
                lvl1 = int(xp**(1/4))
        except Exception as e:
            print(e)
            user1 = "No User"
            rank1 = str(user1)
            msg1 = int(0)
            lvl1 = int(0)

        try:
            two = int(L[1])
            if users[str(two)]['transformation'] == True:
                user2 = names.get_full_name()
                rank2 = str(user2)
                xp = R[str(two)]
                msg2 = int(xp/5)
                lvl2 = int(xp**(1/4))
            else:
                user2 = self.bot.get_user(two)
                rank2 = str(user2)
                xp = R[str(two)]
                msg2 = int(xp/5)
                lvl2 = int(xp**(1/4))
        except:
            user2 = "No User"
            rank2 = str(user2)
            msg2 = int(0)
            lvl2 = int(0)

        try:
            three = int(L[2])
            if users[str(three)]['transformation'] == True:
                user3 = names.get_full_name()
                rank3 = str(user3)
                xp = R[str(three)]
                msg3 = int(xp/5)
                lvl3 = int(xp**(1/4))
            else:
                user3 = self.bot.get_user(three)
                rank3 = str(user3)
                xp = R[str(three)]
                msg3 = int(xp/5)
                lvl3 = int(xp**(1/4))
        except:
            user3 = "No User"
            rank3 = str(user3)
            msg3 = int(0)
            lvl3 = int(0)

        try:
            four = int(L[3])
            if users[str(four)]['transformation'] == True:
                user4 = names.get_full_name()
                rank4 = str(user4)
                xp = R[str(four)]
                msg4 = int(xp/5)
                lvl4 = int(xp**(1/4))
            else:
                user4 = self.bot.get_user(four)
                rank4 = str(user4)
                xp = R[str(four)]
                msg4 = int(xp/5)
                lvl4 = int(xp**(1/4))
        except:
            user4 = "No User"
            rank4 = str(user4)
            msg4 = int(0)
            lvl4 = int(0)

        try:
            five = int(L[4])
            if users[str(five)]['transformation'] == True:
                user5 = names.get_full_name()
                rank5 = str(user5)
                xp = R[str(five)]
                msg5 = int(xp/5)
                lvl5 = int(xp**(1/4))
            else:
                user5 = self.bot.get_user(five)
                rank5 = str(user5)
                xp = R[str(five)]
                msg5 = int(xp/5)
                lvl5 = int(xp**(1/4))
        except:
            user5 = "No User"
            rank5 = str(user5)
            msg5 = int(0)
            lvl5 = int(0)

        theme = users[str(id)]['color']

        if theme == 9807270: #gray
            full_image = Image.open("./pictures/bg.jpg").convert("RGB").resize((850, 550))
        elif theme == 15158332 or theme == 10038562: #red
            full_image = Image.open("./pictures/red.jpg").convert("RGB").resize((850, 550))
        elif theme == 3447003 or theme == 2123412: #blue
            full_image = Image.open("./pictures/blue.jpg").convert("RGB").resize((850, 550))
        elif theme == 3066993 or theme == 2067276: #green
            full_image = Image.open("./pictures/green.jpg").convert("RGB").resize((850, 550))
        elif theme == 10181046 or theme == 7419530: #purple
            full_image = Image.open("./pictures/purple.jpg").convert("RGB").resize((850, 550))
        elif theme == 15844367 or theme == 12745742: #gold
            full_image = Image.open("./pictures/gold.jpg").convert("RGB").resize((850, 550))
        elif theme == 1752220 or theme == 1146986: #teal
            full_image = Image.open("./pictures/teal.png").convert("RGB").resize((850, 550))
        elif theme == 15105570 or theme == 11027200: #orange
            full_image = Image.open("./pictures/orange.jpg").convert("RGB").resize((850, 550))
        elif theme == 15277667 or theme == 11342935: #magenta
            full_image = Image.open("./pictures/magenta.jpg").convert("RGB").resize((850, 550))
        else: #gray
            full_image = Image.open("./pictures/bg.jpg").convert("RGB").resize((850, 550))

        theme = hex(theme).split('x')[-1]

        background = Image.new("RGB", (800, 500))
        draw = ImageDraw.Draw(background, "RGB")

        huge_font = ImageFont.FreeTypeFont("ABeeZee-Regular.otf", 35)
        big_font = ImageFont.FreeTypeFont("ABeeZee-Regular.otf", 20)
        small_font = ImageFont.FreeTypeFont("ABeeZee-Regular.otf", 20)
        little_font = ImageFont.FreeTypeFont("ABeeZee-Regular.otf", 10)

        #LEADERBOARD
        text_size = draw.textsize(f"LEADERBOARD", font=huge_font)
        offset_x = 800 - 280 - text_size[0]
        offset_y = 20
        draw.text((offset_x, offset_y), f"LEADERBOARD", font=huge_font, fill=f"#{theme}")

        #RANK
        text_size = draw.textsize(f"RANK", font=small_font)
        offset_x = 800 - 725 - text_size[0]
        offset_y = 90
        draw.text((offset_x, offset_y), f"RANK", font=small_font, fill=f"#{theme}")

        #LEVEL
        text_size = draw.textsize(f"LEVEL", font=small_font)
        offset_x = 800 - 250 - text_size[0]
        offset_y = 90
        draw.text((offset_x, offset_y), f"LEVEL", font=small_font, fill=f"#{theme}")

        #MESSAGES
        text_size = draw.textsize(f"MESSAGES", font=small_font)
        offset_x = 800 - 50 - text_size[0]
        offset_y = 90
        draw.text((offset_x, offset_y), f"MESSAGES", font=small_font, fill=f"#{theme}")

        #NAME
        text_size = draw.textsize(f"NAME", font=small_font)
        offset_x = 800 - 480 - text_size[0]
        offset_y = 90
        draw.text((offset_x, offset_y), f"NAME", font=small_font, fill=f"#{theme}")

        #User 1

        text_size = draw.textsize(f"1", font=big_font)
        offset_x = 800 - 750 - text_size[0]
        offset_y = 140
        draw.text((offset_x, offset_y), f"1", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{rank1}", font=big_font)
        offset_x = 800 - 450 - text_size[0]
        offset_y = 140
        draw.text((offset_x, offset_y), f"{rank1}", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{lvl1}", font=big_font)
        offset_x = 800 - 260 - text_size[0]
        offset_y = 140
        draw.text((offset_x, offset_y), f"{lvl1}", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{LevelCog.human_format(self, msg1)}", font=big_font)
        offset_x = 800 - 60 - text_size[0]
        offset_y = 140
        draw.text((offset_x, offset_y), f"{LevelCog.human_format(self, msg1)}", font=big_font, fill="#fff")

        #User 2

        text_size = draw.textsize(f"2", font=big_font)
        offset_x = 800 - 750 - text_size[0]
        offset_y = 210
        draw.text((offset_x, offset_y), f"2", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{rank2}", font=big_font)
        offset_x = 800 - 450 - text_size[0]
        offset_y = 210
        draw.text((offset_x, offset_y), f"{rank2}", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{lvl2}", font=big_font)
        offset_x = 800 - 260 - text_size[0]
        offset_y = 210
        draw.text((offset_x, offset_y), f"{lvl2}", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{LevelCog.human_format(self, msg2)}", font=big_font)
        offset_x = 800 - 60 - text_size[0]
        offset_y = 210
        draw.text((offset_x, offset_y), f"{LevelCog.human_format(self, msg2)}", font=big_font, fill="#fff")

        #User 3

        text_size = draw.textsize(f"3", font=big_font)
        offset_x = 800 - 750 - text_size[0]
        offset_y = 280
        draw.text((offset_x, offset_y), f"3", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{rank3}", font=big_font)
        offset_x = 800 - 450 - text_size[0]
        offset_y = 280
        draw.text((offset_x, offset_y), f"{rank3}", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{lvl3}", font=big_font)
        offset_x = 800 - 260 - text_size[0]
        offset_y = 280
        draw.text((offset_x, offset_y), f"{lvl3}", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{LevelCog.human_format(self, msg3)}", font=big_font)
        offset_x = 800 - 60 - text_size[0]
        offset_y = 280
        draw.text((offset_x, offset_y), f"{LevelCog.human_format(self, msg3)}", font=big_font, fill="#fff")

        #User 4

        text_size = draw.textsize(f"4", font=big_font)
        offset_x = 800 - 750 - text_size[0]
        offset_y = 350
        draw.text((offset_x, offset_y), f"4", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{rank4}", font=big_font)
        offset_x = 800 - 450 - text_size[0]
        offset_y = 350
        draw.text((offset_x, offset_y), f"{rank4}", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{lvl4}", font=big_font)
        offset_x = 800 - 260 - text_size[0]
        offset_y = 350
        draw.text((offset_x, offset_y), f"{lvl4}", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{LevelCog.human_format(self, msg4)}", font=big_font)
        offset_x = 800 - 60 - text_size[0]
        offset_y = 350
        draw.text((offset_x, offset_y), f"{LevelCog.human_format(self, msg4)}", font=big_font, fill="#fff")

        #User 5

        text_size = draw.textsize(f"5", font=big_font)
        offset_x = 800 - 750 - text_size[0]
        offset_y = 420
        draw.text((offset_x, offset_y), f"5", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{rank5}", font=big_font)
        offset_x = 800 - 450 - text_size[0]
        offset_y = 420
        draw.text((offset_x, offset_y), f"{rank5}", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{lvl5}", font=big_font)
        offset_x = 800 - 260 - text_size[0]
        offset_y = 420
        draw.text((offset_x, offset_y), f"{lvl5}", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{LevelCog.human_format(self, msg5)}", font=big_font)
        offset_x = 800 - 60 - text_size[0]
        offset_y = 420
        draw.text((offset_x, offset_y), f"{LevelCog.human_format(self, msg5)}", font=big_font, fill="#fff")

        img_w, img_h = background.size
        bg_w, bg_h = full_image.size
        offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)

        full_image.paste(background, offset)

        full_image.save("leader.jpg", quality=100)
        file = discord.File("./leader.jpg")

        await message.channel.send(file=file)
        os.remove("./leader.jpg")

    @commands.command(name = "leader2", aliases = ["leaderboard2", "Leaderboard2", "LEADERBOARD2", "Leader2", "LEADER2", "lb2", "LB2", "Lb2"])
    async def leader2(self, message : discord.Message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        R={}
        for i in users:
            user = i
            exp = users[i]['experience']
            R[user]=exp
        R = dict(sorted(R.items(), key=lambda item: item[1], reverse=True))
        L= list(R)
        
        for i in L:
            if users[str(i)]['chameleon'] == True:
                L.remove(i)

        try:
            six = int(L[5])
            if users[str(six)]['transformation'] == True:
                user6 = names.get_full_name()
                rank6 = str(user6)
                xp = R[str(six)]
                msg6 = int(xp/5)
                lvl6 = int(xp**(1/4))
            else:
                user6 = self.bot.get_user(six)
                rank6 = str(user6)
                xp = R[str(six)]
                msg6 = int(xp/5)
                lvl6 = int(xp**(1/4))
        except:
            user6 = "No User"
            rank6 = str(user6)
            msg6 = int(0)
            lvl6 = int(0)

        try:
            seven = int(L[6])
            if users[str(seven)]['transformation'] == True:
                user7 = names.get_full_name()
                rank7 = str(user7)
                xp = R[str(seven)]
                msg7 = int(xp/5)
                lvl7 = int(xp**(1/4))
            else:
                user7 = self.bot.get_user(seven)
                rank7 = str(user7)
                xp = R[str(seven)]
                msg7 = int(xp/5)
                lvl7 = int(xp**(1/4))
        except:
            user7 = "No User"
            rank7 = str(user7)
            msg7 = int(0)
            lvl7 = int(0)

        try:
            eight = int(L[7])
            if users[str(eight)]['transformation'] == True:
                user8 = names.get_full_name()
                rank8 = str(user8)
                xp = R[str(eight)]
                msg8 = int(xp/5)
                lvl8 = int(xp**(1/4))
            else:
                user8 = self.bot.get_user(eight)
                rank8 = str(user8)
                xp = R[str(eight)]
                msg8 = int(xp/5)
                lvl8 = int(xp**(1/4))
        except:
            user8 = "No User"
            rank8 = str(user8)
            msg8 = int(0)
            lvl8 = int(0)

        try:
            nine = int(L[8])
            if users[str(nine)]['transformation'] == True:
                user9 = names.get_full_name()
                rank9 = str(user9)
                xp = R[str(nine)]
                msg9 = int(xp/5)
                lvl9 = int(xp**(1/4))
            else:
                user9 = self.bot.get_user(nine)
                rank9 = str(user9)
                xp = R[str(nine)]
                msg9 = int(xp/5)
                lvl9 = int(xp**(1/4))
        except:
            user9 = "No User"
            rank9 = str(user9)
            msg9 = int(0)
            lvl9 = int(0)

        try:
            ten = int(L[9])
            if users[str(ten)]['transformation'] == True:
                user10 = names.get_full_name()
                rank10 = str(user10)
                xp = R[str(ten)]
                msg10 = int(xp/5)
                lvl10 = int(xp**(1/4))
            else:
                user10 = self.bot.get_user(ten)
                rank10 = str(user10)
                xp = R[str(ten)]
                msg10 = int(xp/5)
                lvl10 = int(xp**(1/4))
        except:
            user10 = "No User"
            rank10 = str(user10)
            msg10 = int(0)
            lvl10 = int(0)

        theme = users[str(id)]['color']

        if theme == 9807270: #gray
            full_image = Image.open("./pictures/bg.jpg").convert("RGB").resize((850, 550))
        elif theme == 15158332 or theme == 10038562: #red
            full_image = Image.open("./pictures/red.jpg").convert("RGB").resize((850, 550))
        elif theme == 3447003 or theme == 2123412: #blue
            full_image = Image.open("./pictures/blue.jpg").convert("RGB").resize((850, 550))
        elif theme == 3066993 or theme == 2067276: #green
            full_image = Image.open("./pictures/green.jpg").convert("RGB").resize((850, 550))
        elif theme == 10181046 or theme == 7419530: #purple
            full_image = Image.open("./pictures/purple.jpg").convert("RGB").resize((850, 550))
        elif theme == 15844367 or theme == 12745742: #gold
            full_image = Image.open("./pictures/gold.jpg").convert("RGB").resize((850, 550))
        elif theme == 1752220 or theme == 1146986: #teal
            full_image = Image.open("./pictures/teal.png").convert("RGB").resize((850, 550))
        elif theme == 15105570 or theme == 11027200: #orange
            full_image = Image.open("./pictures/orange.jpg").convert("RGB").resize((850, 550))
        elif theme == 15277667 or theme == 11342935: #magenta
            full_image = Image.open("./pictures/magenta.jpg").convert("RGB").resize((850, 550))
        else: #gray
            full_image = Image.open("./pictures/bg.jpg").convert("RGB").resize((850, 550))

        theme = hex(theme).split('x')[-1]

        background = Image.new("RGB", (800, 500))
        draw = ImageDraw.Draw(background, "RGB")

        huge_font = ImageFont.FreeTypeFont("ABeeZee-Regular.otf", 35)
        big_font = ImageFont.FreeTypeFont("ABeeZee-Regular.otf", 20)
        small_font = ImageFont.FreeTypeFont("ABeeZee-Regular.otf", 20)

        #LEADERBOARD
        text_size = draw.textsize(f"LEADERBOARD", font=huge_font)
        offset_x = 800 - 280 - text_size[0]
        offset_y = 20
        draw.text((offset_x, offset_y), f"LEADERBOARD", font=huge_font, fill=f"#{theme}")

        #RANK
        text_size = draw.textsize(f"RANK", font=small_font)
        offset_x = 800 - 725 - text_size[0]
        offset_y = 90
        draw.text((offset_x, offset_y), f"RANK", font=small_font, fill=f"#{theme}")

        #LEVEL
        text_size = draw.textsize(f"LEVEL", font=small_font)
        offset_x = 800 - 250 - text_size[0]
        offset_y = 90
        draw.text((offset_x, offset_y), f"LEVEL", font=small_font, fill=f"#{theme}")

        #MESSAGES
        text_size = draw.textsize(f"MESSAGES", font=small_font)
        offset_x = 800 - 50 - text_size[0]
        offset_y = 90
        draw.text((offset_x, offset_y), f"MESSAGES", font=small_font, fill=f"#{theme}")

        #NAME
        text_size = draw.textsize(f"NAME", font=small_font)
        offset_x = 800 - 480 - text_size[0]
        offset_y = 90
        draw.text((offset_x, offset_y), f"NAME", font=small_font, fill=f"#{theme}")

        #User 6

        text_size = draw.textsize(f"6", font=big_font)
        offset_x = 800 - 750 - text_size[0]
        offset_y = 140
        draw.text((offset_x, offset_y), f"6", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{rank6}", font=big_font)
        offset_x = 800 - 450 - text_size[0]
        offset_y = 140
        draw.text((offset_x, offset_y), f"{rank6}", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{lvl6}", font=big_font)
        offset_x = 800 - 260 - text_size[0]
        offset_y = 140
        draw.text((offset_x, offset_y), f"{lvl6}", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{LevelCog.human_format(self, msg6)}", font=big_font)
        offset_x = 800 - 60 - text_size[0]
        offset_y = 140
        draw.text((offset_x, offset_y), f"{LevelCog.human_format(self, msg6)}", font=big_font, fill="#fff")

        #User 7

        text_size = draw.textsize(f"7", font=big_font)
        offset_x = 800 - 750 - text_size[0]
        offset_y = 210
        draw.text((offset_x, offset_y), f"7", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{rank7}", font=big_font)
        offset_x = 800 - 450 - text_size[0]
        offset_y = 210
        draw.text((offset_x, offset_y), f"{rank7}", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{lvl7}", font=big_font)
        offset_x = 800 - 260 - text_size[0]
        offset_y = 210
        draw.text((offset_x, offset_y), f"{lvl7}", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{LevelCog.human_format(self, msg7)}", font=big_font)
        offset_x = 800 - 60 - text_size[0]
        offset_y = 210
        draw.text((offset_x, offset_y), f"{LevelCog.human_format(self, msg7)}", font=big_font, fill="#fff")

        #User 8

        text_size = draw.textsize(f"8", font=big_font)
        offset_x = 800 - 750 - text_size[0]
        offset_y = 280
        draw.text((offset_x, offset_y), f"8", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{rank8}", font=big_font)
        offset_x = 800 - 450 - text_size[0]
        offset_y = 280
        draw.text((offset_x, offset_y), f"{rank8}", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{lvl8}", font=big_font)
        offset_x = 800 - 260 - text_size[0]
        offset_y = 280
        draw.text((offset_x, offset_y), f"{lvl8}", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{LevelCog.human_format(self, msg8)}", font=big_font)
        offset_x = 800 - 60 - text_size[0]
        offset_y = 280
        draw.text((offset_x, offset_y), f"{LevelCog.human_format(self, msg8)}", font=big_font, fill="#fff")

        #User 9

        text_size = draw.textsize(f"9", font=big_font)
        offset_x = 800 - 750 - text_size[0]
        offset_y = 350
        draw.text((offset_x, offset_y), f"9", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{rank9}", font=big_font)
        offset_x = 800 - 450 - text_size[0]
        offset_y = 350
        draw.text((offset_x, offset_y), f"{rank9}", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{lvl9}", font=big_font)
        offset_x = 800 - 260 - text_size[0]
        offset_y = 350
        draw.text((offset_x, offset_y), f"{lvl9}", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{LevelCog.human_format(self, msg9)}", font=big_font)
        offset_x = 800 - 60 - text_size[0]
        offset_y = 350
        draw.text((offset_x, offset_y), f"{LevelCog.human_format(self, msg9)}", font=big_font, fill="#fff")

        #User 10

        text_size = draw.textsize(f"10", font=big_font)
        offset_x = 800 - 750 - text_size[0]
        offset_y = 420
        draw.text((offset_x, offset_y), f"10", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{rank10}", font=big_font)
        offset_x = 800 - 450 - text_size[0]
        offset_y = 420
        draw.text((offset_x, offset_y), f"{rank10}", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{lvl10}", font=big_font)
        offset_x = 800 - 260 - text_size[0]
        offset_y = 420
        draw.text((offset_x, offset_y), f"{lvl10}", font=big_font, fill="#fff")

        text_size = draw.textsize(f"{LevelCog.human_format(self, msg10)}", font=big_font)
        offset_x = 800 - 60 - text_size[0]
        offset_y = 420
        draw.text((offset_x, offset_y), f"{LevelCog.human_format(self, msg10)}", font=big_font, fill="#fff")
        
        img_w, img_h = background.size
        bg_w, bg_h = full_image.size
        offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)

        full_image.paste(background, offset)

        full_image.save("leader.jpg", quality=100)
        file = discord.File("./leader2.jpg")

        await message.channel.send(file=file)
        os.remove("./leader2.jpg")


def setup(bot):
    bot.add_cog(LevelCog(bot))
