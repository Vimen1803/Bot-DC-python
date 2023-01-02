import discord, random
from discord.ext import commands, tasks
import config
import pyjokes
import datetime

joke = pyjokes.get_joke(language="es", category="all")

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("ponggggg")

    @commands.command()
    async def chiste(self, ctx):
        await ctx.send(joke)

    @commands.command()
    async def avatar(self,ctx, member: discord.Member = None):
        
        if member == None:
            member = ctx.author
            
        if member is not None:
            embed = discord.Embed(title="{}'s Avatar!".format(member.name), colour = 0xccff00)
            embed.set_image(url= member.avatar_url)
            await ctx.send(embed=embed)
    
    @commands.command()
    async def rps(self, ctx, respuesta):
        answer = respuesta
        choices = ["piedra", "papel", "tijera"]
        computers_answer = random.choice(choices)
        if answer not in choices:
            await ctx.send(f" {answer} No es una opción valida, elija 'piedra' 'papel' o 'tijera'")
        else:
            if computers_answer == answer:
                if answer == "papel":
                    await ctx.send(f"Empate!, ambos escojmos :newspaper:, {ctx.author.mention}")
                if answer == "piedra":
                    await ctx.send(f"Empate!, ambos escojmos :moyai:, {ctx.author.mention}")
                if answer == "tijera":
                    await ctx.send(f"Empate!, ambos escojmos :scissors:, {ctx.author.mention}")
                
            if computers_answer == "piedra":
                if answer == "papel":
                    await ctx.send(f":moyai: Has ganado! :, {ctx.author.mention}")
                if answer == "tijera":
                    await ctx.send(f":moyai: Perdiste! :(, {ctx.author.mention}")
                    
            if computers_answer == "papel":
                if answer == "tijera":
                    await ctx.send(f":newspaper: Has ganado! :), {ctx.author.mention} ")
                if answer == "piedra":
                    await ctx.send(f":newspaper: Perdiste! :(, {ctx.author.mention}")
                    
            if computers_answer == "tijera":
                if answer == "piedra":
                    await ctx.send(f":scissors: Has ganado! :), {ctx.author.mention} ")
                if answer == "papel":
                    await ctx.send(f":scissors: Perdiste! :(, {ctx.author.mention}")

def setup(bot):
    bot.add_cog(Fun(bot))