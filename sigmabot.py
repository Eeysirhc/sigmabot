##############################
# Author: eeysirhc
# Date written: 2022-08-12
# Last updated: 2022-08-14
##############################

# LOAD PYTHON MODULES
import os
import random
from dotenv import load_dotenv 
load_dotenv() 

import spectrumdex as spc 
import blox_height as bh 
import address_history as adh 

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
    await client.change_presence(activity = discord.Game("World of ERGcraft"))

## SPECTRUMDEX TOKEN PRICES
@client.command()
async def spf(ctx, token_name):
    token_name = token_name.lower()
    spc.spectrumdex_charts(token_name)
    await ctx.send(file=discord.File(r'toast.png'))

## ERGO BLOCK HEIGHT
@client.command()
async def blox(ctx):
    height = bh.blox_height()
    await ctx.send(height)

## ADDRESS BALANCE HISTORY
@client.command()
async def addy(ctx, address, token_name=""):
    token_name = token_name.lower()
    adh.address_charts(address, token_name)
    await ctx.send(file=discord.File(r'addy.png'))    

# EXECUTE
client.run(TOKEN)


