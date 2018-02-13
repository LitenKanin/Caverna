import discord
from discord.ext import commands
from .utils.chat_formatting import escape_mass_mentions, italics, pagify
from random import randint
from random import choice
from enum import Enum
from urllib.parse import quote_plus
import datetime
import time
import aiohttp
import asyncio


class test:
    """General commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        """Chooses between multiple choices.

        To denote multiple choices, you should use double quotes.
        """
        await self.bot.say("test succied")


def setup(bot):
    n = test(bot)
    bot.add_cog(n)
