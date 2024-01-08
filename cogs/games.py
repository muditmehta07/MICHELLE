import discord
from discord.ext import commands
import datetime
import json
import asyncio
import orjson
import random
import json
import datetime

from discord.ext.commands.context import Context

async def get(session: object, url: object) -> object:
    async with session.get(url) as response:
        return await response.text()

class GamesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def checkint(n):
        try:
            int(n)
            return True

        except ValueError:
            return False

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        id = guild.id

        with open("./local/count.json", "rb") as f:
            data = orjson.loads(f.read())

        if not id in data:
            data[f"{guild.id}"] = {}
            data[f"{guild.id}"]["number"], data[f"{guild.id}"]["previousUser"], data[f"{guild.id}"]["channel"] = 1, 0, 0

            with open("./local/count.json", "wb") as f:
                f.write(orjson.dumps(data))

    @commands.command()
    async def dice(self, ctx):
        roll = random.randint(1, 6)

        compmsg = await ctx.send("A dice was rolled...")
        await asyncio.sleep(1)

        if roll == 1:
            await compmsg.edit("🎲 : It's a **1**")
        elif roll == 2:
           await compmsg.edit("🎲 : It's a **2**")
        elif roll == 3:
            await compmsg.edit("🎲 : It's a **3**")
        elif roll == 4:
            await compmsg.edit("🎲 : It's a **4**")
        elif roll == 5:
            await compmsg.edit("🎲 : It's a **5**")
        elif roll == 6:
            await compmsg.edit("🎲 : It's a **6**")
        else:
            await ctx.message.add_reaction("❓")

    @commands.command()
    async def flip(self, ctx):
        compmsg = await ctx.send("A coin was flipped...")
        await asyncio.sleep(1)
        roll = random.randint(1, 2)
        if roll == 1:
            await compmsg.edit("🪙 : It's **heads**")
        elif roll == 2:
            await compmsg.edit("🪙 : It's **tails**")
        else:
            await compmsg.edit("🪙 : It's **heads**")

    @commands.command(aliases = ['8ball', '8Ball'])
    async def eightball(self, ctx, question : str = None):
        responses = [
            "It is certain.",
            "As I see it, yes.",
            "Reply hazy, try again.",
            "Don't count on it.",
            "It is decidedly so.",
            "Most likely.",
            "Ask again later.",
            "My reply is no.",
            "Without a doubt.",
            "Outlook good.",
            "Better not tell you now.",
            "My sources say no.",
            "Yes definitely.",
            "Yes.",
            "Cannot predict now.",
            "Outlook not so good.",
            "You may rely on it.",
            "Signs point to yes.",
            "Concentrate and ask again.",
            "Very doubtful."
            ]

        if question == None:
            id = ctx.author.id
            guildid = ctx.guild.id
            guildid = './guild data/'+ str(guildid) +'.json'
            with open(guildid, 'r') as f:
                users = json.load(f)

            color = users[str(id)]['color']

            embed = discord.Embed(
                description = f"__**Description**__\n> The magic 8 ball anything. It tells nothing but the truth, trust it at all costs and you shall succeed.\n\n__**Usage**__\n> `{ctx.prefix}8ball <question>`",
                color = color, 
                timestamp=datetime.datetime.utcnow()
                )

            embed.set_author(name = "8 Ball Help ❓")
            await ctx.send(embed = embed)

        else:
            response = random.choice(responses)
            await ctx.send(f"🎱 : {response}")

    @commands.command(aliases=["count"])
    @commands.has_permissions(administrator=True)
    async def counting(self, message):
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

        with open("./local/count.json", "rb") as f:
            data = orjson.loads(f.read())

        guildid, channelid, channel = message.guild.id, message.channel.id, data[f"{message.guild.id}"]["channel"]
        
        if message.channel.id == channel:
            embed = discord.Embed(description="**This channel is already set as the `Counting Channel`**")
            await message.channel.send(embed=embed)

        else:
            data[f"{guildid}"]["channel"], data[f"{guildid}"]["number"], data[f"{guildid}"]["previousUser"] = channelid, 1, 0

            with open("./local/count.json", "wb") as f:
                f.write(orjson.dumps(data))

            embed = discord.Embed(
                description=f"**This channel has now been set as your Counting Channel. You can change it anytime by using this command in another channel, or delete it by using the command `{get_prefix}delcounting`.**\n\n"
                f"__**How To Play**__\n• Once you have setup a counting channel. Type **1** to start counting.\n• You must have a partner that can now send **2**.\n• Continue the count and try not to break it by sending the wrong number.\n\n"
                f"__**Rules**__\n• You cannot count two numbers in a row.\n• Bots are not allowed to count. (Don't bother making one)\n\n"
                f"__**Rewards**__\n• Everytime you count, you are awarded with XP.\n• The higher the count, the higher the XP.\n• Breaking the count drops your XP depending upon how high the count was.",
                color=color,
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name="Counting", icon_url=self.bot.user.avatar)
            await message.channel.send(embed=embed)

    @commands.command(aliases=["delcount"])
    @commands.has_permissions(administrator=True)
    async def delcounting(self, message):
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

        with open("./local/count.json", "r") as f:
            data = json.load(f)

        if str(message.channel.guild.id) in data:
            del data[f"{str(message.channel.guild.id)}"]

            with open("./local/count.json", "w") as f:
                json.dump(data, f, indent=4)

            embed = discord.Embed(description="**Delete Successful!** This server no longer has a `Counting Channel`.")
            await message.channel.send(embed=embed)

        else:
            embed = discord.Embed(description="**Delete Failed!** This server does not have a `Counting Channel`.")
            await message.channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(GamesCog(bot))