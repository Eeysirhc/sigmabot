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
		df = """
		[UTXO-Set Scanning Wallet API]
This Ergo Improvement Proposal focused on extending the wallet to be able to serve the needs of external applications by providing a flexible scanning interface and the possibility for applications to register scans with the wallet to ensure that they are tracked. Scans that have successfully passed are considered to belong to the application.: <https://github.com/ergoplatform/eips/blob/master/eip-0001.md>
		"""
	elif modifier=="2":
		df = """
		[Ergo grant program]
Ergo has a treasury box, that collects coins locked for further development of the platform. This is the proposal of the process of treasury box distribution: <https://github.com/ergoplatform/eips/blob/master/eip-0002.md>
		"""
	elif modifier=="3":
		df = """[Deterministic Wallet Standard] 
This EIP attempts to define a specific `coin_type` for the Ergo ecosystem, as well as a policy for how wallets use the `change` level: <https://github.com/ergoplatform/eips/blob/master/eip-0003.md>
		"""
	elif modifier=="4":
		df = """[Assets standard]
This standard provides a uniform way to issue Ergo tokens. A standard interface allows any tokens on Ergo to be re-used by other applications from wallets to decentralized exchanges: <https://github.com/ergoplatform/eips/blob/master/eip-0004.md>
		"""
	elif modifier=="5":
		df = """
		[Contract Template]
This EIP defines a standard serialization formats and contract metadata for cross-platform reusable contract templates: <https://github.com/ergoplatform/eips/blob/master/eip-0005.md>
		"""
	elif modifier=="6":
		df = """
		[Informal Smart Contract Protocol Specification Format]
Learn more at <https://github.com/ergoplatform/eips/blob/master/eip-0006.md>
		"""
	elif modifier=="17":
		df = """
		[Proxy contracts]
Learn more at <https://github.com/ergoplatform/eips/blob/master/eip-0017.md>
		"""
	elif modifier=="19":
		df = """
		[Cold Wallet: an interaction protocol between Hot and Cold mobile wallets]
This EIP defines a standard for cross-device interaction between "Hot" (online) and "Cold" (offline) wallets for signing Ergo transactions: <https://github.com/ergoplatform/eips/blob/master/eip-0019.md>
		"""
	elif modifier=="20":
		df = """
		[ErgoPay: an interaction protocol between wallet application and dApp] 
This EIP defines a standard for cross-platform interaction between an online dApp and a wallet app for creating, signing and sending Ergo transactions: <https://github.com/ergoplatform/eips/blob/master/eip-0020.md>
		"""
	elif modifier=="21":
		df = """
		[Genuine tokens verification]
This EIP lists the common tokens of value with their unique identifier, so users as well as wallet and explorer applications can verify if a token is genuine. The EIP is meant to be updated regularly when new tokens of value are added.: <https://github.com/ergoplatform/eips/blob/master/eip-0021.md>
		"""
	elif modifier=="22":
		df = """
		[Auction contract]
Decentralized auctioning of any kind of tokens (artwork, share tokens, etc.) is an important part of any blockchain. This EIP is proposing the auction contract with various features listed in the Design section: <https://github.com/ergoplatform/eips/blob/master/eip-0022.md>
		"""
	elif modifier=="24":
		df = """
		[Artwork contract]
With the discovery that we can easily use spent boxes in contracts, some new features are introduced for artworks and can be extended furthur in the future. This EIP is an extension of Asset standard (EIP-0004) and tents to standardize artwrok issuance in particular: <https://github.com/ergoplatform/eips/blob/master/eip-0024.md>
		"""
	elif modifier=="25":
		df = """
		[URI scheme for payment requests]
Like BIP-0021 for Bitcoin, this EIP proposes a URI scheme for initiating payments. The purpose of this URI scheme is to enable users to easily make payments by simply clicking links on webpages or in e-mails: <https://github.com/ergoplatform/eips/blob/master/eip-0025.md>
		"""
	elif modifier=="27":
		df = """
		[Emission Retargeting Soft-Fork] 
This EIP concludes previous discussions and provides further details on the proposed emission soft-fork design and implementation: <https://github.com/ergoplatform/eips/blob/master/eip-0027.md>
		"""
	elif modifier=="37":
		df = """
		[Tweaking Difficulty Adjustment Algorithm]
The Ergo's algorithm works well in most cases, inluding huge price drops, 100x initial difficulty misestimation during mainnet launch, and so on. However, current simplified and limitless version of algorithm is bumpy. Big influx of mining hashrate over multiple epochs, especially with super-linear hashrate growth over time may result in huge spike of difficulty. Similarly, few slow epochs may cause huge drop. Also, for dapps and other applications it would be desirable to make difficulty readjustment more reactive (currently, readjustment takes place every 1024 blocks, and 8 epochs, so about two weeks normally, are considered).   

Read more of the initial draft at <https://github.com/ergoplatform/eips/pull/79/files>

EIP-37 discussions: <https://github.com/ergoplatform/eips/pull/79>
Broader conversations about difficulty adjustments: <https://www.ergoforum.org/t/diff-adjustment-potential-design-tradeoffs/3875>
		"""
	else: 
		df = """
		Ergo Improvement Proposals (EIPs) specify and/or describe standards for the Ergo Platform, including core protocol specifications, client APIs, dApp/contract standards, and other such things.
You can find the full list of EIPs at <https://github.com/ergoplatform/eips#ergo-improvement-proposals>

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




