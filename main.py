import discord
from discord import user
from discord import channel
from discord import message
from discord.colour import Color
from discord.enums import ActivityType, Status
from discord.ext.commands.converter import _get_from_guilds
from discord.message import Message
from discord.utils import get
from discord.ext import commands,tasks
import os, pickle
import json
from itertools import cycle
import datetime
from discord.ext.commands.context import Context

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix= "=" , intents=intents)

@bot.event
async def on_member_join(member):
    guildid = member.guild.id
    guildid = './guild data/'+ str(guildid) +'.json'

    with open(guildid, 'r') as f:
        users = json.load(f)

    await update_data(users, member)

    with open(guildid, 'w') as f:
        json.dump(users, f, indent=4)

@bot.event
async def on_message(message):
        if message.guild:
            guildid = message.channel.guild.id
            guildid = './guild data/'+ str(guildid) +'.json'
            if os.path.exists(guildid):
                with open(guildid, 'r') as f:
                    users = json.load(f)

                await update_data(users, message.author)
                await add_experience(users, message.author, 5)
                await level_up(users, message.author, message)

                with open(guildid, 'w') as f:
                    json.dump(users, f, indent=4)
            elif not os.path.exists(guildid):
                with open(guildid, 'x') as f:
                    print("")
                with open(guildid, 'w') as f:
                    d = {

                    }
                    json.dump(d, f, indent=4)
                with open(guildid, 'r') as f:
                    users = json.load(f)
                await update_data(users, message.author)
                await add_experience(users, message.author, 5)
                await level_up(users, message.author, message)

                with open(guildid, 'w') as f:
                    json.dump(users, f, indent=4)

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

async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp

async def level_up(users, user, message):
    with open('levels.json', 'r') as g:
        levels = json.load(g)
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1 / 4))
    if lvl_start < lvl_end:
        users[f'{user.id}']['level'] = lvl_end
        l1 = users[f'{user.id}']['level']
        color = users[f'{user.id}']['color']
        with open("./bot/status.json", "r") as f:
            D = json.load(f)

        status = D["status"]
        if status == "online" or status == "idle":
            with open("./local/settings.json") as s:
                set = json.load(s)

            if str(message.author.id) in set:
                if set[f"{message.author.id}"]["level_ups"] == True:
                    if l1==10:
                        with open("./local/prefix.json", "r") as f:
                            L = json.load(f)

                        up_message = f'{user.mention} *leveled up to* `Level {lvl_end}` ⏫'
                        up_description = f'Unlocked *{prefix}kill* 🔓'
                        level_embed = discord.Embed(description = up_message, color = color, timestamp=datetime.datetime.utcnow())
                        level_embed.set_footer(text = up_description)
                        level_embed.set_author(name = user, icon_url= user.avatar_url)
                        await message.channel.send(embed=level_embed)
