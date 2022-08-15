##############################
# Author: eeysirhc
# Date written: 2022-08-12
# Last updated: 2022-08-14
##############################

# LOAD PYTHON MODULES
import os 
import requests 
import pandas as pd 

import matplotlib as mpl 
import matplotlib.pyplot as plt 
mpl.rcParams['figure.dpi'] = 300

import seaborn as sns
sns.set(style='darkgrid')

# IMPORT SPECTRUMDEX POOL ID
# future: ideally API has all of this data instead of CSV maintenance (https://github.com/ergolabs/ergo-dex-backend/issues/38)
keys = pd.read_csv("lp.csv")

##########
# FUNCTION: RETRIEVE SPECTRUMDEX DATA
def spectrumdex_data(token_name):
	
	# lookup pool IDs
	pool_id = keys[keys['name'] == token_name]['pool_id'].iloc[0]

	# retrieve pool stats
	df_raw = requests.get("https://api.ergodex.io/v1/amm/pool/" + pool_id + "/chart").json()
	df = pd.DataFrame.from_dict(df_raw)
	df['datetime'] = pd.to_datetime(df['timestamp'] / 1000, unit='s')

	return(df)
##########



##########
# FUNCTION: VISUALIZE DATA
def spectrumdex_charts(user_request):
	
	# token
	token_data = spectrumdex_data(user_request)

	# descriptors
	latest = token_data.tail(1)
	title = "ERG / " + user_request.upper() + " @ " + str(round(latest.price.item(),2))

	plt.clf()
	plt.figure(figsize=(15,10))
	plt.plot(token_data.datetime, token_data.price, marker='o')
	plt.axhline(y=latest.price.item(), linestyle=':')
	plt.title(title, fontsize=15, horizontalalignment='left', x=0.05)

	# if requesting sigUSD then don't flip y-axis 
	if user_request == "sigusd":
		plt.ylim(0, token_data.price.max()*1.20)
	else:
		plt.gca().invert_yaxis()
		plt.ylim(token_data.price.max()*1.20, 0)

	plt.savefig("toast.png")
##########




