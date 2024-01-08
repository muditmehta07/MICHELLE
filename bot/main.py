import settings
import discord
from discord import user
from discord import channel
from discord import message
from discord.colour import Color
from discord.enums import ActivityType, Status
from discord.message import Message
from discord.ext import commands
from discord import app_commands
import os
import pickle
import json
import orjson
from itertools import cycle
import datetime
from discord.ext.commands.context import Context
import asyncio

def get_the_prefix(client, message):
    with open("./local/prefix.json", "r") as f:
        L = json.load(f)
    try:
        if str(message.guild.id) in L:
            prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            prefix = "="
    except:
        prefix = "="

    return prefix


def checkint(n):
    try:
        int(n)
        return True

    except ValueError:
        return False


intents = discord.Intents.default()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix=get_the_prefix, intents=intents)
bot.remove_command('help')

initial_extensions = [
    'cmds.mod',
    'cmds.games',
    'cmds.pings',
    'cmds.translate',
    'cmds.dev',
    'cmds.setup',
    'cmds.fun',
    'cmds.about',
    'cmds.api',
    'cmds.auth',
    'cmds.general',
    'cmds.item',
    'cmds.reaction',
    'cmds.shop',
    'cmds.spells',
    'cmds.theme',
    "cmds.help",
    "cmds.level"
]

disabled_exts = [
    "__init__.py",
    "translate.py",
    "help.py"
]


@bot.event
async def on_ready():
    print(f'**Server Count**: `{str(len(bot.guilds))} Servers`')
    try:
        await bot.tree.sync()
    except Exception as e:
        print(e)

    for cmd_file in settings.cmds_dir.glob("*.py"):
        if cmd_file.name not in disabled_exts:
            await bot.load_extension(f"cmds.{cmd_file.name[:-3]}")

    with open("./bot/status.json", "r") as f:
        S = json.load(f)

    mstat = f'=help'
    status = S["status"]
    activity = S["activity"]
    text = S["text"]

    if status == "online":
        if text == None:
            if activity == None:
                await bot.change_presence(status=discord.Status.online)
            elif activity == "watching":
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=mstat))
                S["text"] = mstat
            elif activity == "listening":
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=mstat))
                S["text"] = mstat
            elif activity == "playing":
                await bot.change_presence(activity=discord.Game(name=mstat))
                S["text"] = mstat
        else:
            if activity == None:
                await bot.change_presence(status=discord.Status.online)
            elif activity == "watching":
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=text))
            elif activity == "listening":
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=text))
            elif activity == "playing":
                await bot.change_presence(activity=discord.Game(name=mstat))

    elif status == "idle":
        if text == None:
            if activity == None:
                await bot.change_presence(status=discord.Status.idle)
            elif activity == "watching":
                await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=mstat))
                S["text"] = mstat
            elif activity == "listening":
                await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name=mstat))
                S["text"] = mstat
            elif activity == "playing":
                await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=mstat))
                S["text"] = mstat
        else:
            if activity == None:
                await bot.change_presence(status=discord.Status.idle)
            elif activity == "watching":
                await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=text))
            elif activity == "listening":
                await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name=text))
            elif activity == "playing":
                await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=mstat))

    elif status == "offline":
        await bot.change_presence(status=discord.Status.offline)

    with open("./bot/status.json", "w") as f:
        json.dump(S, f, indent=4)


@bot.event
async def on_member_remove(member):
    try:
        id = member.guild.id
        with open("./local/goodbye.json", 'r') as f:
            goodbye = json.load(f)

        channelid = goodbye[f'{id}']['channel']
        #msg = goodbye[f'{id}']['message']
        guild = bot.get_guild(id)
        channel = guild.get_channel(channelid)

        await channel.send(f"**{member}** left the server")

    except Exception as e:
        print(e)


