import os
import discord
from discord.ext import commands
import json
import random
from discord.embeds import Embed

with open("cogs/Banco.json", 'r', encoding="utf8") as f:
                user = json.load(f)

class Banco(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.command(aliases=["createacc"])
    async def bancocrear(self, ctx, member: discord.Member = None):
       if not member:
            member = ctx.author
            member_id= str(member.id)

            with open("cogs/Banco.json", 'r', encoding="utf8") as f:
                user = json.load(f)
            if not member_id in user:
                with open("cogs/Banco.json", 'w', encoding="utf8") as f:
                    user[str(member.id)] = {}
                    user[str(member.id)]["Dinero en el banco"] = 2000
                    user[str(member.id)]["Dinero en metalico"] = 150
                    paco = json.dump(user, f, indent=4)
                await ctx.send(f"Cuenta bancaria de {member.name} creada correctamente, iniciarás con 2000$ en el banco y 150$ en metalico")
            else:
                await ctx.send("Ya tienes una cuenta bancaria")
       else:
            member_id= str(member.id)
            with open("cogs/Banco.json", 'r', encoding="utf8") as f:
                user = json.load(f)
            if not member_id in user:
                with open("cogs/Banco.json", 'w', encoding="utf8") as f:
                    user[str(member.id)] = {}
                    user[str(member.id)]["Dinero en el banco"] = 2000
                    user[str(member.id)]["Dinero en metalico"] = 150
                    paco = json.dump(user, f, indent=4)
                await ctx.send(f"Cuenta bancaria de {member.name} creada correctamente, iniciarás con 2000$ en el banco y 150$ en metalico")
            else:
                await ctx.send("Ya tienes una cuenta bancaria")
      
    @commands.command()
    async def add(self, ctx, cantidad, member: discord.Member):
        if not ctx.author.guild_permissions.administrator:
            await ctx.send("No tienes los permisos requeridos para realizar esta operación")
        else:
            with open(f"cogs/Banco.json", 'r', encoding="utf8") as f:
                user = json.load(f)
            member_id= str(member.id)
            banco = user[str(member.id)]["Dinero en el banco"]
            cash = user[str(member.id)]["Dinero en metalico"]
            nuevacantidad = int(cash) + int(cantidad)
            if member_id in user:
                with open(f"cogs/Banco.json", 'w', encoding="utf8") as f:
                    nuevacantidad = int(cash) + int(cantidad)
                    user[str(member.id)] = {}
                    user[str(member.id)]["Dinero en el banco"] = banco
                    user[str(member.id)]["Dinero en metalico"] = nuevacantidad
                    paco = json.dump(user, f, indent=4)
                    await ctx.send(f"{cantidad} añadido con éxito a la cuenta de {member}")    
            else:
                 await ctx.send("Error, cuenta no encontrada") 

    @commands.command()
    async def remove(self, ctx, tipo, cantidad, member: discord.Member):
        if not ctx.author.guild_permissions.administrator:
            await ctx.send("No tienes los permisos requeridos para realizar esta operación")

        else:
            if tipo == "banco":
                with open(f"cogs/Banco.json", 'r', encoding="utf8") as f:
                    user = json.load(f)
                member_id= str(member.id)
                banco = user[str(member.id)]["Dinero en el banco"]
                cash = user[str(member.id)]["Dinero en metalico"]
                if int(banco) < int(cantidad):
                    await ctx.send("Esta persona no tiene tanto dinero en su cuenta")
                else:
                    nuevacantidad = int(banco) - int(cantidad)
                    if member_id in user:
                        with open(f"cogs/Banco.json", 'w', encoding="utf8") as f:
                            nuevacantidad = int(banco) - int(cantidad)
                            user[str(member.id)] = {}
                            user[str(member.id)]["Dinero en el banco"] = nuevacantidad
                            user[str(member.id)]["Dinero en metalico"] = cash
                            paco = json.dump(user, f, indent=4)
                            await ctx.send(f"{cantidad} retirados con éxito a la cuenta bancaria de {member}")    
                    else:
                        await ctx.send("Error, cuenta no encontrada") 

            elif tipo == "cash":
                with open(f"cogs/Banco.json", 'r', encoding="utf8") as f:
                    user = json.load(f)
                member_id= str(member.id)
                banco = user[str(member.id)]["Dinero en el banco"]
                cash = user[str(member.id)]["Dinero en metalico"]
                if int(cash) < int(cantidad):
                    await ctx.send("Esta persona no tiene tanto dinero en efectivo")
                else:
                    nuevacantidad = int(cash) - int(cantidad)
                    if member_id in user:
                        with open(f"cogs/Banco.json", 'w', encoding="utf8") as f:
                            nuevacantidad = int(cash) - int(cantidad)
                            user[str(member.id)] = {}
                            user[str(member.id)]["Dinero en el banco"] = banco
                            user[str(member.id)]["Dinero en metalico"] = nuevacantidad
                            paco = json.dump(user, f, indent=4)
                            await ctx.send(f"{cantidad} retirados con éxito del efectivo de {member}")    
                    else:
                        await ctx.send("Error, cuenta no encontrada")
            else: 
                    await ctx.send("Error")
            

    @commands.command(aliases=["dep"])
    async def ingresar(self, ctx, cantidad, member: discord.Member = None):
            member = ctx.author
            member_id= str(member.id)
            with open(f"cogs/Banco.json", 'r', encoding="utf8") as f:
                user = json.load(f)
            member_id= str(member.id)
            banco = user[str(member.id)]["Dinero en el banco"]
            cash = user[str(member.id)]["Dinero en metalico"]
            if cantidad == "all":
                cantidad = cash
            if int(cantidad) > int(cash):
                await ctx.send("No tienes tanto dinero en efectivo")
            else:
                nuevacantidadbanco = int(banco) + int(cantidad)
                nuevacantidadcash = int(cash) - int(cantidad)
                if member_id in user:
                    with open(f"cogs/Banco.json", 'w', encoding="utf8") as f:
                        nuevacantidad = int(cash) + int(cantidad)
                        user[str(member.id)] = {}
                        user[str(member.id)]["Dinero en el banco"] = nuevacantidadbanco
                        user[str(member.id)]["Dinero en metalico"] = nuevacantidadcash
                        paco = json.dump(user, f, indent=4)
                        await ctx.send(f"{cantidad} añadido con éxito a la cuenta de {member}")    
                else:
                    await ctx.send("Error, cuenta no encontrada")

    @commands.command()
    async def retirar(self, ctx, cantidad, member: discord.Member = None):
        member = ctx.author
        member_id= str(member.id)
        with open(f"cogs/Banco.json", 'r', encoding="utf8") as f:
            user = json.load(f)
        member_id= str(member.id)
        banco = user[str(member.id)]["Dinero en el banco"]
        cash = user[str(member.id)]["Dinero en metalico"]
        if int(cantidad) > int(banco):
            await ctx.send("No tienes tanto dinero en el banco")
        else:
            nuevacantidadbanco = int(banco) - int(cantidad)
            nuevacantidadcash = int(cash) + int(cantidad)
            if member_id in user:
                with open(f"cogs/Banco.json", 'w', encoding="utf8") as f:
                    user[str(member.id)] = {}
                    user[str(member.id)]["Dinero en el banco"] = nuevacantidadbanco
                    user[str(member.id)]["Dinero en metalico"] = nuevacantidadcash
                    paco = json.dump(user, f, indent=4)
                    await ctx.send(f"{cantidad} retirados de la cuenta de {member}")    
            else:
                await ctx.send("Error, cuenta no encontrada")

    @commands.command(aliases=["bal"])
    async def ver(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
            member_id= str(member.id)
        with open(f"cogs./Banco.json", 'r', encoding="utf8") as f:
            user = json.load(f)
            if str(member.id) in user:
                banco = user[str(member.id)]["Dinero en el banco"]
                cash = user[str(member.id)]["Dinero en metalico"]
                cantidadtotal = int(cash) + int(banco)
                embed = discord.Embed(
                    timestamp=ctx.message.created_at,
                    title=(f"Cuenta de {member}"),
                    color=0x008000,
                )
                embed.add_field(
                    name="__Dinero Total__",
                    value=f"{cantidadtotal}$",
                )
                embed.add_field(
                    name="__Metalico__",
                    value=f"{cash}$",
                )
                embed.add_field(
                    name="__Banco__",
                    value=f"{banco}$",
                )
                embed.add_field(
                    name="__Últimas transacciones__",
                    value="En proceso",
                )
                embed.set_footer(
                    text=f"Solicitado por: {ctx.author.name}",
                )
                embed.set_thumbnail(url=member.avatar_url
                )
                await ctx.send(embed = embed)      
            else: 
                await ctx.send("Debes crear una cuenta primero, utiliza el comando '``,bancocrear``")  

    @commands.command()
    async def enviar(self,ctx, cantidad, member: discord.Member):
        member_id= str(member.id)
        with open(f"cogs/Banco.json", 'r', encoding="utf8") as f:
            user = json.load(f)
        author = ctx.author
        author_id = str(author.id)
        member_id = str(member.id)
        banco1 = user[str(author.id)]["Dinero en el banco"]
        cash1 = user[str(author.id)]["Dinero en metalico"]
        banco2 = user[str(member.id)]["Dinero en el banco"]
        cash2 = user[str(member.id)]["Dinero en metalico"]
        if int(cantidad) > int(banco1):
            await ctx.send("No tienes tanto dinero en el banco")
        else:
            with open(f"cogs/Banco.json", 'w', encoding="utf8") as f:
                nuevacantidadbancoautor = int(banco1) - int(cantidad)
                nuevacantidadbancorecibidor = int(banco2) + int(cantidad)
                cashauthor = int(cash1)
                cashreciber = int(cash2)

                user[str(author.id)] = {}
                user[str(author.id)]["Dinero en el banco"] = nuevacantidadbancoautor
                user[str(author.id)]["Dinero en metalico"] = cashauthor
                user[str(member.id)] = {}
                user[str(member.id)]["Dinero en el banco"] = nuevacantidadbancorecibidor
                user[str(member.id)]["Dinero en metalico"] = cashreciber
                paco = json.dump(user, f, indent=4)
                await ctx.send(f"{cantidad} enviada correctamente a {member}, puede ver su cuenta con el comando ',ver'")

    @commands.command()
    async def resetacc(self,ctx, member: discord.Member):
        member_id = str(member.id)
        if not ctx.author.guild_permissions.administrator:
            await ctx.send("No tienes los permisos requeridos para realizar esta operación")
        else:
            with open(f"cogs/Banco.json", 'w', encoding="utf8") as f:
                member_id = str(member.id)
                user[str(member.id)] = {}
                user[str(member.id)]["Dinero en el banco"] = 2000
                user[str(member.id)]["Dinero en metalico"] = 150
                paco = json.dump(user, f, indent=4)
                await ctx.send(f"Cuenta de {member.mention} reseteada correctamente, añadidos 2000$ al banco y 150$ en efectivo")

    @commands.command()  
    async def setacc(self, ctx, member: discord.Member, banco, cash ):
        if not ctx.author.guild_permissions.administrator:
            await ctx.send("No tienes los permisos requeridos para realizar esta operación")
        else:
            member_id = str(member.id)
            with open(f"cogs/Banco.json", 'w', encoding="utf8") as f:
                    member_id = str(member.id)
                    user[str(member.id)] = {}
                    user[str(member.id)]["Dinero en el banco"] = banco
                    user[str(member.id)]["Dinero en metalico"] = cash
                    paco = json.dump(user, f, indent=4)
                    await ctx.send(f"Cuenta de {member.mention} modificada correctamente, añadidos {banco}$ al banco y {cash}$ en efectivo")
    
    @commands.command()
    async def banco(self, ctx):
        author = ctx.author
        embed = discord.Embed(
            timestamp = ctx.message.created_at,
            title = "__COMANDOS ECONOMÍA__",
            color = 0x0100f9,
        )
        embed.add_field(
            name=f"__Comandos para Admins__",
            value="__,add__ \nAñade x cantidad a la cuenta bancaria de un usuario \n__,remove__ \nElimina x cantidad de la cuenta bancario de un usuario \n__,resetacc__ \nReinicia la cuenta de cualquier usuario a 2000$ en banco y 150$ en efectivo \n__,setacc__ \nEstablece una cantidad determinada de dinero en el banco y en efectivo para un usuario"
        )
        embed.add_field(
            name=f"__Comandos para Miembros__",
            value="__,bancocrear / ,createacc__ \nPermite crear tu cuenta bancaria \n__,ingresar / ,dep__ \nPermite ingresar dinero al banco \n__,retirar__ \nPermite retirar dinero de la cuenta bancaria, este se añadirá en efectivo \n__,enviar__ \nPermite enviar x cantidad de dinero de tu cuenta bancaria a la de otro usuario \n__,ver / ,bal__ \nPermite ver tu cuenta y tu dinero en efectivo"
        )
        embed.set_footer(
            text=f"Solicitado por: {ctx.author.name}",
        )
        embed.set_thumbnail(url=author.avatar_url
        )
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Banco(bot))

