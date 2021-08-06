import discord
from discord.ext import commands
import os
import datetime
import json

from discord.ext.commands.context import Context

class GenCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def welcome(self, ctx, msg : str = None):
        user = ctx.author.id
        guildid = ctx.guild.id
        guildname = self.bot.get_guild(guildid).name
        channelid = ctx.channel.id

        with open("./local/welcome.json", 'r') as f:
            auth = json.load(f)

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        try:
            if not f'{guildid}' in auth:
                msg2 = ctx.message.content.replace(f"{get_prefix}welcome", "")
                auth[f'{guildid}'] = {}
                auth[f'{guildid}']['user'] = str(ctx.author.name)
                auth[f'{guildid}']['server'] = str(guildname)
                auth[f'{guildid}']['channel'] = channelid

                if msg != None:
                    embed = discord.Embed(description = f"**Welcome Messages Enabled!** 👋🏻\n*Hey <User>! {msg2}*\n`Above message will be sent here when a user joins this server.`", timestamp=datetime.datetime.utcnow())
                    embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                elif msg == None:
                    msg2 = f'Welcome to {str(guildname)}! Glad to have you here 🥰'
                    embed = discord.Embed(description = f"**Welcome Messages Enabled!** 👋🏻\n`Hey <User>! Welcome to {guildname}! Glad to have you here 🥰` will be sent here when a user joins this server.", timestamp=datetime.datetime.utcnow())
                    embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)

                auth[f'{guildid}']['message'] = msg2

                with open("./local/welcome.json", 'w') as f:
                    json.dump(auth, f, indent=4)

                await ctx.send(embed = embed)

            elif f'{guildid}' in auth:
                msg2 = ctx.message.content.replace(f"{get_prefix}welcome", "")
                auth[f'{guildid}']['user'] = str(ctx.author.name)
                auth[f'{guildid}']['server'] = str(guildname)
                auth[f'{guildid}']['channel'] = channelid
                auth[f'{guildid}']['message'] = msg2

                with open("./local/welcome.json", 'w') as f:
                    json.dump(auth, f, indent=4)

                if msg != None:
                    embed = discord.Embed(description = f"**Welcome Messages Enabled!** 👋🏻\n*Hey <User>! {msg2}*\n`Above message will be sent here when a user joins this server.`", timestamp=datetime.datetime.utcnow())
                    embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                elif msg == None:
                    msg2 = f'Welcome to {str(guildname)}! Glad to have you here 🥰'
                    embed = discord.Embed(description = f"**Welcome Messages Enabled!** 👋🏻\n`Hey <User>! Welcome to {guildname}! Glad to have you here 🥰` will be sent here when a user joins this server.", timestamp=datetime.datetime.utcnow())
                    embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)

                auth[f'{guildid}']['message'] = msg2

                with open("./local/welcome.json", 'w') as f:
                    json.dump(auth, f, indent=4)

                await ctx.send(embed = embed)

            else:
                return None
        except Exception as e:
            print(e)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def delwelcome(self, ctx):
        user = ctx.author.id
        guildid = ctx.guild.id

        with open("./local/welcome.json", 'r') as f:
            auth = json.load(f)

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        try:
            if f'{guildid}' in auth:
                del auth[f'{guildid}']

                with open("./local/welcome.json", 'w') as f:
                    json.dump(auth, f, indent=4)

                embed = discord.Embed(title = "Welcome Messages Disabled! ☹️", description = f"*This server no longer has a channel for me to welcome new members. You can set it up again using command `{get_prefix}welcome` in a channel.*", timestamp=datetime.datetime.utcnow())
                embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)

            else:
                embed = discord.Embed(title = "Something Went Wrong! ☹️", description = f"*You probably have no welcome channel setup yet. You can set it up one using command `{get_prefix}welcome` in a channel.*", timestamp=datetime.datetime.utcnow())
                embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)

        except:
            embed = discord.Embed(title = "Something Went Wrong! ☹️", description = f"*An unexpected error occured, please help us by reporting this error. Use command `{get_prefix}report <problem>` to report this problem. Thank you for your cooperation.*", timestamp=datetime.datetime.utcnow())
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)

    @commands.command()
    async def embed(self, message):
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

        msg = message.message.content.replace(f"{get_prefix}embed", "")
        embed = discord.Embed(description = f"{msg}", color = color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        await message.channel.send(embed = embed)

    '''

    Confession

    '''

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def confess(self, ctx):
        user = ctx.author.id
        guildid = ctx.guild.id
        guildname = self.bot.get_guild(guildid).name
        channelid = ctx.channel.id

        with open("./local/confess.json", 'r') as f:
            auth = json.load(f)

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        try:
            if not f'{guildid}' in auth:
                auth[f'{guildid}'] = {}
                auth[f'{guildid}']['user'] = str(ctx.author.name)
                auth[f'{guildid}']['server'] = str(guildname)
                auth[f'{guildid}']['channel'] = channelid

                with open("./local/confess.json", 'w') as f:
                    json.dump(auth, f, indent=4)
                embed = discord.Embed(title = "Confession Channel Was Made! 😄", description = f"*All confessions made anonymously will be sent in this channel. Use command* `{get_prefix}hi` *in my DM to send an anonymous confession.*", timestamp=datetime.datetime.utcnow())
                embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)

            elif f'{guildid}' in auth:
                auth[f'{guildid}']['user'] = str(ctx.author.name)
                auth[f'{guildid}']['server'] = str(guildname)
                auth[f'{guildid}']['channel'] = channelid

                with open("./local/confess.json", 'w') as f:
                    json.dump(auth, f, indent=4)
                embed = discord.Embed(title = "Confession Channel Was Made! 😄", description = f"*All confessions made anonymously will be sent in this channel. Use command* `{get_prefix}hi` *in my DM to send an anonymous confession.*", timestamp=datetime.datetime.utcnow())
                embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)

            else:
                embed = discord.Embed(title = "Failed with Error Code == 5.", description = "Oops. Something went wrong. 😬")
                embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
        except:
            embed = discord.Embed(title = "Failed with Error Code == 5.", description = "Oops. Something went wrong. 😬")
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def delconfess(self, ctx):
        user = ctx.author.id
        guildid = ctx.guild.id

        with open("./local/confess.json", 'r') as f:
            auth = json.load(f)

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        try:
            if f'{guildid}' in auth:
                del auth[f'{guildid}']

                with open("./local/confess.json", 'w') as f:
                    json.dump(auth, f, indent=4)
                embed = discord.Embed(title = "Confession Channel Was Removed!", description = f"*All confessions made anonymously will not be sent in any channel in this server. Use command* `{get_prefix}confess` to set up a confession channel.*", timestamp=datetime.datetime.utcnow())
                embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)

            else:
                embed = discord.Embed(title = "Failed with Error Code == 4.", description = "Oops. This channel is not set as 'confession channel'. 😬")
                embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
        except:
            embed = discord.Embed(title = "Failed with Error Code == 5.", description = "Oops. Something went wrong. 😬")
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)

    @commands.command()
    async def post(self, message):
        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        if message.guild:
            print("no")
        else:
            post_msg = message.message.content.replace(f"{get_prefix}post", "")
            if len(str(post_msg))>=5:
                guilds = message.message.author.mutual_guilds
                all = ""
                count = 1
                for i in guilds:
                    name = i.name
                    if count == 1:
                        all += f"1️⃣ {name}"
                    elif count == 2:
                        all += f"\n2️⃣ {name}"
                    elif count == 3:
                        all += f"\n3️⃣ {name}"
                    elif count == 4:
                        all += f"\n4️⃣ {name}"
                    elif count == 5:
                        all += f"\n5️⃣ {name}"
                    elif count == 6:
                        all += f"\n6️⃣ {name}"
                    elif count == 7:
                        all += f"\n7️⃣ {name}"
                    elif count == 8:
                        all += f"\n8️⃣ {name}"
                    elif count == 9:
                        all += f"\n9️⃣ {name}"
                    elif count == 10:
                        all += f"\n🔟 {name}"
                    elif count == 11:
                        all += f"\n🥝 {name}"
                    elif count == 12:
                        all += f"\n🍇 {name}"
                    elif count == 13:
                        all += f"\n🍉 {name}"
                    elif count == 14:
                        all += f"\n🍊 {name}"
                    elif count == 15:
                        all += f"\n🍌 {name}"
                    elif count == 16:
                        all += f"\n🍍 {name}"
                    elif count == 17:
                        all += f"\n🥭 {name}"
                    elif count == 18:
                        all += f"\n🍎 {name}"
                    elif count == 19:
                        all += f"\n🍑 {name}"
                    elif count == 20:
                        all += f"\n🍓 {name}"

                    count += 1


                embed = discord.Embed(title = "Choose a server you want to post to... 📮", description = f"{all}")
                msg = await message.author.send(embed=embed)

                if count>0:
                    await msg.add_reaction("❌")
                if count>1:
                    await msg.add_reaction("1️⃣")
                if count>2:
                    await msg.add_reaction("2️⃣")
                if count>3:
                    await msg.add_reaction("3️⃣")
                if count>4:
                    await msg.add_reaction("4️⃣")
                if count>5:
                    await msg.add_reaction("5️⃣")
                if count>6:
                    await msg.add_reaction("6️⃣")
                if count>7:
                    await msg.add_reaction("7️⃣")
                if count>8:
                    await msg.add_reaction("8️⃣")
                if count>9:
                    await msg.add_reaction("9️⃣")
                if count>10:
                    await msg.add_reaction("🔟")
                if count>11:
                    await msg.add_reaction("🥝")
                if count>12:
                    await msg.add_reaction("🍇")
                if count>13:
                    await msg.add_reaction("🍉")
                if count>14:
                    await msg.add_reaction("🍊")
                if count>15:
                    await msg.add_reaction("🍌")
                if count>16:
                    await msg.add_reaction("🍍")
                if count>17:
                    await msg.add_reaction("🥭")
                if count>18:
                    await msg.add_reaction("🍎")
                if count>19:
                    await msg.add_reaction("🍑")
                if count>20:
                    await msg.add_reaction("🍓")
                    
                reaction, user = await self.bot.wait_for("reaction_add", check=lambda r, u: r.message.id == msg.id and u.id == message.author.id)
                if str(reaction.emoji) == '1️⃣':
                    guild1 = guilds[0].id
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                            channelid = auth[f'{guild1}']['channel']
                            channel = self.bot.get_channel(channelid)
                            file = discord.File("./pictures/1.png")
                            embed = discord.Embed(description = f"{post_msg}", timestamp=datetime.datetime.utcnow())
                            embed.set_author(name = f"Confession", icon_url= "attachment://1.png")
                            await channel.send(file = file, embed = embed)
                    except:
                        embed = discord.Embed(title = "1️⃣ server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '2️⃣':
                    guild2 = guilds[1].id
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                            channelid = auth[f'{guild2}']['channel']
                            channel = self.bot.get_channel(channelid)
                            file = discord.File("./pictures/1.png")
                            embed = discord.Embed(title = f"{post_msg}", timestamp=datetime.datetime.utcnow())
                            embed.set_author(name = f"Confession", icon_url= "attachment://1.png")
                            await channel.send(file = file, embed = embed)
                    except:
                        embed = discord.Embed(title = "2️⃣ server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '3️⃣':
                    guild3 = guilds[2].id
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                            channelid = auth[f'{guild3}']['channel']
                            channel = self.bot.get_channel(channelid)
                            file = discord.File("./pictures/1.png")
                            embed = discord.Embed(title = f"{post_msg}", timestamp=datetime.datetime.utcnow())
                            embed.set_author(name = f"Confession", icon_url= "attachment://1.png")
                            await channel.send(file = file, embed = embed)
                    except:
                        embed = discord.Embed(title = "3️⃣ server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '4️⃣':
                    guild4 = guilds[3].id
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                            channelid = auth[f'{guild4}']['channel']
                            channel = self.bot.get_channel(channelid)
                            file = discord.File("./pictures/1.png")
                            embed = discord.Embed(title = f"{post_msg}", timestamp=datetime.datetime.utcnow())
                            embed.set_author(name = f"Confession", icon_url= "attachment://1.png")
                            await channel.send(file = file, embed = embed)
                    except:
                        embed = discord.Embed(title = "4️⃣ server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '5️⃣':
                    guild5 = guilds[4].id
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                            channelid = auth[f'{guild5}']['channel']
                            channel = self.bot.get_channel(channelid)
                            file = discord.File("./pictures/1.png")
                            embed = discord.Embed(title = f"{post_msg}", timestamp=datetime.datetime.utcnow())
                            embed.set_author(name = f"Confession", icon_url= "attachment://1.png")
                            await channel.send(file = file, embed = embed)
                    except:
                        embed = discord.Embed(title = "5️⃣ server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '6️⃣':
                    guild6 = guilds[5].id
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                            channelid = auth[f'{guild6}']['channel']
                            channel = self.bot.get_channel(channelid)
                            file = discord.File("./pictures/1.png")
                            embed = discord.Embed(title = f"{post_msg}", timestamp=datetime.datetime.utcnow())
                            embed.set_author(name = f"Confession", icon_url= "attachment://1.png")
                            await channel.send(file = file, embed = embed)
                    except:
                        embed = discord.Embed(title = "6️⃣ server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '7️⃣':
                    guild7 = guilds[6].id
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                            channelid = auth[f'{guild7}']['channel']
                            channel = self.bot.get_channel(channelid)
                            file = discord.File("./pictures/1.png")
                            embed = discord.Embed(title = f"{post_msg}", timestamp=datetime.datetime.utcnow())
                            embed.set_author(name = f"Confession", icon_url= "attachment://1.png")
                            await channel.send(file = file, embed = embed)
                    except:
                        embed = discord.Embed(title = "7️⃣ server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '8️⃣':
                    guild8 = guilds[7].id
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                            channelid = auth[f'{guild8}']['channel']
                            channel = self.bot.get_channel(channelid)
                            file = discord.File("./pictures/1.png")
                            embed = discord.Embed(title = f"{post_msg}", timestamp=datetime.datetime.utcnow())
                            embed.set_author(name = f"Confession", icon_url= "attachment://1.png")
                            await channel.send(file = file, embed = embed)
                    except:
                        embed = discord.Embed(title = "8️⃣ server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '9️⃣':
                    guild9 = guilds[8].id
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                            channelid = auth[f'{guild9}']['channel']
                            channel = self.bot.get_channel(channelid)
                            file = discord.File("./pictures/1.png")
                            embed = discord.Embed(title = f"{post_msg}", timestamp=datetime.datetime.utcnow())
                            embed.set_author(name = f"Confession", icon_url= "attachment://1.png")
                            await channel.send(file = file, embed = embed)
                    except:
                        embed = discord.Embed(title = "9️⃣ server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '🔟':
                    guild10 = guilds[9].id
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                            channelid = auth[f'{guild10}']['channel']
                            channel = self.bot.get_channel(channelid)
                            file = discord.File("./pictures/1.png")
                            embed = discord.Embed(title = f"{post_msg}", timestamp=datetime.datetime.utcnow())
                            embed.set_author(name = f"Confession", icon_url= "attachment://1.png")
                            await channel.send(file = file, embed = embed)
                    except:
                        embed = discord.Embed(title = "🔟 server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '🥝':
                    guild11 = guilds[10].id
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                            channelid = auth[f'{guild11}']['channel']
                            channel = self.bot.get_channel(channelid)
                            file = discord.File("./pictures/1.png")
                            embed = discord.Embed(title = f"{post_msg}", timestamp=datetime.datetime.utcnow())
                            embed.set_author(name = f"Confession", icon_url= "attachment://1.png")
                            await channel.send(file = file, embed = embed)
                    except:
                        embed = discord.Embed(title = "🥝 server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '🍇':
                    guild12 = guilds[11].id
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                            channelid = auth[f'{guild12}']['channel']
                            channel = self.bot.get_channel(channelid)
                            file = discord.File("./pictures/1.png")
                            embed = discord.Embed(title = f"{post_msg}", timestamp=datetime.datetime.utcnow())
                            embed.set_author(name = f"Confession", icon_url= "attachment://1.png")
                            await channel.send(file = file, embed = embed)
                    except:
                        embed = discord.Embed(title = "🍇 server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '🍉':
                    guild13 = guilds[12].id
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                            channelid = auth[f'{guild13}']['channel']
                            channel = self.bot.get_channel(channelid)
                            file = discord.File("./pictures/1.png")
                            embed = discord.Embed(title = f"{post_msg}", timestamp=datetime.datetime.utcnow())
                            embed.set_author(name = f"Confession", icon_url= "attachment://1.png")
                            await channel.send(file = file, embed = embed)
                    except:
                        embed = discord.Embed(title = "🍉 server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '🍊':
                    guild14 = guilds[13].id
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                            channelid = auth[f'{guild14}']['channel']
                            channel = self.bot.get_channel(channelid)
                            file = discord.File("./pictures/1.png")
                            embed = discord.Embed(title = f"{post_msg}", timestamp=datetime.datetime.utcnow())
                            embed.set_author(name = f"Confession", icon_url= "attachment://1.png")
                            await channel.send(file = file, embed = embed)
                    except:
                        embed = discord.Embed(title = "🍊 server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '🍌':
                    guild15 = guilds[14].id
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                            channelid = auth[f'{guild15}']['channel']
                            channel = self.bot.get_channel(channelid)
                            file = discord.File("./pictures/1.png")
                            embed = discord.Embed(title = f"{post_msg}", timestamp=datetime.datetime.utcnow())
                            embed.set_author(name = f"Confession", icon_url= "attachment://1.png")
                            await channel.send(file = file, embed = embed)
                    except:
                        embed = discord.Embed(title = "🍌 server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '🍍':
                    guild16 = guilds[15].id
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                            channelid = auth[f'{guild16}']['channel']
                            channel = self.bot.get_channel(channelid)
                            file = discord.File("./pictures/1.png")
                            embed = discord.Embed(title = f"{post_msg}", timestamp=datetime.datetime.utcnow())
                            embed.set_author(name = f"Confession", icon_url= "attachment://1.png")
                            await channel.send(file = file, embed = embed)
                    except:
                        embed = discord.Embed(title = "🍍 server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '🥭':
                    guild17 = guilds[16].id
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                            channelid = auth[f'{guild17}']['channel']
                            channel = self.bot.get_channel(channelid)
                            file = discord.File("./pictures/1.png")
                            embed = discord.Embed(title = f"{post_msg}", timestamp=datetime.datetime.utcnow())
                            embed.set_author(name = f"Confession", icon_url= "attachment://1.png")
                            await channel.send(file = file, embed = embed)
                    except:
                        embed = discord.Embed(title = "🥭 server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '🍎':
                    guild18 = guilds[17].id
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                            channelid = auth[f'{guild18}']['channel']
                            channel = self.bot.get_channel(channelid)
                            file = discord.File("./pictures/1.png")
                            embed = discord.Embed(title = f"{post_msg}", timestamp=datetime.datetime.utcnow())
                            embed.set_author(name = f"Confession", icon_url= "attachment://1.png")
                            await channel.send(file = file, embed = embed)
                    except:
                        embed = discord.Embed(title = "🍎 server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '🍑':
                    guild19 = guilds[18].id
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                            channelid = auth[f'{guild19}']['channel']
                            channel = self.bot.get_channel(channelid)
                            file = discord.File("./pictures/1.png")
                            embed = discord.Embed(title = f"{post_msg}", timestamp=datetime.datetime.utcnow())
                            embed.set_author(name = f"Confession", icon_url= "attachment://1.png")
                            await channel.send(file = file, embed = embed)
                    except:
                        embed = discord.Embed(title = "🍑 server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '🍓':
                    guild20 = guilds[19].id
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                            channelid = auth[f'{guild20}']['channel']
                            channel = self.bot.get_channel(channelid)
                            file = discord.File("./pictures/1.png")
                            embed = discord.Embed(title = f"{post_msg}", timestamp=datetime.datetime.utcnow())
                            embed.set_author(name = f"Confession", icon_url= "attachment://1.png")
                            await channel.send(file = file, embed = embed)
                    except:
                        embed = discord.Embed(title = "🍓 server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '❌':
                    embed = discord.Embed(title = "Confession post was cancelled ❌")
                    await message.author.send(embed=embed)

            else:
                embed = discord.Embed(title = "Confession should be atleast 5 characters long ☹️")
                await message.author.send(embed=embed)

    @commands.command(aliases = ["hello", "hey", "hii", "Hi", "HI"])
    async def hi(self, message):
        if message.guild:
            print("no")
        else:
            embed = discord.Embed(title="DM Commands 📱",
            description="`=post <msg>` : *Replace <msg> with a confession message you want to make in a server, I will then send you a list of servers from which you can choose the one where you want to post the confession.*",
            timestamp = datetime.datetime.utcnow())

            await message.author.send(embed=embed)

def setup(bot):
    bot.add_cog(GenCog(bot))