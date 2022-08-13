##############################
# Author: eeysirhc
# Date written: 2022-08-13
# Last updated: 
##############################

# LOAD PYTHON MODULES
import requests
import pandas as pd
from datetime import datetime

import matplotlib as mpl 
import matplotlib.pyplot as plt 
mpl.rcParams['figure.dpi'] = 300

import seaborn as sns
sns.set(style='darkgrid')

##########
# FUNCTION: GET ERGO ADDRESS BALANCE HISTORY
def address_history(address):

	df_raw = requests.get("https://ergo.watch/api/v0/addresses/" + address + "/balance/history?timestamps=true&flat=true&limit=1000&offset=0&desc=true").json()
	df = pd.DataFrame.from_dict(df_raw).sort_values("heights")

	df['balances'] = df['balances'] / 1e9
	df['datetime'] = [datetime.fromtimestamp(x) for x in df['timestamps']/1000]

	return(df)
##########

##########
# FUNCTION: VISUALIZE DATA
def address_charts(address):

	df = address_history(address)

	# save plot
	plt.clf()
	plt.figure(figsize=(15,10))
	plt.plot(df.datetime, df.balances, marker='o')
	plt.ylabel("$ERG Balance")
	plt.ylim(0, df.balances.max()*1.20)
	plt.title(address, fontsize=15, horizontalalignment='left', x=0.05)
	plt.savefig("addy.png")
##########



