##############################
# Author: eeysirhc
# Date written: 2022-08-12
# Last updated: 2022-09-05
##############################

# LOAD PYTHON MODULES
import os
from dotenv import load_dotenv 
load_dotenv() 
import discord
from discord.ext import commands

import faq as fq

# https://stackoverflow.com/questions/68581659/i-want-my-bot-to-process-commands-sent-by-other-bots
class UnfilteredBot(commands.Bot):
	async def process_commands(self, message):
		ctx = await self.get_context(message)
		await self.invoke(ctx)

# CONFIG
intents = discord.Intents().all()
client = UnfilteredBot(command_prefix = '.', intents=intents)
TOKEN = os.getenv("DISCORD_TOKEN")

# EVENTS
## BOT STATUS
@client.event
async def on_ready():
	print('Logged in as {0.user}'.format(client))
	await client.change_presence(activity = discord.Game("on the Rosen Bridge"))

## WELCOME
@client.command()
async def welcome(ctx):
	await ctx.send(fq.faq_welcome())

## GET $ERG
@client.command()
async def geterg(ctx):
	await ctx.send(fq.faq_geterg())

## DEX
@client.command()
async def dex(ctx):
	await ctx.send(fq.faq_dex())

## CEX
@client.command()
async def cex(ctx):
	await ctx.send(fq.faq_cex())

## WALLETS
@client.command()
async def wallets(ctx, modifier=""):
	modifier = modifier.lower()
	response = fq.faq_wallets(modifier)
	await ctx.send(response)

## MINING
@client.command()
async def mining(ctx, modifier=""):
	modifier = modifier.lower()
	response = fq.faq_mining(modifier)
	await ctx.send(response)

## LISTING
@client.command()
async def listing(ctx, modifier=""):
	modifier = modifier.lower()
	response = fq.faq_listing(modifier)
	await ctx.send(response)

## BINANCE
@client.command()
async def binance(ctx):
	await ctx.send(fq.faq_binance())

## TRANSACTIONS
@client.command()
async def tps(ctx):
	await ctx.send(fq.faq_tps())

## MARKET CAPITALIZATION
@client.command()
async def marketcap(ctx):
	await ctx.send(fq.faq_marketcap())

## GENESIS
@client.command()
async def genesis(ctx):
	await ctx.send(fq.faq_genesis())

## NFTs
@client.command()
async def genesis(ctx):
        await ctx.send(fq.faq_nfts())

## TOKENJAY
@client.command()
async def tokenjay(ctx, modifier=""):
	modifier = modifier.lower()
	response = fq.faq_tokenjay(modifier)
	await ctx.send(response)

## PROJECTS
@client.command()
async def projects(ctx, modifier=""):
	modifier = modifier.lower()
	response = fq.faq_projects(modifier)
	await ctx.send(response)

## DOCS
@client.command()
async def docs(ctx):
	await ctx.send(fq.faq_docs())

## MANIFESTO
@client.command()
async def manifesto(ctx):
	await ctx.send(fq.faq_manifesto())

# ADMIN
@client.command()
async def admin(ctx):
	await ctx.send(fq.faq_admin())

# LEDGER
@client.command()
async def ledger(ctx):
	await ctx.send(fq.faq_ledger())

# NODE
@client.command()
async def node(ctx, modifier=""):
	modifier = modifier.lower()
	response = fq.faq_node(modifier)
	await ctx.send(response)

# EXECUTE
client.run(TOKEN)


