##############################
# Author: eeysirhc
# Date written: 2022-08-25
# Last updated: 2022-09-01
##############################

# HELP
def faq_halp():
	df = """
	.welcome 
.geterg: modifies with "dex" and "cex"
.wallets: modifies with "dis", "tg", and "cold"
.mining: modifies with "dis" and "tg" channel links
.projects: valid input with "mixer" as modifier with more to come
	"""
	return(df)

# WELCOME
def faq_welcome():
	df = """
	https://youtu.be/CzGqYAlQRWQ
	"""
	return(df)

# GET $ERG
def faq_geterg(modifier=""):
	if modifier=="dex":
		df = """
		https://app.spectrum.fi/ergo/swap
		"""
	elif modifier=="cex":
		df = """
		GateIO: https://www.gate.io/trade/ERG_USDT
KuCoin: https://www.kucoin.com/trade/ERG-USDT
CoinEx: https://www.coinex.com/exchange?currency=usdt&dest=erg
TradeOgre: https://tradeogre.com/exchange/BTC-ERG
Indodax: https://indodax.com/
HotBit: https://www.hotbit.io/exchange?symbol=ERG_BTC
Bisq: https://www.ergoforum.org/t/bisq-v1-1-6-has-been-released-with-support-for-ergo/88
swop.fi: https://swop.fi/info/3PGVJvV8Ep1u7qMkvUs1DYhRyfvArdRbMsD
FMFW.io: https://fmfw.io/erg-to-btc
Changelly: https://changelly.com/
Changelly PRO: https://pro.changelly.com/
		"""
	else:
		df = """
		https://ergoplatform.org/en/get-erg/
		"""
	return(df)

# WALLETS
def faq_wallets(modifier=""):
	if modifier=="dis":
		df = """
		#🚧│wallets
		"""
	elif modifier=="tg":
		df = """
		@NautilusWallet
@ErgoWalletApp
@SatergoWallet
		"""
	elif modifier=="cold":
		df = """
		https://www.youtube.com/watch?v=7q3Jq_OvhKY
		"""
	else:
		df = """
		https://ergoplatform.org/en/get-erg/#Wallets
		"""
	return(df)

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
	else:
		df = """
		https://ergoplatform.org/en/get-erg/#Mining
		"""
	return(df)

# ERGO PROJECTS 
## future: add categories as modifier (https://github.com/ergoplatform/sigmaverse/blob/master/config/categories.ts)
def faq_projects(modifier=""):
	if modifier=="mixer":
		df = """
		https://www.youtube.com/watch?v=DgztoNDFG8U
		"""
	else:
		df = """
		https://sigmaverse.io/
		"""
	return(df)


