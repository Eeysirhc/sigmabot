##############################
# Author: 
# Description: 
# Date written: 
# Last updated: 
# Bot commands: [list them here easier to reference in the future]
##############################

# https://stackoverflow.com/questions/62351392/load-extension-in-python-discordpy

from discord.ext import commands

# create your function(s)
def ztemplate_toast():
	df = """
	This is just a toast testing template but nothing to see here.
	"""
	return(df)

def ztemplate_roast():
	df = """
	Beef roast is good but this is just an example for multiple functions.
	"""
	return(df)

# rename "DevTemplate" cog to something unique
class DevTemplate(commands.Cog):
	def __init__(self, client):
		self.client = client 

# renmae toast/roast to the bot command and replace with appropriate function(s)
	@commands.command()
	async def toast(self, ctx):
		await ctx.send(ztemplate_toast())

	@commands.command()
	async def roast(self, ctx):
		await ctx.send(ztemplate_roast())

# reminder to change "DevTemplate" cog name to match above
async def setup(client):
	await client.add_cog(DevTemplate(client))


# final step
## update _sigmabot.py to include this file in the list of "cats"



