##############################
# Author: eeysirhc
# Description: Easter Eggs
# Date written: 2022-08-25
# Last updated: 2022-10-13
# Bot commands: wen, why, drama, gulag
##############################

from discord.ext import commands

##### WEN #####
listing_template = "Ergo will be listed on {cex} when enough of its customers want it. Additionally, the team can never give specifics about a listing until the exchange announces it. Listings are covered by a Non-Disclosure Agreement (NDA) and leaks put the listing itself at risk. Just keep your eyes on social media for the announcements."

wen_responses = {
"coinbase": listing_template,

"binance": """While Binance is, in fact, the largest exchange in the world, Ergo is only a few years old and step by step has been achieving all its goals, so eventually, sooner or later, they will inevitably list Ergo.""",

"kraken": listing_template,

"ftx": listing_template,

"tier1": """Armeanio is already in contact with most exchanges. Listing agents are in the chat every day. The only information that can be provided is that there are ongoing discussions, and announcements will be made by the exchanges themselves. If you just want listing for price pump, better to keep discussions in @ErgoTrading.""",

"lambo": """VROOM VROOM""",

"yacht": """I'm on a boat!""",

"bridge": """An einstein rosen bridge? More like a Rainbow Bridge!""",

}

def eggs_wen(modifier=""):
	if modifier in wen_responses:
		try:
			cex = modifier.title()
			df = wen_responses[modifier].format(cex=cex)
		except:
			df = wen_responses[modifier]
	else: 
		df = """Modifiers: `coinbase`, `binance`, `kraken`, `ftx`, `tier1`, `lambo`, `yacht`, `bridge`"""
	return(df)



##### WHY #####
why_responses = {
"pow": """Every blockchain solution requires a careful consideration of costs, benefits and risks. Blockchains are a big tent. There is room for everyone. However, PoW NIPoPows and chain-specific features like storage rent offers unique functionality that can be worth the extra energy expenditure of PoW for some blockchain uses.

Learn more at <https://ergoplatform.org/en/blog/2022-03-29-proof-of-work-energy-and-ergo/>""",

"change": """To absorb more fundamental changes, Ergo follows the approach of soft-forkability that allows changing the protocol significantly while keeping old nodes operational. At the beginning of an epoch, a miner can also propose to vote for a more fundamental change (e.g., adding a new instruction to ErgoScript) describing affected validation rules. Voting for such breaking changes continues for 32,768 blocks and requires at least 90%  votes to be accepted. Once being accepted, a 32,768-blocks long activation period starts to give outdated nodes time to update their software version. If a node software is still not updated after the activation period, then it skips the specified checks but continues to validate all the known rules. List of previous soft-fork changes is recorded into the extension to allow light nodes of any software version to join the network and catch up to the current validation rules. A combination of soft-forkability with the voting protocol allows changing of almost all the parameters of the network except the PoW rules that are responsible for the voting itself."

From the Ergo white paper, pg 10: <https://storage.googleapis.com/ergo-cms-media/whitepaper_668cb39ee5/whitepaper_668cb39ee5.pdf>"""

}

def eggs_why(modifier=""):
	if modifier in why_responses:
		df = why_responses[modifier]
	else: 
		df = """Why what?

Modifiers: `pow`, `change`"""
	return(df)


##### DRAMA #####
def eggs_drama():
	df = """
	Pretend to be nice, please.
	"""
	return(df)

##### GULAG #####
def eggs_gulag():
	df = """
	This chat is for serious discussion. If you want to troll users and share your spicy opinions, please join our community of Ergo edgelords in @ErgoGulag in Telegram or #🚧│random in Discord.
	"""
	return(df)

class EasterEggs(commands.Cog):
	def __init__(self, client):
		self.client = client 

	@commands.command()
	async def wen(self, ctx, modifier=""):
		modifier = modifier.lower()
		response = eggs_wen(modifier)
		await ctx.send(response)

	@commands.command()
	async def why(self, ctx, modifier=""):
		modifier = modifier.lower()
		response = eggs_why(modifier)
		await ctx.send(response)

	@commands.command()
	async def drama(self, ctx):
		await ctx.send(eggs_drama())

	@commands.command()
	async def gulag(self, ctx):
		await ctx.send(eggs_gulag())


def setup(client):
	client.add_cog(EasterEggs(client))

