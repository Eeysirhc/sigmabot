##############################
# Author: eeysirhc
# Description: Exchange
# Date written: 2022-08-25
# Last updated: 2022-09-27
# Bot commands: dex, cex
##############################

from discord.ext import commands



##### DEX #####
def exchange_dex():
	df = """
	<https://app.spectrum.fi/ergo/swap>
	"""
	return(df)

##### CEX #####
def exchange_cex():
	df = """
	[KYC]
Huobi: <https://www.huobi.com/exchange/erg_usdt/>
GateIO: <https://www.gate.io/trade/ERG_USDT>
Indodax: <https://indodax.com/market/ERGIDR>
HotBit: <https://www.hotbit.io/exchange?symbol=ERG_BTC>
FMFW: <https://fmfw.io/erg-to-btc>
Changelly: <https://changelly.com/exchange/erg>
swopfi: <https://swop.fi/info/3PGVJvV8Ep1u7qMkvUs1DYhRyfvArdRbMsD>

[non-KYC]
KuCoin: <https://www.kucoin.com/trade/ERG-USDT>
CoinEx: <https://www.coinex.com/exchange?currency=usdt&dest=erg>
TradeOgre: <https://tradeogre.com/exchange/BTC-ERG>
	"""
	return(df)



class Exchanges(commands.Cog):
	def __init__(self, client):
		self.client = client 

	@commands.command()
	async def dex(self, ctx):
		await ctx.send(exchange_dex())

	@commands.command()
	async def cex(self, ctx):
		await ctx.send(exchange_cex())


async def setup(client):
	await client.add_cog(Exchanges(client))




