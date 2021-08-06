import discord
from discord.ext import commands
import os
import datetime
import json
import emojis

from discord.ext.commands.context import Context

class ReactionCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def reaction(self, ctx):
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
            title = "Reaction Roles 👆🏻",
            description = f"**Create reaction role message** : `{get_prefix}reaction create`\n"
            f"**Add a reaction role** : `{get_prefix}reaction add <emoji> <role>`\n"
            f"**Delete reaction message** : `{get_prefix}reaction rem`\n",
            timestamp = datetime.datetime.utcnow(),
            color=color
        )

        await ctx.send(embed=embed)

    @reaction.command()
    @commands.has_permissions(administrator=True)
    async def create(self, ctx):
        guildid = ctx.guild.id
        guildname = self.bot.get_guild(guildid).name
        channelid = ctx.channel.id
        id = ctx.author.id
        guild = './guild data/'+ str(guildid) +'.json'
        with open(guild, 'r') as g:
            users = json.load(g)

        color = users[str(id)]['color']

        with open("./local/react.json", 'r') as f:
            auth = json.load(f)

        try:
            if not f'{guildid}' in auth:
                auth[f'{guildid}'] = {}
                auth[f'{guildid}']['user'] = str(ctx.author.name)
                auth[f'{guildid}']['server'] = str(guildname)
                auth[f'{guildid}']['channel'] = channelid
                auth[f'{guildid}']['emoji1'] = 'False'
                auth[f'{guildid}']['role1'] = 'False'
                auth[f'{guildid}']['emoji2'] = 'False'
                auth[f'{guildid}']['role2'] = 'False'
                auth[f'{guildid}']['emoji3'] = 'False'
                auth[f'{guildid}']['role3'] = 'False'
                auth[f'{guildid}']['emoji4'] = 'False'
                auth[f'{guildid}']['role4'] = 'False'
                auth[f'{guildid}']['emoji5'] = 'False'
                auth[f'{guildid}']['role5'] = 'False'
                auth[f'{guildid}']['emoji6'] = 'False'
                auth[f'{guildid}']['role6'] = 'False'
                auth[f'{guildid}']['emoji7'] = 'False'
                auth[f'{guildid}']['role7'] = 'False'
                auth[f'{guildid}']['emoji8'] = 'False'
                auth[f'{guildid}']['role8'] = 'False'
                auth[f'{guildid}']['emoji9'] = 'False'
                auth[f'{guildid}']['role9'] = 'False'
                auth[f'{guildid}']['emoji10'] = 'False'
                auth[f'{guildid}']['role10'] = 'False'
                auth[f'{guildid}']['emoji11'] = 'False'
                auth[f'{guildid}']['role11'] = 'False'
                auth[f'{guildid}']['emoji12'] = 'False'
                auth[f'{guildid}']['role12'] = 'False'
                auth[f'{guildid}']['emoji13'] = 'False'
                auth[f'{guildid}']['role13'] = 'False'
                auth[f'{guildid}']['emoji14'] = 'False'
                auth[f'{guildid}']['role14'] = 'False'
                auth[f'{guildid}']['emoji15'] = 'False'
                auth[f'{guildid}']['role15'] = 'False'
                auth[f'{guildid}']['emoji16'] = 'False'
                auth[f'{guildid}']['role16'] = 'False'
                auth[f'{guildid}']['emoji17'] = 'False'
                auth[f'{guildid}']['role17'] = 'False'
                auth[f'{guildid}']['emoji18'] = 'False'
                auth[f'{guildid}']['role18'] = 'False'
                auth[f'{guildid}']['emoji19'] = 'False'
                auth[f'{guildid}']['role19'] = 'False'
                auth[f'{guildid}']['emoji20'] = 'False'
                auth[f'{guildid}']['role20'] = 'False'

                with open("./local/react.json", 'w') as f:
                    json.dump(auth, f, indent=4)
                embed = discord.Embed(
                    title = "Reaction Roles 👆🏻",
                    description = "**This is the reaction message!\nNow add reaction roles.**",
                    timestamp = datetime.datetime.utcnow(),
                    color=color
                )
                message = await ctx.send(embed = embed)
                msgid = message.id
                auth[f'{guildid}']['message'] = msgid
                with open("./local/react.json", 'w') as f:
                    json.dump(auth, f, indent=4)

            elif f'{guildid}' in auth:
                auth[f'{guildid}']['user'] = str(ctx.author.name)
                auth[f'{guildid}']['server'] = str(guildname)
                auth[f'{guildid}']['channel'] = channelid
                auth[f'{guildid}']['emoji1'] = 'False'
                auth[f'{guildid}']['role1'] = 'False'
                auth[f'{guildid}']['emoji2'] = 'False'
                auth[f'{guildid}']['role2'] = 'False'
                auth[f'{guildid}']['emoji3'] = 'False'
                auth[f'{guildid}']['role3'] = 'False'
                auth[f'{guildid}']['emoji4'] = 'False'
                auth[f'{guildid}']['role4'] = 'False'
                auth[f'{guildid}']['emoji5'] = 'False'
                auth[f'{guildid}']['role5'] = 'False'
                auth[f'{guildid}']['emoji6'] = 'False'
                auth[f'{guildid}']['role6'] = 'False'
                auth[f'{guildid}']['emoji7'] = 'False'
                auth[f'{guildid}']['role7'] = 'False'
                auth[f'{guildid}']['emoji8'] = 'False'
                auth[f'{guildid}']['role8'] = 'False'
                auth[f'{guildid}']['emoji9'] = 'False'
                auth[f'{guildid}']['role9'] = 'False'
                auth[f'{guildid}']['emoji10'] = 'False'
                auth[f'{guildid}']['role10'] = 'False'
                auth[f'{guildid}']['emoji11'] = 'False'
                auth[f'{guildid}']['role11'] = 'False'
                auth[f'{guildid}']['emoji12'] = 'False'
                auth[f'{guildid}']['role12'] = 'False'
                auth[f'{guildid}']['emoji13'] = 'False'
                auth[f'{guildid}']['role13'] = 'False'
                auth[f'{guildid}']['emoji14'] = 'False'
                auth[f'{guildid}']['role14'] = 'False'
                auth[f'{guildid}']['emoji15'] = 'False'
                auth[f'{guildid}']['role15'] = 'False'
                auth[f'{guildid}']['emoji16'] = 'False'
                auth[f'{guildid}']['role16'] = 'False'
                auth[f'{guildid}']['emoji17'] = 'False'
                auth[f'{guildid}']['role17'] = 'False'
                auth[f'{guildid}']['emoji18'] = 'False'
                auth[f'{guildid}']['role18'] = 'False'
                auth[f'{guildid}']['emoji19'] = 'False'
                auth[f'{guildid}']['role19'] = 'False'
                auth[f'{guildid}']['emoji20'] = 'False'
                auth[f'{guildid}']['role20'] = 'False'

                with open("./local/react.json", 'w') as f:
                    json.dump(auth, f, indent=4)
                embed = discord.Embed(
                    title = "Reaction Roles 👆🏻",
                    description = "**This is the reaction message!\nNow add reaction roles.**",
                    timestamp = datetime.datetime.utcnow(),
                    color=color
                )
                message = await ctx.send(embed = embed)
                msgid = message.id
                auth[f'{guildid}']['message'] = msgid
                with open("./local/react.json", 'w') as f:
                    json.dump(auth, f, indent=4)

            else:
                embed = discord.Embed(title = "Failed with Error Code == 5.", description = "Oops. Something went wrong. 😬")
                embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
        except:
            embed = discord.Embed(title = "Failed with Error Code == 5.", description = "Oops. Something went wrong. 😬")
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)

    @reaction.command()
    @commands.has_permissions(administrator=True)
    async def add(self, ctx, emoji : str, role : discord.Role):
        guildid = ctx.guild.id
        try:
            with open("./local/react.json", 'r') as f:
                auth = json.load(f)
            L = emojis.get(emoji)
            emoji = list(L)[0]
            role = str(role)
            try:
                if not f'{guildid}' in auth:
                    embed = discord.Embed(
                        title = "Reaction Add 👆🏻",
                        description = "A reaction message does not exist in this server, create one using `=reaction create`",
                        timestamp = datetime.datetime.utcnow())

                    await ctx.send(embed=embed)

                elif f'{guildid}' in auth:
                    msgid = auth[f'{guildid}']['message']
                    msg = await ctx.fetch_message(msgid)
                    embed = msg.embeds[0]
                    embed.description="React to get these roles! 😊"
                    embed.add_field(name = emoji, value = f'`{role}`')

                    if auth[f'{guildid}']['emoji1'] == 'False' and auth[f'{guildid}']['role1'] == 'False':
                        auth[f'{guildid}']['emoji1'] = emoji
                        auth[f'{guildid}']['role1'] = role

                        with open("./local/react.json", 'w') as f:
                            json.dump(auth, f, indent=4)

                        await msg.edit(embed=embed)
                        await msg.add_reaction(emoji)

                    elif auth[f'{guildid}']['emoji2'] == 'False' and auth[f'{guildid}']['role2'] == 'False':
                        auth[f'{guildid}']['emoji2'] = emoji
                        auth[f'{guildid}']['role2'] = role

                        with open("./local/react.json", 'w') as f:
                            json.dump(auth, f, indent=4)

                        await msg.edit(embed=embed)
                        await msg.add_reaction(emoji)

                    elif auth[f'{guildid}']['emoji3'] == 'False' and auth[f'{guildid}']['role3'] == 'False':
                        auth[f'{guildid}']['emoji3'] = emoji
                        auth[f'{guildid}']['role3'] = role

                        with open("./local/react.json", 'w') as f:
                            json.dump(auth, f, indent=4)

                        await msg.edit(embed=embed)
                        await msg.add_reaction(emoji)

                    elif auth[f'{guildid}']['emoji4'] == 'False' and auth[f'{guildid}']['role4'] == 'False':
                        auth[f'{guildid}']['emoji4'] = emoji
                        auth[f'{guildid}']['role4'] = role

                        with open("./local/react.json", 'w') as f:
                            json.dump(auth, f, indent=4)

                        await msg.edit(embed=embed)
                        await msg.add_reaction(emoji)

                    elif auth[f'{guildid}']['emoji5'] == 'False' and auth[f'{guildid}']['role5'] == 'False':
                        auth[f'{guildid}']['emoji5'] = emoji
                        auth[f'{guildid}']['role5'] = role

                        with open("./local/react.json", 'w') as f:
                            json.dump(auth, f, indent=4)

                        await msg.edit(embed=embed)
                        await msg.add_reaction(emoji)

                    elif auth[f'{guildid}']['emoji6'] == 'False' and auth[f'{guildid}']['role6'] == 'False':
                        auth[f'{guildid}']['emoji6'] = emoji
                        auth[f'{guildid}']['role6'] = role

                        with open("./local/react.json", 'w') as f:
                            json.dump(auth, f, indent=4)

                        await msg.edit(embed=embed)
                        await msg.add_reaction(emoji)

                    elif auth[f'{guildid}']['emoji7'] == 'False' and auth[f'{guildid}']['role7'] == 'False':
                        auth[f'{guildid}']['emoji7'] = emoji
                        auth[f'{guildid}']['role7'] = role

                        with open("./local/react.json", 'w') as f:
                            json.dump(auth, f, indent=4)

                        await msg.edit(embed=embed)
                        await msg.add_reaction(emoji)

                    elif auth[f'{guildid}']['emoji8'] == 'False' and auth[f'{guildid}']['role8'] == 'False':
                        auth[f'{guildid}']['emoji8'] = emoji
                        auth[f'{guildid}']['role8'] = role

                        with open("./local/react.json", 'w') as f:
                            json.dump(auth, f, indent=4)

                        await msg.edit(embed=embed)
                        await msg.add_reaction(emoji)

                    elif auth[f'{guildid}']['emoji9'] == 'False' and auth[f'{guildid}']['role9'] == 'False':
                        auth[f'{guildid}']['emoji9'] = emoji
                        auth[f'{guildid}']['role9'] = role

                        with open("./local/react.json", 'w') as f:
                            json.dump(auth, f, indent=4)

                        await msg.edit(embed=embed)
                        await msg.add_reaction(emoji)

                    elif auth[f'{guildid}']['emoji10'] == 'False' and auth[f'{guildid}']['role10'] == 'False':
                        auth[f'{guildid}']['emoji10'] = emoji
                        auth[f'{guildid}']['role10'] = role

                        with open("./local/react.json", 'w') as f:
                            json.dump(auth, f, indent=4)

                        await msg.edit(embed=embed)
                        await msg.add_reaction(emoji)

                    elif auth[f'{guildid}']['emoji11'] == 'False' and auth[f'{guildid}']['role11'] == 'False':
                        auth[f'{guildid}']['emoji11'] = emoji
                        auth[f'{guildid}']['role11'] = role

                        with open("./local/react.json", 'w') as f:
                            json.dump(auth, f, indent=4)

                        await msg.edit(embed=embed)
                        await msg.add_reaction(emoji)

                    elif auth[f'{guildid}']['emoji12'] == 'False' and auth[f'{guildid}']['role12'] == 'False':
                        auth[f'{guildid}']['emoji12'] = emoji
                        auth[f'{guildid}']['role12'] = role

                        with open("./local/react.json", 'w') as f:
                            json.dump(auth, f, indent=4)

                        await msg.edit(embed=embed)
                        await msg.add_reaction(emoji)

                    elif auth[f'{guildid}']['emoji13'] == 'False' and auth[f'{guildid}']['role13'] == 'False':
                        auth[f'{guildid}']['emoji13'] = emoji
                        auth[f'{guildid}']['role13'] = role

                        with open("./local/react.json", 'w') as f:
                            json.dump(auth, f, indent=4)

                        await msg.edit(embed=embed)
                        await msg.add_reaction(emoji)

                    elif auth[f'{guildid}']['emoji14'] == 'False' and auth[f'{guildid}']['role14'] == 'False':
                        auth[f'{guildid}']['emoji14'] = emoji
                        auth[f'{guildid}']['role14'] = role

                        with open("./local/react.json", 'w') as f:
                            json.dump(auth, f, indent=4)

                        await msg.edit(embed=embed)
                        await msg.add_reaction(emoji)

                    elif auth[f'{guildid}']['emoji15'] == 'False' and auth[f'{guildid}']['role15'] == 'False':
                        auth[f'{guildid}']['emoji15'] = emoji
                        auth[f'{guildid}']['role15'] = role

                        with open("./local/react.json", 'w') as f:
                            json.dump(auth, f, indent=4)

                        await msg.edit(embed=embed)
                        await msg.add_reaction(emoji)

                    elif auth[f'{guildid}']['emoji16'] == 'False' and auth[f'{guildid}']['role16'] == 'False':
                        auth[f'{guildid}']['emoji16'] = emoji
                        auth[f'{guildid}']['role16'] = role

                        with open("./local/react.json", 'w') as f:
                            json.dump(auth, f, indent=4)

                        await msg.edit(embed=embed)
                        await msg.add_reaction(emoji)

                    elif auth[f'{guildid}']['emoji17'] == 'False' and auth[f'{guildid}']['role17'] == 'False':
                        auth[f'{guildid}']['emoji17'] = emoji
                        auth[f'{guildid}']['role17'] = role

                        with open("./local/react.json", 'w') as f:
                            json.dump(auth, f, indent=4)

                        await msg.edit(embed=embed)
                        await msg.add_reaction(emoji)

                    elif auth[f'{guildid}']['emoji18'] == 'False' and auth[f'{guildid}']['role18'] == 'False':
                        auth[f'{guildid}']['emoji18'] = emoji
                        auth[f'{guildid}']['role18'] = role

                        with open("./local/react.json", 'w') as f:
                            json.dump(auth, f, indent=4)

                        await msg.edit(embed=embed)
                        await msg.add_reaction(emoji)

                    elif auth[f'{guildid}']['emoji19'] == 'False' and auth[f'{guildid}']['role19'] == 'False':
                        auth[f'{guildid}']['emoji19'] = emoji
                        auth[f'{guildid}']['role19'] = role

                        with open("./local/react.json", 'w') as f:
                            json.dump(auth, f, indent=4)

                        await msg.edit(embed=embed)
                        await msg.add_reaction(emoji)

                    elif auth[f'{guildid}']['emoji20'] == 'False' and auth[f'{guildid}']['role20'] == 'False':
                        auth[f'{guildid}']['emoji20'] = emoji
                        auth[f'{guildid}']['role20'] = role

                        with open("./local/react.json", 'w') as f:
                            json.dump(auth, f, indent=4)

                        await msg.edit(embed=embed)
                        await msg.add_reaction(emoji)
                    
                    else:

                        embed2 = discord.Embed(
                            title = "Reaction Roles 👆🏻", 
                            description = "20 reaction roles is the maximum limit which you have achieved.",
                            timestamp= datetime.datetime.utcnow()
                        )

                        await ctx.send(embed=embed2)


            except Exception as e:
                print(e)
                embed = discord.Embed(title = "Failed with Error Code == 5.", description = "Oops. Something went wrong. 😬")
                embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)

        except Exception as e:
            print(e)
            embed = discord.Embed(title = "Failed with Error Code == 5.", description = "Oops. Something went wrong. 😬")
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)

    @reaction.command()
    @commands.has_permissions(administrator=True)
    async def rem(self, ctx):
        user = ctx.author.id
        guildid = ctx.guild.id

        with open("./local/react.json", 'r') as f:
            auth = json.load(f)

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        try:
            if f'{guildid}' in auth:
                del auth[f'{guildid}']

                with open("./local/react.json", 'w') as f:
                    json.dump(auth, f, indent=4)
                embed = discord.Embed(title = "Reaction Roles 👆🏻", description = f"*The reaction role message will no longer work. Create a new one using `{get_prefix}reaction create`*", timestamp=datetime.datetime.utcnow())
                embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)

            else:
                embed = discord.Embed(title = "Failed with Error Code == 4.", description = "Oops. This channel is not set as 'confession channel'. 😬")
                embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
        except:
            embed = discord.Embed(title = "Failed with Error Code == 5.", description = "Oops. Something went wrong. 😬")
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        with open("./local/react.json", 'r') as f:
            auth = json.load(f)
        guildid = payload.guild_id
        ourmessageid = auth[f'{guildid}']['message']
        emoji1 = auth[f'{guildid}']['emoji1']
        role1 = auth[f'{guildid}']['role1']
        emoji2 = auth[f'{guildid}']['emoji2']
        role2 = auth[f'{guildid}']['role2']
        emoji3 = auth[f'{guildid}']['emoji3']
        role3 = auth[f'{guildid}']['role3']
        emoji4 = auth[f'{guildid}']['emoji4']
        role4 = auth[f'{guildid}']['role4']
        emoji5 = auth[f'{guildid}']['emoji5']
        role5 = auth[f'{guildid}']['role5']
        emoji6 = auth[f'{guildid}']['emoji6']
        role6 = auth[f'{guildid}']['role6']
        emoji7 = auth[f'{guildid}']['emoji7']
        role7 = auth[f'{guildid}']['role7']
        emoji8 = auth[f'{guildid}']['emoji8']
        role8 = auth[f'{guildid}']['role8']
        emoji9 = auth[f'{guildid}']['emoji9']
        role9 = auth[f'{guildid}']['role9']
        emoji10 = auth[f'{guildid}']['emoji10']
        role10 = auth[f'{guildid}']['role10']
        emoji11 = auth[f'{guildid}']['emoji11']
        role11 = auth[f'{guildid}']['role11']
        emoji12 = auth[f'{guildid}']['emoji12']
        role12 = auth[f'{guildid}']['role12']
        emoji13 = auth[f'{guildid}']['emoji13']
        role13 = auth[f'{guildid}']['role13']
        emoji14 = auth[f'{guildid}']['emoji14']
        role14 = auth[f'{guildid}']['role14']
        emoji15= auth[f'{guildid}']['emoji15']
        role15 = auth[f'{guildid}']['role15']
        emoji16 = auth[f'{guildid}']['emoji16']
        role16 = auth[f'{guildid}']['role16']
        emoji17 = auth[f'{guildid}']['emoji17']
        role17 = auth[f'{guildid}']['role17']
        emoji18 = auth[f'{guildid}']['emoji18']
        role18 = auth[f'{guildid}']['role18']
        emoji19 = auth[f'{guildid}']['emoji19']
        role19 = auth[f'{guildid}']['role19']
        emoji20 = auth[f'{guildid}']['emoji20']
        role20 = auth[f'{guildid}']['role20']


        if ourmessageid == payload.message_id:
            member = payload.member
            guild = member.guild
            emoji = payload.emoji.name

            if emoji == f'{emoji1}':
                role = discord.utils.get(guild.roles, name = f'{role1}')
            elif emoji == f'{emoji2}':
                role = discord.utils.get(guild.roles, name = f'{role2}')
            elif emoji == f'{emoji3}':
                role = discord.utils.get(guild.roles, name = f'{role3}')
            elif emoji == f'{emoji4}':
                role = discord.utils.get(guild.roles, name = f'{role4}')
            elif emoji == f'{emoji5}':
                role = discord.utils.get(guild.roles, name = f'{role5}')
            elif emoji == f'{emoji6}':
                role = discord.utils.get(guild.roles, name = f'{role6}')
            elif emoji == f'{emoji7}':
                role = discord.utils.get(guild.roles, name = f'{role7}')
            elif emoji == f'{emoji8}':
                role = discord.utils.get(guild.roles, name = f'{role8}')
            elif emoji == f'{emoji9}':
                role = discord.utils.get(guild.roles, name = f'{role9}')
            elif emoji == f'{emoji10}':
                role = discord.utils.get(guild.roles, name = f'{role10}')
            elif emoji == f'{emoji11}':
                role = discord.utils.get(guild.roles, name = f'{role11}')
            elif emoji == f'{emoji12}':
                role = discord.utils.get(guild.roles, name = f'{role12}')
            elif emoji == f'{emoji13}':
                role = discord.utils.get(guild.roles, name = f'{role13}')
            elif emoji == f'{emoji14}':
                role = discord.utils.get(guild.roles, name = f'{role14}')
            elif emoji == f'{emoji15}':
                role = discord.utils.get(guild.roles, name = f'{role15}')
            elif emoji == f'{emoji16}':
                role = discord.utils.get(guild.roles, name = f'{role16}')
            elif emoji == f'{emoji17}':
                role = discord.utils.get(guild.roles, name = f'{role17}')
            elif emoji == f'{emoji18}':
                role = discord.utils.get(guild.roles, name = f'{role18}')
            elif emoji == f'{emoji19}':
                role = discord.utils.get(guild.roles, name = f'{role19}')
            elif emoji == f'{emoji20}':
                role = discord.utils.get(guild.roles, name = f'{role20}')
            
            if member != self.bot.user:
                await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        with open("./local/react.json", 'r') as f:
            auth = json.load(f)
        guildid = payload.guild_id
        ourmessageid = auth[f'{guildid}']['message']
        emoji1 = auth[f'{guildid}']['emoji1']
        role1 = auth[f'{guildid}']['role1']
        emoji2 = auth[f'{guildid}']['emoji2']
        role2 = auth[f'{guildid}']['role2']
        emoji3 = auth[f'{guildid}']['emoji3']
        role3 = auth[f'{guildid}']['role3']
        emoji4 = auth[f'{guildid}']['emoji4']
        role4 = auth[f'{guildid}']['role4']
        emoji5 = auth[f'{guildid}']['emoji5']
        role5 = auth[f'{guildid}']['role5']
        emoji6 = auth[f'{guildid}']['emoji6']
        role6 = auth[f'{guildid}']['role6']
        emoji7 = auth[f'{guildid}']['emoji7']
        role7 = auth[f'{guildid}']['role7']
        emoji8 = auth[f'{guildid}']['emoji8']
        role8 = auth[f'{guildid}']['role8']
        emoji9 = auth[f'{guildid}']['emoji9']
        role9 = auth[f'{guildid}']['role9']
        emoji10 = auth[f'{guildid}']['emoji10']
        role10 = auth[f'{guildid}']['role10']
        emoji11 = auth[f'{guildid}']['emoji11']
        role11 = auth[f'{guildid}']['role11']
        emoji12 = auth[f'{guildid}']['emoji12']
        role12 = auth[f'{guildid}']['role12']
        emoji13 = auth[f'{guildid}']['emoji13']
        role13 = auth[f'{guildid}']['role13']
        emoji14 = auth[f'{guildid}']['emoji14']
        role14 = auth[f'{guildid}']['role14']
        emoji15= auth[f'{guildid}']['emoji15']
        role15 = auth[f'{guildid}']['role15']
        emoji16 = auth[f'{guildid}']['emoji16']
        role16 = auth[f'{guildid}']['role16']
        emoji17 = auth[f'{guildid}']['emoji17']
        role17 = auth[f'{guildid}']['role17']
        emoji18 = auth[f'{guildid}']['emoji18']
        role18 = auth[f'{guildid}']['role18']
        emoji19 = auth[f'{guildid}']['emoji19']
        role19 = auth[f'{guildid}']['role19']
        emoji20 = auth[f'{guildid}']['emoji20']
        role20 = auth[f'{guildid}']['role20']

        if ourmessageid == payload.message_id:
            guild = await(self.bot.fetch_guild(payload.guild_id))
            emoji = payload.emoji.name

            if emoji == f'{emoji1}':
                role = discord.utils.get(guild.roles, name = f'{role1}')
            elif emoji == f'{emoji2}':
                role = discord.utils.get(guild.roles, name = f'{role2}')
            elif emoji == f'{emoji3}':
                role = discord.utils.get(guild.roles, name = f'{role3}')
            elif emoji == f'{emoji4}':
                role = discord.utils.get(guild.roles, name = f'{role4}')
            elif emoji == f'{emoji5}':
                role = discord.utils.get(guild.roles, name = f'{role5}')
            elif emoji == f'{emoji6}':
                role = discord.utils.get(guild.roles, name = f'{role6}')
            elif emoji == f'{emoji7}':
                role = discord.utils.get(guild.roles, name = f'{role7}')
            elif emoji == f'{emoji8}':
                role = discord.utils.get(guild.roles, name = f'{role8}')
            elif emoji == f'{emoji9}':
                role = discord.utils.get(guild.roles, name = f'{role9}')
            elif emoji == f'{emoji10}':
                role = discord.utils.get(guild.roles, name = f'{role10}')
            elif emoji == f'{emoji11}':
                role = discord.utils.get(guild.roles, name = f'{role11}')
            elif emoji == f'{emoji12}':
                role = discord.utils.get(guild.roles, name = f'{role12}')
            elif emoji == f'{emoji13}':
                role = discord.utils.get(guild.roles, name = f'{role13}')
            elif emoji == f'{emoji14}':
                role = discord.utils.get(guild.roles, name = f'{role14}')
            elif emoji == f'{emoji15}':
                role = discord.utils.get(guild.roles, name = f'{role15}')
            elif emoji == f'{emoji16}':
                role = discord.utils.get(guild.roles, name = f'{role16}')
            elif emoji == f'{emoji17}':
                role = discord.utils.get(guild.roles, name = f'{role17}')
            elif emoji == f'{emoji18}':
                role = discord.utils.get(guild.roles, name = f'{role18}')
            elif emoji == f'{emoji19}':
                role = discord.utils.get(guild.roles, name = f'{role19}')
            elif emoji == f'{emoji20}':
                role = discord.utils.get(guild.roles, name = f'{role20}')

            member = await(guild.fetch_member(payload.user_id))
            if member != self.bot.user:
                if member is not None:
                    await member.remove_roles(role)



def setup(bot):
    bot.add_cog(ReactionCog(bot))