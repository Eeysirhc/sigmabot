##############################
# Author: eeysirhc
# Date written: 2022-08-12
# Last updated: 2022-08-25
##############################

# LOAD PYTHON MODULES
import os
from dotenv import load_dotenv 
load_dotenv() 

import blox_height as bh 
import faq

import discord
from discord.ext import commands

# https://stackoverflow.com/questions/68581659/i-want-my-bot-to-process-commands-sent-by-other-bots
class UnfilteredBot(commands.Bot):
    async def process_commands(self, message):
        ctx = await self.get_content(message)
        await self.invoke(ctx)

# CONFIG
client = UnfilteredBot(command_prefix = '.')
TOKEN = os.getenv("DISCORD_TOKEN")

# EVENTS
## BOT STATUS
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity = discord.Game("in Sigmaverse"))

## ERGO BLOCK HEIGHT
@client.command()
async def blox(ctx):
    height = bh.blox_height()
    await ctx.send(height)

## WELCOME
async def welcome(ctx):
    await ctx.send(faq_welcome())

## GET $ERG
async def geterg(ctx):
    await ctx.send(faq_geterg())

## WALLETS
async def wallets(ctx, modifier=""):
    modifier = modifier.lower()
    response = faq_wallets(modifier)
    await ctx.send(resopnse)

## MINING
async def mining(ctx, modifier=""):
    modifier = modifier.lower()
    response = faq_mining(modifier)
    await ctx.send(response)

## DECENTRALIZED EXCHANGES
async def dex(ctx):
    await ctx.send(faq_dex())

## CENTRALIZED EXCHANGES
async def cex(ctx):
    await ctx.send(faq_cex())

## ERGOMIXER
async def ergomixer(ctx):
    await ctx.send(faq_ergomixer())

## SIGMAVERSE
async def sigmaverse(ctx):
    await ctx.send(faq_sigmaverse())

# EXECUTE
client.run(TOKEN)

