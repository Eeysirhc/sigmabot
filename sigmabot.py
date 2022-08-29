##############################
# Author: eeysirhc
# Date written: 2022-08-12
# Last updated: 2022-08-28
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

## HELP
@client.command()
async def help(ctx):
    await ctx.send(faq_help())

## WELCOME
@client.command()
async def welcome(ctx):
    await ctx.send(faq_welcome())

## GET $ERG
@client.command()
async def geterg(ctx, modifier=""):
    modifier = modifier.lower()
    response = faq_geterg(modifier)
    await ctx.send(response)

## WALLETS
@client.command()
async def wallets(ctx, modifier=""):
    modifier = modifier.lower()
    response = faq_wallets(modifier)
    await ctx.send(resopnse)

## MINING
@client.command()
async def mining(ctx, modifier=""):
    modifier = modifier.lower()
    response = faq_mining(modifier)
    await ctx.send(response)

## PROJECTS
@client.command()
async def projects(ctx, modifier=""):
    modifier = modifier.lower()
    response = faq_projects(modifier)
    await ctx.send(response)

# EXECUTE
client.run(TOKEN)




