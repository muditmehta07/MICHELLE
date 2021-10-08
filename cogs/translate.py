from datetime import date, datetime
import functools, string
import googletrans
from googletrans import Translator
import discord
import datetime
import json
import random
from discord.ext import commands

# Requires the mtranslate module be installed

class Translate(commands.Cog):
            
    def __init__(self, bot):
        self.bot = bot
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

        description = ""
        for lang in googletrans.LANGCODES:
            description += "`{} : {}` ".format(string.capwords(lang), googletrans.LANGCODES[lang])
        embed = discord.Embed(
            title="Available Languages 🔤",
            description=description,
            color=color,
            timestamp = datetime.datetime.utcnow())

        embed.set_author(name = ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def detect(self, ctx, text : str = None):
        id = ctx.author.id
        guildid = ctx.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']
        if text == None:
            usage = f"Usage: `{ctx.prefix}detect [text]`"
            embed = discord.Embed(
                description = usage,
                timestamp = datetime.datetime.utcnow(),
                color = color
            )
            embed.set_author(name = ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)

        else:
            lang_detect = self.translator.detect(text)

            language = "Gibberish"

            for i in googletrans.LANGCODES:
                if str(googletrans.LANGCODES[i]) == str(lang_detect.lang):
                    language = string.capwords(i)
            
            embed = discord.Embed(
                description = f"**Language Detected** `{language}`", 
                timestamp = datetime.datetime.utcnow())

            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)

            await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def tr(self, ctx, *, translate = None):
        id = ctx.author.id
        guildid = ctx.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']

        usage = "Usage : `{}tr [text] [from language code (optional)] [to language code]`".format(ctx.prefix)
        if translate == None:
            embed = discord.Embed(
                description = usage,
                color=color,
                timestamp = datetime.datetime.utcnow()
            )
            embed.set_author(name = ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)

        word_list = translate.split(" ")

        if len(word_list) < 2: return await ctx.send(usage)

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

        embed = discord.Embed(
            force_pm=True,
            description=result,
            color=color,
            timestamp = datetime.datetime.utcnow(),
            footer="{} --> {} - Powered by Google Translate".format(string.capwords(from_lang_name), string.capwords(to_lang_name)))

        embed.set_author(name = f"{ctx.author.name}'s Translation", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def morse(self, ctx, *, content = None):
        id = ctx.author.id
        guildid = ctx.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']
        """Converts ascii to morse code.  Accepts a-z and 0-9.  Each letter is comprised of "-" or "." and separated by 1 space.  Each word is separated by 4 spaces."""

        if content == None:
            await ctx.send("Usage: `{}morse [content]`".format(ctx.prefix))
            return

        # Only accept alpha numeric stuff and spaces
        word_list = content.split()
        morse_list = []
        for word in word_list:
            # Iterate through words
            letter_list = []
            for letter in word:
                # Iterate through each letter of each word
                if letter.lower() in self.to_morse:
                    # It's in our list - add the morse equivalent
                    letter_list.append(self.to_morse[letter.lower()])
            if len(letter_list):
                # We have letters - join them into morse words
                # each separated by a space
                morse_list.append(" ".join(letter_list))
            
        if not len(morse_list):
            # We didn't get any valid words
            await ctx.send("There were no valid a-z/0-9 chars in the passed content.")
            return

        # We got *something*
        msg = "    ".join(morse_list)
        embed = discord.Embed(
            description = f"**Text** : `{content}`\n**Morse** : `{msg}`",
            color=color,
            timestamp = datetime.datetime.utcnow()
        )

        embed.set_author(name = ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    async def unmorse(self, ctx, *, content = None):
        id = ctx.author.id
        guildid = ctx.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']
        """Converts morse code to ascii.  Each letter is comprised of "-" or "." and separated by 1 space.  Each word is separated by 4 spaces."""

        if content == None:
            await ctx.send("Usage `{}unmorse [content]`".format(ctx.prefix))
            return

        # Only accept morse symbols
        content = "".join([x for x in content if x in " .-"])
        word_list = content.split("    ")
        ascii_list = []
        for word in word_list:
            # Split by space for letters
            letter_list = word.split()
            letter_ascii = []
            # Iterate through letters
            for letter in letter_list:
                for key in self.to_morse:
                    if self.to_morse[key] == letter:
                        # Found one
                        letter_ascii.append(key.upper())
            if len(letter_ascii):
                # We have letters - join them into ascii words
                ascii_list.append("".join(letter_ascii))
            
        if not len(ascii_list):
            # We didn't get any valid words
            await ctx.send("There were no valid morse chars in the passed content.")
            return

        # We got *something* - join separated by a space
        msg = " ".join(ascii_list)

        embed = discord.Embed(
            description = f"**Text** : `{content}`\n**Unmorse** : `{msg}`",
            color=color,
            timestamp = datetime.datetime.utcnow()
        )

        embed.set_author(name = ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def groot(self, ctx):
        id = ctx.author.id
        guildid = ctx.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        with open(guildid, 'r') as f:
            users = json.load(f)

        color = users[str(id)]['color']
        groots = [
            "I am Groot",
            "**I AM GROOT**",
            "I... am... *Groot*",
            "I am Grooooot"
        ]

        groot = ctx.message.content.replace(f"{ctx.prefix}groot", "")
        groot = groot.split()
        length = len(groot)

        if length > 3:
            length = length // 3
        else:
            length = 1

        msg = ""

        for i in range(length):
            msg += random.choice(groots)+" "

        embed = discord.Embed(
            description = msg,
            color=color,
            timestamp = datetime.datetime.utcnow()
        )
        embed.set_author(name = ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Translate(bot))