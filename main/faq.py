##############################
# Author: eeysirhc
# Date written: 2022-08-25
# Last updated: 2022-09-20
##############################

# WELCOME
def faq_welcome():
	df = """
	Welcome Ergonauts, in this video you can learn more about Ergo: https://youtu.be/CzGqYAlQRWQ
	"""
	return(df)

# DEX
def faq_dex():
	df = """
	<https://app.spectrum.fi/ergo/swap>
	"""
	return(df)

# CEX
def faq_cex():
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

# WALLETS
def faq_wallets(modifier=""):
	if modifier=="dis":
		df = """
		#🚧│wallets
		"""
	elif modifier=="tg":
		df = """
		@NautilusWallet - web browser extension wallet
@ErgoWalletApp - mobile wallet
@SatergoWallet - full node desktop wallet
		"""
	elif modifier=="cold":
		df = """
		In this tutorial you will find instructions on how to install the cold mobile wallet: https://www.youtube.com/watch?v=7q3Jq_OvhKY
		"""
	else:
		df = """
		[Team Wallets]
Ergo Node: <https://docs.ergoplatform.com/node/install/>
Ergo Mobile: <https://ergoplatform.org/en/mobile-wallets/>
Paper Wallet: <https://ergopaperwallet.org/>

[Other Wallets]
Minotaur (Multi Platform): <https://github.com/minotaur-ergo/minotaur-wallet>
Nautilus (Web): <https://github.com/capt-nemo429/nautilus-wallet>
Satergo (Desktop): <https://satergo.com/>
SAFEW (Web): <https://github.com/ThierryM1212/SAFEW>

Learn more at <https://ergoplatform.org/en/get-erg/#Wallets>

Modifiers: `dis`, `tg`, `cold`
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
	elif modifier=="red":
		df = """
		<https://www.reddit.com/r/erg_miners/>
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

# WEN
## future: probably tidy up the DRY a bit more
def faq_wen(modifier=""):
	listing_template = "Ergo will be listed on {cex} when enough of its customers want it. Additionally, the team can never give specifics about a listing until the exchange announces it. Listings are covered by a Non-Disclosure Agreement (NDA) and leaks put the listing itself at risk. Just keep your eyes on social media for the announcements."
	if modifier=="coinbase":
		cex = modifier.title()
		df = listing_template.format(cex=cex)
	elif modifier=="binance":
		cex = modifier.title()
		df = listing_template.format(cex=cex)
	elif modifier=="kraken":
		cex = modifier.title()
		df = listing_template.format(cex=cex)
	elif modifier=="ftx":
		cex = modifier.upper()
		df = listing_template.format(cex=cex)
	elif modifier=="tier1":
		df = """
		Armeanio is already in contact with most exchanges. Listing agents are in the chat every day. The only information that can be provided is that there are ongoing discussions, and announcements will be made by the exchanges themselves. If you just want listing for price pump, better to keep discussions in @ErgoTrading.
		"""
	elif modifier=="lambo":
		df = """
		VROOM VROOM
		"""
	elif modifier=="yacht":
		df = """
		I'm on a boat!
		"""
	elif modifier=="bridge":
		df = """
		An einstein rosen bridge? More like a Rainbow Bridge!
		"""
	else:
		df = """
		Modifiers: `coinbase`, `binance`, `kraken`, `ftx`, `tier1`, `lambo`, `yacht`, `bridge`
		"""
	return(df)

# TRANSACTIONS
def faq_tps():
	df = """
	TPS (Transactions Per Second) is not a useful metric. On Ergo Reference Node v.5, TPS is estimated to be a minimum of 47.5 tx/s. However, transactions can happen in three scaling layers or levels: 

L0: Ergo Reference Nodes, which can be bootstrapped using NiPoPoWs proofs and UTXO set snapshots. 
L1: Ergo has extensions that allow for a wide variety of scaling solutions such as Sharding, Hydra, or BitcoinNG-style macroblocks. 
L2 (off-chain): Ergo should be compatible with the Lightning Network, Rainbow Network, and many more. The implementation here will depend on the needs of the applications being built on Ergo.

The general idea is that many transactions can happen in L1 or L2 and these transactions can be bundled and settled on the L0 layer of the Ergo blockchain using a single transaction. Thanks to the high flexibility of ErgoScript programming model, many different protocols are possible, each one solving scalability problem in a specific domain (like simple payment transactions).

Ergo blockchain can be thought as common settlement layer for many L1/L2 protocols and applications.    
	"""
	return(df)

# MARKET CAPITALIZATION
def faq_marketcap():
	df = """
	Ergo Explorer displays circulating supply and max supply (97,739,924 ERG). Multiply these amounts by current price to get Ergo's market capitalization. Do not rely on Coinmarketcap data. ERGs value derives from the popularity and utility of the platform + the cost of mining erg.

	https://explorer.ergoplatform.com/
	"""
	return(df)

# GENESIS
def faq_genesis():
	df = """
	The Ergo genesis block was created on 1 July 2019. Prior to that, there was a different coin, EFYT. EFYT was a Waves token that was airdropped, not sold. ICOs cause issues as you're buying from a common enterprise directly - who likely have nothing to show yet so purely for expectations of profits. ERGs value derives from the popularity and utility of the platform + the co.
	"""
	return(df)

# GULAG
def faq_gulag():
	df = """
	This chat is for serious discussion. If you want to troll users and share your spicy opinions, please join our community of Ergo edgelords in @ErgoGulag in Telegram or #🚧│random in Discord. 
	"""
	return(df)

