'''

Developer Only

'''


import discord
from discord.ext import commands
import os
import datetime
import json

from discord.ext.commands.context import Context

class DevCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sendreport(self, message : discord.Message):
        if message.author.id == 488996680058798081 or message.author.id == 840129213968941096:
            file = discord.File("./local/report.json")
            await message.channel.send(file=file)

    @commands.command()
    async def sendauth(self, message : discord.Message):
        if message.author.id == 488996680058798081 or message.author.id == 840129213968941096:
            file = discord.File("./local/auth.json")
            await message.channel.send(file=file)

    @commands.command()
    async def sendconfess(self, message : discord.Message):
        if message.author.id == 488996680058798081 or message.author.id == 840129213968941096:
            file = discord.File("./local/confess.json")
            await message.channel.send(file=file)

    @commands.command()
    async def sendwelcome(self, message : discord.Message):
        if message.author.id == 488996680058798081 or message.author.id == 840129213968941096:
            file = discord.File("./local/welcome.json")
            await message.channel.send(file=file)

    @commands.command()
    async def sendprefix(self, message : discord.Message):
        if message.author.id == 488996680058798081 or message.author.id == 840129213968941096:
            file = discord.File("./local/prefix.json")
            await message.channel.send(file=file)

    @commands.command()
    async def sendreact(self, message : discord.Message):
        if message.author.id == 488996680058798081 or message.author.id == 840129213968941096:
            file = discord.File("./local/react.json")
            await message.channel.send(file=file)

    @commands.command()
    async def sendroast(self, message : discord.Message):
        if message.author.id == 488996680058798081 or message.author.id == 840129213968941096:
            file = discord.File("./local/roast.json")
            await message.channel.send(file=file)

    @commands.command()
    async def sendguild(self, message : discord.Message):
        guildid = message.channel.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        if message.author.id == 488996680058798081 or message.author.id == 840129213968941096:
            file = discord.File(f'{guildid}')
            await message.channel.send(file=file)

    @commands.command()
    async def updatereport(self, ctx : Context):
        if ctx.author.id == 488996680058798081 or ctx.author.id == 840129213968941096:
            try:
                await ctx.message.attachments[0].save(fp = "./update.json")
                with open("update.json", "r") as f:
                    data = json.load(f)

                with open("./local/report.json", "w") as f2:
                    json.dump(data, f2, indent=4)

                await ctx.send(content = "Reports updated")
            except Exception as e:
                await ctx.send(f"Failed. Error : {str(e)}")

            os.remove("./update.json")

    @commands.command()
    async def updateauth(self, ctx : Context):
        if ctx.author.id == 488996680058798081 or ctx.author.id == 840129213968941096:
            try:
                await ctx.message.attachments[0].save(fp = "./update.json")
                with open("update.json", "r") as f:
                    data = json.load(f)

                with open("./local/auth.json", "w") as f2:
                    json.dump(data, f2, indent=4)

                await ctx.send(content = "Users updated")
            except Exception as e:
                await ctx.send(f"Failed. Error : {str(e)}")

            os.remove("./update.json")

    @commands.command()
    async def updateconfess(self, ctx : Context):
        if ctx.author.id == 488996680058798081 or ctx.author.id == 840129213968941096:
            try:
                await ctx.message.attachments[0].save(fp = "./update.json")
                with open("update.json", "r") as f:
                    data = json.load(f)

                with open("./local/confess.json", "w") as f2:
                    json.dump(data, f2, indent=4)

                await ctx.send(content = "Confess updated")
            except Exception as e:
                await ctx.send(f"Failed. Error : {str(e)}")

            os.remove("./update.json")

    @commands.command()
    async def updatewelcome(self, ctx : Context):
        if ctx.author.id == 488996680058798081 or ctx.author.id == 840129213968941096:
            try:
                await ctx.message.attachments[0].save(fp = "./update.json")
                with open("update.json", "r") as f:
                    data = json.load(f)

                with open("./local/welcome.json", "w") as f2:
                    json.dump(data, f2, indent=4)

                await ctx.send(content = "Welcome updated")
            except Exception as e:
                await ctx.send(f"Failed. Error : {str(e)}")

            os.remove("./update.json")

    @commands.command()
    async def updateprefix(self, ctx : Context):
        if ctx.author.id == 488996680058798081 or ctx.author.id == 840129213968941096:
            try:
                await ctx.message.attachments[0].save(fp = "./update.json")
                with open("update.json", "r") as f:
                    data = json.load(f)

                with open("./local/prefix.json", "w") as f2:
                    json.dump(data, f2, indent=4)

                await ctx.send(content = "Prefix updated")
            except Exception as e:
                await ctx.send(f"Failed. Error : {str(e)}")

            os.remove("./update.json")

    @commands.command()
    async def updatereact(self, ctx : Context):
        if ctx.author.id == 488996680058798081 or ctx.author.id == 840129213968941096:
            try:
                await ctx.message.attachments[0].save(fp = "./update.json")
                with open("update.json", "r") as f:
                    data = json.load(f)

                with open("./local/react.json", "w") as f2:
                    json.dump(data, f2, indent=4)

                await ctx.send(content = "Reaction updated")
            except Exception as e:
                await ctx.send(f"Failed. Error : {str(e)}")

            os.remove("./update.json")

    @commands.command()
    async def updateroast(self, ctx : Context):
        if ctx.author.id == 488996680058798081 or ctx.author.id == 840129213968941096:
            try:
                await ctx.message.attachments[0].save(fp = "./update.json")
                with open("update.json", "r") as f:
                    data = json.load(f)

                with open("./local/roast.json", "w") as f2:
                    json.dump(data, f2, indent=4)

                await ctx.send(content = "Roasts updated")
            except Exception as e:
                await ctx.send(f"Failed. Error : {str(e)}")

            os.remove("./update.json")

    @commands.command()
    async def updateguild(self, ctx : Context):
        guildid = ctx.guild.id
        guildid = './guild data/'+ str(guildid) +'.json'
        if ctx.author.id == 488996680058798081 or ctx.author.id == 840129213968941096:
            try:
                await ctx.message.attachments[0].save(fp = "./update.json")
                with open("update.json", "r") as f:
                    data = json.load(f)

                with open(guildid, "w") as f2:
                    json.dump(data, f2, indent=4)

                await ctx.send(content = "Server updated")
            except Exception as e:
                await ctx.send(f"Failed. Error : {str(e)}")

            os.remove("./update.json")

    @commands.command()
    async def guilds(self, ctx : Context):
        if ctx.author.id == 488996680058798081 or ctx.author.id == 840129213968941096:
            L = ""
            for i in self.bot.guilds:
                L+=str(i.name)+"  |  "+str(i.owner)+"\n"

            embed = discord.Embed(
                title = "List of Servers I'm In", 
                description = L,
                timestamp = datetime.datetime.utcnow()
            )

            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(DevCog(bot))
