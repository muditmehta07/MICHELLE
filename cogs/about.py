import discord
from discord.ext import commands
import os
import datetime
import json


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

    @commands.command(name="invite", aliases=["Invite", "INVITE", "links", "LINKS", "LINK", "Links", "Link", "link", "community", "Community", "vote", "VOTE", "Vote"])
    async def invite(self, message):

        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'

        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']
        embed = discord.Embed(
            color=color,
            timestamp=datetime.datetime.utcnow())

        embed.add_field(
            name="Add Michelle", value="[Here](https://discord.com/oauth2/authorize?client_id=840180379389263882&permissions=8&scope=bot+applications.commands)")
        embed.add_field(name="Vote Michelle",
                        value="[Here](https://top.gg/bot/840180379389263882/vote)")
        embed.add_field(name="Michelle Community",
                        value="[Here](https://discord.com/invite/EfHrMURtnA)")
        embed.add_field(name="Michelle Website",
                        value="[Here](https://www.michelle-bot.co/)")
        embed.add_field(name="Michelle GitHub",
                        value="[Here](https://github.com/MuditMehta07/Michelle)")
        embed.add_field(name="Contact Email",
                        value="[Here](https://github.com/MuditMehta07/Michelle/blob/main/README.md#contact)")

        embed.set_author(name="Links", icon_url=self.bot.user.avatar.url)
        await message.channel.send(embed=embed)

    @commands.command()
    async def feedback(self, message):

        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'

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
            title="Feedback 🆘",
            description=f"**Give your feedback on Michelle with as much details as possible, be sure not to include any personal information. Thank you!**\n\nReport a Problem : `{get_prefix}report <problem>`\nExample : `{get_prefix}report Welcome message not working`\n\nGive us a suggestion : `{get_prefix}suggest <suggestion>`\nExample : `{get_prefix}suggest Add level card`",
            color=color, timestamp=datetime.datetime.utcnow()
        )

        await message.channel.send(embed=embed)

    @commands.command()
    async def report(self, message: discord.Message):

        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as guild:
            users = json.load(guild)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        report = str(message.message.content)
        report = report.replace(f'{get_prefix}report', '')

        wordList = report.split()
        wordCount = len(wordList)

        if wordCount >= 10:
            guild1 = self.bot.get_guild(931870251539365899)
            channel1 = guild1.get_channel(931875881079701597)

            embed1 = discord.Embed(
                description=f"{report}", color=color, timestamp=datetime.datetime.utcnow())
            embed1.set_author(name="Report", icon_url=self.bot.user.avatar.url)

            await channel1.send(embed=embed1)

            guild2 = self.bot.get_guild(931870251539365899)
            channel2 = guild2.get_channel(931890827578466334)

            embed2 = discord.Embed(
                description=f"{report}", color=color, timestamp=datetime.datetime.utcnow())
            embed2.set_author(name="Suggestion",
                              icon_url=self.bot.user.avatar.url)
            embed2.set_footer(text="'=feedback' to send a feedback here")

            await channel2.send(content=f"**{message.message.author}** : `{message.author.id}`", embed=embed2)

            embed = discord.Embed(title="Your report has been sent", description="Thank you for the feedback, this would really help us to try improving MICHELLE.",
                                  color=color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name="Report", icon_url=self.bot.user.avatar.url)
            await message.message.channel.send(embed=embed)

        else:
            await message.message.channel.send("A report should contain atleast `10 words`")

    @commands.command()
    async def suggest(self, message: discord.Message):

        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as guild:
            users = json.load(guild)

        color = users[str(id)]['color']

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        report = str(message.message.content)

        report = report.replace(f'{get_prefix}suggest', '')

        wordList = report.split()
        wordCount = len(wordList)

        if wordCount >= 10:
            guild1 = self.bot.get_guild(931870251539365899)
            channel1 = guild1.get_channel(931875881079701597)

            embed1 = discord.Embed(
                description=f"{report}", color=color, timestamp=datetime.datetime.utcnow())
            embed1.set_author(name="Suggestion",
                              icon_url=self.bot.user.avatar.url)
            embed1.set_footer(text="'=feedback' to send a feedback here")

            await channel1.send(embed=embed1)

            guild2 = self.bot.get_guild(931870251539365899)
            channel2 = guild2.get_channel(931890827578466334)

            embed2 = discord.Embed(
                description=f"{report}", color=color, timestamp=datetime.datetime.utcnow())
            embed2.set_author(name="Suggestion",
                              icon_url=self.bot.user.avatar.url)
            embed2.set_footer(text="'=feedback' to send a feedback here")

            await channel2.send(content=f"**{message.message.author}** : `{message.author.id}`", embed=embed2)

            embed = discord.Embed(title="Your suggestion has been sent",
                                  description="Thank you for the feedback, this would really help us to try improving MICHELLE.", color=color, timestamp=datetime.datetime.utcnow())
            embed.set_author(name="Suggestion",
                             icon_url=self.bot.user.avatar.url)
            await message.message.channel.send(embed=embed)

        else:
            await message.message.channel.send("A suggestion should contain atleast `10 words`")

    @commands.command()
    async def profile(self, ctx, *, user: discord.Member = None):

        guildid = ctx.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        if user == self.bot.user:
            embed = discord.Embed(
                description=f"**MICHELLE#5777**", timestamp=datetime.datetime.utcnow())

            embed.set_thumbnail(url=self.bot.user.avatar.url)
            embed.add_field(name="__General__", value=f"**Level** : Same as yours <3\n"
                            f"**Experience** : With Hugs\n"
                            f"**Color** : I mimic yours", inline=False)
            embed.add_field(name="__Server__", value=f"**Name** : Michelle\n"
                            f"**Joined** : Beginning of time\n"
                            f"**Role** : Play", inline=False)

            await ctx.send(embed=embed)

        else:

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

            if theme == 9807270:  # gray
                theme = "Gray"
            elif theme == 15158332 or theme == 10038562:  # red
                theme = "Red"
            elif theme == 3447003 or theme == 2123412:  # blue
                theme = "Blue"
            elif theme == 3066993 or theme == 2067276:  # green
                theme = "Green"
            elif theme == 10181046 or theme == 7419530:  # purple
                theme = "Purple"
            elif theme == 15844367 or theme == 12745742:  # gold
                theme = "Gold"
            elif theme == 1752220 or theme == 1146986:  # teal
                theme = "Teal"
            elif theme == 15105570 or theme == 11027200:  # orange
                theme = "Orange"
            elif theme == 15277667 or theme == 11342935:  # magenta
                theme = "Magenta"
            else:  # gray
                theme = "Gray"

            with open("./local/personalping.json", "r") as f:
                ping = json.load(f)

            P = []

            if str(ctx.author.id) in ping:
                if ping[f"{ctx.author.id}"]["ping1"] != None:
                    ping1 = ping[f"{ctx.author.id}"]["ping1"]
                    P.append(ping1)

                if ping[f"{ctx.author.id}"]["ping2"] != None:
                    ping2 = ping[f"{ctx.author.id}"]["ping2"]
                    P.append(ping2)

                if ping[f"{ctx.author.id}"]["ping3"] != None:
                    ping3 = ping[f"{ctx.author.id}"]["ping3"]
                    P.append(ping3)

            with open("./local/warn.json", "r") as f:
                warn = json.load(f)

            if str(ctx.guild.id) in warn:
                if str(ctx.author.id) in warn[str(ctx.guild.id)]:
                    warnings = warn[str(ctx.guild.id)][str(ctx.author.id)]
                else:
                    warnings = 0
            else:
                warnings = 0

            embed = discord.Embed(
                description=f"**{user}'s Profile**", color=color, timestamp=datetime.datetime.utcnow())

            embed.set_thumbnail(
                url=user.avatar.replace(static_format="png").url)
            embed.add_field(name="__General__", value=f"**Level** : {lvl}\n"
                            f"**Experience** : {AboutCog.human_format(self, xp)}\n"
                            f"**Warnings** : {warnings}\n"
                            f"**Color** : {theme}", inline=False)

            embed.add_field(name="__Server__", value=f"**Nickname** : {nick}\n"
                            f"**Joined** : {user.joined_at.__format__('%A %d %B %Y at %H:%M')}\n"
                            f"**Roles** : {' '.join([r.mention for r in user.roles[1:]])}", inline=False)

            if user == ctx.author:
                if len(P) >= 1:
                    ping_text = ""
                    count = 1
                    for i in P:
                        ping_text += f"**{count}.** `{i}`\n"
                        count += 1

                    embed.add_field(name="__**Personal Pings**__",
                                    value=ping_text, inline=False)

            await ctx.send(embed=embed)

    @commands.group(invoke_without_command=True)
    async def settings(self, ctx):

        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/' + str(guildid) + '.json'
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
        branch = self.bot.get_emoji(942824887666491426)
        replyEmoji = self.bot.get_emoji(929383454469128263)

        embed = discord.Embed(
            color=color,
            timestamp=datetime.datetime.utcnow())

        with open("./local/settings.json", "r") as f:
            set = json.load(f)

        with open("./local/beta.json", "r") as f:
            set2 = json.load(f)

        if str(ctx.author.id) in set:
            personal = set[f"{ctx.author.id}"]["personal_ping"]
            if personal == True:
                personal = f"{check}"
            else:
                personal = f"{cross}"

            server = set[f"{ctx.author.id}"]["server_ping"]
            if server == True:
                server = f"{check}"
            else:
                server = f"{cross}"

            tips = set[f"{ctx.author.id}"]["tips"]
            if tips == True:
                tips = f"{check}"
            else:
                tips = f"{cross}"

            lvlup = set[f"{ctx.author.id}"]["level_ups"]
            if lvlup == True:
                lvlup = f"{check}"
            else:
                lvlup = f"{cross}"

        else:
            personal = f"{check}"
            server = f"{check}"
            tips = f"{check}"
            lvlup = f"{check}"

        with open("./local/beta.json", "r") as f:
            set2 = json.load(f)

        if str(ctx.author.id) in set2:
            beta = set2[f"{ctx.author.id}"]
            if beta == True:
                beta = f"{check}"
            else:
                beta = f"{cross}"

        else:
            beta = f"{cross}"

        embed.description = (
            f"{check} : `Enabled` | {cross} : `Disabled`\n\n"

            f"**settings beta** {beta}\n"
            f"{replyEmoji}Toggles the *Beta Program* ON or OFF\n"

            f"**settings levelup** {lvlup}\n"
            f"{replyEmoji}Toggles whether or not you will recieve a level up message\n"

            f"**settings tips** {tips}\n"
            f"{replyEmoji}Toggles whether or not you will get a *PROTIP* in embeds\n"

            f"**settings personal** {personal}\n"
            f"{replyEmoji}Toggles whether or not you will recieve a response to a ping you created\n"

            f"**settings guild** {server}\n"
            f"{replyEmoji}Toggles whether or not you will recieve a response to a server ping\n"

            f"**passive**\n"
            f"{replyEmoji}Enables Passive Mode\n"

            f"**deletemydata**\n"
            f"{replyEmoji}Delete all your data stored with us"
        )
        embed.set_author(name="Michelle Help Commands",
                         icon_url=self.bot.user.avatar.url)
        embed.set_footer(text=f"use  {get_prefix}  as the command prefix")

        await ctx.send(embed=embed)

    @settings.command()
    async def beta(self, ctx):
        with open("./local/beta.json", "r") as f:
            set = json.load(f)

        cross = ctx.bot.get_emoji(880679527200735273)
        check = ctx.bot.get_emoji(880679486205620234)

        if str(ctx.author.id) in set:
            beta = set[f"{ctx.author.id}"]

            if beta == True:
                del set[f"{ctx.author.id}"]
                await ctx.reply(f"**Beta Program** has been {cross} `Disabled`")
            else:
                set[f"{ctx.author.id}"] = True
                await ctx.reply(f"**Beta Program** has been {check} `Enabled`")

        elif not str(ctx.author.id) in set:
            set[f"{ctx.author.id}"] = True

            await ctx.reply(f"**Beta Program** has been {check} `Enabled`")

        with open("./local/beta.json", "w") as f:
            json.dump(set, f, indent=4)

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

        id = ctx.author.id
        guildid = ctx.guild.id
        guild = self.bot.get_guild(guildid)
        guildid = './guild data/' + str(guildid) + '.json'
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
            react_channel = react[f"{ctx.guild.id}"]["channel"]
            react_channel = self.bot.get_channel(react_channel)
            react_channel = react_channel.mention
        else:
            react_channel = "None"

        with open("./local/count.json", "r") as f:
            count = json.load(f)

        if str(ctx.guild.id) in count and count[str(ctx.guild.id)]["channel"] != 0:
            count_channel = count[f"{ctx.guild.id}"]["channel"]
            count_channel = self.bot.get_channel(count_channel)
            count_channel = count_channel.mention
        else:
            count_channel = "None"

        with open("./local/serverping.json", "r") as f:
            ping = json.load(f)

            P = []

            if str(ctx.guild.id) in ping:
                if ping[f"{ctx.guild.id}"]["ping1"] != None:
                    ping1 = ping[f"{ctx.guild.id}"]["ping1"]
                    P.append(ping1)

                if ping[f"{ctx.guild.id}"]["ping2"] != None:
                    ping2 = ping[f"{ctx.guild.id}"]["ping2"]
                    P.append(ping2)

                if ping[f"{ctx.guild.id}"]["ping3"] != None:
                    ping3 = ping[f"{ctx.guild.id}"]["ping3"]
                    P.append(ping3)

                if ping[f"{ctx.guild.id}"]["ping4"] != None:
                    ping4 = ping[f"{ctx.guild.id}"]["ping4"]
                    P.append(ping4)

                if ping[f"{ctx.guild.id}"]["ping5"] != None:
                    ping5 = ping[f"{ctx.guild.id}"]["ping5"]
                    P.append(ping5)

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

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

        one = int(L[0])
        user1 = self.bot.get_user(one)
        top = str(user1)

        roles = str(len(guild.roles))
        emojis = str(len(guild.emojis))
        text = str(len(guild.text_channels))
        voice = str(len(guild.voice_channels))

        embed = discord.Embed(
            description=f"**{guild}**", color=color, timestamp=datetime.datetime.utcnow())
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
                        f"**Reaction Roles** : {react_channel}\n"
                        f"**Couting Channel** : {count_channel}", inline=False)

        if len(P) >= 1:
            ping_text = ""
            count = 1
            for i in P:
                ping_text += f"**{count}.** `{i}`\n"
                count += 1

            embed.add_field(name="__**Server Pings**__",
                            value=ping_text, inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def message(self, ctx):

        id = ctx.author.id
        guildid = ctx.guild.id
        guild = self.bot.get_guild(guildid)
        guildid = './guild data/' + str(guildid) + '.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        with open("./local/message.json", "r") as f:
            message = json.load(f)

        title = message["title"]
        description = message["description"]
        footer = message["footer"]

        embed = discord.Embed(
            title=title,
            description=description,
            color=color
        )

        embed.set_footer(text=footer)

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(AboutCog(bot))