# NFTs
## need to fix this Ergo server times out the bot due to discord invite links (meant to prevent spam)
def faq_nfts(modifier=""):
	if modifier=="dis":
		df = """
		https://discord.gg/gYZxq38pJn
		"""
	elif modifier=="tg":
		df = """
		@ErgoNFTs
		"""
	else:
		df = """
		@ErgoNFTs or https://discord.gg/gYZxq38pJn

Modifiers: `dis`, `tg`
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
		Mosaik is a JSON-based markup language served via a REST API intended to be used by Ergo platform dApps. For more information: <https://docs.ergoplatform.com/dev/stack/mosaik/intro/>
		"""
	else:
		df = """
		https://tokenjay.app

Modifiers: `mobile`, `escrow`, `mosaik`
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
		A DEX on Ergo, use either Nautilus or SAFEW wallets to access.
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
		Sigmaverse is the most comprehensive list of Ergo projects
		https://sigmaverse.io/

Modifiers: `mixer`, `spectrum`, `ergopad`, `skyharbor`, `ergoauctions`, `raffle`, `sigmavalley`
		"""
	return(df)

# DOCS
def faq_docs():
	df = """
	<https://docs.ergoplatform.com/documents/>
	"""
	return(df)

# ERGO MANIFESTO
def faq_manifesto():
	df = """
	The Ergo Manifesto hopes to educate and offer a vision of what blockchain technology can achieve. We hope to build society through horizontal cooperation through production under the division of labor, trade and exchange, and solidarity and mutual aid. Learn more at <https://ergoplatform.org/en/blog/2021-04-26-the-ergo-manifesto/>
	"""
	return(df)

# ADMIN
def faq_admin():
	df = """
	For technical support on Telegram please join @ErgoSupport
Email team@ergoplatform.org for business inquiries
For marketing queries please email angie@ergoplatform.org
	"""
	return(df)

# LEDGER
def faq_ledger():
	df = """
	Tutorials to sideload Ergo Ledger app

Nano S for Windows: <https://github.com/anon-br/ledger-ergo-js/blob/master/docs/ledger-app-installing-windows.md>

Nano S for Linux/MacOS: <https://github.com/anon-br/ledger-ergo-js/blob/master/docs/ledger-app-installing-unix.md>

Nano S Plus: <https://medium.com/@koutelier/how-to-sideload-ergo-ledger-app-to-nano-s-nano-s-plus-on-linux-fafb2380508a>
	"""
	return(df)

## POUW
def faq_pouw():
	df = """
	While Proof of Useful Work is an interesting idea, it is still in its research phase. Ergo is open to implementing new ideas. But, a radical change to its concensus mechanism that requires a hard fork would likely be outside the scope and resources of Ergo's small core development team and limited budget.
	"""
	return(df)

## STORAGE RENT
def faq_rent():
	df = """
	Storage rent is a fee for long term storage on the Ergo blockchain. Four years from your last transaction, you will be charged ~0.14 ERG and a transaction fee to pay for the costs of storing your digital information. Learn more at <https://ergoplatform.org/en/blog/2022-02-18-ergo-explainer-storage-rent/> and <https://docs.ergoplatform.com/mining/rent/>
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
		<https://docs.ergoplatform.com/node/install/>
		"""
	else:
		df = """
		<https://github.com/ergoplatform/ergo>

Modifiers: `install`, `docs`
		"""
	return(df)

# STAKING
def faq_staking():
	df = """
	Ergo is a Proof of Work blockchain. So, it is not possible to stake Ergo itself as you would in a Proof of Stake blockchain. However, it is possible to earn some yield from your ERG in combination with Ergo in liquidity pools, tokenisation of dApps, trading bots, lending platforms, and other mechanisms. Learn more here at <https://ergonaut.space/en/Guides/yield>
	"""
	return(df)

# DRAMA
## future: add to separate functions list since not a core FAQ
def faq_drama():
	df = """
	Pretend to be nice, please.
	"""
	return(df)

# CONTRIBUTE
def faq_contribute():
	df = """
	<https://docs.ergoplatform.com/contribute/>
	"""
	return(df)

# YOROI
def faq_yoroi():
	df = """
	What are you, some sort of cave person living under a rock? Use a wallet listed here: https://ergoplatform.org/en/get-erg/#Wallets
	"""
	return(df)

# BOTS
def faq_bots():
	df = """
	Beep Boop - don't worry, Human...the bots are just Discord <-> Telegram carrier pigeons (message bridge).
	"""
	return(df)

# MINING DIFFICULTY ADJUSTMENT
def faq_difficulty():
        df = """
	Ergo's difficulty algorithm was designed to reduce the incentive to perform coin-hopping and improve stability of inter-block delays. Coin-hopping is defined as an adversarial miner switching from mining one coin to another in the beginning of an epoch then switching back in the beginning of next epoch when difficulty becomes lower. Difficulty in Ergo is adjusted using the least squares method, which adjusts roughly every two weeks using the past eight epochs to obtain a target block interval of 120 seconds or 2 minutes, on average.

	For more details: 
	https://eprint.iacr.org/2017/731.pdf
        """
        return(df)

# SEED
def faq_seed():
        df = """
        Never give your seed phrase to anyone. You can restore your seed in any wallet, even multiple wallets. With the correct seed, you (and anyone else) can access your assets on the Ergo blockchain."
	"""
        return(df)



