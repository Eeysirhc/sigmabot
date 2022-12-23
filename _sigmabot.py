import os
from dotenv import load_dotenv
load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')

import discord
from discord.ext import commands

import asyncio

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

async def load_extensions():
	for filename in os.listdir("./cogs"):
		if filename.endswith(".py"):
			# cut off the .py from the file name
			await client.load_extension(f'cogs.{filename[:-3]}')

async def main():
	async with client:
		await load_extensions()
		await client.start(TOKEN)

asyncio.run(main())