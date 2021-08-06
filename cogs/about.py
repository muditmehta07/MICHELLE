import discord
from discord.ext import commands
import os
import datetime
import json

from discord.ext.commands.context import Context

class AboutCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = "invite", aliases = ["Invite", "INVITE", "link", "LINK", "Link"])
    async def invite(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        embed = discord.Embed(title = "Invite Link 💌",
        description = "Click the link above to invite me to a server", 
        url = "https://discordapp.com/oauth2/authorize?client_id=840180379389263882&scope=bot&permissions=4228906231",
        color = color, timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        await message.channel.send(embed = embed)

    @commands.command()
    async def feedback(self, message):
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
    async def server(self, ctx):
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = self.bot.get_guild(guildid)
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        roles = str(len(guild.roles))
        emojis = str(len(guild.emojis))
        text = str(len(guild.text_channels))
        voice = str(len(guild.voice_channels))
        cat = voice = str(len(guild.categories))

        embeded = discord.Embed(title=guild, description=f'**Server Owner** : *{guild.owner}*', color=color, timestamp = datetime.datetime.utcnow())
        embeded.set_thumbnail(url=guild.icon_url)
        embeded.add_field(name="Server ID :", value=f'*{guild.id}*', inline=False)
        embeded.add_field(name="Created On :", value=f"*{guild.created_at.strftime('%d %B %Y at %H:%M')}*", inline=False)

        embeded.add_field(name="Server Level", value=f'*{guild.premium_tier}*', inline=True)
        embeded.add_field(name="Server Region", value=f'*{guild.region}*', inline=True)
        embeded.add_field(name="Verification Level", value=f'*{guild.verification_level}*', inline=True)

        embeded.add_field(name="Members", value=f'*{guild.member_count}*', inline=True)
        embeded.add_field(name="Roles", value=f'*{roles}*', inline=True)
        embeded.add_field(name="Emojis", value=f'*{emojis}*', inline=True)
        embeded.add_field(name="Categories", value=f'*{cat}*', inline=True)
        embeded.add_field(name="Text Channels", value=f'*{text}*', inline=True)
        embeded.add_field(name="Voice Channels", value=f'*{voice}*', inline=True)

        await ctx.send(embed=embeded)

    @commands.command()
    async def user(self, ctx, *, user: discord.Member = None):
        id = ctx.author.id
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        if user is None:
            user = ctx.author

        if user.activity == None:
            activity = "No Activity"
        else:
            activity = user.activity.name

        if user.status == discord.Status.online:
            status = "🟢 Online"
        elif user.status == discord.Status.offline or user.status == discord.Status.invisible:
            status = "⚫ Offline"
        elif user.status == discord.Status.dnd:
            status = "🔴 Do Not Disturb"
        elif user.status == discord.Status.idle:
            status = "🟡 Idle"

        if user.nick == None:
            nick = "No Nickname"
        else:
            nick = user.nick

        embed = discord.Embed(
            title=f"{user.display_name}'s Info",
            timestamp = datetime.datetime.utcnow(),
            color=color
        )

        embed.set_thumbnail(url=user.avatar_url_as(format="png"))
        embed.add_field(name="__**General Info**__", value=f"**Name** : {user}\n"
                                                                    f"**Status** : {status}\n"
                                                                    f"**Activity** : {activity}", inline=False)
        embed.add_field(name="__**Server Info**__", value=f"**Nickname** : {nick}\n"
                                                                            f"**Joined** : {user.joined_at.__format__('%A %d %B %Y at %H:%M')}\n"
                                                                            f"**Roles** : {' '.join([r.mention for r in user.roles[1:]])}")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(AboutCog(bot))
