##############################
# Author: eeysirhc
# Description: Ecosystem
# Date written: 2022-08-25
# Last updated: 2023-02-03
##############################

from discord.ext import commands

##### NFTs #####
nfts_responses = {
"dis": """https://discord.gg/gYZxq38pJn""",

"tg": """@ErgoNFTs""",

"watches": """Watches are the NFTs of meat space."""

}

def faq_nfts(modifier=""):
    if modifier in nfts_responses:
        df = nfts_responses[modifier]
    else:
        df = """
        [Marketplaces]
Ergo Auction House: <https://ergoauctions.org>
SkyHarbor: <https://www.skyharbor.io/>

[Socials]
Telegram: @ErgoNFTs
Discord: (add DISCORD).gg/gYZxq38pJn

Modifiers: `dis`, `tg`, `watches`"""
    return(df)

##### TOKENJAY #####
tokenjay_responses = {
"escrow": """For directions on how to use Tokenjay for P2P Escrow trades and verifying Ergopad vesting key NFTs: <https://ergonaut.space/en/dApps/TokenJay> """,

"mobile": """If you haven't already, download Ergo Mobile Wallet (Android) or Terminus Wallet (Apple) and restore seed. Go to Settings. Click on the button Mosaik plugins disabled and make it enabled. A new dApps will appear in the bottom navigation bar of the wallet. Click on dApps, then scroll to the bottom of new page. Click on AgeUSD Dashboard. Then, click the Exchange button for either SigUSD or SigRSV. Then select Buy/Sell from the pull down menu and the amount you want.""",

"mosaik": """Mosaik is a JSON-based markup language served via a REST API intended to be used by Ergo platform dApps. For more information: <https://docs.ergoplatform.com/dev/stack/mosaik/intro/>""",

"sigrsv": """Tokenjay can be used to buy SigRSV directly from the bank. """,

"sigusd": """Tokenjay can be used to buy SigUSD directly from the bank. """,

}

def faq_tokenjay(modifier=""):
    if modifier in tokenjay_responses:
        df = tokenjay_responses[modifier]
    else:
        df = """Website: <https://tokenjay.app>
Details: <https://ergonaut.space/en/dApps/TokenJay>

Modifiers: `escrow`, `mobile`, mosaik`, `sigrsv`, `sigusd` """
    return(df)

##### ERGO PROJECTS #####
projects_responses = {
"mixer": """https://www.youtube.com/watch?v=DgztoNDFG8U""",

"spectrum": """A DEX on Ergo, use either Nautilus or SAFEW wallets to access: https://app.spectrum.fi/""",

"ergopad": """https://www.ergopad.io/""",

"skyharbor": """https://www.skyharbor.io/""",

"ergoauctions": """https://ergoauctions.org/""",

"raffle": """https://ergoraffle.com/""",

"sigmavalley": """https://www.sigmavalley.org/""",

}

def faq_projects(modifier=""):
    if modifier in projects_responses:
        df = projects_responses[modifier]
    else:
        df = """Sigmaverse is the most comprehensive list of Ergo projects: <https://sigmaverse.io/>

Modifiers: `mixer`, `spectrum`, `ergopad`, `skyharbor`, `ergoauctions`, `raffle`, `sigmavalley`"""
    return(df)

##### NODE #####
node_responses = {
"install": """Instructions on how to setup a full Ergo node: https://www.youtube.com/watch?v=fpEDJ1CM6ns""",

"docs": """<https://docs.ergoplatform.com/node/install/>""",

"lists": """Lists of alternative nodes:
<http://ergonodes.net/list>
<https://api.tokenjay.app/peers/list?unreachable=false&limit=50>"""

}

def faq_node(modifier=""):
    if modifier in node_responses:
        df = node_responses[modifier]
    else:
        df = """Node contain the reference implementation of the Ergo Platform Protocol. Details: <https://github.com/ergoplatform/ergo>

Modifiers: `install`, `docs`, `lists`"""
    return(df)

##### GRAPHQL #####
def faq_graphql():
    df = """
GraphQL runs on top of Ergo Explorer and allows for faster access to blockchain information. 
Default: https://gql.ergoplatform.org
    
If you are having trouble connecting to the default, try the list of APIs for alternatives.
<https://ergonaut.space/e/en/Glossary/APIs>"""
    return(df)

def faq_scala():
    df = """ 
    Why is Scala the programming language Ergo is based on? https://ergonaut.space/en/Ergo/Scala
    """
    return(df)

def faq_howie():
    df = """
    Does the Howie Test apply to Ergo? https://ergonaut.space/en/Ergo/Howie
    """
    return(df)

