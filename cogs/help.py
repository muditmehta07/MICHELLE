import discord
from discord.ext import commands
import random
import datetime
import json
import asyncio
from discord.ui import Select
from discord import SelectOption

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Help Command
    @commands.command()
    async def help(self, message):
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        tips = [
            f"Join the [Community Server](https://discord.gg/EfHrMURtnA) to get a **Giftbox**"
        ]
        protip = random.choice(tips)

        with open("./local/settings.json") as s:
            set = json.load(s)

        replyEmoji = self.bot.get_emoji(929383454469128263)

        if str(message.author.id) in set:
            if set[f"{message.author.id}"]["tips"] == True:
                compmsg = embed = discord.Embed(
                    description=f"**PROTIP** : {protip}\n\n"
                    f"**autorole**\n{replyEmoji}Setup an autorole\n"
                    f"**confess**\n{replyEmoji}Setup confessions\n"
                    f"**embed**\n{replyEmoji}Embed a message\n"
                    f"**goodbye**\n{replyEmoji}Setup goodbye messages\n"
                    f"**ping**\n{replyEmoji}Create custom replies\n"
                    f"**reaction**\n{replyEmoji}Setup reaction roles\n"
                    f"**welcome**\n{replyEmoji}Setup welcome messages",
                    color=color,
                    timestamp=datetime.datetime.utcnow(),
                )

                embed.set_author(
                    name="Michelle Help Commands", icon_url=self.bot.user.avatar
                )
                embed.set_footer(text=f"use  {get_prefix}  as the command prefix")
                compmsg = await message.channel.send_message(
                    embed=embed,
                    components=[
                        Select(
                            placeholder="Help Commands",
                            options=[
                                SelectOption(label="General", value="1", default=True),
                                SelectOption(label="Moderation", value="11"),
                                SelectOption(label="Level", value="2"),
                                SelectOption(label="Meme", value="3"),
                                SelectOption(label="Fun", value="4"),
                                SelectOption(label="Games", value="12"),
                                SelectOption(label="Emotes", value="5"),
                                SelectOption(label="Casual", value="6"),
                                SelectOption(label="Store", value="7"),
                                SelectOption(label="Theme", value="8"),
                                SelectOption(label="Info", value="9"),
                                SelectOption(label="Settings", value="10"),
                            ],
                            custom_id="StoreComponents",
                        )
                    ],
                )

            else:
                compmsg = embed = discord.Embed(
                    description=f"**autorole**\n{replyEmoji}Setup an autorole\n"
                    f"**confess**\n{replyEmoji}Setup confessions\n"
                    f"**embed**\n{replyEmoji}Embed a message\n"
                    f"**goodbye**\n{replyEmoji}Setup goodbye messages\n"
                    f"**ping**\n{replyEmoji}Create custom replies\n"
                    f"**reaction**\n{replyEmoji}Setup reaction roles\n"
                    f"**welcome**\n{replyEmoji}Setup welcome messages",
                    color=color,
                    timestamp=datetime.datetime.utcnow(),
                )

                embed.set_author(
                    name="Michelle Help Commands", icon_url=self.bot.user.avatar.url
                )
                embed.set_footer(text=f"use  {get_prefix}  as the command prefix")
                compmsg = await message.channel.send(
                    embed=embed,
                    components=[
                        Select(
                            placeholder="Help Commands",
                            options=[
                                SelectOption(label="General", value="1", default=True),
                                SelectOption(label="Moderation", value="11"),
                                SelectOption(label="Level", value="2"),
                                SelectOption(label="Meme", value="3"),
                                SelectOption(label="Fun", value="4"),
                                SelectOption(label="Games", value="12"),
                                SelectOption(label="Emotes", value="5"),
                                SelectOption(label="Casual", value="6"),
                                SelectOption(label="Store", value="7"),
                                SelectOption(label="Theme", value="8"),
                                SelectOption(label="Info", value="9"),
                                SelectOption(label="Settings", value="10"),
                            ],
                            custom_id="StoreComponents",
                        )
                    ],
                )

        else:
            compmsg = embed = discord.Embed(
                description=f"**PROTIP** : {protip}\n\n"
                f"**autorole**\n{replyEmoji}Setup an autorole\n"
                f"**confess**\n{replyEmoji}Setup confessions\n"
                f"**embed**\n{replyEmoji}Embed a message\n"
                f"**goodbye**\n{replyEmoji}Setup goodbye messages\n"
                f"**ping**\n{replyEmoji}Create custom replies\n"
                f"**reaction**\n{replyEmoji}Setup reaction roles\n"
                f"**welcome**\n{replyEmoji}Setup welcome messages",
                color=color,
                timestamp=datetime.datetime.utcnow(),
            )

            embed.set_author(
                name="Michelle Help Commands", icon_url=self.bot.user.avatar_url
            )
            embed.set_footer(text=f"use  {get_prefix}  as the command prefix")
            compmsg = await message.channel.send(
                embed=embed,
                components=[
                    discord.ui.Select(
                        placeholder="Help Commands",
                        options=[
                            SelectOption(label="General", value="1", default=True),
                            SelectOption(label="Moderation", value="11"),
                            SelectOption(label="Level", value="2"),
                            SelectOption(label="Meme", value="3"),
                            SelectOption(label="Fun", value="4"),
                            SelectOption(label="Games", value="12"),
                            SelectOption(label="Emotes", value="5"),
                            SelectOption(label="Casual", value="6"),
                            SelectOption(label="Store", value="7"),
                            SelectOption(label="Theme", value="8"),
                            SelectOption(label="Info", value="9"),
                            SelectOption(label="Settings", value="10"),
                        ],
                        custom_id="StoreComponents",
                    )
                ],
            )

        while True:
            try:
                interaction = await self.bot.wait_for(
                    "select_option",
                    check=lambda inter: inter.custom_id == "StoreComponents",
                    timeout=40,
                )
                res = interaction.values[0]

                if interaction.user != message.author:
                    await interaction.send("This is not for you!")

                elif res == "1" and interaction.user == message.author:
                    if str(message.author.id) in set:
                        if set[f"{message.author.id}"]["tips"] == True:
                            embed = discord.Embed(
                                description=f"**PROTIP** : {protip}\n\n"
                                f"**autorole**\n{replyEmoji}Setup an autorole\n"
                                f"**confess**\n{replyEmoji}Setup confessions\n"
                                f"**embed**\n{replyEmoji}Embed a message\n"
                                f"**goodbye**\n{replyEmoji}Setup goodbye messages\n"
                                f"**ping**\n{replyEmoji}Create custom replies\n"
                                f"**reaction**\n{replyEmoji}Setup reaction roles\n"
                                f"**welcome**\n{replyEmoji}Setup welcome messages",
                                color=color,
                                timestamp=datetime.datetime.utcnow(),
                            )

                            embed.set_author(
                                name="Michelle Help Commands",
                                icon_url=self.bot.user.avatar_url,
                            )
                            embed.set_footer(
                                text=f"use  {get_prefix}  as the command prefix"
                            )
                            await interaction.message.edit(
                                embed=embed,
                                components=[
                                    Select(
                                        placeholder="Help Commands",
                                        options=[
                                            SelectOption(
                                                label="General", value="1", default=True
                                            ),
                                            SelectOption(
                                                label="Moderation", value="11"
                                            ),
                                            SelectOption(label="Level", value="2"),
                                            SelectOption(label="Meme", value="3"),
                                            SelectOption(label="Fun", value="4"),
                                            SelectOption(label="Games", value="12"),
                                            SelectOption(label="Emotes", value="5"),
                                            SelectOption(label="Casual", value="6"),
                                            SelectOption(label="Store", value="7"),
                                            SelectOption(label="Theme", value="8"),
                                            SelectOption(label="Info", value="9"),
                                            SelectOption(label="Settings", value="10"),
                                        ],
                                        custom_id="StoreComponents",
                                    )
                                ],
                            )

                            try:
                                await interaction.respond()
                            except:
                                pass

                        else:
                            embed = discord.Embed(
                                description=f"**autorole**\n{replyEmoji}Setup an autorole\n"
                                f"**confess**\n{replyEmoji}Setup confessions\n"
                                f"**embed**\n{replyEmoji}Embed a message\n"
                                f"**goodbye**\n{replyEmoji}Setup goodbye messages\n"
                                f"**ping**\n{replyEmoji}Create custom replies\n"
                                f"**reaction**\n{replyEmoji}Setup reaction roles\n"
                                f"**welcome**\n{replyEmoji}Setup welcome messages",
                                color=color,
                                timestamp=datetime.datetime.utcnow(),
                            )

                            embed.set_author(
                                name="Michelle Help Commands",
                                icon_url=self.bot.user.avatar_url,
                            )
                            embed.set_footer(
                                text=f"use  {get_prefix}  as the command prefix"
                            )
                            await interaction.message.edit(
                                embed=embed,
                                components=[
                                    Select(
                                        placeholder="Help Commands",
                                        options=[
                                            SelectOption(
                                                label="General", value="1", default=True
                                            ),
                                            SelectOption(
                                                label="Moderation", value="11"
                                            ),
                                            SelectOption(label="Level", value="2"),
                                            SelectOption(label="Meme", value="3"),
                                            SelectOption(label="Fun", value="4"),
                                            SelectOption(label="Games", value="12"),
                                            SelectOption(label="Emotes", value="5"),
                                            SelectOption(label="Casual", value="6"),
                                            SelectOption(label="Store", value="7"),
                                            SelectOption(label="Theme", value="8"),
                                            SelectOption(label="Info", value="9"),
                                            SelectOption(label="Settings", value="10"),
                                        ],
                                        custom_id="StoreComponents",
                                    )
                                ],
                            )

                            try:
                                await interaction.respond()
                            except:
                                pass

                    else:
                        embed = discord.Embed(
                            description=f"**PROTIP** : {protip}\n\n"
                            f"**autorole**\n{replyEmoji}Setup an autorole\n"
                            f"**confess**\n{replyEmoji}Setup confessions\n"
                            f"**embed**\n{replyEmoji}Embed a message\n"
                            f"**goodbye**\n{replyEmoji}Setup goodbye messages\n"
                            f"**ping**\n{replyEmoji}Create custom replies\n"
                            f"**reaction**\n{replyEmoji}Setup reaction roles\n"
                            f"**welcome**\n{replyEmoji}Setup welcome messages",
                            color=color,
                            timestamp=datetime.datetime.utcnow(),
                        )

                        embed.set_author(
                            name="Michelle Help Commands",
                            icon_url=self.bot.user.avatar_url,
                        )
                        embed.set_footer(
                            text=f"use  {get_prefix}  as the command prefix"
                        )
                        await interaction.message.edit(
                            embed=embed,
                            components=[
                                Select(
                                    placeholder="Help Commands",
                                    options=[
                                        SelectOption(
                                            label="General", value="1", default=True
                                        ),
                                        SelectOption(label="Moderation", value="11"),
                                        SelectOption(label="Level", value="2"),
                                        SelectOption(label="Meme", value="3"),
                                        SelectOption(label="Fun", value="4"),
                                        SelectOption(label="Games", value="12"),
                                        SelectOption(label="Emotes", value="5"),
                                        SelectOption(label="Casual", value="6"),
                                        SelectOption(label="Store", value="7"),
                                        SelectOption(label="Theme", value="8"),
                                        SelectOption(label="Info", value="9"),
                                        SelectOption(label="Settings", value="10"),
                                    ],
                                    custom_id="StoreComponents",
                                )
                            ],
                        )

                        try:
                            await interaction.respond()
                        except:
                            pass

                elif res == "11" and interaction.user == message.author:
                    embed = discord.Embed(
                        description=f"**kick**\n{replyEmoji}Kick the mentioned user\n"
                        f"**ban**\n{replyEmoji}Ban the mentioned user\n"
                        f"**massban**\n{replyEmoji}Ban multiple users",
                        color=color,
                        timestamp=datetime.datetime.utcnow(),
                    )

                    with open("./local/beta.json", "r") as f:
                        beta_users = json.load(f)

                    if str(message.author.id) in beta_users:
                        embed.add_field(
                            name=f"**warn** `Beta`",
                            value=f"{replyEmoji}Warn a user",
                            inline=False,
                        )

                    embed.set_author(
                        name="Michelle Help Commands", icon_url=self.bot.user.avatar_url
                    )
                    embed.set_footer(text=f"use  {get_prefix}  as the command prefix")
                    await interaction.message.edit(
                        embed=embed,
                        components=[
                            Select(
                                placeholder="Help Commands",
                                options=[
                                    SelectOption(label="General", value="1"),
                                    SelectOption(
                                        label="Moderation", value="11", default=True
                                    ),
                                    SelectOption(label="Level", value="2"),
                                    SelectOption(label="Meme", value="3"),
                                    SelectOption(label="Fun", value="4"),
                                    SelectOption(label="Games", value="12"),
                                    SelectOption(label="Emotes", value="5"),
                                    SelectOption(label="Casual", value="6"),
                                    SelectOption(label="Store", value="7"),
                                    SelectOption(label="Theme", value="8"),
                                    SelectOption(label="Info", value="9"),
                                    SelectOption(label="Settings", value="10"),
                                ],
                                custom_id="StoreComponents",
                            )
                        ],
                    )

                    try:
                        await interaction.respond()
                    except:
                        pass

                elif res == "2" and interaction.user == message.author:
                    if str(message.author.id) in set:
                        if set[f"{message.author.id}"]["tips"] == True:
                            embed = discord.Embed(
                                description=f"**PROTIP** : {protip}\n\n"
                                f"**beg**\n{replyEmoji}Beg for XP\n"
                                f"**daily**\n{replyEmoji}Get daily rewards\n"
                                f"**level**\n{replyEmoji}View your level\n"
                                f"**top**\n{replyEmoji}View the top 5 leaderboard\n"
                                f"**leaderboard**\n{replyEmoji}View the leaderboard",
                                color=color,
                                timestamp=datetime.datetime.utcnow(),
                            )
                            embed.set_author(
                                name="Michelle Help Commands",
                                icon_url=self.bot.user.avatar_url,
                            )
                            embed.set_footer(
                                text=f"use  {get_prefix}  as the command prefix"
                            )
                            await interaction.message.edit(
                                embed=embed,
                                components=[
                                    Select(
                                        placeholder="Help Commands",
                                        options=[
                                            SelectOption(label="General", value="1"),
                                            SelectOption(
                                                label="Moderation", value="11"
                                            ),
                                            SelectOption(
                                                label="Level", value="2", default=True
                                            ),
                                            SelectOption(label="Meme", value="3"),
                                            SelectOption(label="Fun", value="4"),
                                            SelectOption(label="Games", value="12"),
                                            SelectOption(label="Emotes", value="5"),
                                            SelectOption(label="Casual", value="6"),
                                            SelectOption(label="Store", value="7"),
                                            SelectOption(label="Theme", value="8"),
                                            SelectOption(label="Info", value="9"),
                                            SelectOption(label="Settings", value="10"),
                                        ],
                                        custom_id="StoreComponents",
                                    )
                                ],
                            )

                            try:
                                await interaction.respond()
                            except:
                                pass

                        else:
                            embed = discord.Embed(
                                description=f"**beg**\n{replyEmoji}Beg for XP\n"
                                f"**daily**\n{replyEmoji}Get daily rewards\n"
                                f"**level**\n{replyEmoji}View your level\n"
                                f"**top**\n{replyEmoji}View the top 5 leaderboard\n"
                                f"**leaderboard**\n{replyEmoji}View the leaderboard",
                                color=color,
                                timestamp=datetime.datetime.utcnow(),
                            )
                            embed.set_author(
                                name="Michelle Help Commands",
                                icon_url=self.bot.user.avatar_url,
                            )
                            embed.set_footer(
                                text=f"use  {get_prefix}  as the command prefix"
                            )
                            await interaction.message.edit(
                                embed=embed,
                                components=[
                                    Select(
                                        placeholder="Help Commands",
                                        options=[
                                            SelectOption(label="General", value="1"),
                                            SelectOption(
                                                label="Moderation", value="11"
                                            ),
                                            SelectOption(
                                                label="Level", value="2", default=True
                                            ),
                                            SelectOption(label="Meme", value="3"),
                                            SelectOption(label="Fun", value="4"),
                                            SelectOption(label="Games", value="12"),
                                            SelectOption(label="Emotes", value="5"),
                                            SelectOption(label="Casual", value="6"),
                                            SelectOption(label="Store", value="7"),
                                            SelectOption(label="Theme", value="8"),
                                            SelectOption(label="Info", value="9"),
                                            SelectOption(label="Settings", value="10"),
                                        ],
                                        custom_id="StoreComponents",
                                    )
                                ],
                            )

                            try:
                                await interaction.respond()
                            except:
                                pass

                    else:
                        embed = discord.Embed(
                            description=f"**PROTIP** : {protip}\n\n"
                            f"**beg**\n{replyEmoji}Beg for XP\n"
                            f"**daily**\n{replyEmoji}Get daily rewards\n"
                            f"**level**\n{replyEmoji}View your level\n"
                            f"**top**\n{replyEmoji}View the top 5 leaderboard\n"
                            f"**leaderboard**\n{replyEmoji}View the leaderboard",
                            color=color,
                            timestamp=datetime.datetime.utcnow(),
                        )
                        embed.set_author(
                            name="Michelle Help Commands",
                            icon_url=self.bot.user.avatar_url,
                        )
                        embed.set_footer(
                            text=f"use  {get_prefix}  as the command prefix"
                        )
                        await interaction.message.edit(
                            embed=embed,
                            components=[
                                Select(
                                    placeholder="Help Commands",
                                    options=[
                                        SelectOption(label="General", value="1"),
                                        SelectOption(label="Moderation", value="11"),
                                        SelectOption(
                                            label="Level", value="2", default=True
                                        ),
                                        SelectOption(label="Meme", value="3"),
                                        SelectOption(label="Fun", value="4"),
                                        SelectOption(label="Games", value="12"),
                                        SelectOption(label="Emotes", value="5"),
                                        SelectOption(label="Casual", value="6"),
                                        SelectOption(label="Store", value="7"),
                                        SelectOption(label="Theme", value="8"),
                                        SelectOption(label="Info", value="9"),
                                        SelectOption(label="Settings", value="10"),
                                    ],
                                    custom_id="StoreComponents",
                                )
                            ],
                        )

                        try:
                            await interaction.respond()
                        except:
                            pass

                elif res == "3" and interaction.user == message.author:
                    embed = discord.Embed(
                        description=f"**aww**\n{replyEmoji}Wholesome posts\n"
                        f"**dadjokes**\n{replyEmoji}Sends a dad joke\n"
                        f"**doggo**\n{replyEmoji}Dog images\n"
                        f"**kitty**\n{replyEmoji}Cat images\n"
                        f"**meme**\n{replyEmoji}Entertain yourself with memes\n"
                        f"**showerthoughts**\n{replyEmoji}Sends a random shower thought\n",
                        color=color,
                        timestamp=datetime.datetime.utcnow(),
                    )
                    embed.set_author(
                        name="Michelle Help Commands", icon_url=self.bot.user.avatar_url
                    )
                    embed.set_footer(text=f"use  {get_prefix}  as the command prefix")
                    await interaction.message.edit(
                        embed=embed,
                        components=[
                            Select(
                                placeholder="Help Commands",
                                options=[
                                    SelectOption(label="General", value="1"),
                                    SelectOption(label="Moderation", value="11"),
                                    SelectOption(label="Level", value="2"),
                                    SelectOption(label="Meme", value="3", default=True),
                                    SelectOption(label="Fun", value="4"),
                                    SelectOption(label="Games", value="12"),
                                    SelectOption(label="Emotes", value="5"),
                                    SelectOption(label="Casual", value="6"),
                                    SelectOption(label="Store", value="7"),
                                    SelectOption(label="Theme", value="8"),
                                    SelectOption(label="Info", value="9"),
                                    SelectOption(label="Settings", value="10"),
                                ],
                                custom_id="StoreComponents",
                            )
                        ],
                    )

                    try:
                        await interaction.respond()
                    except:
                        pass

                elif res == "4" and interaction.user == message.author:
                    if str(message.author.id) in set:
                        if set[f"{message.author.id}"]["tips"] == True:
                            embed = discord.Embed(
                                description=f"**PROTIP** : {protip}\n\n"
                                f"**dice**\n{replyEmoji}Roll a dice\n"
                                f"**dumbrate**\n{replyEmoji}Check how dumb you are\n"
                                f"**emojify**\n{replyEmoji}Emojify text\n"
                                f"**flip**\n{replyEmoji}Flip a coin\n"
                                f"**hack**\n{replyEmoji}Hack a user\n"
                                f"**roast**\n{replyEmoji}Sick of a user? Insult them\n"
                                f"**simprate**\n{replyEmoji}Check how simp you are\n",
                                color=color,
                                timestamp=datetime.datetime.utcnow(),
                            )
                            embed.set_author(
                                name="Michelle Help Commands",
                                icon_url=self.bot.user.avatar_url,
                            )
                            embed.set_footer(
                                text=f"use  {get_prefix}  as the command prefix"
                            )
                            await interaction.message.edit(
                                embed=embed,
                                components=[
                                    Select(
                                        placeholder="Help Commands",
                                        options=[
                                            SelectOption(label="General", value="1"),
                                            SelectOption(
                                                label="Moderation", value="11"
                                            ),
                                            SelectOption(label="Level", value="2"),
                                            SelectOption(label="Meme", value="3"),
                                            SelectOption(
                                                label="Fun", value="4", default=True
                                            ),
                                            SelectOption(label="Games", value="12"),
                                            SelectOption(label="Emotes", value="5"),
                                            SelectOption(label="Casual", value="6"),
                                            SelectOption(label="Store", value="7"),
                                            SelectOption(label="Theme", value="8"),
                                            SelectOption(label="Info", value="9"),
                                            SelectOption(label="Settings", value="10"),
                                        ],
                                        custom_id="StoreComponents",
                                    )
                                ],
                            )

                            try:
                                await interaction.respond()
                            except:
                                pass

                        else:
                            embed = discord.Embed(
                                description=f"**dice**\n{replyEmoji}Roll a dice\n"
                                f"**dumbrate**\n{replyEmoji}Check how dumb you are\n"
                                f"**emojify**\n{replyEmoji}Emojify text\n"
                                f"**flip**\n{replyEmoji}Flip a coin\n"
                                f"**hack**\n{replyEmoji}Hack a user\n"
                                f"**roast**\n{replyEmoji}Sick of a user? Insult them\n"
                                f"**simprate**\n{replyEmoji}Check how simp you are\n",
                                color=color,
                                timestamp=datetime.datetime.utcnow(),
                            )
                            embed.set_author(
                                name="Michelle Help Commands",
                                icon_url=self.bot.user.avatar_url,
                            )
                            embed.set_footer(
                                text=f"use  {get_prefix}  as the command prefix"
                            )
                            await interaction.message.edit(
                                embed=embed,
                                components=[
                                    Select(
                                        placeholder="Help Commands",
                                        options=[
                                            SelectOption(label="General", value="1"),
                                            SelectOption(
                                                label="Moderation", value="11"
                                            ),
                                            SelectOption(label="Level", value="2"),
                                            SelectOption(label="Meme", value="3"),
                                            SelectOption(
                                                label="Fun", value="4", default=True
                                            ),
                                            SelectOption(label="Games", value="12"),
                                            SelectOption(label="Emotes", value="5"),
                                            SelectOption(label="Casual", value="6"),
                                            SelectOption(label="Store", value="7"),
                                            SelectOption(label="Theme", value="8"),
                                            SelectOption(label="Info", value="9"),
                                            SelectOption(label="Settings", value="10"),
                                        ],
                                        custom_id="StoreComponents",
                                    )
                                ],
                            )

                            try:
                                await interaction.respond()
                            except:
                                pass

                    else:
                        embed = discord.Embed(
                            description=f"**PROTIP** : {protip}\n\n"
                            f"**dice**\n{replyEmoji}Roll a dice\n"
                            f"**dumbrate**\n{replyEmoji}Check how dumb you are\n"
                            f"**emojify**\n{replyEmoji}Emojify text\n"
                            f"**flip**\n{replyEmoji}Flip a coin\n"
                            f"**hack**\n{replyEmoji}Hack a user\n"
                            f"**roast**\n{replyEmoji}Sick of a user? Insult them\n"
                            f"**simprate**\n{replyEmoji}Check how simp you are\n",
                            color=color,
                            timestamp=datetime.datetime.utcnow(),
                        )
                        embed.set_author(
                            name="Michelle Help Commands",
                            icon_url=self.bot.user.avatar_url,
                        )
                        embed.set_footer(
                            text=f"use  {get_prefix}  as the command prefix"
                        )
                        await interaction.message.edit(
                            embed=embed,
                            components=[
                                Select(
                                    placeholder="Help Commands",
                                    options=[
                                        SelectOption(label="General", value="1"),
                                        SelectOption(label="Moderation", value="11"),
                                        SelectOption(label="Level", value="2"),
                                        SelectOption(label="Meme", value="3"),
                                        SelectOption(
                                            label="Fun", value="4", default=True
                                        ),
                                        SelectOption(label="Games", value="12"),
                                        SelectOption(label="Emotes", value="5"),
                                        SelectOption(label="Casual", value="6"),
                                        SelectOption(label="Store", value="7"),
                                        SelectOption(label="Theme", value="8"),
                                        SelectOption(label="Info", value="9"),
                                        SelectOption(label="Settings", value="10"),
                                    ],
                                    custom_id="StoreComponents",
                                )
                            ],
                        )

                        try:
                            await interaction.respond()
                        except:
                            pass

                elif res == "12" and interaction.user == message.author:
                    embed = discord.Embed(
                        description=f"**8ball**\n{replyEmoji}Ask the 8-Ball anything you want\n"
                        f"**help counting**\n{replyEmoji}More info on counting\n"
                        f"**guess**\n{replyEmoji}Guess the Pokemon\n",
                        color=color,
                        timestamp=datetime.datetime.utcnow(),
                    )
                    embed.set_author(
                        name="Michelle Help Commands", icon_url=self.bot.user.avatar_url
                    )
                    embed.set_footer(text=f"use  {get_prefix}  as the command prefix")
                    await interaction.message.edit(
                        embed=embed,
                        components=[
                            Select(
                                placeholder="Help Commands",
                                options=[
                                    SelectOption(label="General", value="1"),
                                    SelectOption(label="Moderation", value="11"),
                                    SelectOption(label="Level", value="2"),
                                    SelectOption(label="Meme", value="3"),
                                    SelectOption(label="Fun", value="4"),
                                    SelectOption(
                                        label="Games", value="12", default=True
                                    ),
                                    SelectOption(label="Emotes", value="5"),
                                    SelectOption(label="Casual", value="6"),
                                    SelectOption(label="Store", value="7"),
                                    SelectOption(label="Theme", value="8"),
                                    SelectOption(label="Info", value="9"),
                                    SelectOption(label="Settings", value="10"),
                                ],
                                custom_id="StoreComponents",
                            )
                        ],
                    )

                    try:
                        await interaction.respond()
                    except:
                        pass

                elif res == "7" and interaction.user == message.author:
                    embed = discord.Embed(
                        description=f"**inventory**\n{replyEmoji}Open your Inventory\n"
                        f"**giftbox**\n{replyEmoji}Claim your Gift Box\n"
                        f"**chest**\n{replyEmoji}Store XP in a chest\n"
                        f"**buy**\n{replyEmoji}Buy an item\n"
                        f"**sell**\n{replyEmoji}Sell an item\n",
                        color=color,
                        timestamp=datetime.datetime.utcnow(),
                    )
                    embed.set_author(
                        name="Michelle Help Commands", icon_url=self.bot.user.avatar_url
                    )
                    embed.set_footer(text=f"use  {get_prefix}  as the command prefix")
                    await interaction.message.edit(
                        embed=embed,
                        components=[
                            Select(
                                placeholder="Help Commands",
                                options=[
                                    SelectOption(label="General", value="1"),
                                    SelectOption(label="Moderation", value="11"),
                                    SelectOption(label="Level", value="2"),
                                    SelectOption(label="Meme", value="3"),
                                    SelectOption(label="Fun", value="4"),
                                    SelectOption(label="Games", value="12"),
                                    SelectOption(label="Emotes", value="5"),
                                    SelectOption(label="Casual", value="6"),
                                    SelectOption(
                                        label="Store", value="7", default=True
                                    ),
                                    SelectOption(label="Theme", value="8"),
                                    SelectOption(label="Info", value="9"),
                                    SelectOption(label="Settings", value="10"),
                                ],
                                custom_id="StoreComponents",
                            )
                        ],
                    )

                    try:
                        await interaction.respond()
                    except:
                        pass

                elif res == "5" and interaction.user == message.author:
                    if str(message.author.id) in set:
                        if set[f"{message.author.id}"]["tips"] == True:
                            embed = discord.Embed(
                                description=f"**PROTIP** : {protip}\n\n"
                                f"**highfive**\n{replyEmoji}Request the highest of fives\n"
                                f"**hug**\n{replyEmoji}Hug your friends when they need it\n"
                                f"**kiss**\n{replyEmoji}Kiss your friends (only when necessary)\n"
                                f"**pat**\n{replyEmoji}Comfort your loved ones\n"
                                f"**punch**\n{replyEmoji}Punch someone when you're irritated\n"
                                f"**slap**\n{replyEmoji}Sick of a person? Slap them without violating any laws\n",
                                color=color,
                                timestamp=datetime.datetime.utcnow(),
                            )
                            embed.set_author(
                                name="Michelle Help Commands",
                                icon_url=self.bot.user.avatar_url,
                            )
                            embed.set_footer(
                                text=f"use  {get_prefix}  as the command prefix"
                            )
                            await interaction.message.edit(
                                embed=embed,
                                components=[
                                    Select(
                                        placeholder="Help Commands",
                                        options=[
                                            SelectOption(label="General", value="1"),
                                            SelectOption(
                                                label="Moderation", value="11"
                                            ),
                                            SelectOption(label="Level", value="2"),
                                            SelectOption(label="Meme", value="3"),
                                            SelectOption(label="Fun", value="4"),
                                            SelectOption(label="Games", value="12"),
                                            SelectOption(
                                                label="Emotes", value="5", default=True
                                            ),
                                            SelectOption(label="Casual", value="6"),
                                            SelectOption(label="Store", value="7"),
                                            SelectOption(label="Theme", value="8"),
                                            SelectOption(label="Info", value="9"),
                                            SelectOption(label="Settings", value="10"),
                                        ],
                                        custom_id="StoreComponents",
                                    )
                                ],
                            )

                            try:
                                await interaction.respond()
                            except:
                                pass

                        else:
                            embed = discord.Embed(
                                description=f"**highfive**\n{replyEmoji}Request the highest of fives\n"
                                f"**hug**\n{replyEmoji}Hug your friends when they need it\n"
                                f"**kiss**\n{replyEmoji}Kiss your friends (only when necessary)\n"
                                f"**pat**\n{replyEmoji}Comfort your loved ones\n"
                                f"**punch**\n{replyEmoji}Punch someone when you're irritated\n"
                                f"**slap**\n{replyEmoji}Sick of a person? Slap them without violating any laws\n",
                                color=color,
                                timestamp=datetime.datetime.utcnow(),
                            )
                            embed.set_author(
                                name="Michelle Help Commands",
                                icon_url=self.bot.user.avatar_url,
                            )
                            embed.set_footer(
                                text=f"use  {get_prefix}  as the command prefix"
                            )
                            await interaction.message.edit(
                                embed=embed,
                                components=[
                                    Select(
                                        placeholder="Help Commands",
                                        options=[
                                            SelectOption(label="General", value="1"),
                                            SelectOption(
                                                label="Moderation", value="11"
                                            ),
                                            SelectOption(label="Level", value="2"),
                                            SelectOption(label="Meme", value="3"),
                                            SelectOption(label="Fun", value="4"),
                                            SelectOption(label="Games", value="12"),
                                            SelectOption(
                                                label="Emotes", value="5", default=True
                                            ),
                                            SelectOption(label="Casual", value="6"),
                                            SelectOption(label="Store", value="7"),
                                            SelectOption(label="Theme", value="8"),
                                            SelectOption(label="Info", value="9"),
                                            SelectOption(label="Settings", value="10"),
                                        ],
                                        custom_id="StoreComponents",
                                    )
                                ],
                            )

                            try:
                                await interaction.respond()
                            except:
                                pass
                    else:
                        embed = discord.Embed(
                            description=f"**PROTIP** : {protip}\n\n"
                            f"**highfive**\n{replyEmoji}Request the highest of fives\n"
                            f"**hug**\n{replyEmoji}Hug your friends when they need it\n"
                            f"**kiss**\n{replyEmoji}Kiss your friends (only when necessary)\n"
                            f"**pat**\n{replyEmoji}Comfort your loved ones\n"
                            f"**punch**\n{replyEmoji}Punch someone when you're irritated\n"
                            f"**slap**\n{replyEmoji}Sick of a person? Slap them without violating any laws\n",
                            color=color,
                            timestamp=datetime.datetime.utcnow(),
                        )
                        embed.set_author(
                            name="Michelle Help Commands",
                            icon_url=self.bot.user.avatar_url,
                        )
                        embed.set_footer(
                            text=f"use  {get_prefix}  as the command prefix"
                        )
                        await interaction.message.edit(
                            embed=embed,
                            components=[
                                Select(
                                    placeholder="Help Commands",
                                    options=[
                                        SelectOption(label="General", value="1"),
                                        SelectOption(label="Moderation", value="11"),
                                        SelectOption(label="Level", value="2"),
                                        SelectOption(label="Meme", value="3"),
                                        SelectOption(label="Fun", value="4"),
                                        SelectOption(label="Games", value="12"),
                                        SelectOption(
                                            label="Emotes", value="5", default=True
                                        ),
                                        SelectOption(label="Casual", value="6"),
                                        SelectOption(label="Store", value="7"),
                                        SelectOption(label="Theme", value="8"),
                                        SelectOption(label="Info", value="9"),
                                        SelectOption(label="Settings", value="10"),
                                    ],
                                    custom_id="StoreComponents",
                                )
                            ],
                        )

                        try:
                            await interaction.respond()
                        except:
                            pass

                elif res == "6" and interaction.user == message.author:
                    embed = discord.Embed(
                        description=f"**lang**\n{replyEmoji}List of language codes\n"
                        f"**detect**\n{replyEmoji}Detect the given text's language\n"
                        f"**translate**\n{replyEmoji}Translate text to any language\n"
                        f"**wiki?**\n{replyEmoji}Search on wikipedia\n"
                        f"**wiki**\n{replyEmoji}Get wikipedia results\n"
                        f"**reddit**\n{replyEmoji}Get a post from a specific subreddit\n"
                        f"**youtube**\n{replyEmoji}Search a youtube video\n",
                        color=color,
                        timestamp=datetime.datetime.utcnow(),
                    )

                    embed.set_author(
                        name="Michelle Help Commands", icon_url=self.bot.user.avatar_url
                    )
                    embed.set_footer(text=f"use  {get_prefix}  as the command prefix")
                    await interaction.message.edit(
                        embed=embed,
                        components=[
                            Select(
                                placeholder="Help Commands",
                                options=[
                                    SelectOption(label="General", value="1"),
                                    SelectOption(label="Moderation", value="11"),
                                    SelectOption(label="Level", value="2"),
                                    SelectOption(label="Meme", value="3"),
                                    SelectOption(label="Fun", value="4"),
                                    SelectOption(label="Games", value="12"),
                                    SelectOption(label="Emotes", value="5"),
                                    SelectOption(
                                        label="Casual", value="6", default=True
                                    ),
                                    SelectOption(label="Store", value="7"),
                                    SelectOption(label="Theme", value="8"),
                                    SelectOption(label="Info", value="9"),
                                    SelectOption(label="Settings", value="10"),
                                ],
                                custom_id="StoreComponents",
                            )
                        ],
                    )

                    try:
                        await interaction.respond()
                    except:
                        pass

                elif res == "8" and interaction.user == message.author:
                    embed = discord.Embed(
                        description=f"**grey**\n{replyEmoji}Change theme to the color : `grey`\n"
                        f"**red**\n{replyEmoji}Change theme to the color : `red`\n"
                        f"**blue**\n{replyEmoji}Change theme to the color : `blue`\n"
                        f"**green**\n{replyEmoji}Change theme to the color : `green`\n"
                        f"**yellow**\n{replyEmoji}Change theme to the color : `yellow`\n"
                        f"**pink**\n{replyEmoji}Change theme to the color : `pink`\n"
                        f"**orange**\n{replyEmoji}Change theme to the color : `orange`\n"
                        f"**purple**\n{replyEmoji}Change theme to the color : `purple`\n"
                        f"**cyan**\n{replyEmoji}Change theme to the color : `cyan`\n",
                        color=color,
                        timestamp=datetime.datetime.utcnow(),
                    )
                    embed.set_author(
                        name="Michelle Help Commands", icon_url=self.bot.user.avatar_url
                    )
                    embed.set_footer(text=f"use  {get_prefix}  as the command prefix")
                    await interaction.message.edit(
                        embed=embed,
                        components=[
                            Select(
                                placeholder="Help Commands",
                                options=[
                                    SelectOption(label="General", value="1"),
                                    SelectOption(label="Moderation", value="11"),
                                    SelectOption(label="Level", value="2"),
                                    SelectOption(label="Meme", value="3"),
                                    SelectOption(label="Fun", value="4"),
                                    SelectOption(label="Games", value="12"),
                                    SelectOption(label="Emotes", value="5"),
                                    SelectOption(label="Casual", value="6"),
                                    SelectOption(label="Store", value="7"),
                                    SelectOption(
                                        label="Theme", value="8", default=True
                                    ),
                                    SelectOption(label="Info", value="9"),
                                    SelectOption(label="Settings", value="10"),
                                ],
                                custom_id="StoreComponents",
                            )
                        ],
                    )

                    try:
                        await interaction.respond()
                    except:
                        pass

                elif res == "9" and interaction.user == message.author:
                    embed = discord.Embed(
                        description=f"**feedback**\n{replyEmoji}Tell us what you think about Michelle\n"
                        f"**invite**\n{replyEmoji}Invite Michelle to other servers\n"
                        f"**message**\n{replyEmoji}View the latest message from our Developers\n"
                        f"**michelle**\n{replyEmoji}About Michelle\n"
                        f"**prefix**\n{replyEmoji}Change server prefix\n"
                        f"**profile**\n{replyEmoji}View your profile\n"
                        f"**server**\n{replyEmoji}View current server's profile\n"
                        f"**vote**\n{replyEmoji}Vote Michelle and support us\n",
                        color=color,
                        timestamp=datetime.datetime.utcnow(),
                    )
                    embed.set_author(
                        name="Michelle Help Commands", icon_url=self.bot.user.avatar_url
                    )
                    embed.set_footer(text=f"use  {get_prefix}  as the command prefix")
                    await interaction.message.edit(
                        embed=embed,
                        components=[
                            Select(
                                placeholder="Help Commands",
                                options=[
                                    SelectOption(label="General", value="1"),
                                    SelectOption(label="Moderation", value="11"),
                                    SelectOption(label="Level", value="2"),
                                    SelectOption(label="Meme", value="3"),
                                    SelectOption(label="Fun", value="4"),
                                    SelectOption(label="Games", value="12"),
                                    SelectOption(label="Emotes", value="5"),
                                    SelectOption(label="Casual", value="6"),
                                    SelectOption(label="Store", value="7"),
                                    SelectOption(label="Theme", value="8"),
                                    SelectOption(label="Info", value="9", default=True),
                                    SelectOption(label="Settings", value="10"),
                                ],
                                custom_id="StoreComponents",
                            )
                        ],
                    )

                    try:
                        await interaction.respond()
                    except:
                        pass

                elif res == "10" and interaction.user == message.author:
                    cross = self.bot.get_emoji(880679527200735273)
                    check = self.bot.get_emoji(880679486205620234)
                    branch = self.bot.get_emoji(942824887666491426)

                    embed = discord.Embed(
                        color=color, timestamp=datetime.datetime.utcnow()
                    )

                    with open("./local/settings.json", "r") as f:
                        set = json.load(f)

                    if str(message.author.id) in set:
                        personal = set[f"{message.author.id}"]["personal_ping"]
                        if personal == True:
                            personal = f"{check}"
                        else:
                            personal = f"{cross}"

                        server = set[f"{message.author.id}"]["server_ping"]
                        if server == True:
                            server = f"{check}"
                        else:
                            server = f"{cross}"

                        tips = set[f"{message.author.id}"]["tips"]
                        if tips == True:
                            tips = f"{check}"
                        else:
                            tips = f"{cross}"

                        lvlup = set[f"{message.author.id}"]["level_ups"]
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

                    if str(message.author.id) in set2:
                        beta = set2[f"{message.author.id}"]
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
                    embed.set_author(
                        name="Michelle Help Commands", icon_url=self.bot.user.avatar_url
                    )
                    embed.set_footer(text=f"use  {get_prefix}  as the command prefix")

                    await interaction.message.edit(
                        embed=embed,
                        components=[
                            Select(
                                placeholder="Help Commands",
                                options=[
                                    SelectOption(label="General", value="1"),
                                    SelectOption(label="Moderation", value="11"),
                                    SelectOption(label="Level", value="2"),
                                    SelectOption(label="Meme", value="3"),
                                    SelectOption(label="Fun", value="4"),
                                    SelectOption(label="Games", value="12"),
                                    SelectOption(label="Emotes", value="5"),
                                    SelectOption(label="Casual", value="6"),
                                    SelectOption(label="Store", value="7"),
                                    SelectOption(label="Theme", value="8"),
                                    SelectOption(label="Info", value="9"),
                                    SelectOption(
                                        label="Settings", value="10", default=True
                                    ),
                                ],
                                custom_id="StoreComponents",
                            )
                        ],
                    )

                    try:
                        await interaction.respond()
                    except:
                        pass

                else:
                    await interaction.send("This is not for you")

            except asyncio.TimeoutError:
                await compmsg.edit(
                    components=[
                        Select(
                            placeholder="Help Commands",
                            options=[
                                SelectOption(label="General", value="1"),
                                SelectOption(label="Moderation", value="11"),
                                SelectOption(label="Level", value="2"),
                                SelectOption(label="Meme", value="3"),
                                SelectOption(label="Fun", value="4"),
                                SelectOption(label="Games", value="12"),
                                SelectOption(label="Emotes", value="5"),
                                SelectOption(label="Casual", value="6"),
                                SelectOption(label="Store", value="7"),
                                SelectOption(label="Theme", value="8"),
                                SelectOption(label="Info", value="9"),
                                SelectOption(label="Settings", value="10"),
                            ],
                            custom_id="StoreComponents",
                            disabled=True,
                        )
                    ]
                )

                break

    # Welcome
    @help.command()
    async def welcome(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(
            description=f"**Permissions** : `Administrator`\n\n__**Usage**__\n**{get_prefix}welcome <optional-message>**\n> This command sets the channel as `welcome-channel`. If the `optional-message` field is left blank, a default message will be added.\n\n**{get_prefix}delwelcome**\n> This command deletes the `welcome-message` and will not send them again.\n\n**Note:** Use **{get_prefix}welcome <new_message>** to set a new `welcome-message`.",
            color=color,
            timestamp=datetime.datetime.utcnow(),
        )

        embed.set_author(name="Welcome Help ❓", icon_url=self.bot.user.avatar_url)
        await message.channel.send(embed=embed)

    # Confession

    @help.command()
    async def confess(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(
            description=f"**Permissions** : `Administrator`\n\n__**Usage**__\n**{get_prefix}confess**\n> This command sets the channel as `confession-channel`.\n\n**{get_prefix}delconfess**\n> This command removes the `confession-channel` and will not send confessions again.\n\n**{get_prefix}hi**> This command will send a DM providing info about sending a `confession-message`.",
            timestamp=datetime.datetime.utcnow(),
        )

        embed.set_author(name="Confession Help ❓", icon_url=self.bot.user.avatar_url)
        await message.channel.send(embed=embed)

    # Developer

    @commands.command()
    async def dev(self, message):
        await message.channel.trigger_typing()
        id = message.author.id

        if id == 488996680058798081:
            guildid = message.channel.guild.id
            guildid = "./guild data/" + str(guildid) + ".json"
            with open(guildid, "r") as f:
                users = json.load(f)

            color = users[str(id)]["color"]

            with open("./local/prefix.json", "r") as f:
                L = json.load(f)

            if str(message.guild.id) in L:
                get_prefix = L[str(message.guild.id)]["prefix"]
            elif str(message.guild.id) not in L:
                get_prefix = "="

            embed = discord.Embed(
                description=f"**Auth Users** : `{get_prefix}authlist`\n**Authorise/Deauthorise** : `{get_prefix}authorise <user>` `{get_prefix}deauthorise <user>`\n**Send and Update Report** : `{get_prefix}sendreport` `{get_prefix}updatereport`\n**Send and Update Auth** : `{get_prefix}sendauth` `{get_prefix}updateauth`\n**Send and Update Confess** : `{get_prefix}sendconfess` `{get_prefix}updateconfess`\n**Send and Update Welcome** : `{get_prefix}sendwelcome` `{get_prefix}updatewelcome`\n**Send and Update Prefix** : `{get_prefix}sendprefix` `{get_prefix}updateprefix`\n**Send and Update React** : `{get_prefix}sendreact` `{get_prefix}updatereact`\n**Send and Update Roast** : `{get_prefix}sendroast` `{get_prefix}updateroast`\n**Send and Update Guild** : `{get_prefix}sendguild` `{get_prefix}updateguild`\n**Send and Update P Ping** : `{get_prefix}sendping` `{get_prefix}updateping`\n**Send and Update S Pings** : `{get_prefix}sendpings` `{get_prefix}updatepings`\n**Send and Update Pings** : `{get_prefix}sendstatus` `{get_prefix}updatestatus`\n**Send and Update Invite** : `{get_prefix}sendinvite` `{get_prefix}updateinvite`\n**Send and Update Items** : `{get_prefix}senditems` `{get_prefix}updateitems`",
                color=color,
                timestamp=datetime.datetime.utcnow(),
            )

            embed.set_author(
                name=f"Developer",
                icon_url="https://cdn.discordapp.com/emojis/880689362721972224.png?v=1",
            )

            await message.channel.send(embed=embed)

    # Status

    @commands.command()
    async def status(self, message):
        await message.channel.trigger_typing()
        id = message.author.id

        with open("./local/auth.json", "r") as f:
            auth = json.load(f)

        if str(id) in auth:
            if auth[f"{id}"]["auth"] == True:
                guildid = message.channel.guild.id
                guildid = "./guild data/" + str(guildid) + ".json"
                with open(guildid, "r") as f:
                    users = json.load(f)

                color = users[str(id)]["color"]

                with open("./local/prefix.json", "r") as f:
                    L = json.load(f)

                if str(message.guild.id) in L:
                    get_prefix = L[str(message.guild.id)]["prefix"]
                elif str(message.guild.id) not in L:
                    get_prefix = "="

                embed = discord.Embed(
                    description=f"**Listening** : `{get_prefix}listening`\n**Playing** : `{get_prefix}playing`\n**Watching** : `{get_prefix}watching`\n**Default** : `{get_prefix}default`",
                    color=color,
                    timestamp=datetime.datetime.utcnow(),
                )

                embed.set_author(
                    name=f"Status",
                    icon_url="https://cdn.discordapp.com/emojis/880689107276296223.png?v=1",
                )

                await message.channel.send(embed=embed)

    # Auth

    @commands.command()
    async def auth(self, message):
        await message.channel.trigger_typing()
        id = message.author.id

        with open("./local/auth.json", "r") as f:
            auth = json.load(f)

        if str(id) in auth:
            if auth[f"{id}"]["auth"] == True:
                guildid = message.channel.guild.id
                guildid = "./guild data/" + str(guildid) + ".json"
                with open(guildid, "r") as f:
                    users = json.load(f)

                color = users[str(id)]["color"]

                with open("./local/prefix.json", "r") as f:
                    L = json.load(f)

                if str(message.guild.id) in L:
                    get_prefix = L[str(message.guild.id)]["prefix"]
                elif str(message.guild.id) not in L:
                    get_prefix = "="

                embed = discord.Embed(
                    description=f"**SetXP** : `{get_prefix}setxp <user> <xp>`",
                    color=color,
                    timestamp=datetime.datetime.utcnow(),
                )

                embed.set_author(
                    name=f"Auth",
                    icon_url="https://cdn.discordapp.com/emojis/880689269000241212.png?v=1",
                )

                await message.channel.send(embed=embed)

    # Meme

    @help.command()
    async def meme(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(
            description=f"**Description** : Sends a meme of the desired category using Reddit's API. If category is not specified, it uses `meme` subreddit\n\n**Usage** : `{get_prefix}meme <optional category>`\n**Example** : `{get_prefix}meme marvel` to get a Marvel Meme",
            color=color,
            timestamp=datetime.datetime.utcnow(),
        )

        embed.set_author(
            name="Meme Help ❓",
            icon_url="https://cdn.discordapp.com/emojis/880689402567884821.png?v=1",
        )
        await message.channel.send(embed=embed)

    # Roast

    @help.command()
    async def roast(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(
            description=f"**Description** : Roasts the mentioned user\n\n**Usage** : `{get_prefix}roast <user mention>`\n**Example** : `{get_prefix}roast @user` to roast a user",
            color=color,
            timestamp=datetime.datetime.utcnow(),
        )

        embed.set_author(
            name="Roast Help ❓",
            icon_url="https://cdn.discordapp.com/emojis/880689402567884821.png?v=1",
        )
        await message.channel.send(embed=embed)

    # Kill

    @help.command()
    async def kill(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(
            description=f"**Description** : Kills the mentioned user. Killing a user drops their XP and raises yours. You may also fail to kill them which would drop your XP and raise their's\n\n**Usage** : `{get_prefix}kill <user mention>`\n**Example** : `{get_prefix}kill @user` to kill a user",
            color=color,
            timestamp=datetime.datetime.utcnow(),
        )

        embed.set_author(
            name="Kill Help ❓",
            icon_url="https://cdn.discordapp.com/emojis/880689402567884821.png?v=1",
        )
        await message.channel.send(embed=embed)

    # Counting
    @help.command(aliases=["count"])
    async def counting(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(
            description=f"__**Setup**__\n• Go to a channel that you want to set as the counting channel.\n• Use command `{get_prefix}counting` (Administrator Only) to set it as the counting channel.\n• Use command `{get_prefix}delcounting` (Administrator Only) to delete the counting channel.\n\n"
            f"__**How To Play**__\n• Once you have setup a counting channel. Type **1** to start counting.\n• You must have a partner that can now send **2**.\n• Continue the count and try not to break it by sending the wrong number.\n\n"
            f"__**Rules**__\n• You cannot count two numbers in a row.\n• Bots are not allowed to count. (Don't bother making one)\n\n"
            f"__**Rewards**__\n• Everytime you count, you are awarded with XP.\n• The higher the count, the higher the XP.\n• Breaking the count drops your XP depending upon how high the count was.",
            color=color,
            timestamp=datetime.datetime.utcnow(),
        )

        embed.set_author(name="Counting", icon_url=self.bot.user.avatar_url)
        await message.channel.send(embed=embed)

    # Hug
    @help.command()
    async def hug(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        theme = users[str(id)]["color"]
        if theme == 9807270:  # gray
            url = "https://cdn.discordapp.com/emojis/909410043580010516.png?v=1"

        elif theme == 15158332 or theme == 10038562:  # red
            url = "https://cdn.discordapp.com/emojis/909411552044662804.png?v=1"

        elif theme == 3447003 or theme == 2123412:  # blue
            url = "https://cdn.discordapp.com/emojis/880689143359868999.png?v=1"

        elif theme == 3066993 or theme == 2067276:  # green
            url = "https://cdn.discordapp.com/emojis/909410754522906685.png?v=1"

        elif theme == 10181046 or theme == 7419530:  # purple
            url = "https://cdn.discordapp.com/emojis/909411520314769460.png?v=1"

        elif theme == 15844367 or theme == 12745742:  # gold
            url = "https://cdn.discordapp.com/emojis/909411582163968061.png?v=1"

        elif theme == 1752220 or theme == 1146986:  # teal
            url = "https://cdn.discordapp.com/emojis/909410348531068938.png?v=1"

        elif theme == 15105570 or theme == 11027200:  # orange
            url = "https://cdn.discordapp.com/emojis/909411487389450291.png?v=1"

        elif theme == 15277667 or theme == 11342935:  # magenta
            url = "https://cdn.discordapp.com/emojis/909410987394883614.png?v=1"

        else:  # gray
            url = "https://cdn.discordapp.com/emojis/909410043580010516.png?v=1"

        embed = discord.Embed(
            description=f"**Description** : Hugs the mentioned user by sending a GIF\n\n**Usage** : `{get_prefix}hug <user mention>`\n**Example** : `{get_prefix}hug @user` to hug a user",
            color=color,
            timestamp=datetime.datetime.utcnow(),
        )

        embed.set_author(name="Hug Help ❓", icon_url=url)
        await message.channel.send(embed=embed)

    # Kiss

    @help.command()
    async def kiss(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        theme = users[str(id)]["color"]
        if theme == 9807270:  # gray
            url = "https://cdn.discordapp.com/emojis/909410043580010516.png?v=1"

        elif theme == 15158332 or theme == 10038562:  # red
            url = "https://cdn.discordapp.com/emojis/909411552044662804.png?v=1"

        elif theme == 3447003 or theme == 2123412:  # blue
            url = "https://cdn.discordapp.com/emojis/880689143359868999.png?v=1"

        elif theme == 3066993 or theme == 2067276:  # green
            url = "https://cdn.discordapp.com/emojis/909410754522906685.png?v=1"

        elif theme == 10181046 or theme == 7419530:  # purple
            url = "https://cdn.discordapp.com/emojis/909411520314769460.png?v=1"

        elif theme == 15844367 or theme == 12745742:  # gold
            url = "https://cdn.discordapp.com/emojis/909411582163968061.png?v=1"

        elif theme == 1752220 or theme == 1146986:  # teal
            url = "https://cdn.discordapp.com/emojis/909410348531068938.png?v=1"

        elif theme == 15105570 or theme == 11027200:  # orange
            url = "https://cdn.discordapp.com/emojis/909411487389450291.png?v=1"

        elif theme == 15277667 or theme == 11342935:  # magenta
            url = "https://cdn.discordapp.com/emojis/909410987394883614.png?v=1"

        else:  # gray
            url = "https://cdn.discordapp.com/emojis/909410043580010516.png?v=1"

        embed = discord.Embed(
            description=f"**Description** : Kisses the mentioned user by sending a GIF\n\n**Usage** : `{get_prefix}kiss <user mention>`\n**Example** : `{get_prefix}kiss @user` to kiss a user",
            color=color,
            timestamp=datetime.datetime.utcnow(),
        )

        embed.set_author(name="Kiss Help ❓", icon_url=url)
        await message.channel.send(embed=embed)

    # Slap

    @help.command()
    async def slap(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        theme = users[str(id)]["color"]
        if theme == 9807270:  # gray
            url = "https://cdn.discordapp.com/emojis/909410043580010516.png?v=1"

        elif theme == 15158332 or theme == 10038562:  # red
            url = "https://cdn.discordapp.com/emojis/909411552044662804.png?v=1"

        elif theme == 3447003 or theme == 2123412:  # blue
            url = "https://cdn.discordapp.com/emojis/880689143359868999.png?v=1"

        elif theme == 3066993 or theme == 2067276:  # green
            url = "https://cdn.discordapp.com/emojis/909410754522906685.png?v=1"

        elif theme == 10181046 or theme == 7419530:  # purple
            url = "https://cdn.discordapp.com/emojis/909411520314769460.png?v=1"

        elif theme == 15844367 or theme == 12745742:  # gold
            url = "https://cdn.discordapp.com/emojis/909411582163968061.png?v=1"

        elif theme == 1752220 or theme == 1146986:  # teal
            url = "https://cdn.discordapp.com/emojis/909410348531068938.png?v=1"

        elif theme == 15105570 or theme == 11027200:  # orange
            url = "https://cdn.discordapp.com/emojis/909411487389450291.png?v=1"

        elif theme == 15277667 or theme == 11342935:  # magenta
            url = "https://cdn.discordapp.com/emojis/909410987394883614.png?v=1"

        else:  # gray
            url = "https://cdn.discordapp.com/emojis/909410043580010516.png?v=1"

        embed = discord.Embed(
            description=f"**Description** : Slaps the mentioned user by sending a GIF\n\n**Usage** : `{get_prefix}slap <user mention>`\n**Example** : `{get_prefix}slap @user` to slap a user",
            color=color,
            timestamp=datetime.datetime.utcnow(),
        )

        embed.set_author(name="Slap Help ❓", icon_url=url)
        await message.channel.send(embed=embed)

    # Level
    @help.command()
    async def level(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        theme = users[str(id)]["color"]
        if theme == 9807270:  # gray
            url = "https://cdn.discordapp.com/emojis/909410043458388019.png?v=1"

        elif theme == 15158332 or theme == 10038562:  # red
            url = "https://cdn.discordapp.com/emojis/909411551730090015.png?v=1"

        elif theme == 3447003 or theme == 2123412:  # blue
            url = "https://cdn.discordapp.com/emojis/880689068613189653.png?v=1"

        elif theme == 3066993 or theme == 2067276:  # green
            url = "https://cdn.discordapp.com/emojis/909410753965084673.png?v=1"

        elif theme == 10181046 or theme == 7419530:  # purple
            url = "https://cdn.discordapp.com/emojis/909411520264417281.png?v=1"

        elif theme == 15844367 or theme == 12745742:  # gold
            url = "https://cdn.discordapp.com/emojis/909411582365290516.png?v=1"

        elif theme == 1752220 or theme == 1146986:  # teal
            url = "https://cdn.discordapp.com/emojis/909410347885133835.png?v=1"

        elif theme == 15105570 or theme == 11027200:  # orange
            url = "https://cdn.discordapp.com/emojis/909411487624347648.png?v=1"

        elif theme == 15277667 or theme == 11342935:  # magenta
            url = "https://cdn.discordapp.com/emojis/909410987243868240.png?v=1"

        else:  # gray
            url = "https://cdn.discordapp.com/emojis/909410043458388019.png?v=1"

        embed = discord.Embed(
            description=f"**Description** : Returns the level of a user\n\n**Usage** : `{get_prefix}level` to get your Level Card\n**Example** : `{get_prefix}level @user` to get user's level",
            color=color,
            timestamp=datetime.datetime.utcnow(),
        )

        embed.set_author(name="Level Help ❓", icon_url=url)
        await message.channel.send(embed=embed)

    # Leader

    @help.command()
    async def leader(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        theme = users[str(id)]["color"]
        if theme == 9807270:  # gray
            url = "https://cdn.discordapp.com/emojis/909410043458388019.png?v=1"

        elif theme == 15158332 or theme == 10038562:  # red
            url = "https://cdn.discordapp.com/emojis/909411551730090015.png?v=1"

        elif theme == 3447003 or theme == 2123412:  # blue
            url = "https://cdn.discordapp.com/emojis/880689068613189653.png?v=1"

        elif theme == 3066993 or theme == 2067276:  # green
            url = "https://cdn.discordapp.com/emojis/909410753965084673.png?v=1"

        elif theme == 10181046 or theme == 7419530:  # purple
            url = "https://cdn.discordapp.com/emojis/909411520264417281.png?v=1"

        elif theme == 15844367 or theme == 12745742:  # gold
            url = "https://cdn.discordapp.com/emojis/909411582365290516.png?v=1"

        elif theme == 1752220 or theme == 1146986:  # teal
            url = "https://cdn.discordapp.com/emojis/909410347885133835.png?v=1"

        elif theme == 15105570 or theme == 11027200:  # orange
            url = "https://cdn.discordapp.com/emojis/909411487624347648.png?v=1"

        elif theme == 15277667 or theme == 11342935:  # magenta
            url = "https://cdn.discordapp.com/emojis/909410987243868240.png?v=1"

        else:  # gray
            url = "https://cdn.discordapp.com/emojis/909410043458388019.png?v=1"

        embed = discord.Embed(
            description=f"**Description** : Returns the leaderboard of a guild\n\n**Usage** : `{get_prefix}leader` to get Leaderboard",
            color=color,
            timestamp=datetime.datetime.utcnow(),
        )

        embed.set_author(name="Leaderboard Help ❓", icon_url=url)
        await message.channel.send(embed=embed)

    # Michelle
    @commands.command(
        aliases=["help michelle", "Michelle", "help Michelle", "MICHELLE"]
    )
    async def michelle(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        embed = discord.Embed(
            description=f"**Michelle is a multipurpose bot with a Leveling System, Fun and much more!**\n",
            color=color,
            timestamp=datetime.datetime.utcnow(),
        )

        embed.add_field(
            name="__Commands__",
            value="[Here is a list of all the commands](https://www.michelle-bot.co/commands.html)",
            inline=False,
        )

        embed.add_field(
            name="__Patch Notes__",
            value="[Here are the Patch Notes for Michelle](https://www.michelle-bot.co/patch.html)\n\n",
            inline=False,
        )

        embed.set_author(name="About Michelle", icon_url=self.bot.user.avatar_url)
        await message.channel.send(embed=embed)

    @help.command()
    async def giftbox(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        theme = users[str(id)]["color"]
        if theme == 9807270:  # gray
            url = "https://cdn.discordapp.com/emojis/909410043630333982.png?v=1"

        elif theme == 15158332 or theme == 10038562:  # red
            url = "https://cdn.discordapp.com/emojis/909411551906234378.png?v=1"

        elif theme == 3447003 or theme == 2123412:  # blue
            url = "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1"

        elif theme == 3066993 or theme == 2067276:  # green
            url = "https://cdn.discordapp.com/emojis/909410753960902718.png?v=1"

        elif theme == 10181046 or theme == 7419530:  # purple
            url = "https://cdn.discordapp.com/emojis/909411520373477406.png?v=1"

        elif theme == 15844367 or theme == 12745742:  # gold
            url = "https://cdn.discordapp.com/emojis/909411582465949746.png?v=1"

        elif theme == 1752220 or theme == 1146986:  # teal
            url = "https://cdn.discordapp.com/emojis/909410348480733244.png?v=1"

        elif theme == 15105570 or theme == 11027200:  # orange
            url = "https://cdn.discordapp.com/emojis/909411487632744509.png?v=1"

        elif theme == 15277667 or theme == 11342935:  # magenta
            url = "https://cdn.discordapp.com/emojis/909410987285827655.png?v=1"

        else:  # gray
            url = "https://cdn.discordapp.com/emojis/909410043630333982.png?v=1"

        embed = discord.Embed(
            description=f"A Gift Box is exactly what it sounds like, open it and recieve XP.\n\n__**Usage**__\n`{get_prefix}giftbox` - To open a gift box\n\n__**How to get it?**__\nJoin the [Michelle's Community](https://discord.gg/EfHrMURtnA) Server to recieve a gift box.",
            timestamp=datetime.datetime.utcnow(),
            color=color,
        )
        embed.set_author(name="Gift Box", icon_url=url)
        await message.channel.send(embed=embed)

    # Sage

    @help.command()
    async def sage(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        replyEmoji = self.bot.get_emoji(929383454469128263)
        branchEmoji = self.bot.get_emoji(942824887666491426)

        file = discord.File("./pictures/sage.png")

        embed = discord.Embed(
            description=f"> This peculiar spell makes the user invulnerable. A Sage user is immortal and hence, cannot be killed. They are also forbidden from killing anyone and can be hunted by **Hunter Spell** users.\n\n**Price** : `50,000 XP`\n**Buy** : `{get_prefix}buy sage`\n\n**Exclusive Command : `Gift`**\nDescription : `Gift your levels to other users.`\nUsage : `{get_prefix}gift <user> <level>`",
            timestamp=datetime.datetime.utcnow(),
            color=color,
        )
        embed.set_author(name="Sage Spell")
        embed.set_thumbnail(url="attachment://sage.png")
        await message.channel.send(file=file, embed=embed)

    # Hunter

    @help.command()
    async def hunter(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        file = discord.File("./pictures/hunter.png")
        embed = discord.Embed(
            description=f"> This spell is for the predators and risk-takers. A Hunter Spell user can hunt Sage Spell users to drop their Levels.\n\n**Price** : `20,000 XP`\n**Buy** : `{get_prefix}buy hunter`\n\n**Exclusive Commands**\n**1. Seek**\n> Get a list of Sage Spell users of the current server.\nUsage : `{get_prefix}seek`\n\n**2. Hunt**\n> When this command is used, the Hunter Spell user will lose 1 Level and the Sage Spell user on whom the command is being used, will lose 2 Levels.\nUsage : `{get_prefix}hunt <user>`",
            timestamp=datetime.datetime.utcnow(),
            color=color,
        )
        embed.set_thumbnail(url="attachment://hunter.png")
        embed.set_author(name="Hunter Spell")
        await message.channel.send(file=file, embed=embed)

    # Chameleon

    @help.command()
    async def chameleon(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        theme = users[str(id)]["color"]
        if theme == 9807270:  # gray
            url = "https://cdn.discordapp.com/emojis/909410043630333982.png?v=1"

        elif theme == 15158332 or theme == 10038562:  # red
            url = "https://cdn.discordapp.com/emojis/909411551906234378.png?v=1"

        elif theme == 3447003 or theme == 2123412:  # blue
            url = "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1"

        elif theme == 3066993 or theme == 2067276:  # green
            url = "https://cdn.discordapp.com/emojis/909410753960902718.png?v=1"

        elif theme == 10181046 or theme == 7419530:  # purple
            url = "https://cdn.discordapp.com/emojis/909411520373477406.png?v=1"

        elif theme == 15844367 or theme == 12745742:  # gold
            url = "https://cdn.discordapp.com/emojis/909411582465949746.png?v=1"

        elif theme == 1752220 or theme == 1146986:  # teal
            url = "https://cdn.discordapp.com/emojis/909410348480733244.png?v=1"

        elif theme == 15105570 or theme == 11027200:  # orange
            url = "https://cdn.discordapp.com/emojis/909411487632744509.png?v=1"

        elif theme == 15277667 or theme == 11342935:  # magenta
            url = "https://cdn.discordapp.com/emojis/909410987285827655.png?v=1"

        else:  # gray
            url = "https://cdn.discordapp.com/emojis/909410043630333982.png?v=1"

        file = discord.File("./pictures/chameleon.jpg")
        embed = discord.Embed(
            description=f"This Ninjutsu will hide your name from the Leaderboard\n**Price** : `10,000 XP`\n**Buy** : `{get_prefix}buy chameleon`",
            timestamp=datetime.datetime.utcnow(),
            color=color,
        )
        embed.set_thumbnail(url="attachment://chameleon.jpg")
        embed.set_author(name="Chameleon Jutsu", icon_url=url)
        await message.channel.send(file=file, embed=embed)

    # Transform

    @help.command(aliases=["transformation"])
    async def transform(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        theme = users[str(id)]["color"]
        if theme == 9807270:  # gray
            url = "https://cdn.discordapp.com/emojis/909410043630333982.png?v=1"

        elif theme == 15158332 or theme == 10038562:  # red
            url = "https://cdn.discordapp.com/emojis/909411551906234378.png?v=1"

        elif theme == 3447003 or theme == 2123412:  # blue
            url = "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1"

        elif theme == 3066993 or theme == 2067276:  # green
            url = "https://cdn.discordapp.com/emojis/909410753960902718.png?v=1"

        elif theme == 10181046 or theme == 7419530:  # purple
            url = "https://cdn.discordapp.com/emojis/909411520373477406.png?v=1"

        elif theme == 15844367 or theme == 12745742:  # gold
            url = "https://cdn.discordapp.com/emojis/909411582465949746.png?v=1"

        elif theme == 1752220 or theme == 1146986:  # teal
            url = "https://cdn.discordapp.com/emojis/909410348480733244.png?v=1"

        elif theme == 15105570 or theme == 11027200:  # orange
            url = "https://cdn.discordapp.com/emojis/909411487632744509.png?v=1"

        elif theme == 15277667 or theme == 11342935:  # magenta
            url = "https://cdn.discordapp.com/emojis/909410987285827655.png?v=1"

        else:  # gray
            url = "https://cdn.discordapp.com/emojis/909410043630333982.png?v=1"

        file = discord.File("./pictures/transformation.jpg")
        embed = discord.Embed(
            description=f"This Ninjutsu will disguise your name on the Leaderboard\n**Price** : `12,000 XP`\n**Buy** : `{get_prefix}buy transformation`\n\n__**Exclusive Command**__\n`{get_prefix}transform <name>` - Change your name on the leaderboard",
            timestamp=datetime.datetime.utcnow(),
            color=color,
        )
        embed.set_thumbnail(url="attachment://transformation.jpg")
        embed.set_author(name="Transformation Jutsu", icon_url=url)
        await message.channel.send(file=file, embed=embed)

    """
    @weapons.command()
    async def fictional(self, message):
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
        description=f"**Light Saber** : `{get_prefix}help lightsaber`\n\n**Riptide** : `{get_prefix}help riptide`\n\n**Elderwand** : `{get_prefix}help elderwand`\n\n**Death Note** : `{get_prefix}help deathnote`\n\n**Infinity Gauntlet** : `{get_prefix}help gauntlet`",
        color = color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name = "Fictional Weapons 📺", icon_url =  "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
        await message.channel.send(embed = embed)

    @weapons.command()
    async def godly(self, message):
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
        description=f"**Spear of Lugh** : `{get_prefix}help lugh`\n\n**Magical Katana** : `{get_prefix}help murasame`\n\n**King Arthur's Sword** : `{get_prefix}help excalibur`\n\n**Thor's Hammer** : `{get_prefix}help mjolnir`\n\n**Shiva's Trident** : `{get_prefix}help trishula`\n\n**Zeus' Bolt** : `{get_prefix}help astrape`",
        color = color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name = "Godly Weapons 😇", icon_url =  "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
        await message.channel.send(embed = embed)

    @weapons.command()
    async def legendary(self, message):
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
        description=f"🍌 **Banana** : `{get_prefix}help banana`\n\n🦶🏻 **Smelly Feet** : `{get_prefix}help feet`\n\n💉 **Cough Syrup** : `{get_prefix}help syrup`",
        color = color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name = "Legendary Weapons 👽", icon_url = "https://cdn.discordapp.com/emojis/880689176268374037.png?v=1")
        await message.channel.send(embed = embed)
    """

    @help.command()
    async def knife(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        file = discord.File("./pictures/weapon/knife.png")
        embed = discord.Embed(
            description=f"**A weapon to kill**\n\nXP Drop : `0.25% XP` • Cooldown : `30sec`\nPrice : `3,000 XP` • Buy : `{get_prefix}buy knife`\n\n**Usage** : `{get_prefix}kill knife @user`",
            timestamp=datetime.datetime.utcnow(),
            color=color,
        )
        embed.set_thumbnail(url="attachment://knife.png")
        embed.set_author(
            name="Knife",
            icon_url="https://cdn.discordapp.com/emojis/881474984193703999.png?v=1",
        )
        await message.channel.send(file=file, embed=embed)

    @help.command()
    async def machette(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        file = discord.File("./pictures/weapon/machette.png")
        embed = discord.Embed(
            description=f"**A weapon to kill**\n\nXP Drop : `0.5% XP` • Cooldown : `2min`\nPrice : `12,000 XP` • Buy : `{get_prefix}buy machette`\n\n**Usage** : `{get_prefix}kill machette @user`",
            timestamp=datetime.datetime.utcnow(),
            color=color,
        )
        embed.set_thumbnail(url="attachment://machette.png")
        embed.set_author(
            name="Machette",
            icon_url="https://cdn.discordapp.com/emojis/881478895503806464.png?v=1",
        )
        await message.channel.send(file=file, embed=embed)

    @help.command()
    async def dagger(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        file = discord.File("./pictures/weapon/dagger.png")
        embed = discord.Embed(
            description=f"**A weapon to kill**\n\nXP Drop : `0.75% XP` • Cooldown : `5min`\nPrice : `10,000 XP` • Buy : `{get_prefix}buy dagger`",
            timestamp=datetime.datetime.utcnow(),
            color=color,
        )
        embed.set_thumbnail(url="attachment://dagger.png")
        embed.set_author(
            name="Dagger",
            icon_url="https://cdn.discordapp.com/emojis/881478895835164682.png?v=1",
        )
        await message.channel.send(file=file, embed=embed)

    @help.command()
    async def sword(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        file = discord.File("./pictures/weapon/sword.png")
        embed = discord.Embed(
            description=f"**A weapon to kill**\n\nXP Drop : `1% XP` • Cooldown : `8min`\nPrice : `15,000 XP` • Buy : `{get_prefix}buy sword`",
            timestamp=datetime.datetime.utcnow(),
            color=color,
        )
        embed.set_thumbnail(url="attachment://sword.png")
        embed.set_author(
            name="Sword",
            icon_url="https://cdn.discordapp.com/emojis/881478895247949887.png?v=1",
        )
        await message.channel.send(file=file, embed=embed)

    @help.command()
    async def scythe(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        file = discord.File("./pictures/weapon/scythe.png")
        embed = discord.Embed(
            description=f"**A weapon to kill**\n\nXP Drop : `1.5% XP` • Cooldown : `15min`\nPrice : `17,000 XP` • Buy : `{get_prefix}buy scythe`",
            timestamp=datetime.datetime.utcnow(),
            color=color,
        )
        embed.set_thumbnail(url="attachment://scythe.png")
        embed.set_author(
            name="Scythe",
            icon_url="https://cdn.discordapp.com/emojis/881478895604494376.png?v=1",
        )
        await message.channel.send(file=file, embed=embed)

    @help.command()
    async def shuriken(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        file = discord.File("./pictures/weapon/shuriken.png")
        embed = discord.Embed(
            description=f"**A weapon to kill**\n\nXP Drop : `2% XP` • Cooldown : `30min`\nPrice : `23,000 XP` • Buy : `{get_prefix}buy shuriken`",
            timestamp=datetime.datetime.utcnow(),
            color=color,
        )
        embed.set_thumbnail(url="attachment://shuriken.png")
        embed.set_author(
            name="Shuriken",
            icon_url="https://cdn.discordapp.com/emojis/881478895889690674.png?v=1",
        )
        await message.channel.send(file=file, embed=embed)

    @help.command()
    async def chest(self, message):
        await message.channel.trigger_typing()
        id = message.author.id
        guildid = message.channel.guild.id
        guildid = "./guild data/" + str(guildid) + ".json"
        with open(guildid, "r") as f:
            users = json.load(f)

        color = users[str(id)]["color"]

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(message.guild.id) in L:
            get_prefix = L[str(message.guild.id)]["prefix"]
        elif str(message.guild.id) not in L:
            get_prefix = "="

        replyEmoji = self.bot.get_emoji(929383454469128263)

        embed = discord.Embed(
            description=f"> Chests are used to store and secure XP. When a user kills you, a percentage of your on-hand XP is deducted. Transfer your XP to a chest and keep it safe from killers. **Chest ID** can be viewed from your `Inventory` if you own a chest.\n\n"
            f"**View chest**\n{replyEmoji}`{get_prefix}chest <id>`\n"
            f"**Deposit XP to Chest**\n{replyEmoji}`{get_prefix}chest deposit`\n"
            f"**Withdraw XP from Chest**\n{replyEmoji}`{get_prefix}chest withdraw`\n"
            f"**Upgrade Chest**\n{replyEmoji}`{get_prefix}chest upgrade`\n",
            color=color,
            timestamp=datetime.datetime.utcnow(),
        )

        embed.set_author(name="Chest Help ❓")
        await message.channel.send(embed=embed)

    @help.command()
    async def common(self, message):
        if "chest" in message.message.content:
            await message.channel.trigger_typing()
            id = message.author.id
            guildid = message.channel.guild.id
            guildid = "./guild data/" + str(guildid) + ".json"
            with open(guildid, "r") as f:
                users = json.load(f)

            color = users[str(id)]["color"]

            chest_emoji = "https://cdn.discordapp.com/emojis/955783898577661973.webp?size=96&quality=lossless"

            embed = discord.Embed(
                description=f"**Description**: A regular chest made out of wood from the `Enchanted Forest`. It is said that the `Dark Queen` used to summon her `Minions` in that forest.\n\n**Capacity : 20,000 XP**",
                color=color,
                timestamp=datetime.datetime.utcnow(),
            )

            embed.set_author(name="Common Chest", icon_url=chest_emoji)
            embed.set_footer(text="Upgrade for more storage")

            await message.channel.send(embed=embed)

    @help.command()
    async def amazing(self, message):
        if "chest" in message.message.content:
            await message.channel.trigger_typing()
            id = message.author.id
            guildid = message.channel.guild.id
            guildid = "./guild data/" + str(guildid) + ".json"
            with open(guildid, "r") as f:
                users = json.load(f)

            color = users[str(id)]["color"]

            chest_emoji = "https://cdn.discordapp.com/emojis/955783898577661973.webp?size=96&quality=lossless"

            embed = discord.Embed(
                description=f"**Description**: A chest made out of silver obtained from the silver mines of `Underworld`. The mines were guarded by `Goblins`.\n\n**Capacity : 100,000 XP**",
                color=color,
                timestamp=datetime.datetime.utcnow(),
            )

            embed.set_author(name="Amazing Chest", icon_url=chest_emoji)
            embed.set_footer(text="Upgrade for more storage")

            await message.channel.send(embed=embed)

    @help.command()
    async def brilliant(self, message):
        if "chest" in message.message.content:
            await message.channel.trigger_typing()
            id = message.author.id
            guildid = message.channel.guild.id
            guildid = "./guild data/" + str(guildid) + ".json"
            with open(guildid, "r") as f:
                users = json.load(f)

            color = users[str(id)]["color"]

            chest_emoji = "https://cdn.discordapp.com/emojis/955783898577661973.webp?size=96&quality=lossless"

            embed = discord.Embed(
                description=f"**Description**: A chest made out of gold obtained from the gold mines of `Underworld`. The mines were heavily guarded by `Hobgoblins`.\n\n**Capacity : 175,000 XP**",
                color=color,
                timestamp=datetime.datetime.utcnow(),
            )

            embed.set_author(name="Brilliant Chest", icon_url=chest_emoji)
            embed.set_footer(text="Upgrade for more storage")

            await message.channel.send(embed=embed)

    @help.command()
    async def divine(self, message):
        if "chest" in message.message.content:
            await message.channel.trigger_typing()
            id = message.author.id
            guildid = message.channel.guild.id
            guildid = "./guild data/" + str(guildid) + ".json"
            with open(guildid, "r") as f:
                users = json.load(f)

            color = users[str(id)]["color"]

            chest_emoji = "https://cdn.discordapp.com/emojis/955783898577661973.webp?size=96&quality=lossless"

            embed = discord.Embed(
                description=f"**Description**: A chest made out of `Celestial Bronze` obtained from the bottom of `Mount Olympus`. `Golems` are often found there.\n\n**Capacity : 500,000 XP**",
                color=color,
                timestamp=datetime.datetime.utcnow(),
            )

            embed.set_author(name="Divine Chest", icon_url=chest_emoji)
            embed.set_footer(text="Upgrade for more storage")

            await message.channel.send(embed=embed)

    @help.command()
    async def exquisite(self, message):
        if "chest" in message.message.content:
            await message.channel.trigger_typing()
            id = message.author.id
            guildid = message.channel.guild.id
            guildid = "./guild data/" + str(guildid) + ".json"
            with open(guildid, "r") as f:
                users = json.load(f)

            color = users[str(id)]["color"]

            chest_emoji = "https://cdn.discordapp.com/emojis/955783898577661973.webp?size=96&quality=lossless"

            embed = discord.Embed(
                description=f"**Description**: A chest made out of `Terrestrial Obsidian` obtained from the depths of the `Underworld`. The `Obsidian` is protected by `Dracula`.\n\n**Capacity : 1,000,000 XP**",
                color=color,
                timestamp=datetime.datetime.utcnow(),
            )

            embed.set_author(name="Exquisite Chest", icon_url=chest_emoji)
            embed.set_footer(text="Upgrade for more storage")

            await message.channel.send(embed=embed)

    @help.command()
    async def legendary(self, message):
        if "chest" in message.message.content:
            await message.channel.trigger_typing()
            id = message.author.id
            guildid = message.channel.guild.id
            guildid = "./guild data/" + str(guildid) + ".json"
            with open(guildid, "r") as f:
                users = json.load(f)

            color = users[str(id)]["color"]

            chest_emoji = "https://cdn.discordapp.com/emojis/955783898577661973.webp?size=96&quality=lossless"

            embed = discord.Embed(
                description=f"**Description**: A chest made out of `Imperial Gold` obtained from the top of `Mount Olympus`. The material is extremely difficult to obtain as it is limited and guarded by the `Imperial Dragon`.\n\n**Capacity: Infinite**",
                color=color,
                timestamp=datetime.datetime.utcnow(),
            )

            embed.set_author(name="Legendary Chest", icon_url=chest_emoji)
            embed.set_footer(text="Upgrade for more storage")

            await message.channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(HelpCog(bot))
