##############################
# Author: eeysirhc
# Date written: 2022-08-12
# Last updated: 
##############################

# LOAD PYTHON MODULES
import os
import random
from dotenv import load_dotenv 
load_dotenv() 

from spectrumdex import *
from blox_height import * 

import discord
from discord.ext import commands

# CONFIG
client = commands.Bot(command_prefix = '.')
TOKEN = os.getenv("DISCORD_TOKEN")

# EVENTS
## BOT STATUS
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity = discord.Game("on the Rosen Bridge"))

## SPECTRUMDEX TOKEN PRICES
@client.command()
async def spf(ctx, token_name):
    token_name = token_name.lower()
    spectrumdex_charts(token_name)
    await ctx.send(file=discord.File(r'toast.png'))

## ERGO BLOCK HEIGHT
@client.command()
async def blox(ctx):
    height = blox_height()
    await ctx.send(height)


# EXECUTE
client.run(TOKEN)




