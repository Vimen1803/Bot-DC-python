import discord 
from discord.ext import commands, tasks
import config

class Redes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def tw(self, ctx):
        await ctx.send("https://twitter.com/Viiictooor18")
    
    @commands.command()
    async def ig(self, ctx):
        await ctx.send("https://www.instagram.com/viictoor._18/")     
 
def setup(bot):
    bot.add_cog(Redes(bot))
        