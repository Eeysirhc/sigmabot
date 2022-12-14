##############################
# Author: eeysirhc
# Description: Mining
# Date written: 2022-08-25
# Last updated: 2022-12-26
# Bot commands: mining, difficulty
##############################

from discord.ext import commands


##### MINING #####
mining_responses = {
"dis": """#🚧│mining""",

"tg": """@Ergo_Mining
@GuapSwapCommunity""",

"red": """<https://www.reddit.com/r/erg_miners/>""",

"profit": """With the Ethereum merge, 95% of the market for miners just got rugged. Imagine an economy where 95% of workers get laid off and take their tools home. It is going to take time for mining hash rate to balance out."""
}


def faq_mining(modifier=""):
	if modifier in mining_responses:
		df = mining_responses[modifier]
	else: 
		df = """Welcome new miners! Remember to spread out the hashrate to support decentralization.

Learn more at <https://ergoplatform.org/en/get-erg/#Mining>

Modifiers: `dis`, `tg`, `red`"""
	return(df)

##### MINING DIFFICULTY ADJUSTMENT #####
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


async def setup(client):
	await client.add_cog(Mining(client))


