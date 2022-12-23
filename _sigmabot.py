import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import logging.handlers
import asyncio

load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')

# https://stackoverflow.com/questions/68581659/i-want-my-bot-to-process-commands-sent-by-other-bots

class UnfilteredBot(commands.Bot):
	async def process_commands(self, message):
		ctx = await self.get_context(message)
		await self.invoke(ctx)

# CONFIG
intents = discord.Intents().all()
client = UnfilteredBot(command_prefix=".", intents=intents)
TOKEN = os.getenv("DISCORD_TOKEN")

# EVENT, BOT STATUS
@client.event
async def on_ready():
	print("Logged in as {0.user}".format(client))
	await client.change_presence(activity=discord.Game("on the Rosen Bridge"))

# Load cogs
async def load_extensions():
	for filename in os.listdir("./cogs"):
		if filename.endswith(".py"):
			# cut off the .py from the file name
			await client.load_extension(f'cogs.{filename[:-3]}')

# Logging, cribbed from:
# https://discordpy.readthedocs.io/en/stable/logging.html
# Filter to dot commands: $grep -E "content': '\." discord.log
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='a')
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

async def main():
	async with client:
		await load_extensions()
		# None, due to handling logs in previous section
		await client.start(TOKEN)

asyncio.run(main())
