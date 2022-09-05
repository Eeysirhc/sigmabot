##############################
# Author: eeysirhc
# Date written: 2022-08-25
# Last updated: 2022-09-05
##############################

# WELCOME
def faq_welcome():
	df = """
	Welcome Ergonauts, in this video you can learn more about Ergo: https://youtu.be/CzGqYAlQRWQ
	"""
	return(df)

# GET $ERG
def faq_geterg():
	df = """
	https://ergoplatform.org/en/get-erg/
	"""
	return(df)

# DEX
def faq_dex():
	df = """
	https://app.spectrum.fi/ergo/swap
	"""
	return(df)

# CEX
def faq_cex():
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
		In this tutorial you will find instructions on how to install the cold mobile wallet: https://www.youtube.com/watch?v=7q3Jq_OvhKY
		"""
	else:
		df = """
		https://ergoplatform.org/en/get-erg/#Wallets

Modifiers: dis, tg, cold
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

Modifiers: dis, tg
		"""
	return(df)

# LISTING
## future: cut down repetition by adding lookup list, if exists, then string interpolation response
def faq_listing(modifier=""):
	if modifier=="binance":
		df = """
		Ergo will be listed on Binance when its customers want it.
		"""
	elif modifier=="coinbase":
		df = """
		Ergo will be listed on Coinbase when its customers want it.
		"""
	elif modifier=="kraken":
		df = """
		Ergo will be listed on Kraken when its customers want it.
		"""
	elif modifier=="ftx":
		df = """
		Ergo will be listed on FTX when its customers want it.
		"""
	elif modifier=="tier1":
		df = """
		Armeanio is already in contact with most exchanges. Listing agents are in the chat every day. The only information that can be provided is that there are ongoing discussions, and announcements will be made by the exchanges themselves. If you just want listing for price pump, betterto keep discussion in @ErgoTrading.
		"""
	else:
		df = """ 
		The team can never give specifics about a listing until the exchange announces it. Listings are covered by a Non-Disclosure Agreement (NDA) and leaks put the listing itself at risk. Just keep your eyes on socials when it is announced you will see.  
		"""
	return(df)

# WEN BINANCE
def faq_binance():
	df = """
	Ergo will be listed on Binance when its customers want it.
	"""
	return(df)

# TRANSACTIONS
def faq_tps():
	df = """
	Ergo's TPS (Transactions per second) on the version 5 Node TPS is estimated to be a minimum of 47.5tx/s. There are three scaling layers or levels: L0: Ergo nodes, which can be bootstrapped using NiPoPoWs proofs and UTXO set snapshots are planned. L1: Ergo has an extension section in its code that allows the implementation of a wide variety of scaling solutions such as Sharding, Hydra, or BitcoinNG-style macroblocks. L2 (off-chain): Ergo should be compatible with the Lightning Network, Rainbow Network, and many more. The implementation here will depend on the needs of the applications being built on Ergo.

The general idea, roughtly, is that large chunks of transactions can happen in layer 2 and the whole chunks will be settled in Ergo blockchain using single transaction. Thanks to the high flexibility of ErgoScript programming model, many different protocols will be possible on layer2, each one solving scalability problem in a specific domain (like simple payment transactions).

