##############################
# Author: eeysirhc
# Date written: 2022-08-12
# Last updated: 2022-08-22
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

# https://stackoverflow.com/questions/68581659/i-want-my-bot-to-process-commands-sent-by-other-bots
class UnfilteredBot(commands.Bot):
    async def process_commands(self, message):
        ctx = await self.get_content(message)
        await self.invoke(ctx)

# CONFIG
#client = commands.Bot(command_prefix = '.')
client = UnfilteredBot(command_prefix = '.')
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

"""
## GAZZA WEN COMMAND
@client.command()
async def wen(ctx):
    userid = '<@userid>'
    responses = ["Please ser {userid} wen $SPF token?",
                "Where to /register for airdrop {userid}?",
                "{userid} ser wen wallet wen layer 2 wen ethereum wen cardano"]
    await ctx.send(random.choice(responses).format(userid=userid))
"""

# EXECUTE
client.run(TOKEN)




