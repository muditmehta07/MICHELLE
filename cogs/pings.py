import discord
from discord.ext import commands
import os
import datetime
import json
from discord.ext.commands.context import Context

class PingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def ping(self, ctx):
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

        embed = discord.Embed(
            title = "Custom Pings ❣️",
            description = f"**Create a custom ping** : `{get_prefix}ping create`\n"
            f"**Remove a custom ping** : `{get_prefix}ping rem`\n",
            timestamp = datetime.datetime.utcnow(),
            color=color
        )

        await ctx.send(embed=embed)

    @ping.command()
    async def create(self, ctx):
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

        embed = discord.Embed(
            title = "Create Ping ❣️",
            description = f"**Choose ping type**",
            timestamp = datetime.datetime.utcnow(),
            color=color
        )

        embed.add_field(name = "🦄", value = "`For Me`")
        embed.add_field(name = "🐲", value = "`For Everyone in Server`")

        msg = await ctx.send(embed=embed)
        await msg.add_reaction("🦄")
        await msg.add_reaction("🐲")

        reaction, user = await self.bot.wait_for("reaction_add", check=lambda r, u: r.message.id == msg.id and u.id == ctx.author.id)

        if str(reaction.emoji) == '🦄':
            with open("./local/personalping.json", "r") as m:
                users = json.load(m)

            if str(ctx.author.id) in users:
                if users[f'{ctx.author.id}']['ping1'] != None and users[f'{ctx.author.id}']['ping2'] != None and users[f'{ctx.author.id}']['ping3'] != None:

                    quit_embed = discord.Embed(
                        description = f"You already have **3** personal pings. Delete any existing ones using `{get_prefix}ping rem` to add more",
                        color = color,
                        timestamp = datetime.datetime.utcnow()
                    )

                    quit_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                    await ctx.send(embed=quit_embed)

                else:
                    ping_all_msg = "For Me"

                    embed2 = discord.Embed(
                        title = "Create Ping ❣️",
                        description = f"Ping Type : `{ping_all_msg}`\n\n**Choose ping look**",
                        timestamp = datetime.datetime.utcnow(),
                        color=color
                    )

                    embed2.add_field(name = "🦄", value = "`Embed`")
                    embed2.add_field(name = "🐲", value = "`Message`")

                    msg2 = await ctx.send(embed=embed2)
                    await msg2.add_reaction("🦄")
                    await msg2.add_reaction("🐲")

                    reaction2, user = await self.bot.wait_for("reaction_add", check=lambda r, u: r.message.id == msg2.id and u.id == ctx.author.id)
                    if str(reaction2.emoji) == '🦄':
                        ping_embed = True
                        ping_embed_msg = "Embed"
                    elif str(reaction2.emoji) == '🐲':
                        ping_embed = False
                        ping_embed_msg = "Message"

                    embed3 = discord.Embed(
                        title = "Create Ping ❣️",
                        description = f"Ping Type : `{ping_all_msg}`\nPing Look : `{ping_embed_msg}`\n\n**Type ping to which I have to respond**",
                        timestamp = datetime.datetime.utcnow(),
                        color=color
                    )

                    await ctx.send(embed=embed3)

                    ping = await self.bot.wait_for("message", check=lambda m: m.author.id == ctx.author.id)
                    ping = ping.content

                    embed4 = discord.Embed(
                        title = "Create Ping ❣️",
                        description = f"Ping Type : `{ping_all_msg}`\nPing Look : `{ping_embed_msg}`\nPing : `{ping}`\n\n**Type the response to the ping**",
                        timestamp = datetime.datetime.utcnow(),
                        color=color
                    )

                    await ctx.send(embed=embed4)

                    response = await self.bot.wait_for("message", check=lambda m: m.author.id == ctx.author.id)
                    response = response.content

                    wordList = response.split()
                    
                    for i in wordList:
                        if i.startswith("@"):
                            mention = True

                        else:
                            mention = False

                    if mention == True:
                        await ctx.send("You cannot mention anyone in a personal ping")

                    else:

                        with open("./local/personalping.json", "r") as f:
                            users = json.load(f)

                        if not str(ctx.author.id) in users:
                            users[f'{ctx.author.id}'] = {}
                            users[f'{ctx.author.id}']['ping1'] = ping
                            users[f'{ctx.author.id}']['res1'] = response
                            users[f'{ctx.author.id}']['embed1'] = ping_embed

                            users[f'{ctx.author.id}']['ping2'] = None
                            users[f'{ctx.author.id}']['res2'] = None
                            users[f'{ctx.author.id}']['embed2'] = None

                            users[f'{ctx.author.id}']['ping3'] = None
                            users[f'{ctx.author.id}']['res3'] = None
                            users[f'{ctx.author.id}']['embed3'] = None

                        elif str(ctx.author.id) in users:

                            if users[f'{ctx.author.id}']['ping1'] == None:
                                users[f'{ctx.author.id}']['ping1'] = ping
                                users[f'{ctx.author.id}']['res1'] = response
                                users[f'{ctx.author.id}']['embed1'] = ping_embed

                            elif users[f'{ctx.author.id}']['ping2'] == None:
                                users[f'{ctx.author.id}']['ping2'] = ping
                                users[f'{ctx.author.id}']['res2'] = response
                                users[f'{ctx.author.id}']['embed2'] = ping_embed

                            elif users[f'{ctx.author.id}']['ping3'] == None:
                                users[f'{ctx.author.id}']['ping3'] = ping
                                users[f'{ctx.author.id}']['res3'] = response
                                users[f'{ctx.author.id}']['embed3'] = ping_embed

                        with open("./local/personalping.json", 'w') as f:
                            json.dump(users, f)

                        if ping_embed_msg == "Embed":
                            r_msg = "An `embed`"

                        else:
                            r_msg = "A `message`"


                        embed5 = discord.Embed(
                            title = "Ping Created ❣️",
                            description = f"Ping : `{ping}`\nResponse : `{response}`\n\n{r_msg} will be sent when this ping is called, `only you` can use this ping",
                            timestamp = datetime.datetime.utcnow(),
                            color=color
                        )

                        await ctx.send(embed=embed5)


            else:
                ping_all_msg = "For Me"

                embed2 = discord.Embed(
                    title = "Create Ping ❣️",
                    description = f"Ping Type : `{ping_all_msg}`\n\n**Choose ping look**",
                    timestamp = datetime.datetime.utcnow(),
                    color=color
                )

                embed2.add_field(name = "🦄", value = "`Embed`")
                embed2.add_field(name = "🐲", value = "`Message`")

                msg2 = await ctx.send(embed=embed2)
                await msg2.add_reaction("🦄")
                await msg2.add_reaction("🐲")

                reaction2, user = await self.bot.wait_for("reaction_add", check=lambda r, u: r.message.id == msg2.id and u.id == ctx.author.id)
                if str(reaction2.emoji) == '🦄':
                    ping_embed = True
                    ping_embed_msg = "Embed"
                elif str(reaction2.emoji) == '🐲':
                    ping_embed = False
                    ping_embed_msg = "Message"

                embed3 = discord.Embed(
                    title = "Create Ping ❣️",
                    description = f"Ping Type : `{ping_all_msg}`\nPing Look : `{ping_embed_msg}`\n\n**Type ping to which I have to respond**",
                    timestamp = datetime.datetime.utcnow(),
                    color=color
                )

                await ctx.send(embed=embed3)

                ping = await self.bot.wait_for("message", check=lambda m: m.author.id == ctx.author.id)
                ping = ping.content

                embed4 = discord.Embed(
                    title = "Create Ping ❣️",
                    description = f"Ping Type : `{ping_all_msg}`\nPing Look : `{ping_embed_msg}`\nPing : `{ping}`\n\n**Type the response to the ping**",
                    timestamp = datetime.datetime.utcnow(),
                    color=color
                )

                await ctx.send(embed=embed4)

                response = await self.bot.wait_for("message", check=lambda m: m.author.id == ctx.author.id)
                response = response.content

                wordList = response.split()
                
                for i in wordList:
                    if i.startswith("@"):
                        mention = True

                    else:
                        mention = False

                if mention == True:
                    await ctx.send("You cannot mention anyone in a personal ping")

                else:

                    with open("./local/personalping.json", "r") as f:
                        users = json.load(f)

                    if not str(ctx.author.id) in users:
                        users[f'{ctx.author.id}'] = {}
                        users[f'{ctx.author.id}']['ping1'] = ping
                        users[f'{ctx.author.id}']['res1'] = response
                        users[f'{ctx.author.id}']['embed1'] = ping_embed

                        users[f'{ctx.author.id}']['ping2'] = None
                        users[f'{ctx.author.id}']['res2'] = None
                        users[f'{ctx.author.id}']['embed2'] = None

                        users[f'{ctx.author.id}']['ping3'] = None
                        users[f'{ctx.author.id}']['res3'] = None
                        users[f'{ctx.author.id}']['embed3'] = None

                    elif str(ctx.author.id) in users:

                        if users[f'{ctx.author.id}']['ping1'] == None:
                            users[f'{ctx.author.id}']['ping1'] = ping
                            users[f'{ctx.author.id}']['res1'] = response
                            users[f'{ctx.author.id}']['embed1'] = ping_embed

                        elif users[f'{ctx.author.id}']['ping2'] == None:
                            users[f'{ctx.author.id}']['ping2'] = ping
                            users[f'{ctx.author.id}']['res2'] = response
                            users[f'{ctx.author.id}']['embed2'] = ping_embed

                        elif users[f'{ctx.author.id}']['ping3'] == None:
                            users[f'{ctx.author.id}']['ping3'] = ping
                            users[f'{ctx.author.id}']['res3'] = response
                            users[f'{ctx.author.id}']['embed3'] = ping_embed

                    with open("./local/personalping.json", 'w') as f:
                        json.dump(users, f)

                    if ping_embed_msg == "Embed":
                        r_msg = "An `embed`"

                    else:
                        r_msg = "A `message`"


                    embed5 = discord.Embed(
                        title = "Ping Created ❣️",
                        description = f"Ping : `{ping}`\nResponse : `{response}`\n\n{r_msg} will be sent when this ping is called, `only you` can use this ping",
                        timestamp = datetime.datetime.utcnow(),
                        color=color
                    )

                    await ctx.send(embed=embed5)


        elif str(reaction.emoji) == '🐲':
            if ctx.author.permissions_in(ctx.channel).manage_messages:
                with open("./local/serverping.json", "r") as m:
                    users = json.load(m)

                if str(ctx.guild.id) in users:
                    if users[f'{ctx.guild.id}']['ping1'] != None and users[f'{ctx.guild.id}']['ping2'] != None and users[f'{ctx.guild.id}']['ping3'] != None and users[f'{ctx.guild.id}']['ping4'] != None and users[f'{ctx.guild.id}']['ping5'] != None:

                        quit_embed = discord.Embed(
                            description = f"You already have **5** server pings.\nDelete any existing ones using `{get_prefix}ping rem` to add more",
                            color = color,
                            timestamp = datetime.datetime.utcnow()
                        )

                        quit_embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                        await ctx.send(embed=quit_embed)

                    else:
                        ping_all_msg = "For Everyone in Server"

                        embed2 = discord.Embed(
                            title = "Create Ping ❣️",
                            description = f"Ping Type : `{ping_all_msg}`\n\n**Choose ping look**",
                            timestamp = datetime.datetime.utcnow(),
                            color=color
                        )

                        embed2.add_field(name = "🦄", value = "`Embed`")
                        embed2.add_field(name = "🐲", value = "`Message`")

                        msg2 = await ctx.send(embed=embed2)
                        await msg2.add_reaction("🦄")
                        await msg2.add_reaction("🐲")

                        reaction2, user = await self.bot.wait_for("reaction_add", check=lambda r, u: r.message.id == msg2.id and u.id == ctx.author.id)
                        if str(reaction2.emoji) == '🦄':
                            ping_embed = True
                            ping_embed_msg = "Embed"
                        elif str(reaction2.emoji) == '🐲':
                            ping_embed = False
                            ping_embed_msg = "Message"

                        embed3 = discord.Embed(
                            title = "Create Ping ❣️",
                            description = f"Ping Type : `{ping_all_msg}`\nPing Look : `{ping_embed_msg}`\n\n**Type ping to which I have to respond**",
                            timestamp = datetime.datetime.utcnow(),
                            color=color
                        )

                        await ctx.send(embed=embed3)

                        ping = await self.bot.wait_for("message", check=lambda m: m.author.id == ctx.author.id)
                        ping = ping.content

                        embed4 = discord.Embed(
                            title = "Create Ping ❣️",
                            description = f"Ping Type : `{ping_all_msg}`\nPing Look : `{ping_embed_msg}`\nPing : `{ping}`\n\n**Type the response to the ping**",
                            timestamp = datetime.datetime.utcnow(),
                            color=color
                        )

                        await ctx.send(embed=embed4)

                        response = await self.bot.wait_for("message", check=lambda m: m.author.id == ctx.author.id)
                        response = response.content

                        wordList = response.split()
                        
                        for i in wordList:
                            if i.startswith("@"):
                                mention = True

                            else:
                                mention = False

                        if mention == True:
                            await ctx.send("You cannot mention anyone in a personal ping")

                        else:

                            with open('./local/serverping.json', 'r') as f:
                                users = json.load(f)

                            if not str(ctx.guild.id) in users:
                                users[f'{ctx.guild.id}'] = {}
                                users[f'{ctx.guild.id}']['ping1'] = ping
                                users[f'{ctx.guild.id}']['res1'] = response
                                users[f'{ctx.guild.id}']['embed1'] = ping_embed

                                users[f'{ctx.guild.id}']['ping2'] = None
                                users[f'{ctx.guild.id}']['res2'] = None
                                users[f'{ctx.guild.id}']['embed2'] = None

                                users[f'{ctx.guild.id}']['ping3'] = None
                                users[f'{ctx.guild.id}']['res3'] = None
                                users[f'{ctx.guild.id}']['embed3'] = None

                                users[f'{ctx.guild.id}']['ping4'] = None
                                users[f'{ctx.guild.id}']['res4'] = None
                                users[f'{ctx.guild.id}']['embed4'] = None

                                users[f'{ctx.guild.id}']['ping5'] = None
                                users[f'{ctx.guild.id}']['res5'] = None
                                users[f'{ctx.guild.id}']['embed5'] = None

                            elif str(ctx.guild.id) in users:

                                if users[f'{ctx.guild.id}']['ping1'] == None:
                                    users[f'{ctx.guild.id}']['ping1'] = ping
                                    users[f'{ctx.guild.id}']['res1'] = response
                                    users[f'{ctx.guild.id}']['embed1'] = ping_embed

                                elif users[f'{ctx.guild.id}']['ping2'] == None:
                                    users[f'{ctx.guild.id}']['ping2'] = ping
                                    users[f'{ctx.guild.id}']['res2'] = response
                                    users[f'{ctx.guild.id}']['embed2'] = ping_embed

                                elif users[f'{ctx.guild.id}']['ping3'] == None:
                                    users[f'{ctx.guild.id}']['ping3'] = ping
                                    users[f'{ctx.guild.id}']['res3'] = response
                                    users[f'{ctx.guild.id}']['embed3'] = ping_embed

                                elif users[f'{ctx.guild.id}']['ping4'] == None:
                                    users[f'{ctx.guild.id}']['ping4'] = ping
                                    users[f'{ctx.guild.id}']['res4'] = response
                                    users[f'{ctx.guild.id}']['embed4'] = ping_embed

                                elif users[f'{ctx.guild.id}']['ping5'] == None:
                                    users[f'{ctx.guild.id}']['ping5'] = ping
                                    users[f'{ctx.guild.id}']['res5'] = response
                                    users[f'{ctx.guild.id}']['embed5'] = ping_embed

                            with open("./local/serverping.json", 'w') as f:
                                json.dump(users, f)

                            if ping_embed_msg == "Embed":
                                r_msg = "An `embed`"

                            else:
                                r_msg = "A `message`"


                            embed5 = discord.Embed(
                                title = "Ping Created ❣️",
                                description = f"Ping : `{ping}`\nResponse : `{response}`\n\n{r_msg} will be sent when this ping is called, `everyone in this server` can use this ping",
                                timestamp = datetime.datetime.utcnow(),
                                color=color
                            )

                            await ctx.send(embed=embed5)

                else:
                    ping_all_msg = "For Everyone in Server"

                    embed2 = discord.Embed(
                        title = "Create Ping ❣️",
                        description = f"Ping Type : `{ping_all_msg}`\n\n**Choose ping look**",
                        timestamp = datetime.datetime.utcnow(),
                        color=color
                    )

                    embed2.add_field(name = "🦄", value = "`Embed`")
                    embed2.add_field(name = "🐲", value = "`Message`")

                    msg2 = await ctx.send(embed=embed2)
                    await msg2.add_reaction("🦄")
                    await msg2.add_reaction("🐲")

                    reaction2, user = await self.bot.wait_for("reaction_add", check=lambda r, u: r.message.id == msg2.id and u.id == ctx.author.id)
                    if str(reaction2.emoji) == '🦄':
                        ping_embed = True
                        ping_embed_msg = "Embed"
                    elif str(reaction2.emoji) == '🐲':
                        ping_embed = False
                        ping_embed_msg = "Message"

                    embed3 = discord.Embed(
                        title = "Create Ping ❣️",
                        description = f"Ping Type : `{ping_all_msg}`\nPing Look : `{ping_embed_msg}`\n\n**Type ping to which I have to respond**",
                        timestamp = datetime.datetime.utcnow(),
                        color=color
                    )

                    await ctx.send(embed=embed3)

                    ping = await self.bot.wait_for("message", check=lambda m: m.author.id == ctx.author.id)
                    ping = ping.content

                    embed4 = discord.Embed(
                        title = "Create Ping ❣️",
                        description = f"Ping Type : `{ping_all_msg}`\nPing Look : `{ping_embed_msg}`\nPing : `{ping}`\n\n**Type the response to the ping**",
                        timestamp = datetime.datetime.utcnow(),
                        color=color
                    )

                    await ctx.send(embed=embed4)

                    response = await self.bot.wait_for("message", check=lambda m: m.author.id == ctx.author.id)
                    response = response.content

                    wordList = response.split()
                    
                    for i in wordList:
                        if i.startswith("@"):
                            mention = True

                        else:
                            mention = False

                    if mention == True:
                        await ctx.send("You cannot mention anyone in a personal ping")

                    else:

                        with open('./local/serverping.json', 'r') as f:
                            users = json.load(f)

                        if not str(ctx.guild.id) in users:
                            users[f'{ctx.guild.id}'] = {}
                            users[f'{ctx.guild.id}']['ping1'] = ping
                            users[f'{ctx.guild.id}']['res1'] = response
                            users[f'{ctx.guild.id}']['embed1'] = ping_embed

                            users[f'{ctx.guild.id}']['ping2'] = None
                            users[f'{ctx.guild.id}']['res2'] = None
                            users[f'{ctx.guild.id}']['embed2'] = None

                            users[f'{ctx.guild.id}']['ping3'] = None
                            users[f'{ctx.guild.id}']['res3'] = None
                            users[f'{ctx.guild.id}']['embed3'] = None

                            users[f'{ctx.guild.id}']['ping4'] = None
                            users[f'{ctx.guild.id}']['res4'] = None
                            users[f'{ctx.guild.id}']['embed4'] = None

                            users[f'{ctx.guild.id}']['ping5'] = None
                            users[f'{ctx.guild.id}']['res5'] = None
                            users[f'{ctx.guild.id}']['embed5'] = None

                        elif str(ctx.guild.id) in users:

                            if users[f'{ctx.guild.id}']['ping1'] == None:
                                users[f'{ctx.guild.id}']['ping1'] = ping
                                users[f'{ctx.guild.id}']['res1'] = response
                                users[f'{ctx.guild.id}']['embed1'] = ping_embed

                            elif users[f'{ctx.guild.id}']['ping2'] == None:
                                users[f'{ctx.guild.id}']['ping2'] = ping
                                users[f'{ctx.guild.id}']['res2'] = response
                                users[f'{ctx.guild.id}']['embed2'] = ping_embed

                            elif users[f'{ctx.guild.id}']['ping3'] == None:
                                users[f'{ctx.guild.id}']['ping3'] = ping
                                users[f'{ctx.guild.id}']['res3'] = response
                                users[f'{ctx.guild.id}']['embed3'] = ping_embed

                            elif users[f'{ctx.guild.id}']['ping4'] == None:
                                users[f'{ctx.guild.id}']['ping4'] = ping
                                users[f'{ctx.guild.id}']['res4'] = response
                                users[f'{ctx.guild.id}']['embed4'] = ping_embed

                            elif users[f'{ctx.guild.id}']['ping5'] == None:
                                users[f'{ctx.guild.id}']['ping5'] = ping
                                users[f'{ctx.guild.id}']['res5'] = response
                                users[f'{ctx.guild.id}']['embed5'] = ping_embed

                        with open("./local/serverping.json", 'w') as f:
                            json.dump(users, f)

                        if ping_embed_msg == "Embed":
                            r_msg = "An `embed`"

                        else:
                            r_msg = "A `message`"


                        embed5 = discord.Embed(
                            title = "Ping Created ❣️",
                            description = f"Ping : `{ping}`\nResponse : `{response}`\n\n{r_msg} will be sent when this ping is called, `everyone in this server` can use this ping",
                            timestamp = datetime.datetime.utcnow(),
                            color=color
                        )

                        await ctx.send(embed=embed5)

            else:
                embed5 = discord.Embed(
                    description = f"A Ping with `type : everyone` cannot be created since you do not have `Manage Messages` permission",
                    timestamp = datetime.datetime.utcnow(),
                    color=color
                )

                await ctx.send(embed=embed5)

    @ping.command()
    async def rem(self, ctx):
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

        embed = discord.Embed(
            title = "Delete Ping ❣️",
            description = f"**Choose ping type to delete**\nPersonal Ping : `{get_prefix}ping rem1`\nServer Ping : `{get_prefix}ping rem2`",
            timestamp = datetime.datetime.utcnow(),
            color=color
        )

        embed.set_author(name = ctx.author, icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @ping.command()
    async def rem1(self, ctx):
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

        with open("./local/personalping.json", "r") as f:
            users = json.load(f)

        if str(ctx.author.id) in users:
            ping_str = ""
            if users[f'{ctx.author.id}']['ping1'] != None:
                ping1 = users[f'{ctx.author.id}']['ping1']
                ping_str += f"{ping1} : `{get_prefix}ping remp {ping1}`\n"

            if users[f'{ctx.author.id}']['ping2'] != None:
                ping2 = users[f'{ctx.author.id}']['ping2']
                ping_str += f"{ping2} : `{get_prefix}ping remp {ping2}`\n"

            if users[f'{ctx.author.id}']['ping3'] != None:
                ping3 = users[f'{ctx.author.id}']['ping3']
                ping_str += f"{ping3} : `{get_prefix}ping remp {ping3}`\n"

            if ping_str == "":
                ping_str += "No added pings"

        else:
            ping_str = "No added pings"

        embed = discord.Embed(
            title = "Delete Personal Ping ❣️",
            description = f"{ping_str}",
            timestamp = datetime.datetime.utcnow(),
            color=color
        )

        embed.set_author(name = ctx.author, icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @ping.command()
    async def remp(self, ctx):
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

        ping = ctx.message.content.replace(f"{get_prefix}ping remp ", "")

        if ping == "":
            embed = discord.Embed(
                description = f"**Usage 📝**\n`{get_prefix}ping remp <ping>`",
                color=color, timestamp = datetime.datetime.utcnow()
            )

            embed.set_author(name = ctx.author, icon_url=ctx.author.avatar_url)

            await ctx.send(embed=embed)

        else:
            with open("./local/personalping.json", "r") as f:
                users = json.load(f)

            if users[f'{ctx.author.id}']['ping1'] == ping:
                users[f'{ctx.author.id}']['ping1'] = None
                users[f'{ctx.author.id}']['res1'] = None
                users[f'{ctx.author.id}']['embed1'] = None

            elif users[f'{ctx.author.id}']['ping2'] == ping:
                users[f'{ctx.author.id}']['ping2'] = None
                users[f'{ctx.author.id}']['res2'] = None
                users[f'{ctx.author.id}']['embed2'] = None

            elif users[f'{ctx.author.id}']['ping3'] == ping:
                users[f'{ctx.author.id}']['ping3'] = None
                users[f'{ctx.author.id}']['res3'] = None
                users[f'{ctx.author.id}']['embed3'] = None

            with open("./local/personalping.json", "w") as f:
                json.dump(users, f)

            await ctx.message.add_reaction("✅")

    @ping.command()
    async def rem2(self, ctx):
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

        with open("./local/serverping.json", "r") as f:
            users = json.load(f)

        if str(ctx.guild.id) in users:
            ping_str = ""
            if users[f'{ctx.guild.id}']['ping1'] != None:
                ping1 = users[f'{ctx.guild.id}']['ping1']
                ping_str += f"{ping1} : `{get_prefix}ping rems {ping1}`\n"

            if users[f'{ctx.guild.id}']['ping2'] != None:
                ping2 = users[f'{ctx.guild.id}']['ping2']
                ping_str += f"{ping2} : `{get_prefix}ping rems {ping2}`\n"

            if users[f'{ctx.guild.id}']['ping3'] != None:
                ping3 = users[f'{ctx.guild.id}']['ping3']
                ping_str += f"{ping3} : `{get_prefix}ping rems {ping3}`\n"

            if users[f'{ctx.guild.id}']['ping4'] != None:
                ping4 = users[f'{ctx.guild.id}']['ping4']
                ping_str += f"{ping4} : `{get_prefix}ping rems {ping4}`\n"

            if users[f'{ctx.guild.id}']['ping5'] != None:
                ping5 = users[f'{ctx.guild.id}']['ping5']
                ping_str += f"{ping5} : `{get_prefix}ping rems {ping5}`\n"

            if ping_str == "":
                ping_str += "No added pings"

        else:
            ping_str = "No added pings"


        embed = discord.Embed(
            title = "Delete Server Ping ❣️",
            description = f"{ping_str}",
            timestamp = datetime.datetime.utcnow(),
            color=color
        )

        embed.set_author(name = ctx.author, icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @ping.command()
    async def rems(self, ctx):
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

        ping = ctx.message.content.replace(f"{get_prefix}ping rems ", "")

        if ctx.author.permissions_in(ctx.channel).manage_messages:
            if ping == "":
                embed = discord.Embed(
                    description = f"**Usage 📝**\n`{get_prefix}ping rems <ping>`",
                    color=color, timestamp = datetime.datetime.utcnow()
                )

                embed.set_author(name = ctx.author, icon_url=ctx.author.avatar_url)

                await ctx.send(embed=embed)

            else:
                with open("./local/serverping.json", "r") as f:
                    users = json.load(f)

                if users[f'{ctx.guild.id}']['ping1'] == ping:
                    users[f'{ctx.guild.id}']['ping1'] = None
                    users[f'{ctx.guild.id}']['res1'] = None
                    users[f'{ctx.guild.id}']['embed1'] = None

                elif users[f'{ctx.guild.id}']['ping2'] == ping:
                    users[f'{ctx.guild.id}']['ping2'] = None
                    users[f'{ctx.guild.id}']['res2'] = None
                    users[f'{ctx.guild.id}']['embed2'] = None

                elif users[f'{ctx.guild.id}']['ping3'] == ping:
                    users[f'{ctx.guild.id}']['ping3'] = None
                    users[f'{ctx.guild.id}']['res3'] = None
                    users[f'{ctx.guild.id}']['embed3'] = None

                elif users[f'{ctx.guild.id}']['ping4'] == ping:
                    users[f'{ctx.guild.id}']['ping4'] = None
                    users[f'{ctx.guild.id}']['res4'] = None
                    users[f'{ctx.guild.id}']['embed4'] = None

                elif users[f'{ctx.guild.id}']['ping5'] == ping:
                    users[f'{ctx.guild.id}']['ping5'] = None
                    users[f'{ctx.guild.id}']['res5'] = None
                    users[f'{ctx.guild.id}']['embed5'] = None

                with open("./local/serverping.json", "w") as f:
                    json.dump(users, f)

                await ctx.message.add_reaction("✅")

async def setup(bot):
    await bot.add_cog(PingCog(bot))