@bot.event
async def on_member_join(member):
    if member.guild.id == 931870251539365899:
        guild = member.guild
        user = member.id
        with open("./local/invite.json", "r") as h:
            users = json.load(h)

        if not str(user) in users:
            users[str(user)] = {}
            users[f"{user}"]["done"] = True

            with open("./local/items.json", "r") as e:
                auth = json.load(e)

            if not str(user) in auth:
                auth[f"{user}"] = {}
                auth[f"{user}"]["items"] = ["gift_box"]

            elif str(user) in auth:
                item_list = auth[f"{user}"]["items"]
                item_list.append("gift_box")
                auth[f"{user}"]["items"] = item_list

            with open("./local/items.json", "w") as e:
                json.dump(auth, e, indent=4)

            with open("./local/invite.json", "w") as h:
                json.dump(users, h, indent=4)

            invite_user = bot.get_user(user)
            await invite_user.send(f"Hi `{invite_user.name}`, thank you for joining Michelle's Community. You just recieved a **Gift Box**🎁. Go to a server and use command `=giftbox` to open it and recieve 100K XP")

    with open("./local/autorole.json", "r") as f:
        roles = json.load(f)

    if str(member.guild.id) in roles:
        roleId = roles[str(member.guild.id)]
        guild = member.guild
        role = discord.utils.get(guild.roles, id=roleId)
        if member != bot.user:
            await member.add_roles(role)

    with open("./bot/status.json", "r") as f:
        D = json.load(f)

    status = D["status"]
    if status == "online" or status == "idle":
        try:
            id = member.guild.id
            with open("./local/welcome.json", 'r') as f:
                welcome = json.load(f)
            channelid = welcome[f'{id}']['channel']
            msg = welcome[f'{id}']['message']
            guild = bot.get_guild(id)
            channel = guild.get_channel(channelid)

            embed = discord.Embed(description=f'{msg}',
                                  timestamp=datetime.datetime.utcnow())

            embed.set_author(
                name=f"Welcome {member}!", icon_url=member.avatar)
            await channel.send(embed=embed)

        except Exception as e:
            print(e)

    guildid = member.guild.id
    guildid = './guild data/' + str(guildid) + '.json'
    if member.bot == False:
        if os.path.exists(guildid):
            with open(guildid, 'r') as f:
                users = json.load(f)

            await update_data(users, member)

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)
        elif not os.path.exists(guildid):
            with open(guildid, "x") as f:
                print("")
            with open(guildid, 'w') as f:
                d = {

                }
                json.dump(d, f, indent=4)
            with open(guildid, 'r') as f:
                users = json.load(f)

            await update_data(users, member)

            with open(guildid, 'w') as f:
                json.dump(users, f, indent=4)


