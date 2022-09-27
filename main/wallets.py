##############################
# Author: eeysirhc
# Description: Wallets
# Date written: 2022-08-25
# Last updated: 2022-09-26
# Bot commands: wallets, ledger, yoroi, seed, tipbot
##############################

from discord.ext import commands

# WALLETS
def faq_wallets(modifier=""):
	if modifier=="dis":
		df = """
		#🚧│wallets
		"""
	elif modifier=="tg":
		df = """
		@NautilusWallet - web browser extension wallet
@ErgoWalletApp - mobile wallet
@SatergoWallet - full node desktop wallet
		"""
	elif modifier=="cold":
		df = """
		In this tutorial you will find instructions on how to install the cold mobile wallet: https://www.youtube.com/watch?v=7q3Jq_OvhKY
		"""
	else:
		df = """
		[Team Wallets]
Ergo Node: <https://docs.ergoplatform.com/node/install/>
Ergo Mobile: <https://ergoplatform.org/en/mobile-wallets/>
Paper Wallet: <https://ergopaperwallet.org/>

[Other Wallets]
Minotaur (Multi Platform): <https://github.com/minotaur-ergo/minotaur-wallet>
Nautilus (Web): <https://github.com/capt-nemo429/nautilus-wallet>
Satergo (Desktop): <https://satergo.com/>
SAFEW (Web): <https://github.com/ThierryM1212/SAFEW>
Zelcore (Multi Platform): <https://zelcore.io/>

Learn more at <https://ergoplatform.org/en/get-erg/#Wallets>

Modifiers: `dis`, `tg`, `cold`
		"""
	return(df)

# LEDGER
def faq_ledger():
	df = """
	Tutorials to sideload Ergo Ledger app

Nano S for Windows: <https://github.com/anon-br/ledger-ergo-js/blob/master/docs/ledger-app-installing-windows.md>

Nano S for Linux/MacOS: <https://github.com/anon-br/ledger-ergo-js/blob/master/docs/ledger-app-installing-unix.md>

Nano S Plus: <https://medium.com/@koutelier/how-to-sideload-ergo-ledger-app-to-nano-s-nano-s-plus-on-linux-fafb2380508a>
	"""
	return(df)

# YOROI
def faq_yoroi():
	df = """
	What are you, some sort of cave person living under a rock? Use a wallet listed here: https://ergoplatform.org/en/get-erg/#Wallets
	"""
	return(df)

# SEED
def faq_seed():
	df = """
	Never give your seed phrase to anyone. You can restore your seed in any wallet, even multiple wallets. With the correct seed, you (and anyone else) can access your assets on the Ergo blockchain.
	"""
	return(df)

# TIPBOT
def faq_tipbot(modifier=""):
	if modifier=="dis":
		df = """
		To initialize a Discord wallet, message /start to @Ergo Tipper Bot[BETA]#0902.
		"""
	elif modifier=="reddit":
		df = """
		To initialize a Reddit wallet. message !start to /u/ErgoTipperBot.
		"""
	elif modifier=="tg":
		df = """
		To initialize a Telegram wallet, message /start to @ergotipperbot.
		"""
	elif modifier=="twitter":
		df = """
		To initalize a Twitter wallet, message !start to @ErgoTipperBot.
		"""
	else:
		df = """
		Ergo's Tipper Bot can be setup on Discord, Reddit, Telegram and Twitter. You can initialize a tip wallet by messaging the tipbot on each platform.

Platform | Message | Bot Name
=============================
Discord  | /start  | @Ergo Tipper Bot[BETA]#0902
Reddit   | !start  | ErgoTipperBot
Telegram | /start  | @ergotipperbot
Twitter  | !start  | @ErgoTipperBot

Pro-Tip: If you restore the same wallet into each service, you can use the same tip wallet across platforms.

Modifiers: `dis`, `reddit`, `tg`, `twitter`
		"""
	return(df)



class Wallets(commands.Cog):
	def __init__(self, client):
		self.client = client 

	@commands.command()
	async def wallets(self, ctx, modifier=""):
		modifier = modifier.lower()
		response = faq_wallets(modifier)
		await ctx.send(response)

	@commands.command()
	async def ledger(self, ctx):
		await ctx.send(faq_ledger())

	@commands.command()
	async def yoroi(self, ctx):
		await ctx.send(faq_yoroi())

	@commands.command()
	async def seed(self, ctx):
		await ctx.send(faq_seed())

	@commands.command()
	async def tipbot(self, ctx, modifier=""):
		modifier = modifier.lower()
		response = faq_tipbot(modifier)
		await ctx.send(response)


def setup(client):
	client.add_cog(Wallets(client))



