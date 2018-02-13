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
    async def mscts(ctx, url):
        
        author = ctx.message.author
        voice_channel = author.voice_channel
        vc = await self.bot.join_voice_channel(voice_channel)

        player = await vc.create_ytdl_player(url)
        player.start()


def setup(bot):
    n = test(bot)
    bot.add_cog(n)
