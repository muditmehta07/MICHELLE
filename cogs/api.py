import discord
from discord.ext import commands
import os
import datetime
import json
import praw
import random
import urllib, re
import wikipedia
from discord.ext.commands.context import Context
from discord.ext.commands.core import command
from wikipedia.exceptions import WikipediaException

class ApiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''

    Wikipedia

    '''

    @commands.command(aliases = ["wiki?"])
    async def wikisearch(self, ctx, wiki : str = None):
        
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

        if wiki == None:
            embed = discord.Embed(
                description = f"**Description** : Get Wikipedia search results\n\n**Usage** : `{get_prefix}wiki? <query>`\n**Example** : `{get_prefix}wiki? Spider-Man`" , 
                color = color, 
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Wikipedia Search Help ❓", icon_url = self.bot.user.avatar_url)

            await ctx.send(embed=embed)

        else:
            wiki = ctx.message.content.replace(f"{get_prefix}search ", "")
            results=wikipedia.search(wiki)

            if len(results) == 1:
                embed = discord.Embed(title=f"Results For : {wiki}",
                description=f"{results[0]}",
                color=color,
                timestamp = datetime.datetime.utcnow())

            elif len(results) == 2:
                embed = discord.Embed(title=f"Results For : {wiki}", 
                description=f"**1** {results[0]}\n**2** {results[1]}",
                color=color,
                timestamp = datetime.datetime.utcnow())

            elif len(results) == 3:
                embed = discord.Embed(title=f"Results For : {wiki}", 
                description=f"**1** {results[0]}\n**2** {results[1]}\n**3** {results[2]}",
                color=color,
                timestamp = datetime.datetime.utcnow())

            elif len(results) == 4:
                embed = discord.Embed(title=f"Results For : {wiki}", 
                description=f"**1** {results[0]}\n**2** {results[1]}\n**3** {results[2]}\n**4** {results[3]}",
                color=color,
                timestamp = datetime.datetime.utcnow())

            elif len(results) == 5:
                embed = discord.Embed(title=f"Results For : {wiki}", 
                description=f"**1** {results[0]}\n**2** {results[1]}\n**3** {results[2]}\n**4** {results[3]}\n**5** {results[4]}",
                color=color,
                timestamp = datetime.datetime.utcnow())

            elif len(results) == 6:
                embed = discord.Embed(title=f"Results For : {wiki}", 
                description=f"**1** {results[0]}\n**2** {results[1]}\n**3** {results[2]}\n**4** {results[3]}\n**5** {results[4]}\n**6** {results[5]}",
                color=color,
                timestamp = datetime.datetime.utcnow())
            elif not results:
                embed = discord.Embed(title=f"Results For : {wiki}", 
                description=f"Nothing to show here. No results found.",
                color=color,
                timestamp = datetime.datetime.utcnow())
            else:
                embed = discord.Embed(title=f"Results For : {wiki}", 
                description=f"**1** {results[0]}\n**2** {results[1]}\n**3** {results[2]}\n**4** {results[3]}\n**5** {results[4]}\n**6** {results[5]}",
                color=color,
                timestamp = datetime.datetime.utcnow())


            embed.set_author(name = ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @commands.command()
    async def wiki(self, ctx, wiki : str = None):
        
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

        if wiki == None:
            embed = discord.Embed(
                description = f"**Description** : Get Wikipedia Result for the given query\n\n**Usage** : `{get_prefix}wiki <query>`\n**Example** : `{get_prefix}wiki Spider-Man`" , 
                color = color, 
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Wikipedia Help ❓", icon_url = self.bot.user.avatar_url)

            await ctx.send(embed=embed)

        else:
            wiki = ctx.message.content.replace(f"{get_prefix}wiki ", "")

            try:
                results=wikipedia.summary(wiki, sentences=3)
                page = wikipedia.page(wiki)
                embed = discord.Embed(title = page.title,
                url = page.url,
                description=f"*{results}*",
                color=color,
                timestamp = datetime.datetime.utcnow())

                embed.set_thumbnail(url = page.images[0])
                embed.set_author(name = ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)

            except Exception as e:
                embed = discord.Embed(title=f"Suggestions for keyword : {wiki}",
                description=f"{e}",
                color=color,
                timestamp = datetime.datetime.utcnow())

                await ctx.send(embed=embed)

    '''

    Reddit Commands

    '''

    @commands.command(name = "reddit", aliases = ["r/", "r?", "Reddit", "REDDIT"])
    async def reddit(self, ctx, category : str = None):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = self.bot.get_guild(guildid)
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

        if category == None:
            embed = discord.Embed(
                description = f"**Description** : Get a Reddit result for the given subreddit\n\n**Usage** : `{get_prefix}reddit <subreddit>`\n**Example** : `{get_prefix}reddit Dankmemer`" , 
                color = color, 
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "Reddit Help ❓", icon_url = self.bot.user.avatar_url)

            await ctx.send(embed=embed)

        else:
            try:
                reddit = praw.Reddit(client_id = 'vOtMxaMzhnpD9A', client_secret = 'NIzr13jWXE8MPVsIxtRVe_HqftPAOQ', user_agent = 'Olivia')
                memes_submissions = reddit.subreddit(category).hot()
                post = random.randint(1, 100)
                for i in range(0, post):
                    submission = next(x for x in memes_submissions if not x.stickied)

                if submission.url.endswith('.png') or submission.url.endswith('.jpg') or submission.url.endswith('.gif'):
                    embed = discord.Embed(description = f"{submission.title}",
                    timestamp=datetime.datetime.utcnow(),
                    color=color)

                    embed.set_footer(text = f"r/{category}")
                    embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                    embed.set_image(url=f"{submission.url}")

                    await ctx.send(embed=embed)

                else:
                    await ctx.send(f'Called by : {ctx.author}\nTitle : {submission.title}\n{submission.url}')

            except:

                await ctx.reply(f'The Subreddit does not exist!')



    @commands.command(name = "meme", aliases = ["lol", "Meme", "MEME"])
    async def meme(self, ctx, category : str = None):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = self.bot.get_guild(guildid)
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

        try:

            if category == None:
                embed = discord.Embed(
                    description = f"**Description** : Get a Meme the given category\n\n**Usage** : `{get_prefix}meme <category>`\n**Example** : `{get_prefix}meme cat`" , 
                    color = color, 
                    timestamp=datetime.datetime.utcnow())

                embed.set_author(name = "Meme Help ❓", icon_url = self.bot.user.avatar_url)

                await ctx.send(embed=embed)

            else:
                category += "memes"
                reddit = praw.Reddit(client_id = 'vOtMxaMzhnpD9A', client_secret = 'NIzr13jWXE8MPVsIxtRVe_HqftPAOQ', user_agent = 'Olivia')
                memes_submissions = reddit.subreddit(category).hot()
                post = random.randint(1, 100)
                for i in range(0, post):
                    submission = next(x for x in memes_submissions if not x.stickied)

                if submission.url.endswith('.png') or submission.url.endswith('.jpg') or submission.url.endswith('.gif'):
                    embed = discord.Embed(title = f"{submission.title}",
                    timestamp=datetime.datetime.utcnow(),
                    color=color)

                    embed.set_footer(text = f"r/{category}")
                    embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                    embed.set_image(url=f"{submission.url}")

                    await ctx.send(embed=embed)

                else:
                    await ctx.send(f'`Called by : {ctx.author}`\n{submission.url}')

        except:

            await ctx.author.send(f'**Something went wrong**\nError from : `{guild.name}`')

    '''

    Youtube Commands

    '''


    @commands.command(name = "youtube", aliases = ["yt"])
    async def youtube(self, ctx, *, search : str = None):
        
        id = ctx.author.id
        guildid = ctx.guild.id
        guild = self.bot.get_guild(guildid)
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

        if search == None:
            embed = discord.Embed(
                description = f"**Description** : Get YouTube result for the given query\n\n**Usage** : `{get_prefix}yt <query>`\n**Example** : `{get_prefix}yt Doctor Strange trailer`" , 
                color = color, 
                timestamp=datetime.datetime.utcnow())

            embed.set_author(name = "YouTube Help ❓", icon_url = self.bot.user.avatar_url)

            await ctx.send(embed=embed)

        else:
            query_string = urllib.parse.urlencode({'search_query': search})
            html_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
            search_content= html_content.read().decode()
            search_results = re.findall(r'\/watch\?v=\w+', search_content)
            #print(search_results)
            await ctx.send('https://www.youtube.com' + search_results[0])



async def setup(bot):
    await bot.add_cog(ApiCog(bot))