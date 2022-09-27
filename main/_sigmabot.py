##############################
# Author: eeysirhc
# Date written: 2022-08-12
# Last updated: 2022-09-26
##############################

# LOAD PYTHON MODULES
import os
from dotenv import load_dotenv
load_dotenv()

import discord
from discord.ext import commands

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


cats = ["ztemplate", "eip", "eastereggs", "wallets", "exchange", "mining", "protocol", "ecosystem", "faq"]

if __name__ == "__main__":
	for cat in cats:
		client.load_extension(cat)






# EXECUTE
client.run(TOKEN)



