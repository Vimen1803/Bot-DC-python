import json
import brawlstats
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix =",", intents=intents)

class BrawlStars(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

        bs = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjVkNWUxNmE5LWM3YzctNDA3Zi1iZWEwLTJjN2Y1OTU0YzMxZiIsImlhdCI6MTY2NDEzMDYzOSwic3ViIjoiZGV2ZWxvcGVyLzBiODE0Y2YyLTJkOWUtMzI3Yy00Y2FkLTcwZWJlNDdkZDZlMCIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiODQuNzYuMTUzLjcxIl0sInR5cGUiOiJjbGllbnQifV19.Z2hLzgzVsslU15Hi3GhDTURiET3VNCTlwtt6-_lvd4ypb5wsbX-xSKX_UMQaaNWW0Ry8Q7XPaLMUeAcKtLejXg"
        self.client = brawlstats.Client(bs, is_async=True)

    @commands.command()
    async def save(self, ctx, tag, member: discord.Member= None):
        if not member:
            member = ctx.author
        member_id= str(member.id)
        try:
            player = await self.client.get_profile(tag)
        except brawlstats.errors.NotFoundError:
            return await ctx.send("tag no encontrado")
                
        with open("cogs/SAVE.json", 'r', encoding="utf8") as f:
            user = json.load(f)
        if not member_id in user:
            with open("cogs/SAVE.json", 'w', encoding="utf8") as f:
                user[str(member.id)] = {}
                user[str(member.id)]["tag"] = tag
                alberto = json.dump(user, f, indent=4)
            await ctx.send("{} vinculado a {}".format(member.name, player.name))
        else:
            await ctx.send("Ya tienes una cuenta vinculada")

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
        
def setup(bot):
    bot.add_cog(BrawlStars(bot))