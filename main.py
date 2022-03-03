import discord
from discord.ext import commands
from datetime import datetime
import random
import requests
import json

client = commands.Bot(command_prefix=".",intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f".chuck"))

@client.command()        
async def chuck(ctx):
    response = requests.get('https://api.chucknorris.io/jokes/random')
    json_data = json.loads(response.text)
    chuck_norris_joke = json_data['value']
    embed = discord.Embed(title = "Chuck Norris", url = "https://cdn2.hubspot.net/hubfs/2264894/cmas-blog/chuck%20norris%20blog/chuck-3.jpg",
    description = f"`{chuck_norris_joke}`",
    color = discord.Colour.random())
    embed.set_thumbnail(url = "https://cdn2.hubspot.net/hubfs/2264894/cmas-blog/chuck%20norris%20blog/chuck-3.jpg")
    embed.set_footer(text="Your Server Name Here")
    embed.timestamp = datetime.utcnow()
    await ctx.message.delete()
    await  ctx.send(embed=embed)

client.run("Bot Token Here")
