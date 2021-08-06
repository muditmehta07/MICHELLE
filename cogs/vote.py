import discord
from discord.ext import commands
import os
import datetime
import json
from discord.ext.commands.context import Context
from aiohttp import web
import topgg

class TopGG(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ijg0MDE4MDM3OTM4OTI2Mzg4MiIsImJvdCI6dHJ1ZSwiaWF0IjoxNjI3OTkyMTUwfQ._X0TPcRYBhNKzUFP7LzoxK5mt2aVVs3mTwTkMyCEyN0'
        self.topggpy = topgg.DBLClient(self.bot, self.token)
        self.bot.topgg_webhook = topgg.WebhookManager(bot).dbl_webhook("/dbl    ", "kirito27")
        self.bot.topgg_webhook.run(5000)

    @commands.Cog.listener()
    async def on_dbl_vote(self, data):
        if data["type"] == "test":
            # this is roughly equivalent to
            # return await on_dbl_test(data) in this case
            return self.bot.dispatch('dbl_test', data)

        print(f"Received a vote:\n{data}")

    @commands.Cog.listener()
    async def on_dbl_test(self, data):
        """An event that is called whenever someone tests the webhook system for your bot on top.gg."""
        print("Received a test upvote:", "\n", data, sep="")

def setup(bot):
    bot.add_cog(TopGG(bot))