##############################
# Author: eeysirhc
# Date written: 2022-08-25
# Last updated: 2022-09-04
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

# LISTING
def faq_listing(modifier=""):
	if modifier=="binance":
		df = """
		Ergo will be listed on Binance when its customers want it.
		"""
        elif modifier=="coinbase":
		df = """
		Ergo will be listed on Coinbase when its customers want it.
		"""
        elif modifier=="kracken":
		df = """
		Ergo will be listed on Kracken when its customers want it.
		"""
        elif modifier=="kucoin":              
                df = """                       
                Ergo will be listed on KuCoin when its customers want it                
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
        
def faq_binance(modifier=""):                                                              
        df = """                               
        Ergo will be listed on Binance when its customers want it.
        """                                               
        return(df)                                                                              


# TRANSACTIONS
def faq_tps(modifier=""):                                     
        df = """                                                  
        Ergo's TPS (Transactions per second) on the version 5 Node TPS is estimated to be a minimum of 47.5tx/s. There are three scaling layers or levels: L0: Ergo nodes, which can be bootstrapped using NiPoPoWs proofs and UTXO set snapshots are planned. L1: Ergo has an extension section in its code that allows the implementation of a wide variety of scaling solutions such as Sharding, Hydra, or BitcoinNG-style macroblocks. L2 (off-chain): Ergo should be compatible with the Lightning Network, Rainbow Network, and many more. The implementation here will depend on the needs of the applications being built on Ergo.

The general idea, roughtly, is that large chunks of transactions can happen in layer 2 and the whole chunks will be settled in Ergo blockchain using single transaction. Thanks to the high flexibility of ErgoScript programming model, many different protocols will be possible on layer2, each one solving scalability problem in a specific domain (like simple payment transactions).

Thus, Ergo blockchain can be thought as common settlement layer for many L2 protocols and applications.    
        """                                                      
        return(df)                                                

# MARKET CAPITALIZATION
def faq_marketcap(modifier=""):                                                   
        df = """
        Ergo Explorer displays circulating supply and max supply (97,739,924 ERG). Multiply these amounts by current price to get Ergo's market capitalization. Coinmarketcap displays incorrect data and should not be relied upon.                         
        """
        return(df)

# GENESIS
def faq_genesis(modifier=""):                                                   
        df = """
        Ergo genesis block was 1 July 2019. Prior to that, there was a different coin, EFYT. EFYT was a Waves token that was airdropped, not sold. ICOs cause issues as you're buying from a common enterprise directly - who likely have nothing to show yet so purely for expectations of profits. ERGs value derives from the popularity and utility of the platform + the cost of mining erg.
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
