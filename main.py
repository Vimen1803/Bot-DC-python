import discord
from discord.ext import commands
import json
import config
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix =",", intents=intents)

token = "ODA3Nzk2MDQxNzM4NzQ3OTE0.G0KyoI.frnk_s5JT8zDwpGXwcGqK3sM5RcIFq6xgqMarg"
@bot.event
async def on_ready():
    print("Hydra's bot online")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py" or ".PY"):
        bot.load_extension(f"cogs.{filename [:-3]}")
        print(f"loaded cog: {filename [:-3]}")
    else:
        print("unable to load cogs")
    
bot.run(token)
