import discord
from discord.ext import commands
import os
import datetime
import json
import asyncio

from discord.ext.commands.context import Context

class DevCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def botban(self, ctx : Context, id : str = None):
        if ctx.author.id == 488996680058798081:
            if id != None:
                id = int(id)
                with open('./local/banned.json', 'r') as f:
                    users = json.load(f)

                if str(id) not in users:
                    users[str(id)] = True

                    member = self.bot.get_user(id)

                    embed = discord.Embed(
                        title = "Michelle | Banned",
                        description = "You have been **banned** from using the Discord Bot - `MICHELLE`.\n\nWe have noticed some unusual activity from you, and therefore are banning your account to be able to access any of the bot's commands.\n\nLet us know if we made a mistake and request unban:\n[Unban Request Form](https://forms.gle/eHmSGmThAezskCTn9)",
                        timestamp = datetime.datetime.utcnow()
                    )

                    await member.send(embed=embed)

                elif str(id) in users:
                    del users[str(id)]

                    member = self.bot.get_user(id)

                    embed = discord.Embed(
                        title = "Michelle | Unbanned",
                        description = "You have been **unbanned** from using the Discord Bot - `MICHELLE`.\n\nWe are happy to inform you that your ban has been removed. You now have complete access to all of Michelle's commands.\n**Have a great day!**",
                        timestamp = datetime.datetime.utcnow()
                    )

                    await member.send(embed=embed)

                with open('./local/banned.json', 'w') as f:
                    json.dump(users, f, indent=4)

                await ctx.message.add_reaction("✅")

    @commands.command()
    async def passive(self, ctx : Context):
        id = ctx.author.id
        cross = self.bot.get_emoji(880679527200735273)

        if id != None:
            id = int(id)
            with open('./local/banned.json', 'r') as f:
                users = json.load(f)

            if str(id) not in users:

                embed = discord.Embed(title = "Passive Mode",
                description = f"**Are you sure you want to enable Passive Mode? Michelle will no longer work for you, nor respond to any of your commands. To disable Passive Mode, you must contact our team through mail or the support server which could take days.**\n\n**Do you still wish to enable Passive Mode? Type `yes` to continue**",
                timestamp=datetime.datetime.utcnow())
                
                botmsg = await ctx.send(embed = embed)

                try:
                    def check(message):
                        if message.author.id == ctx.author.id:
                            message.content = message.content.lower()
                            return message.content == "yes"

                    ping = await self.bot.wait_for("message", check=check, timeout=20)
                    ping = ping.content
                
                    if "yes" == ping:
                        users[str(id)] = True

                        embed = discord.Embed(
                            title = "Passive Mode",
                            description = "**Passive Mode has been enabled.**\n\nYou have enabled the Passive Mode, Michelle will stop responding and reading any of your `Message.Content`. You will no longer be able to use most of Michelle's features.\n**Contact Us : `michelle.discordbot@gmail.com` to get the Passive Mode disabled.**",
                            timestamp = datetime.datetime.utcnow()
                        )

                        await ctx.send(embed=embed)

                        with open('./local/banned.json', 'w') as f:
                            json.dump(users, f, indent=4)

                except asyncio.TimeoutError:
                    await botmsg.add_reaction(f"{cross}")

    @commands.command()
    async def active(self, ctx : Context, id : str = None):
        if ctx.author.id == 488996680058798081:
            if id != None:
                id = int(id)
                with open('./local/banned.json', 'r') as f:
                    users = json.load(f)

                if str(id) in users:
                    del users[str(id)]

                    member = self.bot.get_user(id)

                    embed = discord.Embed(
                        title = "Active Mode",
                        description = "**Passive Mode has been disabled.**\n\nMichelle will start responding to you, and also read your `Message.Content` data. If you don't want Michelle to read and record any of your data, kindly enable the Passive Mode.",
                        timestamp = datetime.datetime.utcnow()
                    )

                    await member.send(embed=embed)

                    with open('./local/banned.json', 'w') as f:
                        json.dump(users, f, indent=4)

    @commands.command()
    async def deletemydata(self, ctx : Context):
        id = ctx.author.id

        embed = discord.Embed(title = "Delete My Data",
        description = f"**Are you sure you want to delete all your data? Your Michelle data will be lost forever including your `XP`, `Items`, `Weapons`, `Chests`, `Personal Pings` and `Settings`.**\n\n**Do you still wish to Delete your data? Type `yes` to continue**",
        timestamp=datetime.datetime.utcnow())

        botmsg = await ctx.send(embed = embed)

        cross = self.bot.get_emoji(880679527200735273)

        try:
            def check(message):
                if message.author.id == ctx.author.id:
                    message.content = message.content.lower()
                    return message.content == "yes"

            ping = await self.bot.wait_for("message", check=check, timeout=20)
            ping = ping.content
        
            if "yes" == ping:
                guild_path = "./guild data"
                guild_list = os.listdir(guild_path)

                for i in guild_list:
                    with open(f"./guild data/{i}", "r") as f:
                        users = json.load(f)

                    if str(id) in users:
                        del users[str(id)]

                    with open(f"./guild data/{i}", "w") as f:
                        json.dump(users, f, indent=4)

                local_list = ["beta.json", "chest.json", "invite.json", "items.json", "personalping.json", "settings.json", "warn.json", "weapons.json"]

                for i in local_list:
                    with open(f"./local/{i}", "r") as f:
                        users = json.load(f)

                    if str(id) in users:
                        del users[str(id)]

                    with open(f"./local/{i}", "w") as f:
                        json.dump(users, f, indent=4)

                embed = discord.Embed(
                    title = "Delete My Data",
                    description = "All your data stored in Michelle has been erased.\n\n**If you do not want Michelle to create any new data for you, use command `=passive` to switch to Passive Mode (Michelle will no longer work for you in that case)**",
                    timestamp = datetime.datetime.utcnow()
                )

                await ctx.send(embed=embed)

        except asyncio.TimeoutError:
            await botmsg.add_reaction(f"{cross}")


async def setup(bot):
    await bot.add_cog(DevCog(bot))
