import discord
from discord.ext import commands
import os
import datetime
import json

from discord.ext.commands.context import Context

class AboutCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def human_format(self, num):
        num = float('{:.3g}'.format(num))
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num /= 1000.0
        return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])
    
    @commands.command(name = "invite", aliases = ["Invite", "INVITE", "link", "LINK", "Link"])
    async def invite(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        embed = discord.Embed(
        description = "**Invite Links**\n[Michelle](https://discordapp.com/oauth2/authorize?client_id=840180379389263882&permissions=4228906231&scope=bot%20applications.commands)   •   [Beta](https://discordapp.com/oauth2/authorize?client_id=840521197699072020&permissions=4228906231&scope=bot%20applications.commands)  •  [Website](https://top.gg/bot/840180379389263882)", 
        color = color, timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_author(name = "💌", icon_url = self.bot.user.avatar_url)
        await message.channel.send(embed = embed)

    @commands.command()
    async def vote(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        embed = discord.Embed(title = "Vote Link",
        description = "Click the link above to vote me on **TOP.GG**", 
        url = "https://top.gg/bot/840180379389263882/vote",
        color = color, timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_author(name = "☑️", icon_url = self.bot.user.avatar_url)
        await message.channel.send(embed = embed)

    @commands.command()
    async def feedback(self, message):
        await message.channel.trigger_typing()
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

        embed = discord.Embed(
            title = "Feedback 🆘",
            description = f"Give your feedback on this bot (Michelle), give as much details as possible, do not include any personal information. Thank you!\n\n*Report a Problem* : `{get_prefix}report <problem>`\nExample : `{get_prefix}report welcome message not working`",
            color = color, timestamp=datetime.datetime.utcnow()
        )

        await message.channel.send(embed=embed)

    @commands.command()
    async def report(self, message : discord.Message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as guild:
            users = json.load(guild)

        color = users[str(id)]['color']

        name = message.author.id
        with open("./local/report.json", 'r') as f:
            users = json.load(f)

        try:
            if str(name) not in users:
                users[str(name)] = {}
                users[str(name)]["name"] = message.author.name
                users[str(name)]["count"] = 1
                users[str(name)]["report1"] = str(message.message.content)
                users[str(name)]["report2"] = None
                users[str(name)]["report3"] = None

                embed = discord.Embed(
                    title = "Report ❗",
                    description = f'{message.author.mention} The issue was reported!',
                    color=color,
                    timestamp = datetime.datetime.utcnow()
                )
                await message.channel.send(embed=embed)

                with open("./local/report.json", 'w') as f:
                    json.dump(users, f, indent=4)
            elif str(name) in users:
                if users[str(name)]["count"] == 1:
                    users[str(name)]["count"] = 2
                    users[str(name)]["report2"] = str(message.message.content)
                    users[str(name)]["report3"] = None

                    embed = discord.Embed(
                        title = "Report ❗",
                        description = f'{message.author.mention} The issue was reported!',
                        color=color,
                        timestamp = datetime.datetime.utcnow()
                    )
                    await message.channel.send(embed=embed)

                    with open("./local/report.json", 'w') as f:
                        json.dump(users, f, indent=4)

                elif users[str(name)]["count"] == 2:
                    users[str(name)]["count"] = 3
                    users[str(name)]["report3"] = str(message.message.content)

                    embed = discord.Embed(
                        title = "Report ❗",
                        description = f'{message.author.mention} The issue was reported!',
                        color=color,
                        timestamp = datetime.datetime.utcnow()
                    )
                    await message.channel.send(embed=embed)

                    with open("./local/report.json", 'w') as f:
                        json.dump(users, f, indent=4)

                elif users[str(name)]["count"] == 3:
                    embed = discord.Embed(
                        title = "Report ❗",
                        description = f"{message.author.mention} You've reached the Maximum number of Reports = 3",
                        color=color,
                        timestamp = datetime.datetime.utcnow()
                    )
                    await message.channel.send(embed=embed)
                else:
                    embed = discord.Embed(
                        title = "Report ❗",
                        description = f"{message.author.mention} Something went wrong, try again later!",
                        color=color,
                        timestamp = datetime.datetime.utcnow()
                    )
                    await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(
                    title = "Report ❗",
                    description = f"{message.author.mention} Something went wrong, try again later!",
                    color=color,
                    timestamp = datetime.datetime.utcnow()
                )
                await message.channel.send(embed=embed)
        except:
            embed = discord.Embed(
                title = "Report ❗",
                description = f"{message.author.mention} Something went wrong, try again later!",
                color=color,
                timestamp = datetime.datetime.utcnow()
            )
            await message.channel.send(embed=embed)

    @commands.command()
    async def profile(self, ctx, *, user: discord.Member = None):
        await ctx.channel.trigger_typing()
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        if user is None:
            user = ctx.author

        id = user.id

        color = users[str(id)]['color']
        xp = users[str(id)]['experience']
        lvl = users[str(id)]['level']

        if user.nick == None:
            nick = "None"
        else:
            nick = user.nick

        theme = color

        if theme == 9807270: #gray
            theme = "Gray"
        elif theme == 15158332 or theme == 10038562: #red
            theme = "Red"
        elif theme == 3447003 or theme == 2123412: #blue
            theme = "Blue"
        elif theme == 3066993 or theme == 2067276: #green
            theme = "Green"
        elif theme == 10181046 or theme == 7419530: #purple
            theme = "Purple"
        elif theme == 15844367 or theme == 12745742: #gold
            theme = "Gold"
        elif theme == 1752220 or theme == 1146986: #teal
            theme = "Teal"
        elif theme == 15105570 or theme == 11027200: #orange
            theme = "Orange"
        elif theme == 15277667 or theme == 11342935: #magenta
            theme = "Magenta"
        else: #gray
            theme = "Gray"

        with open("./local/personalping.json", "r") as f:
            ping = json.load(f)

        if str(ctx.author.id) in ping:
            ping1 = ping[f"{ctx.author.id}"]["ping1"]
            ping2 = ping[f"{ctx.author.id}"]["ping2"]
            ping3 = ping[f"{ctx.author.id}"]["ping3"]

        else:
            ping1 = "None"
            ping2 = "None"
            ping3 = "None"

        with open("./local/weapons.json", "r") as f:
            weapons = json.load(f)

        if str(user.id) in weapons:
            if weapons[f"{user.id}"]["knife"] == True:
                knife = self.bot.get_emoji(881474984193703999)
                w = f"Knife {knife}"

            elif weapons[f"{user.id}"]["machette"] == True:
                machette = self.bot.get_emoji(881478895503806464)
                w = f"Machette {machette}"

            elif weapons[f"{user.id}"]["dagger"] == True:
                dagger = self.bot.get_emoji(881478895835164682)
                w = f"Dagger {dagger}"

            elif weapons[f"{user.id}"]["sword"] == True:
                sword = self.bot.get_emoji(881478895247949887)
                w = f"Sword {sword}"

            elif weapons[f"{user.id}"]["scythe"] == True:
                scythe = self.bot.get_emoji(881478895604494376)
                w = f"Scythe {scythe}"

            elif weapons[f"{user.id}"]["shuriken"] == True:
                shuriken = self.bot.get_emoji(881478895889690674)
                w = f"Shuriken {shuriken}"

            else:
                w = "None"

        else:
            w = "None"

        embed = discord.Embed(
            description=f"**{user}**", color=color, timestamp = datetime.datetime.utcnow())

        embed.set_thumbnail(url=user.avatar_url_as(format="png"))
        embed.add_field(name="__General__", value=f"**Level** : {lvl}\n"
        f"**Experience** : {AboutCog.human_format(self, xp)}\n"
        f"**Weapon** : {w}\n"
        f"**Color** : {theme}", inline=False)
        embed.add_field(name="__Server__", value=f"**Name** : {nick}\n"
        f"**Joined** : {user.joined_at.__format__('%A %d %B %Y at %H:%M')}\n"
        f"**Roles** : {' '.join([r.mention for r in user.roles[1:]])}", inline=False)

        if user == ctx.author:
            embed.add_field(name="__Personal Pings__", value=f"**1** : `{ping1}`\n"
            f"**2** : `{ping2}`\n"
            f"**3** : `{ping3}`", inline=False)

        await ctx.send(embed=embed)

    @commands.group(invoke_without_command=True)
    async def settings(self, ctx):
        await ctx.channel.trigger_typing()
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        cross = ctx.bot.get_emoji(880679527200735273)
        check = ctx.bot.get_emoji(880679486205620234)

        embed = discord.Embed(
            color = color, 
            timestamp=datetime.datetime.utcnow())

        with open("./local/settings.json", "r") as f:
            set = json.load(f)

        if str(ctx.author.id) in set:
            personal = set[f"{ctx.author.id}"]["personal_ping"]
            if personal == True:
                personal = f"{check} `Enabled`"
            else:
                personal = f"{cross} `Disabled`"

            server = set[f"{ctx.author.id}"]["server_ping"]
            if server == True:
                server = f"{check} `Enabled`"
            else:
                server = f"{cross} `Disabled`"

            tips = set[f"{ctx.author.id}"]["tips"]
            if tips == True:
                tips = f"{check} `Enabled`"
            else:
                tips = f"{cross} `Disabled`"

            lvlup = set[f"{ctx.author.id}"]["level_ups"]
            if lvlup == True:
                lvlup = f"{check} `Enabled`"
            else:
                lvlup = f"{cross} `Disabled`"

        else:
            personal = f"{check} `Enabled`"
            server = f"{check} `Enabled`"
            tips = f"{check} `Enabled`"
            lvlup = f"{check} `Enabled`"

        embed.add_field(name = f"**Level Up Messages** - `{get_prefix}settings levelup` - {lvlup}", value = f"*Toggles whether or not you will recieve a level up message.*\n\n"
        f"**Pro Tips** - `{get_prefix}settings tips` - {tips}\n"
        f"*Toggles whether or not you will get a `PROTIP` in embeds.*\n\n"
        f"**Personal Pings** - `{get_prefix}settings personal` - {personal}\n"
        f"*Toggles whether or not you will recieve a response to a ping you created.*\n\n"
        f"**Server Pings** - `{get_prefix}settings guild` - {server}\n"
        f"*Toggles whether or not you will recieve a response to a server ping.*", inline=False)
        
        embed.set_author(name = f"Settings", icon_url = "https://cdn.discordapp.com/emojis/880689241724686346.png?v=1")
        await ctx.send(embed = embed)

    @settings.command()
    async def levelup(self, ctx):
        with open("./local/settings.json", "r") as f:
            set = json.load(f)

        cross = ctx.bot.get_emoji(880679527200735273)
        check = ctx.bot.get_emoji(880679486205620234)

        if str(ctx.author.id) in set:
            levelup = set[f"{ctx.author.id}"]["level_ups"]

            if levelup == True:
                set[f"{ctx.author.id}"]["level_ups"] = False
                await ctx.reply(f"**Level Up Messages** have been {cross} `Disabled`")
            else:
                set[f"{ctx.author.id}"]["level_ups"] = True
                await ctx.reply(f"**Level Up Messages** have been {check} `Enabled`")

        elif not str(ctx.author.id) in set:
            set[f"{ctx.author.id}"] = {}
            set[f"{ctx.author.id}"]["level_ups"] = False
            set[f"{ctx.author.id}"]["tips"] = True
            set[f"{ctx.author.id}"]["personal_ping"] = True
            set[f"{ctx.author.id}"]["server_ping"] = True

            await ctx.reply(f"**Level Up Messages** have been {cross} `Disabled`")

        with open("./local/settings.json", "w") as f:
            json.dump(set, f, indent=4)

    @settings.command()
    async def tips(self, ctx):
        with open("./local/settings.json", "r") as f:
            set = json.load(f)

        cross = ctx.bot.get_emoji(880679527200735273)
        check = ctx.bot.get_emoji(880679486205620234)

        if str(ctx.author.id) in set:
            tips = set[f"{ctx.author.id}"]["tips"]

            if tips == True:
                set[f"{ctx.author.id}"]["tips"] = False
                await ctx.reply(f"**PROTIPS** have been {cross} `Disabled`")
            else:
                set[f"{ctx.author.id}"]["tips"] = True
                await ctx.reply(f"**PROTIPS** have been {check} `Enabled`")

        elif not str(ctx.author.id) in set:
            set[f"{ctx.author.id}"] = {}
            set[f"{ctx.author.id}"]["level_ups"] = True
            set[f"{ctx.author.id}"]["tips"] = False
            set[f"{ctx.author.id}"]["personal_ping"] = True
            set[f"{ctx.author.id}"]["server_ping"] = True

            await ctx.reply(f"**PROTIPS** have been {cross} `Disabled`")

        with open("./local/settings.json", "w") as f:
            json.dump(set, f, indent=4)

    @settings.command()
    async def guild(self, ctx):
        with open("./local/settings.json", "r") as f:
            set = json.load(f)

        cross = ctx.bot.get_emoji(880679527200735273)
        check = ctx.bot.get_emoji(880679486205620234)

        if str(ctx.author.id) in set:
            tips = set[f"{ctx.author.id}"]["server_ping"]

            if tips == True:
                set[f"{ctx.author.id}"]["server_ping"] = False
                await ctx.reply(f"**Server Pings** have been {cross} `Disabled`")
            else:
                set[f"{ctx.author.id}"]["server_ping"] = True
                await ctx.reply(f"**Server Pings** have been {check} `Enabled`")

        elif not str(ctx.author.id) in set:
            set[f"{ctx.author.id}"] = {}
            set[f"{ctx.author.id}"]["level_ups"] = True
            set[f"{ctx.author.id}"]["tips"] = True
            set[f"{ctx.author.id}"]["personal_ping"] = True
            set[f"{ctx.author.id}"]["server_ping"] = False

            await ctx.reply(f"**Server Pings** have been {cross} `Disabled`")

        with open("./local/settings.json", "w") as f:
            json.dump(set, f, indent=4)

    @settings.command()
    async def personal(self, ctx):
        with open("./local/settings.json", "r") as f:
            set = json.load(f)

        cross = ctx.bot.get_emoji(880679527200735273)
        check = ctx.bot.get_emoji(880679486205620234)

        if str(ctx.author.id) in set:
            tips = set[f"{ctx.author.id}"]["personal_ping"]

            if tips == True:
                set[f"{ctx.author.id}"]["personal_ping"] = False
                await ctx.reply(f"**Personal Pings** have been {cross} `Disabled`")
            else:
                set[f"{ctx.author.id}"]["personal_ping"] = True
                await ctx.reply(f"**Personal Pings** have been {check} `Enabled`")

        elif not str(ctx.author.id) in set:
            set[f"{ctx.author.id}"] = {}
            set[f"{ctx.author.id}"]["level_ups"] = True
            set[f"{ctx.author.id}"]["tips"] = True
            set[f"{ctx.author.id}"]["personal_ping"] = False
            set[f"{ctx.author.id}"]["server_ping"] = True

            await ctx.reply(f"**Personal Pings** have been {cross} `Disabled`")

        with open("./local/settings.json", "w") as f:
            json.dump(set, f, indent=4)

    @commands.command()
    async def server(self, ctx):
        await ctx.channel.trigger_typing()
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = self.bot.get_guild(guildid)
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/confess.json", "r") as f:
            confess = json.load(f)

        if str(ctx.guild.id) in confess:
            confess_channel = confess[f"{ctx.guild.id}"]["channel"]
            confess_channel = self.bot.get_channel(confess_channel)
            confess_channel = confess_channel.mention
        else:
            confess_channel = "None"

        with open("./local/welcome.json", "r") as f:
            welcome = json.load(f)

        if str(ctx.guild.id) in welcome:
            welcome_channel = welcome[f"{ctx.guild.id}"]["channel"]
            welcome_channel = self.bot.get_channel(welcome_channel)
            welcome_channel = welcome_channel.mention
        else:
            welcome_channel = "None"

        with open("./local/react.json", "r") as f:
            react = json.load(f)

        if str(ctx.guild.id) in react:
            reaction_channel = "Enabled"
        else:
            reaction_channel = "None"

        with open("./local/serverping.json", "r") as f:
            ping = json.load(f)

        if str(ctx.guild.id) in ping:
            ping1 = ping[f"{ctx.guild.id}"]["ping1"]
            ping2 = ping[f"{ctx.guild.id}"]["ping2"]
            ping3 = ping[f"{ctx.guild.id}"]["ping3"]
            ping4 = ping[f"{ctx.guild.id}"]["ping4"]
            ping5 = ping[f"{ctx.guild.id}"]["ping5"]

        else:
            ping1 = "None"
            ping2 = "None"
            ping3 = "None"
            ping4 = "None"
            ping5 = "None"

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

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

        one = int(L[0])
        user1 = self.bot.get_user(one)
        top = str(user1)

        roles = str(len(guild.roles))
        emojis = str(len(guild.emojis))
        text = str(len(guild.text_channels))
        voice = str(len(guild.voice_channels))

        embed = discord.Embed(description= f"**{guild}**", color=color, timestamp = datetime.datetime.utcnow())
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name="__Guild__", value=f"**Roles** : {roles}\n"
        f"**Emojis** : {emojis}\n"
        f"**Members** : {guild.member_count}\n"
        f"**Text Channels** : {text}\n"
        f"**Voice Channels** : {voice}")
        embed.add_field(name="__General__", value=f"**Level** : {guild.premium_tier}\n"
        f"**Region** : {str(guild.region).capitalize()}\n"
        f"**Verification** : {str(guild.verification_level).capitalize()}\n"
        f"**ID** : {guild.id}\n"
        f"**Made On** : {guild.created_at.strftime('%d %B %Y at %H:%M')}\n"
        f"**Owner** : {guild.owner}", inline=False)

        embed.add_field(name="__Michelle__", value=f"**Prefix** : `{get_prefix}`\n"
        f"**Top User** : {top}\n"
        f"**Welcome Channel** : {welcome_channel}\n"
        f"**Confession Channel** : {confess_channel}\n"
        f"**Reaction Roles** : {reaction_channel}", inline=False)

        embed.add_field(name=f"__Server Pings__", value=f"**1** : `{ping1}`\n"
        f"**2** : `{ping2}`\n**3** : `{ping3}`\n**4** : `{ping4}`\n**5** : `{ping5}`", inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(AboutCog(bot))