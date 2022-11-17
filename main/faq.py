##############################
# Author: eeysirhc
# Description: Basic Frequently Asked Questions
# Date written: 2022-08-25
# Last updated: 2022-11-16
# Bot commands: welcome, tps, marketcap, docs, manifesto, admin, contribute, bots, forum, partnerships 
##############################

from discord.ext import commands

##### WELCOME #####
def faq_welcome():
	df = """
	Welcome Ergonauts, in this video you can learn more about Ergo: https://youtu.be/CzGqYAlQRWQ
	"""
	return(df)


##### TRANSACTIONS #####
def faq_tps():
	df = """
	TPS (Transactions Per Second) is not a useful metric. On Ergo Reference Node v.5, TPS is estimated to be a minimum of 47.5 tx/s. However, transactions can happen in three scaling layers or levels:

L0: Ergo Reference Nodes, which can be bootstrapped using NiPoPoWs proofs and UTXO set snapshots.
L1: Ergo has extensions that allow for a wide variety of scaling solutions such as Sharding, Hydra, or BitcoinNG-style macroblocks.
L2 (off-chain): Ergo should be compatible with the Lightning Network, Rainbow Network, and many more. The implementation here will depend on the needs of the applications being built on Ergo.

The general idea is that many transactions can happen in L1 or L2 and these transactions can be bundled and settled on the L0 layer of the Ergo blockchain using a single transaction. Thanks to the high flexibility of ErgoScript programming model, many different protocols are possible, each one solving scalability problem in a specific domain (like simple payment transactions).

Ergo blockchain can be thought as common settlement layer for many L1/L2 protocols and applications.
	"""
	return(df)


##### MARKET CAPITALIZATION #####
def faq_marketcap():
	df = """
	Ergo Explorer displays circulating supply and max supply (97,739,924 ERG). Multiply these amounts by current price to get Ergo's market capitalization. Do not rely on Coinmarketcap data. ERGs value derives from the popularity and utility of the platform + the cost of mining erg.

	https://explorer.ergoplatform.com/
	"""
	return(df)


##### DOCS #####
def faq_docs():
	df = """
	<https://docs.ergoplatform.com/documents/>
	"""
	return(df)

##### ERGO MANIFESTO #####
def faq_manifesto():
	df = """
	The Ergo Manifesto hopes to educate and offer a vision of what blockchain technology can achieve. We hope to build society through horizontal cooperation through production under the division of labor, trade and exchange, and solidarity and mutual aid. Learn more at <https://ergoplatform.org/en/blog/2021-04-26-the-ergo-manifesto/>
	"""
	return(df)

##### ADMIN #####
def faq_admin():
	df = """
	For technical support on Telegram please join @ErgoSupport
Email team@ergoplatform.org for business inquiries
For marketing queries please email angie@ergoplatform.org
	"""
	return(df)


##### CONTRIBUTE #####
def faq_contribute():
	df = """
	<https://docs.ergoplatform.com/contribute/>
	"""
	return(df)


##### BOTS #####
def faq_bots():
	df = """
	Beep Boop - don't worry, Human...the bots are just Discord <-> Telegram carrier pigeons (message bridge).
	"""
	return(df)


##### FORUM #####
def faq_forum():
	df = """
	Telegram and Discord are for informal discussion. Ergo's Community Forum is preferred for formal discussion of ecosystem development, hard forks (such as a mining difficulty adjustment) and soft forks (emission retargeting), and so forth. The Forum provides a means for the community to develop and comment on ideas that can be turned into Ergo Improvement Proposals (EIPs). EIPs are voted upon by the larger community before being implemented. Anyone can contribute to the forum or submit an EIP, and the Ergo community is open to ideas from anyone.

Links
<https://www.ergoforum.org/>
<https://github.com/ergoplatform/eips>
	"""
	return(df)


##### PARTNERSHIPS #####
def faq_partnerships():
	df = """
	The Ergo team welcomes partnerships. However, it is helpful to see and have Ergo's engineers understand partner code first. Projects without code are hard to distinquish from mere marketing. Ergo's focus is on engineering. Please contact team@ergoplatform.org when you are ready to share your code with Ergo's developers.
	"""
	return(df)

##### BRIDGE #####
def faq_bridge():
	df = """
	In cryptocurrencies, bridges move assets from one cryptocurrency blockchain to another. The two most frequently discussed on Ergo are Rosen Bridge and AnetaBTC.

Rosen Bridge video: <https://www.youtube.com/watch?v=Xsiy-yPJQ6w>
Rosen Bridge compared to Interlay bridges: <https://medium.com/@anetaBTC/rosen-bridge-vs-interlay-an-analysis-on-wrapping-bitcoin-c9ae84da0e9d>
	"""
	return(df)

#### SOCIALS #####
def faq_socials():
	df = """
	Ergo Telegram groups: <https://t.me/Ergo_Chats>
On Discord, select #rules and select a role to see relevant channels.
	"""
	return(df)


class FrequentQuestions(commands.Cog):
	def __init__(self, client):
		self.client = client 

	@commands.command()
	async def welcome(self, ctx):
		await ctx.send(faq_welcome())

	@commands.command()
	async def tps(self, ctx):
		await ctx.send(faq_tps())

	@commands.command()
	async def marketcap(self, ctx):
		await ctx.send(faq_marketcap())

	@commands.command()
	async def docs(self, ctx):
		await ctx.send(faq_docs())

	@commands.command()
	async def manifesto(self, ctx):
		await ctx.send(faq_manifesto())

	@commands.command()
	async def admin(self, ctx):
		await ctx.send(faq_admin())

	@commands.command()
	async def contribute(self, ctx):
		await ctx.send(faq_contribute())

	@commands.command()
	async def bots(self, ctx):
		await ctx.send(faq_bots())

	@commands.command()
	async def forum(self, ctx):
		await ctx.send(faq_forum())

	@commands.command()
	async def partnerships(self, ctx):
		await ctx.send(faq_partnerships())

	@commands.command()
	async def bridge(self, ctx):
		await ctx.send(faq_bridge())

	@commands.command()
	async def socials(self,ctx):
		await ctx.send(faq_socials())

def setup(client):
	client.add_cog(FrequentQuestions(client))