def faq_ergo():
    df = """Ergo represents the next step in the evolution of proof-of-work blockchain technology, combining Bitcoin’s ledger model with smart contract functionality. Ergo’s extended UTXO design is built to offer secure and robust tooling through the use of its native language, ErgoScript, and its inherent Sigma protocols that utilize non-interactive zero-knowledge proofs.

Ergo’s Autolykos v2 mining consensus algorithm is GPU friendly and ASIC resistant, allowing for anyone with consumer-grade GPU hardware to easily and effectively participate in securing the network.

The Ergo blockchain launched in 2019 with no pre-mining or pre-allocation of any coins. The platform strives to be fair and accessible to all with an emphasis on building truly decentralized financial products and services. The ecosystem currently features the SigUSD stablecoin, ErgoMixer, a cross-chain DEX, and much more. More information can be found at ergoplatform.org, sigmaverse.io and ergonaut.space."""
    return(df)

def faq_newdev():
    df = """If you are a developer new to the Ergo ecosystem, these links may be useful:
    
    - Ergo Documentation: <https://docs.ergoplatform.com/dev/start/>
    - Ergo Appkit: <https://github.com/ergoplatform/ergo-appkit>
    - Fleet: <https://fleet-sdk.github.io/docs/>
    - DeCo Education (video): <https://www.youtube.com/@decoeducation9394>
    - DeCo Education (docs): <https://deco-education.github.io/deco-docs/docs/category/into-the-woods/>
    - Ergohack: <https://ergohack.io/>

To access the Development channel in Discord, go to channels in the side bar. Click Channels & Roles (near the top). Then, select Start Developing."""
    return(df)

def faq_rosen():
    df = """
    Rosen Bridge is a cross-chain bridge on Ergo that only requires a multi-signature wallet on the other chain. Rosen has dual layers of confirmation. One layer is watchers, which watch for changes on the other chains and notify the second layer when something happens on the other chain. Then, the guards verify that the event they were notified of actually happened. A consensus among guards needs to be reached before funds are transferred or released.02

For more information: <https://docs.ergoplatform.com/eco/rosen/>
    """
    return(df)

def faq_efyt():
    df = """
    <https://docs.ergoplatform.com/mining/emission/#what-is-efyt>
    """
    return(df)

def faq_explorer():
    df = """Ergo Explorer is the main source for Ergo blockchain information. Details: <https://docs.ergoplatform.com/dev/stack/explorer>

Default website: <https://explorer.ergoplatform.com>
Alternative: <https://ergexplorer.com/>

If you are having trouble connecting to the default, alternative explorer instances can be found here: <https://ergonaut.space/e/en/Glossary/APIs>
    """
    return(df)

def faq_consolidate():
    df = """Trouble using a dApp? Often consolidating your wallet will solve the problem. There are three methods to consolidating a wallet.
    
    1. In Nautilus, select dApps (the four squares icon). Click on Wallet Optimization, then Optimize. 
    2. In Ergo Mobile Wallet / Terminus, click on dApps. Then, click on Box Consolidation.
    3. Send all assets to your own wallet address.
    
If you continue to have trouble, try the support channel in Ergo Discord/Telegram.
    """
    return(df)

def faq_unfrackit():
    df = """People from Cardano sometimes ask about Unfrack.it on Ergo.  With the exceptions of token isolation on Ledger wallets and UTXO compression, the problems of parellelism are solved with Ergo's state of art chained transactions. In short, a dApp like unfrack.it are already implemeented in the Ergo protocol.
    """
    return(df)

class Ecosystem(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def nfts(self, ctx, modifier=""):
        modifier = modifier.lower()
        response = faq_nfts(modifier)
        await ctx.send(response)

    @commands.command()
    async def tokenjay(self, ctx, modifier=""):
        modifier = modifier.lower()
        response = faq_tokenjay(modifier)
        await ctx.send(response)

    @commands.command()
    async def projects(self, ctx, modifier=""):
        modifier = modifier.lower()
        response = faq_projects(modifier)
        await ctx.send(response)

    @commands.command()
    async def node(self, ctx, modifier=""):
        modifier = modifier.lower()
        response = faq_node(modifier)
        await ctx.send(response)

    @commands.command()
    async def graphql(self, ctx):
        await ctx.send(faq_graphql())

    @commands.command()
    async def scala(self, ctx):
        await ctx.send(faq_scala())

    @commands.command()
    async def howie(self, ctx):
        await ctx.send(faq_howie())

    @commands.command()
    async def ergo(self, ctx):
        await ctx.send(faq_ergo())

    @commands.command()
    async def newdev(self, ctx):
        await ctx.send(faq_newdev())

    @commands.command()
    async def rosen(self, ctx):
        await ctx.send(faq_rosen())

    @commands.command()
    async def efyt(self, ctx):
        await ctx.send(faq_efyt())

    @commands.command()
    async def explorer(self, ctx):
        await ctx.send(faq_explorer())

    @commands.command()
    async def consolidate(self, ctx):
        await ctx.send(faq_consolidate())

    @commands.command()
    async def unfrackit(self, ctx):
        await ctx.send(faq_unfrackit())

async def setup(client):
    await client.add_cog(Ecosystem(client))