Thus, Ergo blockchain can be thought as common settlement layer for many L2 protocols and applications.    
	"""
	return(df)

# MARKET CAPITALIZATION
def faq_marketcap():
	df = """
	Ergo Explorer displays circulating supply and max supply (97,739,924 ERG). Multiply these amounts by current price to get Ergo's market capitalization. Coinmarketcap displays incorrect data and should not be relied upon.
	"""
	return(df)

# GENESIS
def faq_genesis():
	df = """
	Ergo genesis block was 1 July 2019. Prior to that, there was a different coin, EFYT. EFYT was a Waves token that was airdropped, not sold. ICOs cause issues as you're buying from a common enterprise directly - who likely have nothing to show yet so purely for expectations of profits. ERGs value derives from the popularity and utility of the platform + the cost of mining erg.
	"""
	return(df)

# TOKENJAY
def faq_tokenjay(modifier=""):
	if modifier=="mobile":
		df = """
		If you haven't already, download Ergo Mobile Wallet (Android) or Terminus Wallet (Apple) and restore seed. Go to Settings. Click on the button Mosaik plugins disabled and make it enabled. A new dApps will appear in the bottom navigation bar of the wallet. Click on dApps, then scroll to the bottom of new page. Click on AgeUSD Dashboard. Then, click the Exchange button for either SigUSD or SigRSV. Then select Buy/Sell from the pull down menu and the amount you want.
		"""
	elif modifier=="escrow":
		df = """
		The open P2P Escrow service is a smart contract that enables trustless, person-to-person (P2P), private sales on the Ergo blockchain for a small fee. The contract accepts Ergo tokens, such as a non-fungible token (NFT), 100 SigUSD, or other token(s) from the seller. Once in the contract, only a defined buyer sending a defined amount of ERG can access the token(s). If this happens, the contract sends the NFT, SigUSD or other token(s) to the buyer and the ERG to the seller. The seller can cancel the contract at any time before the exchange is made.
		"""
	elif modifier=="mosaik":
		df = """
		Mosaik is a JSON-based markup language served via a REST API intended to be used by Ergo platform dApps. For more information: https://docs.ergoplatform.com/dev/stack/mosaik/intro/ 
		"""
	else:
		df = """
		https://tokenjay.app

Modifiers: mobile, escrow, mosaik
		"""
	return(df)

# ERGO PROJECTS 
## future: add categories as modifier (https://github.com/ergoplatform/sigmaverse/blob/master/config/categories.ts)
def faq_projects(modifier=""):
	if modifier=="mixer":
		df = """
		https://www.youtube.com/watch?v=DgztoNDFG8U
		"""
	elif modifier=="spectrum":
		df = """
		https://app.spectrum.fi/
		"""
	elif modifier=="ergopad":
		df = """
		https://www.ergopad.io/
		"""
	elif modifier=="skyharbor":
		df = """
		https://www.skyharbor.io/
		"""
	elif modifier=="ergoauctions":
		df = """
		https://ergoauctions.org/
		"""
	elif modifier=="raffle":
		df = """
		https://ergoraffle.com/
		"""
	elif modifier=="sigmavalley":
		df = """
		https://www.sigmavalley.org/
		"""
	else:
		df = """
		https://sigmaverse.io/
		"""
	return(df)

# DOCS
def faq_docs():
	df = """
	https://docs.ergoplatform.com/documents/
	"""
	return(df)

# ERGO MANIFESTEO
def faq_manifesto():
	df = """
	https://ergoplatform.org/en/blog/2021-04-26-the-ergo-manifesto/
	"""
	return(df)

# ADMIN
def faq_admin():
	df = """
	For technical support please join @ErgoSupport
For marketing queries please email angie@ergoplatform.org
	"""
	return(df)

# LEDGER
def faq_ledger():
	df = """
	Tutorials to sideload Ergo Ledger app

Nano S for Windows: https://github.com/anon-br/ledger-ergo-js/blob/master/docs/ledger-app-installing-windows.md
Nano S for Linux/MacOS: https://github.com/anon-br/ledger-ergo-js/blob/master/docs/ledger-app-installing-unix.md

Nano S Plus: https://medium.com/@koutelier/how-to-sideload-ergo-ledger-app-to-nano-s-nano-s-plus-on-linux-fafb2380508a
	"""
	return(df)

# NODE
def faq_node(modifier=""):
	if modifier=="install":
		df = """
		Instructions on how to setup a full Ergo node: https://www.youtube.com/watch?v=fpEDJ1CM6ns
		"""
	elif modifier=="docs":
		df = """
		https://docs.ergoplatform.com/node/install/
		"""
	else:
		df = """
		https://github.com/ergoplatform/ergo

Modifiers: install, docs
		"""
	return(df)