@bot.event
async def on_message(message):
    if not message.guild:
        get_prefix = "="

        post_msg = message.content.replace(f"{get_prefix}post ", "")
        if len(str(post_msg)) >= 5:
            guilds = message.author.mutual_guilds

            with open("./local/confess.json", "r") as f:
                server = json.load(f)

            all = ""

            idlist = []
            count = 1
            for i in guilds:
                if str(i.id) in server:
                    name = i.name
                    if count == 1:
                        idlist.append(str(i.id))
                        all += f"1️⃣ {name}"
                    elif count == 2:
                        idlist.append(str(i.id))
                        all += f"\n2️⃣ {name}"
                    elif count == 3:
                        idlist.append(str(i.id))
                        all += f"\n3️⃣ {name}"
                    elif count == 4:
                        idlist.append(str(i.id))
                        all += f"\n4️⃣ {name}"
                    elif count == 5:
                        idlist.append(str(i.id))
                        all += f"\n5️⃣ {name}"
                    elif count == 6:
                        idlist.append(str(i.id))
                        all += f"\n6️⃣ {name}"
                    elif count == 7:
                        idlist.append(str(i.id))
                        all += f"\n7️⃣ {name}"
                    elif count == 8:
                        idlist.append(str(i.id))
                        all += f"\n8️⃣ {name}"
                    elif count == 9:
                        idlist.append(str(i.id))
                        all += f"\n9️⃣ {name}"
                    elif count == 10:
                        idlist.append(str(i.id))
                        all += f"\n🔟 {name}"
                    elif count == 11:
                        idlist.append(str(i.id))
                        all += f"\n🥝 {name}"
                    elif count == 12:
                        idlist.append(str(i.id))
                        all += f"\n🍇 {name}"
                    elif count == 13:
                        idlist.append(str(i.id))
                        all += f"\n🍉 {name}"
                    elif count == 14:
                        idlist.append(str(i.id))
                        all += f"\n🍊 {name}"
                    elif count == 15:
                        idlist.append(str(i.id))
                        all += f"\n🍌 {name}"
                    elif count == 16:
                        idlist.append(str(i.id))
                        all += f"\n🍍 {name}"
                    elif count == 17:
                        idlist.append(str(i.id))
                        all += f"\n🥭 {name}"
                    elif count == 18:
                        idlist.append(str(i.id))
                        all += f"\n🍎 {name}"
                    elif count == 19:
                        idlist.append(str(i.id))
                        all += f"\n🍑 {name}"
                    elif count == 20:
                        idlist.append(str(i.id))
                        all += f"\n🍓 {name}"

                    count += 1

            embed = discord.Embed(title="Choose a confession server...",
                                  description=f"> To choose a server, look at the emoji next to the server of your choice, then react to the same emoji down below\n\n"
                                  f"{all}",
                                  timestamp=datetime.datetime.utcnow())

            msg = await message.author.send(embed=embed)

            if count > 0:
                await msg.add_reaction("❌")
            if count > 1:
                await msg.add_reaction("1️⃣")
            if count > 2:
                await msg.add_reaction("2️⃣")
            if count > 3:
                await msg.add_reaction("3️⃣")
            if count > 4:
                await msg.add_reaction("4️⃣")
            if count > 5:
                await msg.add_reaction("5️⃣")
            if count > 6:
                await msg.add_reaction("6️⃣")
            if count > 7:
                await msg.add_reaction("7️⃣")
            if count > 8:
                await msg.add_reaction("8️⃣")
            if count > 9:
                await msg.add_reaction("9️⃣")
            if count > 10:
                await msg.add_reaction("🔟")
            if count > 11:
                await msg.add_reaction("🥝")
            if count > 12:
                await msg.add_reaction("🍇")
            if count > 13:
                await msg.add_reaction("🍉")
            if count > 14:
                await msg.add_reaction("🍊")
            if count > 15:
                await msg.add_reaction("🍌")
            if count > 16:
                await msg.add_reaction("🍍")
            if count > 17:
                await msg.add_reaction("🥭")
            if count > 18:
                await msg.add_reaction("🍎")
            if count > 19:
                await msg.add_reaction("🍑")
            if count > 20:
                await msg.add_reaction("🍓")

            try:
                reaction, user = await bot.wait_for("reaction_add", check=lambda r, u: r.message.id == msg.id and u.id == message.author.id, timeout=10)
                if str(reaction.emoji) == '1️⃣':
                    guild1 = idlist[0]
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)

                        channelid = auth[f'{guild1}']['channel']
                        channel = bot.get_channel(channelid)
                        embed = discord.Embed(
                            description=f"{post_msg}", timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=f"Confession",
                                         icon_url=bot.user.avatar)
                        await channel.send(embed=embed)
                    except:
                        embed = discord.Embed(
                            title="1️⃣ server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '2️⃣':
                    guild2 = idlist[1]
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                        channelid = auth[f'{guild2}']['channel']
                        channel = bot.get_channel(channelid)
                        embed = discord.Embed(
                            description=f"{post_msg}", timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=f"Confession",
                                         icon_url=bot.user.avatar)
                        await channel.send(embed=embed)
                    except:
                        embed = discord.Embed(
                            title="2️⃣ server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '3️⃣':
                    guild3 = idlist[2]
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                        channelid = auth[f'{guild3}']['channel']
                        channel = bot.get_channel(channelid)
                        embed = discord.Embed(
                            description=f"{post_msg}", timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=f"Confession",
                                         icon_url=bot.user.avatar)
                        await channel.send(embed=embed)
                    except:
                        embed = discord.Embed(
                            title="3️⃣ server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '4️⃣':
                    guild4 = idlist[3]
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                        channelid = auth[f'{guild4}']['channel']
                        channel = bot.get_channel(channelid)
                        embed = discord.Embed(
                            description=f"{post_msg}", timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=f"Confession",
                                         icon_url=bot.user.avatar)
                        await channel.send(embed=embed)
                    except:
                        embed = discord.Embed(
                            title="4️⃣ server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '5️⃣':
                    guild5 = idlist[4]
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                        channelid = auth[f'{guild5}']['channel']
                        channel = bot.get_channel(channelid)
                        embed = discord.Embed(
                            description=f"{post_msg}", timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=f"Confession",
                                         icon_url=bot.user.avatar)
                        await channel.send(embed=embed)
                    except:
                        embed = discord.Embed(
                            title="5️⃣ server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '6️⃣':
                    guild6 = idlist[5]
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                        channelid = auth[f'{guild6}']['channel']
                        channel = bot.get_channel(channelid)
                        embed = discord.Embed(
                            description=f"{post_msg}", timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=f"Confession",
                                         icon_url=bot.user.avatar)
                        await channel.send(embed=embed)
                    except:
                        embed = discord.Embed(
                            title="6️⃣ server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '7️⃣':
                    guild7 = idlist[6]
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                        channelid = auth[f'{guild7}']['channel']
                        channel = bot.get_channel(channelid)
                        embed = discord.Embed(
                            description=f"{post_msg}", timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=f"Confession",
                                         icon_url=bot.user.avatar)
                        await channel.send(embed=embed)
                    except:
                        embed = discord.Embed(
                            title="7️⃣ server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '8️⃣':
                    guild8 = idlist[7]
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                        channelid = auth[f'{guild8}']['channel']
                        channel = bot.get_channel(channelid)
                        embed = discord.Embed(
                            description=f"{post_msg}", timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=f"Confession",
                                         icon_url=bot.user.avatar)
                        await channel.send(embed=embed)
                    except:
                        embed = discord.Embed(
                            title="8️⃣ server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '9️⃣':
                    guild9 = idlist[8]
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                        channelid = auth[f'{guild9}']['channel']
                        channel = bot.get_channel(channelid)
                        embed = discord.Embed(
                            description=f"{post_msg}", timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=f"Confession",
                                         icon_url=bot.user.avatar)
                        await channel.send(embed=embed)
                    except:
                        embed = discord.Embed(
                            title="9️⃣ server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '🔟':
                    guild10 = idlist[9]
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                        channelid = auth[f'{guild10}']['channel']
                        channel = bot.get_channel(channelid)
                        embed = discord.Embed(
                            description=f"{post_msg}", timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=f"Confession",
                                         icon_url=bot.user.avatar)
                        await channel.send(embed=embed)
                    except:
                        embed = discord.Embed(
                            title="🔟 server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '🥝':
                    guild11 = idlist[10]
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                        channelid = auth[f'{guild11}']['channel']
                        channel = bot.get_channel(channelid)
                        embed = discord.Embed(
                            description=f"{post_msg}", timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=f"Confession",
                                         icon_url=bot.user.avatar)
                        await channel.send(embed=embed)
                    except:
                        embed = discord.Embed(
                            title="🥝 server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '🍇':
                    guild12 = idlist[11]
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                        channelid = auth[f'{guild12}']['channel']
                        channel = bot.get_channel(channelid)
                        embed = discord.Embed(
                            description=f"{post_msg}", timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=f"Confession",
                                         icon_url=bot.user.avatar)
                        await channel.send(embed=embed)
                    except:
                        embed = discord.Embed(
                            title="🍇 server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '🍉':
                    guild13 = idlist[12]
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                        channelid = auth[f'{guild13}']['channel']
                        channel = bot.get_channel(channelid)
                        embed = discord.Embed(
                            description=f"{post_msg}", timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=f"Confession",
                                         icon_url=bot.user.avatar)
                        await channel.send(embed=embed)
                    except:
                        embed = discord.Embed(
                            title="🍉 server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '🍊':
                    guild14 = idlist[13]
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                        channelid = auth[f'{guild14}']['channel']
                        channel = bot.get_channel(channelid)
                        embed = discord.Embed(
                            description=f"{post_msg}", timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=f"Confession",
                                         icon_url=bot.user.avatar)
                        await channel.send(embed=embed)
                    except:
                        embed = discord.Embed(
                            title="🍊 server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '🍌':
                    guild15 = idlist[14]
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                        channelid = auth[f'{guild15}']['channel']
                        channel = bot.get_channel(channelid)
                        embed = discord.Embed(
                            description=f"{post_msg}", timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=f"Confession",
                                         icon_url=bot.user.avatar)
                        await channel.send(embed=embed)
                    except:
                        embed = discord.Embed(
                            title="🍌 server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '🍍':
                    guild16 = idlist[15]
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                        channelid = auth[f'{guild16}']['channel']
                        channel = bot.get_channel(channelid)
                        embed = discord.Embed(
                            description=f"{post_msg}", timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=f"Confession",
                                         icon_url=bot.user.avatar)
                        await channel.send(embed=embed)
                    except:
                        embed = discord.Embed(
                            title="🍍 server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '🥭':
                    guild17 = idlist[16]
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                        channelid = auth[f'{guild17}']['channel']
                        channel = bot.get_channel(channelid)
                        embed = discord.Embed(
                            description=f"{post_msg}", timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=f"Confession",
                                         icon_url=bot.user.avatar)
                        await channel.send(embed=embed)
                    except:
                        embed = discord.Embed(
                            title="🥭 server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '🍎':
                    guild18 = idlist[17]
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                        channelid = auth[f'{guild18}']['channel']
                        channel = bot.get_channel(channelid)
                        embed = discord.Embed(
                            description=f"{post_msg}", timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=f"Confession",
                                         icon_url=bot.user.avatar)
                        await channel.send(embed=embed)
                    except:
                        embed = discord.Embed(
                            title="🍎 server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '🍑':
                    guild19 = idlist[18]
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                        channelid = auth[f'{guild19}']['channel']
                        channel = bot.get_channel(channelid)
                        embed = discord.Embed(
                            description=f"{post_msg}", timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=f"Confession",
                                         icon_url=bot.user.avatar)
                        await channel.send(embed=embed)
                    except:
                        embed = discord.Embed(
                            title="🍑 server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '🍓':
                    guild20 = idlist[19]
                    try:
                        with open("./local/confess.json", "r") as f:
                            auth = json.load(f)
                        channelid = auth[f'{guild20}']['channel']
                        channel = bot.get_channel(channelid)
                        embed = discord.Embed(
                            description=f"{post_msg}", timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=f"Confession",
                                         icon_url=bot.user.avatar)
                        await channel.send(embed=embed)
                    except:
                        embed = discord.Embed(
                            title="🍓 server has no confession channel, setup one using `=confess`")
                        await message.author.send(embed=embed)

                elif str(reaction.emoji) == '❌':
                    embed = discord.Embed(
                        title="Confession post was cancelled ❌")
                    await message.author.send(embed=embed)

            except asyncio.TimeoutError:
                await msg.edit(content="> **You can no longer react to this message**")

        else:
            embed = discord.Embed(
                title="Confession Error", description="A confession should be atleast 5 characters long. Try writing sentences")
            await message.author.send(embed=embed)

    elif message.guild:
        if message.author.bot == False:
            guildid = message.guild.id
            guildid = './guild data/' + str(guildid) + '.json'
            if os.path.exists(guildid):
                with open(guildid, 'r') as f:
                    users = json.load(f)

                await update_data(users, message.author)

                with open(guildid, 'w') as f:
                    json.dump(users, f, indent=4)
            elif not os.path.exists(guildid):
                with open(guildid, "x") as f:
                    print("")
                with open(guildid, 'w') as f:
                    d = {

                    }
                    json.dump(d, f, indent=4)
                with open(guildid, 'r') as f:
                    users = json.load(f)

                await update_data(users, message.author)

                with open(guildid, 'w') as f:
                    json.dump(users, f, indent=4)

            with open("./bot/status.json", "r") as f:
                D = json.load(f)

            status = D["status"]

            if status == "online" or status == "idle":

                with open('./local/banned.json', 'r') as f:
                    banned_users = json.load(f)

                if str(message.author.id) not in banned_users or banned_users[str(message.author.id)] == False:
                    try:
                        with open("./local/settings.json") as s:
                            set = json.load(s)

                        if str(message.author.id) not in set or set[f"{message.author.id}"]["personal_ping"] == True:
                            with open("./local/personalping.json", "r") as f:
                                ping = json.load(f)

                            if str(message.author.id) in ping:
                                id = message.author.id
                                guildid = message.channel.guild.id
                                guildid = './guild data/' + \
                                    str(guildid) + '.json'
                                with open(guildid, 'r') as g:
                                    users = json.load(g)

                                color = users[str(id)]['color']

                                ping1 = ping[f'{message.author.id}']['ping1']
                                ping2 = ping[f'{message.author.id}']['ping2']
                                ping3 = ping[f'{message.author.id}']['ping3']

                                if ping1 == message.content:
                                    res1 = ping[f'{message.author.id}']['res1']
                                    emb1 = ping[f'{message.author.id}']['embed1']

                                    if emb1 == True:

                                        embed = discord.Embed(
                                            description=str(res1),
                                            color=color,
                                            timestamp=datetime.datetime.utcnow()
                                        )

                                        embed.set_author(
                                            name=message.author, icon_url=message.author.avatar)

                                        await message.channel.send(embed=embed)

                                    elif emb1 == False:

                                        await message.channel.send(res1)

                                elif ping2 == message.content:
                                    res2 = ping[f'{message.author.id}']['res2']
                                    emb2 = ping[f'{message.author.id}']['embed2']

                                    if emb2 == True:

                                        embed = discord.Embed(
                                            description=str(res2),
                                            color=color,
                                            timestamp=datetime.datetime.utcnow()
                                        )

                                        embed.set_author(
                                            name=message.author, icon_url=message.author.avatar)

                                        await message.channel.send(embed=embed)

                                    elif emb2 == False:

                                        await message.channel.send(res2)

                                elif ping3 == message.content:
                                    res3 = ping[f'{message.author.id}']['res3']
                                    emb3 = ping[f'{message.author.id}']['embed3']

                                    if emb3 == True:

                                        embed = discord.Embed(
                                            description=str(res3),
                                            color=color,
                                            timestamp=datetime.datetime.utcnow()
                                        )

                                        embed.set_author(
                                            name=message.author, icon_url=message.author.avatar)

                                        await message.channel.send(embed=embed)

                                    elif emb3 == False:

                                        await message.channel.send(res3)

                    except:
                        print("Error")

                with open('./local/banned.json', 'r') as f:
                    banned_users = json.load(f)

                if str(message.author.id) not in banned_users or banned_users[str(message.author.id)] == False:
                    try:
                        with open("./local/settings.json") as s:
                            set = json.load(s)

                        if str(message.author.id) not in set or set[f"{message.author.id}"]["server_ping"] == True:
                            with open("./local/serverping.json", "r") as f:
                                ping = json.load(f)

                            if str(message.guild.id) in ping:
                                id = message.author.id
                                guildid = message.channel.guild.id
                                guildid = './guild data/' + \
                                    str(guildid) + '.json'
                                with open(guildid, 'r') as g:
                                    users = json.load(g)

                                color = users[str(id)]['color']

                                ping1 = ping[f'{message.guild.id}']['ping1']
                                ping2 = ping[f'{message.guild.id}']['ping2']
                                ping3 = ping[f'{message.guild.id}']['ping3']
                                ping4 = ping[f'{message.guild.id}']['ping4']
                                ping5 = ping[f'{message.guild.id}']['ping5']

                                if ping1 == message.content:
                                    res1 = ping[f'{message.guild.id}']['res1']
                                    emb1 = ping[f'{message.guild.id}']['embed1']

                                    if emb1 == True:

                                        embed = discord.Embed(
                                            description=str(res1),
                                            color=color,
                                            timestamp=datetime.datetime.utcnow()
                                        )

                                        embed.set_author(
                                            name=message.author, icon_url=message.author.avatar)

                                        await message.channel.send(embed=embed)

                                    elif emb1 == False:

                                        await message.channel.send(res1)

                                elif ping2 == message.content:
                                    res2 = ping[f'{message.guild.id}']['res2']
                                    emb2 = ping[f'{message.guild.id}']['embed2']

                                    if emb2 == True:

                                        embed = discord.Embed(
                                            description=str(res2),
                                            color=color,
                                            timestamp=datetime.datetime.utcnow()
                                        )

                                        embed.set_author(
                                            name=message.author, icon_url=message.author.avatar)

                                        await message.channel.send(embed=embed)

                                    elif emb2 == False:

                                        await message.channel.send(res2)

                                elif ping3 == message.content:
                                    res3 = ping[f'{message.guild.id}']['res3']
                                    emb3 = ping[f'{message.guild.id}']['embed3']

                                    if emb3 == True:

                                        embed = discord.Embed(
                                            description=str(res3),
                                            color=color,
                                            timestamp=datetime.datetime.utcnow()
                                        )

                                        embed.set_author(
                                            name=message.author, icon_url=message.author.avatar)

                                        await message.channel.send(embed=embed)

                                    elif emb3 == False:

                                        await message.channel.send(res3)

                                elif ping4 == message.content:
                                    res4 = ping[f'{message.guild.id}']['res4']
                                    emb4 = ping[f'{message.guild.id}']['embed4']

                                    if emb4 == True:

                                        embed = discord.Embed(
                                            description=str(res4),
                                            color=color,
                                            timestamp=datetime.datetime.utcnow()
                                        )

                                        embed.set_author(
                                            name=message.author, icon_url=message.author.avatar)

                                        await message.channel.send(embed=embed)

                                    elif emb4 == False:

                                        await message.channel.send(res4)

                                elif ping5 == message.content:
                                    res5 = ping[f'{message.guild.id}']['res5']
                                    emb5 = ping[f'{message.guild.id}']['embed5']

                                    if emb5 == True:

                                        embed = discord.Embed(
                                            description=str(res5),
                                            color=color,
                                            timestamp=datetime.datetime.utcnow()
                                        )

                                        embed.set_author(
                                            name=message.author, icon_url=message.author.avatar)

                                        await message.channel.send(embed=embed)

                                    elif emb5 == False:

                                        await message.channel.send(res5)

                    except:
                        print("Error")

                with open('./local/banned.json', 'r') as f:
                    banned_users = json.load(f)

                if str(message.author.id) not in banned_users or banned_users[str(message.author.id)] == False:
                    guildid = message.guild.id
                    channelid = message.channel.id

                    with open("./local/count.json", "rb") as f:
                        data = orjson.loads(f.read())

                    if str(guildid) in data:
                        if data[f"{guildid}"]["channel"] == channelid and checkint(message.content):
                            content, current = int(
                                message.content), data[f"{guildid}"]["number"]

                            if data[f"{guildid}"]["previousUser"] == message.author.id:
                                await message.add_reaction("❌")
                                embed = discord.Embed(
                                    description=f"{message.author.mention} **You cannot count twice in a row.** Next number is **1**.")
                                await message.channel.send(embed=embed)
                                data[f"{guildid}"]["number"], data[f"{guildid}"]["previousUser"] = 1, 0

                                with open("./local/count.json", "wb") as f:
                                    f.write(orjson.dumps(data))

                                with open(f"./guild data/{guildid}.json", "r") as f:
                                    users = json.load(f)

                                xp = users[str(message.author.id)
                                           ]['experience'] - current
                                lvl = int(xp ** (1/4))
                                users[str(id)]['level'] = lvl
                                users[str(message.author.id)
                                      ]['experience'] = xp

                                with open(f"./guild data/{guildid}.json", 'w') as f:
                                    json.dump(users, f, indent=4)

                            else:
                                if content == current and content == 100:
                                    await message.add_reaction("💯")

                                    next = current + 1
                                    data[f"{guildid}"]["number"], data[f"{guildid}"]["previousUser"] = next, message.author.id

                                    with open("./local/count.json", "wb") as f:
                                        f.write(orjson.dumps(data))

                                    with open(f"./guild data/{guildid}.json", "r") as f:
                                        users = json.load(f)

                                    xp = users[str(message.author.id)
                                               ]['experience'] + current
                                    lvl = int(xp ** (1/4))
                                    users[str(id)]['level'] = lvl
                                    users[str(message.author.id)
                                          ]['experience'] = xp

                                    with open(f"./guild data/{guildid}.json", 'w') as f:
                                        json.dump(users, f, indent=4)

                                elif content == current and content != 100:
                                    await message.add_reaction("✅")

                                    next = current + 1
                                    data[f"{guildid}"]["number"], data[f"{guildid}"]["previousUser"] = next, message.author.id

                                    with open("./local/count.json", "wb") as f:
                                        f.write(orjson.dumps(data))

                                    with open(f"./guild data/{guildid}.json", "r") as f:
                                        users = json.load(f)

                                    xp = users[str(message.author.id)
                                               ]['experience'] + current
                                    lvl = int(xp ** (1/4))
                                    users[str(id)]['level'] = lvl
                                    users[str(message.author.id)
                                          ]['experience'] = xp

                                    with open(f"./guild data/{guildid}.json", 'w') as f:
                                        json.dump(users, f, indent=4)

                                else:
                                    await message.add_reaction("❌")
                                    embed = discord.Embed(
                                        description=f"{message.author.mention} Ruined the count at **{current}**! Next number is **1**.")
                                    await message.channel.send(embed=embed)
                                    data[f"{guildid}"]["number"] = 1

                                    with open("./local/count.json", "wb") as f:
                                        f.write(orjson.dumps(data))

                                    with open(f"./guild data/{guildid}.json", "r") as f:
                                        users = json.load(f)

                                    xp = users[str(message.author.id)
                                               ]['experience'] - current
                                    lvl = int(xp ** (1/4))
                                    users[str(id)]['level'] = lvl
                                    users[str(message.author.id)
                                          ]['experience'] = xp

                                    with open(f"./guild data/{guildid}.json", 'w') as f:
                                        json.dump(users, f, indent=4)
                    else:
                        data[f"{guildid}"] = {}
                        data[f"{guildid}"]["number"], data[f"{guildid}"]["previousUser"], data[f"{guildid}"]["channel"] = 1, 0, 0

                        with open("./local/count.json", "wb") as f:
                            f.write(orjson.dumps(data))

                    if "michelle" == message.content or "Michelle" == message.content or "MICHELLE" == message.content:
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
                            description=f"Use `{get_prefix}help` for the help command",
                            color=color,
                            timestamp=datetime.datetime.utcnow()
                        )

                        embed.set_author(name=message.author,
                                         icon_url=message.author.avatar)
                        await message.channel.send(embed=embed)

            with open('./local/banned.json', 'r') as f:
                banned_users = json.load(f)

            if str(message.author.id) not in banned_users or banned_users[str(message.author.id)] == False:
                if message.guild:
                    guildid = message.channel.guild.id
                    guildid = './guild data/' + str(guildid) + '.json'
                    if os.path.exists(guildid):
                        await bot.process_commands(message)

                    elif not os.path.exists(guildid):
                        with open(guildid, 'x') as f:
                            print("")
                        with open(guildid, 'w') as f:
                            d = {

                            }
                            json.dump(d, f, indent=4)

                        await bot.process_commands(message)
                else:
                    await bot.process_commands(message)


async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['name'] = str(user.name)
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['rank'] = 0
        users[f'{user.id}']['level'] = 1
        users[f'{user.id}']['color'] = 0x95a5a6
        users[f'{user.id}']['sage_spell'] = False
        users[f'{user.id}']['hunter_spell'] = False
        users[f'{user.id}']['wraith_spell'] = False
        users[f'{user.id}']['chameleon'] = False
        users[f'{user.id}']['transformation'] = False


@bot.command()
async def online(ctx):
    with open("./local/auth.json", 'r') as f:
        auth = json.load(f)
    userid = ctx.author.id

    with open("./local/prefix.json", "r") as f:
        L = json.load(f)

    if str(ctx.guild.id) in L:
        get_prefix = L[str(ctx.guild.id)]["prefix"]
    elif str(ctx.guild.id) not in L:
        get_prefix = "="

    try:
        if auth[str(userid)]['auth'] == True:
            with open("./bot/status.json", "r") as f:
                D = json.load(f)

            status = D["status"]
            if status == "offline":
                for i in initial_extensions:
                    bot.load_extension(i)

            D["status"] = "online"
            text = D["text"]
            activity = D["activity"]

            if text == None:
                if activity == None:
                    await bot.change_presence(status=discord.Status.online)
                elif activity == "playing":
                    await bot.change_presence(activity=discord.Game(name="VALORANT"))
                    D["text"] = "VALORANT"
                elif activity == "watching":
                    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Spider-Man : No Way Home"))
                    D["text"] = "Spider-Man : No Way Home"
                elif activity == "listening":
                    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Spotify"))
                    D["text"] = "Spotify"
            else:
                if activity == None:
                    await bot.change_presence(status=discord.Status.online)
                elif activity == "playing":
                    await bot.change_presence(activity=discord.Game(name=text))
                elif activity == "watching":
                    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=text))
                elif activity == "listening":
                    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=text))

            with open("./bot/status.json", "w") as f:
                json.dump(D, f, indent=4)

    except:
        await ctx.author.send(content=f'Oh! You are not authorised to use that')


@bot.command()
async def idle(ctx):
    with open("./local/auth.json", 'r') as f:
        auth = json.load(f)
    userid = ctx.author.id

    with open("./local/prefix.json", "r") as f:
        L = json.load(f)

    if str(ctx.guild.id) in L:
        get_prefix = L[str(ctx.guild.id)]["prefix"]
    elif str(ctx.guild.id) not in L:
        get_prefix = "="

    try:
        if auth[str(userid)]['auth'] == True:
            with open("./bot/status.json", "r") as f:
                D = json.load(f)

            status = D["status"]
            if status == "offline":
                for i in initial_extensions:
                    bot.load_extension(i)

            D["status"] = "idle"
            text = D["text"]
            activity = D["activity"]

            if text == None:
                if activity == None:
                    await bot.change_presence(status=discord.Status.idle)
                elif activity == "playing":
                    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name="VALORANT"))
                    D["text"] = "VALORANT"
                elif activity == "watching":
                    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="Avengers Endgame"))
                    D["text"] = "Avengers Endgame"
                elif activity == "listening":
                    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name="Spotify"))
                    D["text"] = "Spotify"
            else:
                if activity == None:
                    await bot.change_presence(status=discord.Status.idle)
                elif activity == "playing":
                    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=text))
                elif activity == "watching":
                    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=text))
                elif activity == "listening":
                    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name=text))

            with open("./bot/status.json", "w") as f:
                json.dump(D, f, indent=4)

    except:
        await ctx.author.send(content=f'Oh! You are not authorised to use that')


@bot.command()
async def offline(ctx):
    with open("./local/auth.json", 'r') as f:
        auth = json.load(f)
    userid = ctx.author.id

    with open("./local/prefix.json", "r") as f:
        L = json.load(f)

    if str(ctx.guild.id) in L:
        get_prefix = L[str(ctx.guild.id)]["prefix"]
    elif str(ctx.guild.id) not in L:
        get_prefix = "="

    try:
        if auth[str(userid)]['auth'] == True:
            with open("./bot/status.json", "r") as f:
                D = json.load(f)

            D["status"] = "offline"
            D["activity"] = None
            D["text"] = None

            await bot.change_presence(status=discord.Status.offline)
            for i in initial_extensions:
                bot.unload_extension(i)

            with open("./bot/status.json", "w") as f:
                json.dump(D, f, indent=4)

    except:
        await ctx.author.send(content=f'Oh! You are not authorised to use that')


@bot.command()
async def invisible(ctx):
    await bot.change_presence(status=discord.Status.invisible)


@bot.command(aliases=["authlist"])
async def botauth(ctx: Context):
    with open("./local/auth.json", 'r') as f:
        auth = json.load(f)

    try:
        if auth[str(ctx.author.id)]['auth'] == True:
            with open("./local/auth.json", "r") as f:
                users = json.load(f)

            L = ""
            count = 1
            for i in users:
                if users[str(i)]["auth"] == True:
                    i = int(i)
                    name = bot.get_user(i)
                    L += f"**{count}.** `{name}`\n"
                    count += 1

            await ctx.send(f"**Auth List**\n{L}")

    except:
        pass


@bot.command()
async def botstatus(ctx):
    with open("./local/auth.json", 'r') as f:
        auth = json.load(f)

    try:
        if auth[str(ctx.author.id)]['auth'] == True:
            with open("./bot/status.json", "r") as f:
                stat = json.load(f)

            status = stat["status"]

            await ctx.send(f"**Status**: `{status}`")

    except:
        pass


@bot.command()
async def botping(ctx):
    with open("./local/auth.json", 'r') as f:
        auth = json.load(f)

    try:
        if auth[str(ctx.author.id)]['auth'] == True:
            await ctx.send(f'**Ping**: `{round(bot.latency*1000)} ms`')

    except:
        pass


@bot.command()
async def botcount(ctx):
    with open("./local/auth.json", 'r') as f:
        auth = json.load(f)

    try:
        if auth[str(ctx.author.id)]['auth'] == True:
            await ctx.send(f'**Server Count**: `{str(len(bot.guilds))} Servers`')

    except:
        pass

bot.run(settings.apiToken)
