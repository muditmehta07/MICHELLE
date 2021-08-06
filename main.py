import discord
from discord import user
from discord import channel
from discord import message
from discord.colour import Color
from discord.enums import ActivityType
from discord.ext.commands.converter import _get_from_guilds
from discord.message import Message
from discord.utils import get
from discord.ext import commands,tasks
import os
import json
from itertools import cycle
import datetime
import topgg

def get_the_prefix(client, message):
    with open("./local/prefix.json", "r") as f:
        L = json.load(f)

    if str(message.guild.id) in L:
        prefix = L[str(message.guild.id)]["prefix"]
    elif str(message.guild.id) not in L:
        prefix = "="

    return prefix


intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix= get_the_prefix , intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
        mstat = f'{str(len(bot.guilds))} servers || =help'
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=mstat))

@bot.event
async def on_member_join(member):
    guildid = member.guild.id
    guildid = './guild data/'+ str(guildid) +'.json'
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
    if message.author.bot == False:
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
        if l1==10:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(message.guild.id) in L:
                prefix = L[str(message.guild.id)]["prefix"]
            elif str(message.guild.id) not in L:
                prefix = "="
            up_message = f'{user.mention} *leveled up to* `Level {lvl_end}` ⏫'
            up_description = f'Unlocked *{prefix}kill* 🔓'
            level_embed = discord.Embed(description = up_message, color = color, timestamp=datetime.datetime.utcnow())
            level_embed.set_footer(text = up_description)
            level_embed.set_author(name = user, icon_url= user.avatar_url)
            await message.channel.send(embed=level_embed)
        elif l1==5:
            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(message.guild.id) in L:
                prefix = L[str(message.guild.id)]["prefix"]
            elif str(message.guild.id) not in L:
                prefix = "="
            up_message = f'{user.mention} *leveled up to* `Level {lvl_end}` ⏫'
            up_description = f'Unlocked *{prefix}theme* 🔓'
            level_embed = discord.Embed(description = up_message, color = color, timestamp=datetime.datetime.utcnow())
            level_embed.set_footer(text = up_description)
            level_embed.set_author(name = user, icon_url= user.avatar_url)
            await message.channel.send(embed=level_embed)
        else:
            up_message = f'{user.mention} leveled up to `Level {lvl_end}` ⏫ '
            level_embed = discord.Embed(description = up_message, color = color, timestamp=datetime.datetime.utcnow())
            level_embed.set_author(name = user, icon_url= user.avatar_url)
            await message.channel.send(embed=level_embed)
