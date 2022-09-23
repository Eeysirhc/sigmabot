##############################
# Author: eeysirhc
# Date written: 2022-08-12
# Last updated: 2022-09-23
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
client = UnfilteredBot(command_prefix=".", intents=intents)
TOKEN = os.getenv("DISCORD_TOKEN")

# EVENTS
## BOT STATUS
@client.event
async def on_ready():
	print("Logged in as {0.user}".format(client))
	await client.change_presence(activity=discord.Game("on the Rosen Bridge"))

## WELCOME
@client.command()
async def welcome(ctx):
	await ctx.send(fq.faq_welcome())

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

## WEN
@client.command()
async def wen(ctx, modifier=""):
	modifier = modifier.lower()
	response = fq.faq_wen(modifier)
	await ctx.send(response)

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

## GULAG
@client.command()
async def gulag(ctx):
	await ctx.send(fq.faq_gulag())

## NFTs
@client.command()
async def nfts(ctx, modifier=""):
	modifier = modifier.lower()
	response = fq.faq_nfts(modifier)
	await ctx.send(response)

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

## ADMIN
@client.command()
async def admin(ctx):
	await ctx.send(fq.faq_admin())

## LEDGER
@client.command()
async def ledger(ctx):
	await ctx.send(fq.faq_ledger())

## POUW
@client.command()
async def pouw(ctx):
		await ctx.send(fq.faq_pouw())

## STORAGE RENT
@client.command()
async def rent(ctx):
		await ctx.send(fq.faq_rent())

## NODE
@client.command()
async def node(ctx, modifier=""):
	modifier = modifier.lower()
	response = fq.faq_node(modifier)
	await ctx.send(response)

## YOROI
@client.command()
async def yoroi(ctx):
	await ctx.send(fq.faq_yoroi())

## STAKING
@client.command()
async def staking(ctx):
	await ctx.send(fq.faq_staking())

## DRAMA
@client.command()
async def drama(ctx):
	await ctx.send(fq.faq_drama())

## CONTRIBUTE
@client.command()
async def contribute(ctx):
	await ctx.send(fq.faq_contribute())

## BOTS
@client.command()
async def bots(ctx):
	await ctx.send(fq.faq_bots())

## MINING DIFFICULTY ADJUSTMENTS
@client.command()
async def difficulty(ctx):
	await ctx.send(fq.faq_difficulty())

## SEED
@client.command()
async def seed(ctx):
	await ctx.send(fq.faq_seed())

## FORUM
@client.command()
async def forum(ctx):
	await ctx.send(fq.faq_forum())

########## EIP ##########
def faq_eip(modifier=""):
	if modifier=="1":
		df = """UTXO-Set Scanning Wallet API: <https://github.com/ergoplatform/eips/blob/master/eip-0001.md>"""
	elif modifier=="2":
		df = """Ergo grant program: <https://github.com/ergoplatform/eips/blob/master/eip-0002.md>"""
	elif modifier=="3":
		df = """Deterministic Wallet Standard: <https://github.com/ergoplatform/eips/blob/master/eip-0003.md>"""
	elif modifier=="4":
		df = """Assets standard: <https://github.com/ergoplatform/eips/blob/master/eip-0004.md>"""
	elif modifier=="5":
		df = """Contract Template: <https://github.com/ergoplatform/eips/blob/master/eip-0005.md>"""
	elif modifier=="6":
		df = """Informal Smart Contract Protocol Specification Format: <https://github.com/ergoplatform/eips/blob/master/eip-0006.md>"""
	elif modifier=="17":
		df = """Proxy contracts: <https://github.com/ergoplatform/eips/blob/master/eip-0017.md>"""
	elif modifier=="19":
		df = """[Cold Wallet] An interaction protocol between Hot and Cold mobile wallets: <https://github.com/ergoplatform/eips/blob/master/eip-0019.md>"""
	elif modifier=="20":
		df = """[ErgoPay] An interaction protocol between wallet application and dApp: <https://github.com/ergoplatform/eips/blob/master/eip-0020.md>"""
	elif modifier=="21":
		df = """Genuine tokens verification: <https://github.com/ergoplatform/eips/blob/master/eip-0021.md>"""
	elif modifier=="22":
		df = """Auction contract: <https://github.com/ergoplatform/eips/blob/master/eip-0022.md>"""
	elif modifier=="24":
		df = """Artwork contract: <https://github.com/ergoplatform/eips/blob/master/eip-0024.md>"""
	elif modifier=="25":
		df = """URI scheme for payment requests: <https://github.com/ergoplatform/eips/blob/master/eip-0025.md>"""
	elif modifier=="27":
		df = """Emission Retargeting Soft-Forkr: <https://github.com/ergoplatform/eips/blob/master/eip-0027.md>"""
	elif modifier=="37":
		df = """[DRAFT] Tweatking Difficulty Adjustment Algorithm: <https://github.com/ergoplatform/eips/pull/79/commits/3c8494ba16f9ae85648f9624a8a715f87a19f785>"""
	else: 
		df = """
		Ergo Improvement Proposals (EIP) can be found at <https://github.com/ergoplatform/eips#ergo-improvement-proposals>.

Modifiers: `1`, `2`, `3`, `4`, `5`, `6`, `17`, `19`, `20`, `21`, `22`, `24`, `25`, `27`, `37`
		"""
	return(df)

@client.command()
async def eip(ctx, modifier=""):
	modifier = str(modifier)
	response = faq_eip(modifier)
	await ctx.send(response)

# EXECUTE
client.run(TOKEN)



