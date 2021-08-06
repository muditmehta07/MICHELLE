# Michelle

__Website__ : https://top.gg/bot/840180379389263882

Okay so, this is a tutorial thingy, you can learn how to make a discord bot like Michelle here. I'll be explaining the code here in the easiest way.

# main.py

**Step 1** : Import all the necessary modules that we'll be using.

```Python

import discord
from discord import user
from discord import channel
from discord import message
from discord.colour import Color
from discord.enums import ActivityType
from discord.ext.commands.converter import _get_from_guilds
from discord.message import Message
from discord.utils import get
from discord.ext import commands,tasks
import os
import json
from itertools import cycle
import datetime

```
