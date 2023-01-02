import discord 
from discord.ext import commands, tasks
import config
import json

class Créditos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def tw(self, ctx):
        await ctx.send("https://twitter.com/Viiictooor18")
    
    @commands.command()
    async def ig(self, ctx):
        await ctx.send("https://www.instagram.com/viictoor._18/")

           
    @commands.command()
    async def tiktok(self, ctx):
        await ctx.send("https://www.tiktok.com/@carla._bs?")
 
 
def setup(bot):
    bot.add_cog(Créditos(bot))
        