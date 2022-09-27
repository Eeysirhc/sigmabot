##############################
# Author: eeysirhc
# Description: Mining
# Date written: 2022-08-25
# Last updated: 2022-09-26
# Bot commands: mining, difficulty
##############################

from discord.ext import commands


# MINING
def faq_mining(modifier=""):
	if modifier=="dis":
		df = """
		#🚧│mining
		"""
	elif modifier=="tg":
		df = """
		@Ergo_Mining
@GetBlok
@GuapSwapCommunity
		"""
	elif modifier=="red":
		df = """
		<https://www.reddit.com/r/erg_miners/>
		"""
	elif modifier=="profit":
		df = """
		With the Ethereum merge, 95% of the market for miners just got rugged. Imagine an economy where 95% of workers get laid off and take their tools home. It is going to take time for mining hash rate to balance out.
		"""
	else:
		df = """
		Welcome new miners! Remember to spread out the hashrate to support decentralization.

Learn more at <https://ergoplatform.org/en/get-erg/#Mining>

[Sub-Mining Pools]
With GetBlok you can mine Ergo or native tokens such as Neta, Ergopad or Comet: <https://ergo.getblok.io/>

Modifiers: `dis`, `tg`, `red`
		"""
	return(df)

# MINING DIFFICULTY ADJUSTMENT
def faq_difficulty():
	df = """
	Ergo's difficulty algorithm was designed to reduce the incentive to perform coin-hopping and improve stability of inter-block delays. Coin-hopping is defined as an adversarial miner switching from mining one coin to another in the beginning of an epoch then switching back in the beginning of next epoch when difficulty becomes lower. Difficulty in Ergo is adjusted using the least squares method, which adjusts roughly every 34 hrs using the past eight epochs (8 epochs=⁓11 days), to obtain the target block interval of 120 seconds or 2 minutes, on average.

Learn more: <https://eprint.iacr.org/2017/731.pdf>
For Ergo Forum discussion: <https://www.ergoforum.org/t/diff-adjustment-potential-design-tradeoffs/3875>
For EIP-37 GitHub discussion: <https://github.com/ergoplatform/eips/pull/79>
Difficulty statistics: <https://cds.oette.info/ergo_diff.htm>
	"""
	return(df)





class Mining(commands.Cog):
	def __init__(self, client):
		self.client = client 

	@commands.command()
	async def mining(self, ctx, modifier=""):
		modifier = modifier.lower()
		response = faq_mining(modifier)
		await ctx.send(response)

	@commands.command()
	async def difficulty(self, ctx):
		await ctx.send(faq_difficulty())


def setup(client):
	client.add_cog(Mining(client))


