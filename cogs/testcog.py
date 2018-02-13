import asyncio
import os
import random
import time
from operator import itemgetter

# Discord and Caverna
import discord
from .utils import checks
from __main__ import send_cmd_help
from .utils.dataIO import dataIO
from discord.ext import commands


    @commands.group(pass_context=True, no_pm=True)
    async def setcarrot(self, ctx):
        """Carrot settings group command"""

        await self.bot.say("there's nothing wrong with the other cogs, perhaps check the code of this one")
