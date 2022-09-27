##############################
# Author: eeysirhc
# Description: Ecosystem
# Date written: 2022-08-25
# Last updated: 2022-09-26
# Bot commands: nfts, tokenjay, projects, node, graphql, nodelist
##############################

from discord.ext import commands


# NFTs
## need to fix this Ergo server times out the bot due to discord invite links (meant to prevent spam)
def faq_nfts(modifier=""):
	if modifier=="dis":
		df = """
		https://discord.gg/gYZxq38pJn
		"""
	elif modifier=="tg":
		df = """
		@ErgoNFTs
		"""
	elif modifier=="watches":
		df = """
		Watches are the NFTs of meat space.
		"""
	else:
		df = """
		@ErgoNFTs or https://discord.gg/gYZxq38pJn

Modifiers: `dis`, `tg`, `watches`
		"""
	return(df)

# TOKENJAY
def faq_tokenjay(modifier=""):
	if modifier=="mobile":
		df = """
		If you haven't already, download Ergo Mobile Wallet (Android) or Terminus Wallet (Apple) and restore seed. Go to Settings. Click on the button Mosaik plugins disabled and make it enabled. A new dApps will appear in the bottom navigation bar of the wallet. Click on dApps, then scroll to the bottom of new page. Click on AgeUSD Dashboard. Then, click the Exchange button for either SigUSD or SigRSV. Then select Buy/Sell from the pull down menu and the amount you want.
		"""
	elif modifier=="escrow":
		df = """
		The open P2P Escrow service is a smart contract that enables trustless, person-to-person (P2P), private sales on the Ergo blockchain for a small fee. The contract accepts Ergo tokens, such as a non-fungible token (NFT), 100 SigUSD, or other token(s) from the seller. Once in the contract, only a defined buyer sending a defined amount of ERG can access the token(s). If this happens, the contract sends the NFT, SigUSD or other token(s) to the buyer and the ERG to the seller. The seller can cancel the contract at any time before the exchange is made.
		"""
	elif modifier=="mosaik":
		df = """
		Mosaik is a JSON-based markup language served via a REST API intended to be used by Ergo platform dApps. For more information: <https://docs.ergoplatform.com/dev/stack/mosaik/intro/>
		"""
	else:
		df = """
		https://tokenjay.app

Modifiers: `mobile`, `escrow`, `mosaik`
		"""
	return(df)

# ERGO PROJECTS
## future: add categories as modifier (https://github.com/ergoplatform/sigmaverse/blob/master/config/categories.ts)
def faq_projects(modifier=""):
	if modifier=="mixer":
		df = """
		https://www.youtube.com/watch?v=DgztoNDFG8U
		"""
	elif modifier=="spectrum":
		df = """
		A DEX on Ergo, use either Nautilus or SAFEW wallets to access.
		https://app.spectrum.fi/
		"""
	elif modifier=="ergopad":
		df = """
		https://www.ergopad.io/
		"""
	elif modifier=="skyharbor":
		df = """
		https://www.skyharbor.io/
		"""
	elif modifier=="ergoauctions":
		df = """
		https://ergoauctions.org/
		"""
	elif modifier=="raffle":
		df = """
		https://ergoraffle.com/
		"""
	elif modifier=="sigmavalley":
		df = """
		https://www.sigmavalley.org/
		"""
	else:
		df = """
		Sigmaverse is the most comprehensive list of Ergo projects
		https://sigmaverse.io/

Modifiers: `mixer`, `spectrum`, `ergopad`, `skyharbor`, `ergoauctions`, `raffle`, `sigmavalley`
		"""
	return(df)


# NODE
def faq_node(modifier=""):
	if modifier=="install":
		df = """
		Instructions on how to setup a full Ergo node: https://www.youtube.com/watch?v=fpEDJ1CM6ns
		"""
	elif modifier=="docs":
		df = """
		<https://docs.ergoplatform.com/node/install/>
		"""
	else:
		df = """
		<https://github.com/ergoplatform/ergo>

Modifiers: `install`, `docs`
		"""
	return(df)



# GRAPHQL
def faq_graphql():
	df = """
	GraphQL runs on top of Ergo Explorer and allows for faster access to blockchain information. If you are having trouble connecting from the main instance, try one of the alternatives.

Main GraphQL instance: <https://ergo-explorer.getblok.io/graphql/>

Alternative instances:
<https://ergo-explorer.getblok.io/graphql/>
<https://graphql.erg.zelcore.io>
<https://explore.sigmaspace.io/api/graphql>
		"""
	return(df)

# NODELIST
def faq_nodelist():
	df = """
	Lists of alternative nodes:
<http://ergonodes.net/list>
<https://api.tokenjay.app/peers/list?unreachable=false&limit=50>
		"""
	return(df)



class Ecosystem(commands.Cog):
	def __init__(self, client):
		self.client = client 

	@commands.command()
	async def nfts(self, ctx, modifier=""):
		modifier = modifier.lower()
		response = faq_nfts(modifier)
		await ctx.send(response)

	@commands.command()
	async def tokenjay(self, ctx, modifier=""):
		modifier = modifier.lower()
		response = faq_tokenjay(modifier)
		await ctx.send(response)

	@commands.command()
	async def projects(self, ctx, modifier=""):
		modifier = modifier.lower()
		response = faq_projects(modifier)
		await ctx.send(response)

	@commands.command()
	async def node(self, ctx, modifier=""):
		modifier = modifier.lower()
		response = faq_node(modifier)
		await ctx.send(response)

	@commands.command()
	async def graphql(self, ctx):
		await ctx.send(faq_graphql())

	@commands.command()
	async def nodelist(self, ctx):
		await ctx.send(faq_nodelist())


def setup(client):
	client.add_cog(Ecosystem(client))


