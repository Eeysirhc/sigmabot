##############################
# Author: eeysirhc
# Description: Protocol
# Date written: 2022-08-25
# Last updated: 2022-09-26
# Bot commands: gensis, pouw, rent, staking
##############################

from discord.ext import commands


# GENESIS
def faq_genesis():
	df = """
	The Ergo genesis block was created on 1 July 2019. Prior to that, there was a different coin, EFYT. EFYT was a Waves token that was airdropped, not sold. ICOs cause issues as you're buying from a common enterprise directly - who likely have nothing to show yet so purely for expectations of profits. ERGs value derives from the popularity and utility of the platform + the co.
	"""
	return(df)

## POUW
def faq_pouw():
	df = """
	While Proof of Useful Work is an interesting idea, it is still in its research phase. Ergo is open to implementing new ideas. But, a radical change to its concensus mechanism that requires a hard fork would likely be outside the scope and resources of Ergo's small core development team and limited budget.
	"""
	return(df)

## STORAGE RENT
def faq_rent():
	df = """
	Storage rent is a fee for long term storage on the Ergo blockchain. Four years from your last transaction, you will be charged ~0.14 ERG and a transaction fee to pay for the costs of storing your digital information. Learn more at <https://ergoplatform.org/en/blog/2022-02-18-ergo-explainer-storage-rent/> and <https://docs.ergoplatform.com/mining/rent/>
	"""
	return(df)

# STAKING
def faq_staking():
	df = """
	Ergo is a Proof of Work blockchain. So, it is not possible to stake Ergo itself as you would in a Proof of Stake blockchain. However, it is possible to earn some yield from your ERG in combination with Ergo in liquidity pools, tokenisation of dApps, trading bots, lending platforms, and other mechanisms. Learn more here at <https://ergonaut.space/en/Guides/yield>
	"""
	return(df)


class Protocol(commands.Cog):
	def __init__(self, client):
		self.client = client 

	@commands.command()
	async def genesis(self, ctx):
		await ctx.send(faq_genesis())

	@commands.command()
	async def pouw(self, ctx):
		await ctx.send(faq_pouw())

	@commands.command()
	async def rent(self, ctx):
		await ctx.send(faq_rent())

	@commands.command()
	async def staking(self, ctx):
		await ctx.send(faq_staking())


def setup(client):
	client.add_cog(Protocol(client))

