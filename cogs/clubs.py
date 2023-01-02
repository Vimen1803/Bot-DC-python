from ast import If
from sqlite3 import Timestamp
from turtle import color
import discord 
from discord.ext import commands, tasks
from discord import User, Embed, Member
import config, asyncio

class ClubManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def desc(self, ctx,tipo, rango, reg):
         
        if tipo == "leg":
             await ctx.send(f"` <c40ff00>•LA</c> {reg}|•ᴅɪꜱᴄ →<c40ff00> wUNZHAS</c>| <c5>LASpain_</c> 🕊️|😈<cff0303>Legendario {rango}</c>`")
             
        elif tipo =="mítico":
             await ctx.send(f"` <c40ff00>•LA</c> {reg}|•ᴅɪꜱᴄ →<c40ff00> wUNZHAS</c>| <c5>LASpain_</c> 🕊️|🔮<cd426fc>Mítico {rango}</c>`")
             
        elif tipo == "diamante":
             await ctx.send(f"` <c40ff00>•LA</c> {reg}|•ᴅɪꜱᴄ →<c40ff00> wUNZHAS</c>| <c5>LASpain_</c> 🕊️|💎<c5>Diamante {rango}</c>`")
       
        elif tipo == "oro":
             await ctx.send(f"` <c40ff00>•LA</c> {reg}|•ᴅɪꜱᴄ →<c40ff00> wUNZHAS</c>| <c5>LASpain_</c> 🕊️|🥇<c7>Oro {rango}</c>`")
             
        elif tipo == "plata":
             await ctx.send(f"` <c40ff00>•LA</c> {reg}|•ᴅɪꜱᴄ →<c40ff00> wUNZHAS</c>| <c5>LASpain_</c> 🕊️|🥈<c1>Plata {rango}</c>`")
        
        elif tipo == "bronce":
            await ctx.send(f"` <c40ff00>•LA</c> {reg}|•ᴅɪꜱᴄ →<c40ff00> wUNZHAS</c>| <c5>LASpain_</c> 🕊️|🥉<c2>Bronce {rango} </c>`")
        
        else:
             await ctx.send("El rango de Liga De Club no es válida")
             
    @commands.command()
    async def desc2(self, ctx,tipo, reg=None):
        if tipo == "maestros":
            await ctx.send(f"` <c40ff00>•LA</c> {reg}|•ᴅɪꜱᴄ →<c40ff00> wUNZHAS</c>| <c5>LASpain_</c> 🕊️|👑<cfff800>Maestros</c>`")
            
        if tipo == "kings":
            await ctx.send("``<c7>• ONLY KINGS👑</c>| •<c3> Ini mi religión</c>🛐|ㅤ <c9>push = gay</c> | <cff9900>we dont respect LA</c>|``")
            
    @commands.command()
    async def mention(self, ctx, numero : int, member : discord.Member = None):
        x = 0
        
        if member == None:
            await ctx.send(f"Indica tu víctima {ctx.author.mention}")
        else:
            while x < numero:
                x = x + 1
                await ctx.send(f"{member.mention}")
            
    @commands.command()
    async def av(self,ctx, member: discord.Member = None):
        
        if member == None:
            member = ctx.author
            
        if member is not None:
            embed = discord.Embed(title="{}'s Avatar!".format(member.name), colour = 0xccff00)
            embed.set_image(url= member.avatar_url)
            await ctx.send(embed=embed)
            
def setup(bot):
    bot.add_cog(ClubManagement(bot))