import discord
from discord.ext import commands, tasks
import brawlstats
from typing_extensions import Self
import config
from re import sub
import asyncio
import discord.ext.commands.errors



class brawl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def v(self, ctx,tag):
        txt = tag
        x = txt.upper().replace("O", "0")
        if x.startswith("#"):
            await ctx.send(f"Tag {x} vinculado correctamente al usuario {ctx.author.name}")
        else:
            await ctx.send("Tag no válido, recuerda añadir # al inicio")
        
def setup(bot):
    bot.add_cog(brawl(bot))