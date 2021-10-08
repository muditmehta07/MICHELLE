import discord
from discord.ext import commands
import datetime
import json
import asyncio
import os
import hashlib
import requests
import random
from PIL import Image

from aiohttp import ClientSession
import json
import datetime

from discord.ext.commands.context import Context

async def get(session: object, url: object) -> object:
    async with session.get(url) as response:
        return await response.text()

class GamesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dice(self, ctx):
        roll = random.randint(1, 6)

        if roll == 1:
            await ctx.message.add_reaction("1️⃣")
        elif roll == 2:
            await ctx.message.add_reaction("2️⃣")
        elif roll == 3:
            await ctx.message.add_reaction("3️⃣")
        elif roll == 4:
            await ctx.message.add_reaction("4️⃣")
        elif roll == 5:
            await ctx.message.add_reaction("5️⃣")
        elif roll == 6:
            await ctx.message.add_reaction("6️⃣")
        else:
            await ctx.message.add_reaction("❓")

    @commands.command()
    async def flip(self, ctx):
        await ctx.send("A coin was flipped...")
        await asyncio.sleep(1)
        roll = random.randint(1, 2)
        if roll == 1:
            await ctx.send("It's **heads**")
        elif roll == 2:
            await ctx.send("It's **tails**")
        else:
            await ctx.send("It's **heads**")

    @commands.command(aliases = ['8ball', '8Ball'])
    async def eightball(self, ctx, question : str = None):
        await ctx.channel.trigger_typing()
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        responses = ['As I see it, yes.',
                'Yes',
                'Positive',
                'From my point of view? Yes',
                'Convinced',
                'Most Likley',
                'Chances High',
                'No',
                'Negative',
                'Not Convinced',
                'Perhaps',
                'Not Sure',
                'Maybe',
                'I cannot predict now',
                'Im to lazy to predict',
                'I am tired. *proceeds with sleeping*']

        if question == None:
            response = "Dude, you had to ask a question"
        else:
            response = random.choice(responses)

        embed=discord.Embed(
            description = f"**🎱  8 Ball** :\n{response}",
            timestamp = datetime.datetime.utcnow(),
            color=color
        )

        file = discord.File("./pictures/8.png")
        embed.set_thumbnail(url="attachment://8.png")
        embed.set_author(name = ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(file=file, embed=embed)

def setup(bot):
    bot.add_cog(GamesCog(bot))