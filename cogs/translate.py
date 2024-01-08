from datetime import date, datetime
import functools, string
import googletrans
from googletrans import Translator
import discord
import datetime
import json
import random
from discord.ext import commands
from discord_components import DiscordComponents, Button, Select, SelectOption, ComponentsBot
import asyncio

# Requires the mtranslate module be installed

class Translate(commands.Cog):
            
    def __init__(self, bot):
        self.bot = bot
        DiscordComponents(self.bot)
        self.translator = Translator()
        self.to_morse = { 
			"a" : ".-",
			"b" : "-...",
			"c" : "-.-.",
			"d" : "-..",
			"e" : ".",
			"f" : "..-.",
			"g" : "--.",
			"h" : "....",
			"i" : "..",
			"j" : ".---",
			"k" : "-.-",
			"l" : ".-..",
			"m" : "--",
			"n" : "-.",
			"o" : "---",
			"p" : ".--.",
			"q" : "--.-",
			"r" : ".-.",
			"s" : "...",
			"t" : "-",
			"u" : "..-",
			"v" : "...-",
			"w" : ".--",
			"x" : "-..-",
			"y" : "-.--",
			"z" : "--..",
			"1" : ".----",
			"2" : "..---",
			"3" : "...--",
			"4" : "....-",
			"5" : ".....",
			"6" : "-....",
			"7" : "--...",
			"8" : "---..",
			"9" : "----.",
			"0" : "-----"
			}

    @commands.command(pass_context=True)
    async def lang(self, ctx):
        id = ctx.author.id
        guildid = ctx.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        description = "Afrikaans : `af`   Albanian : `sq`   Amharic : `am`\nArabic : `ar`   Armenian : `hy`   Azerbaijani : `az`\nBasque : `eu`   Belarusian : `be`   Bengali : `bn`\nBosnian : `bs`   Bulgarian : `bg`   Catalan : `ca`\nCebuano : `ceb`   Chichewa : `ny`  Chinese (S) : `zh-cn`\nChinese (T) : `zh-tw`  Corsican : `co`   Croatian : `hr`"

        embed = discord.Embed(
            description=description,
            color=color,
            timestamp = datetime.datetime.utcnow())

        embed.set_author(name = ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="Page 1")

        compmsg = await ctx.send(embed = embed, components= [Select(
                    placeholder="Choose a Page",
                    options= [
                        SelectOption(label="Page 1", value="1", default=True),
                        SelectOption(label="Page 2", value="2"),
                        SelectOption(label="Page 3", value="3"),
                        SelectOption(label="Page 4", value="4"),
                        SelectOption(label="Page 5", value="5"),
                        SelectOption(label="Page 6", value="6")
                        ],
                        custom_id="PageComponents"
                )])

        while True:
            try:
                interaction = await self.bot.wait_for('select_option', check=lambda inter: inter.custom_id == "PageComponents", timeout=40)
                res = interaction.values[0]

                if interaction.user != ctx.author:
                    await interaction.send("This is not for you!")

                elif res == "1" and interaction.user == ctx.author:
                    description = "Afrikaans : `af`   Albanian : `sq`   Amharic : `am`\nArabic : `ar`   Armenian : `hy`   Azerbaijani : `az`\nBasque : `eu`   Belarusian : `be`   Bengali : `bn`\nBosnian : `bs`   Bulgarian : `bg`   Catalan : `ca`\nCebuano : `ceb`   Chichewa : `ny`  Chinese (S) : `zh-cn`\nChinese (T) : `zh-tw`  Corsican : `co`   Croatian : `hr`"

                    embed = discord.Embed(
                        description=description,
                        color=color,
                        timestamp = datetime.datetime.utcnow())

                    embed.set_author(name = ctx.author.name, icon_url=ctx.author.avatar_url)
                    embed.set_footer(text="Page 1")

                    await interaction.message.edit(embed = embed, components= [Select(
                                placeholder="Choose a Page",
                                options= [
                                    SelectOption(label="Page 1", value="1", default=True),
                                    SelectOption(label="Page 2", value="2"),
                                    SelectOption(label="Page 3", value="3"),
                                    SelectOption(label="Page 4", value="4"),
                                    SelectOption(label="Page 5", value="5"),
                                    SelectOption(label="Page 6", value="6")
                                    ],
                                    custom_id="PageComponents"
                            )])

                    try:
                        await interaction.respond()
                    except:
                        pass

                elif res == "2" and interaction.user == ctx.author:
                    description = "Czech : `cs`   Danish : `da`   Dutch : `nl`\nEnglish : `en`   Esperanto : `eo`   Estonian : `et`\nFilipino : `tl`   Finnish : `fi`   French : `fr`\nFrisian : `fy`   Galician : `gl`   Georgian : `ka`\nGerman : `de`   Greek : `el`   Gujarati : `gu`\nHaitian Creole : `ht`   Hausa : `ha`   Hawaiian : `haw`"

                    embed = discord.Embed(
                        description=description,
                        color=color,
                        timestamp = datetime.datetime.utcnow())

                    embed.set_author(name = ctx.author.name, icon_url=ctx.author.avatar_url)
                    embed.set_footer(text="Page 2")

                    await interaction.message.edit(embed = embed, components= [Select(
                                placeholder="Choose a Page",
                                options= [
                                    SelectOption(label="Page 1", value="1"),
                                    SelectOption(label="Page 2", value="2", default=True),
                                    SelectOption(label="Page 3", value="3"),
                                    SelectOption(label="Page 4", value="4"),
                                    SelectOption(label="Page 5", value="5"),
                                    SelectOption(label="Page 6", value="6")
                                    ],
                                    custom_id="PageComponents"
                            )])

                    try:
                        await interaction.respond()
                    except:
                        pass

                elif res == "3" and interaction.user == ctx.author:
                    description = "Hebrew : `he`   Hindi : `hi`   Hmong : `hmn`\nHungarian : `hu`   Icelandic : `is`   Igbo : `ig`\nIndonesian : `id`   Irish : `ga`   Italian : `it`\nJapanese : `ja`   Javanese : `jw`   Kannada : `kn`\nKazakh : `kk`   Khmer : `km`   Korean : `ko`\nKurdish : `ku`   Kyrgyz : `ky`   Lao : `lo`"

                    embed = discord.Embed(
                        description=description,
                        color=color,
                        timestamp = datetime.datetime.utcnow())

                    embed.set_author(name = ctx.author.name, icon_url=ctx.author.avatar_url)
                    embed.set_footer(text="Page 3")

                    await interaction.message.edit(embed = embed, components= [Select(
                                placeholder="Choose a Page",
                                options= [
                                    SelectOption(label="Page 1", value="1"),
                                    SelectOption(label="Page 2", value="2"),
                                    SelectOption(label="Page 3", value="3", default=True),
                                    SelectOption(label="Page 4", value="4"),
                                    SelectOption(label="Page 5", value="5"),
                                    SelectOption(label="Page 6", value="6")
                                    ],
                                    custom_id="PageComponents"
                            )])

                    try:
                        await interaction.respond()
                    except:
                        pass

                elif res == "4" and interaction.user == ctx.author:
                    description = "Latin : `la`   Latvian : `lv`   Lithuanian : `lt`\nLuxembourgish : `lb`   Macedonian : `mk`   Malagasy : `mg`\nMalay : `ms`   Malayalam : `ml`   Maltese : `mt`\nMaori : `mi`   Marathi : `mr`   Mongolian : `mn`\nMyanmar : `my` Nepali : `ne`   Norwegian : `no`\nOdia : `or`   Pashto : `ps`  Persian : `fa`"

                    embed = discord.Embed(
                        description=description,
                        color=color,
                        timestamp = datetime.datetime.utcnow())

                    embed.set_author(name = ctx.author.name, icon_url=ctx.author.avatar_url)
                    embed.set_footer(text="Page 4")

                    await interaction.message.edit(embed = embed, components= [Select(
                                placeholder="Choose a Page",
                                options= [
                                    SelectOption(label="Page 1", value="1"),
                                    SelectOption(label="Page 2", value="2"),
                                    SelectOption(label="Page 3", value="3"),
                                    SelectOption(label="Page 4", value="4", default=True),
                                    SelectOption(label="Page 5", value="5"),
                                    SelectOption(label="Page 6", value="6")
                                    ],
                                    custom_id="PageComponents"
                            )])

                    try:
                        await interaction.respond()
                    except:
                        pass

                elif res == "5" and interaction.user == ctx.author:
                    description = "Polish : `pl`   Portuguese : `pt`   Punjabi : `pa`\nRomanian : `ro`   Russian : `ru`   Samoan : `sm`\nScots Gaelic : `gd`   Serbian : `sr`   Sesotho : `st`\nShona : `sn`   Sindhi : `sd`   Sinhala : `si`\nSlovak : `sk`   Slovenian : `sl`   Somali : `so`\nSpanish : `es`   Sundanese : `su`   Swahili : `sw`"

                    embed = discord.Embed(
                        description=description,
                        color=color,
                        timestamp = datetime.datetime.utcnow())

                    embed.set_author(name = ctx.author.name, icon_url=ctx.author.avatar_url)
                    embed.set_footer(text="Page 5")

                    await interaction.message.edit(embed = embed, components= [Select(
                                placeholder="Choose a Page",
                                options= [
                                    SelectOption(label="Page 1", value="1"),
                                    SelectOption(label="Page 2", value="2"),
                                    SelectOption(label="Page 3", value="3"),
                                    SelectOption(label="Page 4", value="4"),
                                    SelectOption(label="Page 5", value="5", default=True),
                                    SelectOption(label="Page 6", value="6")
                                    ],
                                    custom_id="PageComponents"
                            )])

                    try:
                        await interaction.respond()
                    except:
                        pass

                elif res == "6" and interaction.user == ctx.author:
                    description = "Swedish : `sv`   Tajik : `tg`   Tamil : `ta`\nTelugu : `te`   Thai : `th`   Turkish : `tr`\nUkrainian : `uk`   Urdu : `ur`   Uyghur : `ug`\nUzbek : `uz`   Vietnamese : `vi`   Welsh : `cy`\nXhosa : `xh`   Yiddish : `yi`   Yoruba : `yo`\nZulu : `zu`"

                    embed = discord.Embed(
                        description=description,
                        color=color,
                        timestamp = datetime.datetime.utcnow())

                    embed.set_author(name = ctx.author.name, icon_url=ctx.author.avatar_url)
                    embed.set_footer(text="Page 6")

                    await interaction.message.edit(embed = embed, components= [Select(
                                placeholder="Choose a Page",
                                options= [
                                    SelectOption(label="Page 1", value="1"),
                                    SelectOption(label="Page 2", value="2"),
                                    SelectOption(label="Page 3", value="3"),
                                    SelectOption(label="Page 4", value="4"),
                                    SelectOption(label="Page 5", value="5"),
                                    SelectOption(label="Page 6", value="6", default=True)
                                    ],
                                    custom_id="PageComponents"
                            )])

                    try:
                        await interaction.respond()
                    except:
                        pass

            except asyncio.TimeoutError:
                    await compmsg.edit(embed = embed, components= [Select(
                                placeholder="Choose a Page",
                                options= [
                                    SelectOption(label="1", value="1"),
                                    SelectOption(label="2", value="2", default=True),
                                    SelectOption(label="3", value="3"),
                                    SelectOption(label="4", value="4"),
                                    SelectOption(label="5", value="5"),
                                    SelectOption(label="6", value="6")
                                    ],
                                    custom_id="PageComponents", disabled=True
                            )])

                    break

    @commands.command(pass_context=True)
    async def detect(self, ctx, text : str = None):
        id = ctx.author.id
        guildid = ctx.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        with open("./local/prefix.json", "r") as f:
            L = json.load(f)

        if str(ctx.guild.id) in L:
            get_prefix = L[str(ctx.guild.id)]["prefix"]
        elif str(ctx.guild.id) not in L:
            get_prefix = "="

        color = users[str(id)]['color']
        if text == None:
            embed = discord.Embed(
                description = f"**Description** : Detect a given language\n\n**Usage** : `{get_prefix}detect <text>`\n**Example** : `{get_prefix}detect my name is michelle`" , 
                color = color, 
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Detect Help ❓", icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = embed)

        else:
            lang_detect = self.translator.detect(text)

            language = "Gibberish"

            for i in googletrans.LANGCODES:
                if str(googletrans.LANGCODES[i]) == str(lang_detect.lang):
                    language = string.capwords(i)
            
            embed = discord.Embed(
                description = f"**Language Detected** : `{language}`\n**Text** : {text}", 
                timestamp = datetime.datetime.utcnow())

            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)

            await ctx.send(embed=embed)

    @commands.command(aliases = ["translate"], pass_context=True)
    async def tr(self, ctx, *, translate = None):
        id = ctx.author.id
        guildid = ctx.channel.guild.id
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


        if translate == None:
            embed = discord.Embed(
                description = f"**Description** : Translate text into other languages\n\n**Usage** : `{get_prefix}tr <text> <language code to which you want to translate>`\n**Example** : `{get_prefix}tr my name is michelle fr` where *fr* is the language code for the French language\n\n**Note** : You can get a list of language codes using command : `{get_prefix}lang`" , 
                color = color, 
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Translate Help ❓", icon_url = self.bot.user.avatar_url)
            await ctx.send(embed = embed)

        else:
            word_list = translate.split(" ")

            embed_usage = discord.Embed(
                description = f"**Description** : Translate text into other languages\n\n**Usage** : `{get_prefix}tr <text> <language code to which you want to translate>`\n**Example** : `{get_prefix}tr my name is michelle fr` where *fr* is the language code for the French language\n\n**Note** : You can get a list of language codes using command : `{get_prefix}lang`" , 
                color = color, 
                timestamp=datetime.datetime.utcnow())

            embed_usage.set_author(name = "Translate Help ❓", icon_url = self.bot.user.avatar_url)

            if len(word_list) < 2: return await ctx.send(embed_usage)

            to_lang   = word_list[len(word_list)-1]
            from_lang = word_list[len(word_list)-2] if len(word_list) >= 3 else ""

            # Get the from language name from the passed code
            from_lang_name = googletrans.LANGUAGES.get(from_lang.lower(),None)
            # Get the to language name from the passed code
            to_lang_name   = googletrans.LANGUAGES.get(to_lang.lower(),None)
            if not to_lang_name: # No dice on the language :(
                embed = discord.Embed(
                        title="Something went wrong...",
                        description="I couldn't find that language!",
                        color=color,
                        timestamp=datetime.datetime.utcnow())

                await ctx.send(embed=embed)

            trans = " ".join(word_list[:-2] if from_lang_name else word_list[:-1])

            if not from_lang_name:
                from_output = await self.bot.loop.run_in_executor(None, self.translator.detect, trans)
                from_lang = from_output.lang
                from_lang_name = googletrans.LANGUAGES.get(from_lang,"Unknown")

            result_output = await self.bot.loop.run_in_executor(None, functools.partial(self.translator.translate, trans, dest=to_lang, src=from_lang))
            result = result_output.text
            

            if not result:
                embed = discord.Embed(
                    title="Something went wrong...",
                    description="I wasn't able to translate that!",
                    color=color,
                    timestamp =datetime.datetime.utcnow())
                
                await ctx.send(embed=embed)
            
            if result == trans:
                # We got back what we put in...
                embed = discord.Embed(
                    title="Something went wrong...",
                    description="The text returned from Google was the same as the text put in.  Either the translation failed - or you were translating from/to the same language (en -> en)")

                await ctx.send(embed=embed)

            translate = translate[:-2]

            embed = discord.Embed(
                force_pm=True,
                description=f"`{string.capwords(from_lang_name)}` → `{string.capwords(to_lang_name)}`\n**Translation** : {result}",
                color=color,
                timestamp = datetime.datetime.utcnow()
                )

            embed.set_author(name = f"{ctx.author.name}", icon_url=ctx.author.avatar_url)

            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Translate(bot))