import discord
from discord.ext import commands
import os
import datetime
import json
import names
from discord import message
from discord.ext.commands.context import Context
from PIL import Image, ImageDraw, ImageFont
import asyncio


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

    @commands.command(name="level", aliases=["rank", "Level", "LEVEL", "Rank", "RANK"])
    async def level(self, ctx, member: discord.Member = None):

        guildid = ctx.message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        if not member:
            id = ctx.message.author.id
            with open(guildid, 'r') as f:
                users = json.load(f)

            R = {}
            for i in users:
                user = i
                exp = users[i]['experience']
                R[user] = exp
            R = dict(sorted(R.items(), key=lambda item: item[1], reverse=True))
            L = list(R)
            theme = users[str(id)]['color']
            rank = L.index(str(id))+1
            level = users[str(id)]['level']
            currentxp = users[str(id)]['experience']
            xp = currentxp
            final_xp = (int(level)+1) ** 4
            user_name = f"@{ctx.author.name}"
            discriminator = "#"+ctx.author.discriminator
            await ctx.message.author.avatar.save(("logo.jpg"))

            level = LevelCog.human_format(self, level)

            if theme == 9807270:  # gray
                full_image = Image.open(
                    "./pictures/bg.jpg").convert("RGB").resize((1060, 320))
            elif theme == 15158332 or theme == 10038562:  # red
                full_image = Image.open(
                    "./pictures/red.jpg").convert("RGB").resize((1060, 320))
            elif theme == 3447003 or theme == 2123412:  # blue
                full_image = Image.open(
                    "./pictures/blue.jpg").convert("RGB").resize((1060, 320))
            elif theme == 3066993 or theme == 2067276:  # green
                full_image = Image.open(
                    "./pictures/green.jpg").convert("RGB").resize((1060, 320))
            elif theme == 10181046 or theme == 7419530:  # purple
                full_image = Image.open(
                    "./pictures/purple.jpg").convert("RGB").resize((1060, 320))
            elif theme == 15844367 or theme == 12745742:  # gold
                full_image = Image.open(
                    "./pictures/gold.jpg").convert("RGB").resize((1060, 320))
            elif theme == 1752220 or theme == 1146986:  # teal
                full_image = Image.open(
                    "./pictures/teal.png").convert("RGB").resize((1060, 320))
            elif theme == 15105570 or theme == 11027200:  # orange
                full_image = Image.open(
                    "./pictures/orange.jpg").convert("RGB").resize((1060, 320))
            elif theme == 15277667 or theme == 11342935:  # magenta
                full_image = Image.open(
                    "./pictures/magenta.jpg").convert("RGB").resize((1060, 320))
            else:  # gray
                full_image = Image.open(
                    "./pictures/bg.jpg").convert("RGB").resize((1060, 320))

            background = Image.new("RGB", (1000, 240))

            theme = hex(theme).split('x')[-1]

            try:
                logo = Image.open("logo.jpg").convert("RGB").resize((180, 180))
            except:
                logo = Image.open(
                    "./pictures/discord.png").convert("RGB").resize((180, 180))
            bigsize = (logo.size[0] * 3, logo.size[1] * 3)
            mask = Image.new("L", bigsize, 0)

            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + bigsize, 255)

            draw.ellipse((140 * 3, 140 * 3, 189 * 3, 189 * 3), 0)

            mask = mask.resize(logo.size, Image.Resampling.LANCZOS)
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

            text_size = draw.textlength(str(level), font=big_font)
            offset_x = 1000 - 15 - round(text_size)
            offset_y = 10
            draw.text((offset_x, offset_y), str(level),
                      font=big_font, fill=f"#{theme}")

            text_size = draw.textlength("LEVEL", font=small_font)
            offset_x -= text_size + 5
            draw.text((offset_x, offset_y + 27), "LEVEL",
                      font=small_font, fill=f"#{theme}")

            text_size = draw.textlength(f"#{rank}", font=big_font)
            offset_x -= text_size + 15
            draw.text((offset_x, offset_y),
                      f"#{rank}", font=big_font, fill="#fff")

            text_size = draw.textlength("RANK", font=small_font)
            offset_x -= text_size + 5
            draw.text((offset_x, offset_y + 27), "RANK",
                      font=small_font, fill="#fff")

            bar_offset_x = 320
            bar_offset_y = 160
            bar_offset_x_1 = 950
            bar_offset_y_1 = 200
            circle_size = bar_offset_y_1 - bar_offset_y

            draw.rectangle((bar_offset_x, bar_offset_y,
                           bar_offset_x_1, bar_offset_y_1), fill="#727175")

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

            draw.rectangle((bar_offset_x, bar_offset_y,
                           bar_offset_x_1, bar_offset_y_1), fill=f"#{theme}")

            draw.ellipse(
                (bar_offset_x - circle_size // 2, bar_offset_y, bar_offset_x + circle_size // 2, bar_offset_y_1), fill=f"#{theme}"
            )

            draw.ellipse(
                (bar_offset_x_1 - circle_size // 2, bar_offset_y, bar_offset_x_1 + circle_size // 2, bar_offset_y_1), fill=f"#{theme}"
            )

            text_size = draw.textlength(
                f"/ {LevelCog.human_format(self, final_xp)} XP", font=small_font)

            offset_x = 950 - text_size
            offset_y = bar_offset_y - text_size + 100

            draw.text((offset_x, offset_y),
                      f"/ {LevelCog.human_format(self, final_xp)} XP", font=small_font, fill="#727175")

            text_size = draw.textlength(
                f"{LevelCog.human_format(self, xp)}", font=small_font)
            offset_x -= text_size + 8
            draw.text((offset_x, offset_y),
                      f"{LevelCog.human_format(self, xp)}", font=small_font, fill="#fff")

            text_size = draw.textlength(user_name, font=medium_font)

            offset_x = bar_offset_x
            offset_y = bar_offset_y - text_size + 270
            draw.text((offset_x, offset_y), user_name,
                      font=medium_font, fill="#fff")

            img_w, img_h = background.size
            bg_w, bg_h = full_image.size
            offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)

            full_image.paste(background, offset)

            full_image.save("image.jpg", quality=100)
            file = discord.File("image.jpg", filename="level.jpg")
            await ctx.send(file=file)
            os.remove("image.jpg")
            os.remove("logo.jpg")

        else:
            id = member.id
            with open(guildid, 'r') as f:
                users = json.load(f)

            R = {}
            for i in users:
                user = i
                exp = users[i]['experience']
                R[user] = exp
            R = dict(sorted(R.items(), key=lambda item: item[1], reverse=True))
            L = list(R)
            theme = users[str(id)]['color']
            rank = L.index(str(id))+1
            level = users[str(id)]['level']
            currentxp = users[str(id)]['experience']
            xp = currentxp
            final_xp = (int(level)+1) ** 4
            card_user = self.bot.get_user(id)
            user_name = card_user.name
            discriminator = "#"+card_user.discriminator
            await card_user.avatar.save(("logo.jpg"))

            level = LevelCog.human_format(self, level)

            if theme == 9807270:  # gray
                full_image = Image.open(
                    "./pictures/bg.jpg").convert("RGB").resize((1060, 320))
            elif theme == 15158332 or theme == 10038562:  # red
                full_image = Image.open(
                    "./pictures/red.jpg").convert("RGB").resize((1060, 320))
            elif theme == 3447003 or theme == 2123412:  # blue
                full_image = Image.open(
                    "./pictures/blue.jpg").convert("RGB").resize((1060, 320))
            elif theme == 3066993 or theme == 2067276:  # green
                full_image = Image.open(
                    "./pictures/green.jpg").convert("RGB").resize((1060, 320))
            elif theme == 10181046 or theme == 7419530:  # purple
                full_image = Image.open(
                    "./pictures/purple.jpg").convert("RGB").resize((1060, 320))
            elif theme == 15844367 or theme == 12745742:  # gold
                full_image = Image.open(
                    "./pictures/gold.jpg").convert("RGB").resize((1060, 320))
            elif theme == 1752220 or theme == 1146986:  # teal
                full_image = Image.open(
                    "./pictures/teal.png").convert("RGB").resize((1060, 320))
            elif theme == 15105570 or theme == 11027200:  # orange
                full_image = Image.open(
                    "./pictures/orange.jpg").convert("RGB").resize((1060, 320))
            elif theme == 15277667 or theme == 11342935:  # magenta
                full_image = Image.open(
                    "./pictures/magenta.jpg").convert("RGB").resize((1060, 320))
            else:  # gray
                full_image = Image.open(
                    "./pictures/bg.jpg").convert("RGB").resize((1060, 320))

            background = Image.new("RGB", (1000, 240))

            theme = hex(theme).split('x')[-1]

            try:
                logo = Image.open("logo.jpg").convert("RGB").resize((180, 180))
            except:
                logo = Image.open(
                    "./pictures/discord.png").convert("RGB").resize((180, 180))
            bigsize = (logo.size[0] * 3, logo.size[1] * 3)
            mask = Image.new("L", bigsize, 0)

            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + bigsize, 255)

            draw.ellipse((140 * 3, 140 * 3, 189 * 3, 189 * 3), 0)

            mask = mask.resize(logo.size, Image.Resampling.LANCZOS)
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

            text_size = draw.textlength(str(level), font=big_font)
            offset_x = 1000 - 15 - text_size
            offset_y = 10
            draw.text((offset_x, offset_y), str(level),
                      font=big_font, fill=f"#{theme}")

            text_size = draw.textlength("LEVEL", font=small_font)
            offset_x -= text_size + 5
            draw.text((offset_x, offset_y + 27), "LEVEL",
                      font=small_font, fill=f"#{theme}")

            text_size = draw.textlength(f"#{rank}", font=big_font)
            offset_x -= text_size + 15
            draw.text((offset_x, offset_y),
                      f"#{rank}", font=big_font, fill="#fff")

            text_size = draw.textlength("RANK", font=small_font)
            offset_x -= text_size + 5
            draw.text((offset_x, offset_y + 27), "RANK",
                      font=small_font, fill="#fff")

            bar_offset_x = 320
            bar_offset_y = 160
            bar_offset_x_1 = 950
            bar_offset_y_1 = 200
            circle_size = bar_offset_y_1 - bar_offset_y

            draw.rectangle((bar_offset_x, bar_offset_y,
                           bar_offset_x_1, bar_offset_y_1), fill="#727175")

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

            draw.rectangle((bar_offset_x, bar_offset_y,
                           bar_offset_x_1, bar_offset_y_1), fill=f"#{theme}")

            draw.ellipse(
                (bar_offset_x - circle_size // 2, bar_offset_y, bar_offset_x + circle_size // 2, bar_offset_y_1), fill=f"#{theme}"
            )

            draw.ellipse(
                (bar_offset_x_1 - circle_size // 2, bar_offset_y, bar_offset_x_1 + circle_size // 2, bar_offset_y_1), fill=f"#{theme}"
            )

            text_size = draw.textlength(
                f"/ {LevelCog.human_format(self, final_xp)} XP", font=small_font)

            offset_x = 950 - text_size
            offset_y = bar_offset_y - text_size - 14

            draw.text((offset_x, offset_y),
                      f"/ {LevelCog.human_format(self, final_xp)} XP", font=small_font, fill="#727175")

            text_size = draw.textlength(
                f"{LevelCog.human_format(self, xp)}", font=small_font)
            offset_x -= text_size + 8
            draw.text((offset_x, offset_y),
                      f"{LevelCog.human_format(self, xp)}", font=small_font, fill="#fff")

            text_size = draw.textlength(user_name, font=medium_font)

            offset_x = bar_offset_x
            offset_y = bar_offset_y - text_size - 14
            draw.text((offset_x, offset_y), user_name,
                      font=medium_font, fill="#fff")

            offset_x += text_size + 5
            offset_y += 10

            draw.text((offset_x, offset_y), discriminator,
                      font=small_font, fill="#727175")

            img_w, img_h = background.size
            bg_w, bg_h = full_image.size
            offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)

            full_image.paste(background, offset)

            full_image.save("image.jpg", quality=100)
            file = discord.File("image.jpg", filename="level.jpg")
            await ctx.send(file=file)
            os.remove("image.jpg")
            os.remove("logo.jpg")

    @commands.command(aliases=["lb", "leader"])
    async def leaderboard(self, ctx):

        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        R = {}
        for i in users:
            user = i
            exp = users[i]['experience']
            R[user] = exp
        R = dict(sorted(R.items(), key=lambda item: item[1], reverse=True))
        L = list(R)

        if len(L) <= 5:
            embed = discord.Embed(description=f"**Server must have 5+ members for this command**\nCurrent members = {len(L)}\n\n**Note** : You can instead use `=top` command to see top 5 users in the server",
                                  color=color,
                                  timestamp=datetime.datetime.utcnow())

            embed.set_author(name=ctx.author.name,
                             icon_url=ctx.author.avatar.url)

            await ctx.send(embed=embed)

        else:
            for i in L:
                if users[str(i)]['chameleon'] == True:
                    L.remove(i)

                else:
                    i = int(i)
                    index = L.index(f"{i}")
                    L[index] = i

            for i in range(5):
                L.pop(0)

            all = ""
            count = 5
            for i in L:
                count += 1

                with open(guildid, 'r') as g:
                    users_check = json.load(g)

                if isinstance(i, int):

                    if users_check[str(i)]['transformation'] == True:
                        if "transform" in users_check[str(i)]:
                            if users_check[str(i)]["transform"] != None:
                                transform = users_check[str(i)]["transform"]

                        else:
                            transform = names.get_full_name()

                        xp = users_check[str(i)]['experience']
                        i = f"**{transform}**"

                    else:
                        xp = users_check[str(i)]['experience']
                        i = f"<@{i}>"

                all += f"**{count}.** {i} : `{xp} XP`\n"

            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(ctx.guild.id) in L:
                get_prefix = L[str(ctx.guild.id)]["prefix"]
            elif str(ctx.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(title=f"Server Leaderboard",
                                  description=f"For **Top 5** members, use : `{get_prefix}top`\n\n{all}",
                                  color=color,
                                  timestamp=datetime.datetime.utcnow())

            await ctx.send(embed=embed)

    @commands.command(aliases=["top5"])
    async def top(self, ctx):

        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        R = {}
        for i in users:
            user = i
            exp = users[i]['experience']
            R[user] = exp
        R = dict(sorted(R.items(), key=lambda item: item[1], reverse=True))
        L = list(R)

        for i in L:
            if users[str(i)]['chameleon'] == True:
                L.remove(i)

        try:
            one = int(L[0])
            if users[str(one)]['transformation'] == True:
                if "transform" in users[str(one)]:
                    if users[str(one)]["transform"] != None:
                        user1 = users[str(one)]["transform"]
                else:
                    user1 = names.get_full_name()
                rank1 = str(user1)
                xp = R[str(one)]
                msg1 = int(xp)
                lvl1 = int(xp**(1/4))
            else:
                user1 = self.bot.get_user(one)
                rank1 = str(user1)
                xp = R[str(one)]
                msg1 = int(xp)
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
                if "transform" in users[str(two)]:
                    if users[str(two)]["transform"] != None:
                        user2 = users[str(two)]["transform"]
                else:
                    user2 = names.get_full_name()
                rank2 = str(user2)
                xp = R[str(two)]
                msg2 = int(xp)
                lvl2 = int(xp**(1/4))
            else:
                user2 = self.bot.get_user(two)
                rank2 = str(user2)
                xp = R[str(two)]
                msg2 = int(xp)
                lvl2 = int(xp**(1/4))
        except:
            user2 = "No User"
            rank2 = str(user2)
            msg2 = int(0)
            lvl2 = int(0)

        try:
            three = int(L[2])
            if users[str(three)]['transformation'] == True:
                if "transform" in users[str(three)]:
                    if users[str(three)]["transform"] != None:
                        user3 = users[str(three)]["transform"]
                else:
                    user3 = names.get_full_name()
                rank3 = str(user3)
                xp = R[str(three)]
                msg3 = int(xp)
                lvl3 = int(xp**(1/4))
            else:
                user3 = self.bot.get_user(three)
                rank3 = str(user3)
                xp = R[str(three)]
                msg3 = int(xp)
                lvl3 = int(xp**(1/4))
        except:
            user3 = "No User"
            rank3 = str(user3)
            msg3 = int(0)
            lvl3 = int(0)

        try:
            four = int(L[3])
            if users[str(four)]['transformation'] == True:
                if "transform" in users[str(four)]:
                    if users[str(four)]["transform"] != None:
                        user4 = users[str(four)]["transform"]
                else:
                    user4 = names.get_full_name()
                rank4 = str(user4)
                xp = R[str(four)]
                msg4 = int(xp)
                lvl4 = int(xp**(1/4))
            else:
                user4 = self.bot.get_user(four)
                rank4 = str(user4)
                xp = R[str(four)]
                msg4 = int(xp)
                lvl4 = int(xp**(1/4))
        except:
            user4 = "No User"
            rank4 = str(user4)
            msg4 = int(0)
            lvl4 = int(0)

        try:
            five = int(L[4])
            if users[str(five)]['transformation'] == True:
                if "transform" in users[str(five)]:
                    if users[str(five)]["transform"] != None:
                        user5 = users[str(five)]["transform"]
                else:
                    user5 = names.get_full_name()
                rank5 = str(user5)
                xp = R[str(five)]
                msg5 = int(xp)
                lvl5 = int(xp**(1/4))
            else:
                user5 = self.bot.get_user(five)
                rank5 = str(user5)
                xp = R[str(five)]
                msg5 = int(xp)
                lvl5 = int(xp**(1/4))
        except:
            user5 = "No User"
            rank5 = str(user5)
            msg5 = int(0)
            lvl5 = int(0)

        theme = users[str(id)]['color']

        if theme == 9807270:  # gray
            full_image = Image.open(
                "./pictures/bg.jpg").convert("RGB").resize((850, 550))
        elif theme == 15158332 or theme == 10038562:  # red
            full_image = Image.open(
                "./pictures/red.jpg").convert("RGB").resize((850, 550))
        elif theme == 3447003 or theme == 2123412:  # blue
            full_image = Image.open(
                "./pictures/blue.jpg").convert("RGB").resize((850, 550))
        elif theme == 3066993 or theme == 2067276:  # green
            full_image = Image.open(
                "./pictures/green.jpg").convert("RGB").resize((850, 550))
        elif theme == 10181046 or theme == 7419530:  # purple
            full_image = Image.open(
                "./pictures/purple.jpg").convert("RGB").resize((850, 550))
        elif theme == 15844367 or theme == 12745742:  # gold
            full_image = Image.open(
                "./pictures/gold.jpg").convert("RGB").resize((850, 550))
        elif theme == 1752220 or theme == 1146986:  # teal
            full_image = Image.open(
                "./pictures/teal.png").convert("RGB").resize((850, 550))
        elif theme == 15105570 or theme == 11027200:  # orange
            full_image = Image.open(
                "./pictures/orange.jpg").convert("RGB").resize((850, 550))
        elif theme == 15277667 or theme == 11342935:  # magenta
            full_image = Image.open(
                "./pictures/magenta.jpg").convert("RGB").resize((850, 550))
        else:  # gray
            full_image = Image.open(
                "./pictures/bg.jpg").convert("RGB").resize((850, 550))

        theme = hex(theme).split('x')[-1]

        background = Image.new("RGB", (800, 500))
        draw = ImageDraw.Draw(background, "RGB")

        huge_font = ImageFont.FreeTypeFont("ABeeZee-Regular.otf", 35)
        big_font = ImageFont.FreeTypeFont("ABeeZee-Regular.otf", 20)
        small_font = ImageFont.FreeTypeFont("ABeeZee-Regular.otf", 20)
        little_font = ImageFont.FreeTypeFont("ABeeZee-Regular.otf", 10)

        # LEADERBOARD
        text_size = draw.textlength(f"LEADERBOARD", font=huge_font)
        offset_x = 800 - 280 - text_size
        offset_y = 20
        draw.text((offset_x, offset_y), f"LEADERBOARD",
                  font=huge_font, fill=f"#{theme}")

        # RANK
        text_size = draw.textlength(f"RANK", font=small_font)
        offset_x = 800 - 725 - text_size
        offset_y = 90
        draw.text((offset_x, offset_y), f"RANK",
                  font=small_font, fill=f"#{theme}")

        # LEVEL
        text_size = draw.textlength(f"LEVEL", font=small_font)
        offset_x = 800 - 250 - text_size
        offset_y = 90
        draw.text((offset_x, offset_y), f"LEVEL",
                  font=small_font, fill=f"#{theme}")

        # XP
        text_size = draw.textlength(f"XP", font=small_font)
        offset_x = 800 - 75 - text_size
        offset_y = 90
        draw.text((offset_x, offset_y), f"XP",
                  font=small_font, fill=f"#{theme}")

        # NAME
        text_size = draw.textlength(f"NAME", font=small_font)
        offset_x = 800 - 480 - text_size
        offset_y = 90
        draw.text((offset_x, offset_y), f"NAME",
                  font=small_font, fill=f"#{theme}")

        # User 1

        text_size = draw.textlength(f"1", font=big_font)
        offset_x = 800 - 750 - text_size
        offset_y = 140
        draw.text((offset_x, offset_y), f"1", font=big_font, fill="#fff")

        text_size = draw.textlength(f"{rank1}", font=big_font)
        offset_x = 800 - 450 - text_size
        offset_y = 140
        draw.text((offset_x, offset_y), f"{rank1}", font=big_font, fill="#fff")

        text_size = draw.textlength(f"{lvl1}", font=big_font)
        offset_x = 800 - 260 - text_size
        offset_y = 140
        draw.text((offset_x, offset_y), f"{lvl1}", font=big_font, fill="#fff")

        text_size = draw.textlength(
            f"{LevelCog.human_format(self, msg1)}", font=big_font)
        offset_x = 800 - 60 - text_size
        offset_y = 140
        draw.text((offset_x, offset_y),
                  f"{LevelCog.human_format(self, msg1)}", font=big_font, fill="#fff")

        # User 2

        text_size = draw.textlength(f"2", font=big_font)
        offset_x = 800 - 750 - text_size
        offset_y = 210
        draw.text((offset_x, offset_y), f"2", font=big_font, fill="#fff")

        text_size = draw.textlength(f"{rank2}", font=big_font)
        offset_x = 800 - 450 - text_size
        offset_y = 210
        draw.text((offset_x, offset_y), f"{rank2}", font=big_font, fill="#fff")

        text_size = draw.textlength(f"{lvl2}", font=big_font)
        offset_x = 800 - 260 - text_size
        offset_y = 210
        draw.text((offset_x, offset_y), f"{lvl2}", font=big_font, fill="#fff")

        text_size = draw.textlength(
            f"{LevelCog.human_format(self, msg2)}", font=big_font)
        offset_x = 800 - 60 - text_size
        offset_y = 210
        draw.text((offset_x, offset_y),
                  f"{LevelCog.human_format(self, msg2)}", font=big_font, fill="#fff")

        # User 3

        text_size = draw.textlength(f"3", font=big_font)
        offset_x = 800 - 750 - text_size
        offset_y = 280
        draw.text((offset_x, offset_y), f"3", font=big_font, fill="#fff")

        text_size = draw.textlength(f"{rank3}", font=big_font)
        offset_x = 800 - 450 - text_size
        offset_y = 280
        draw.text((offset_x, offset_y), f"{rank3}", font=big_font, fill="#fff")

        text_size = draw.textlength(f"{lvl3}", font=big_font)
        offset_x = 800 - 260 - text_size
        offset_y = 280
        draw.text((offset_x, offset_y), f"{lvl3}", font=big_font, fill="#fff")

        text_size = draw.textlength(
            f"{LevelCog.human_format(self, msg3)}", font=big_font)
        offset_x = 800 - 60 - text_size
        offset_y = 280
        draw.text((offset_x, offset_y),
                  f"{LevelCog.human_format(self, msg3)}", font=big_font, fill="#fff")

        # User 4

        text_size = draw.textlength(f"4", font=big_font)
        offset_x = 800 - 750 - text_size
        offset_y = 350
        draw.text((offset_x, offset_y), f"4", font=big_font, fill="#fff")

        text_size = draw.textlength(f"{rank4}", font=big_font)
        offset_x = 800 - 450 - text_size
        offset_y = 350
        draw.text((offset_x, offset_y), f"{rank4}", font=big_font, fill="#fff")

        text_size = draw.textlength(f"{lvl4}", font=big_font)
        offset_x = 800 - 260 - text_size
        offset_y = 350
        draw.text((offset_x, offset_y), f"{lvl4}", font=big_font, fill="#fff")

        text_size = draw.textlength(
            f"{LevelCog.human_format(self, msg4)}", font=big_font)
        offset_x = 800 - 60 - text_size
        offset_y = 350
        draw.text((offset_x, offset_y),
                  f"{LevelCog.human_format(self, msg4)}", font=big_font, fill="#fff")

        # User 5

        text_size = draw.textlength(f"5", font=big_font)
        offset_x = 800 - 750 - text_size
        offset_y = 420
        draw.text((offset_x, offset_y), f"5", font=big_font, fill="#fff")

        text_size = draw.textlength(f"{rank5}", font=big_font)
        offset_x = 800 - 450 - text_size
        offset_y = 420
        draw.text((offset_x, offset_y), f"{rank5}", font=big_font, fill="#fff")

        text_size = draw.textlength(f"{lvl5}", font=big_font)
        offset_x = 800 - 260 - text_size
        offset_y = 420
        draw.text((offset_x, offset_y), f"{lvl5}", font=big_font, fill="#fff")

        text_size = draw.textlength(
            f"{LevelCog.human_format(self, msg5)}", font=big_font)
        offset_x = 800 - 60 - text_size
        offset_y = 420
        draw.text((offset_x, offset_y),
                  f"{LevelCog.human_format(self, msg5)}", font=big_font, fill="#fff")

        img_w, img_h = background.size
        bg_w, bg_h = full_image.size
        offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)

        full_image.paste(background, offset)

        full_image.save(f"{ctx.author.id}.jpg", quality=100)

        file = discord.File(f"./{ctx.author.id}.jpg", filename="top.jpg")

        await ctx.send(file=file)

        os.remove(f"./{ctx.author.id}.jpg")


async def setup(bot):
    await bot.add_cog(LevelCog(bot))
