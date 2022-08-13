##############################
# Author: eeysirhc
# Date written: 2022-08-12
# Last updated: 
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
	token = token_name
	pool_id = keys[keys['name'] == token]['pool_id'].iloc[0]

	# retrieve pool stats
	df_raw = requests.get("https://api.ergodex.io/v1/amm/pool/" + pool_id + "/chart").json()
	df = pd.DataFrame.from_dict(df_raw)
	df['datetime'] = pd.to_datetime(df['timestamp'] / 1000, unit='s')

	return(df)
##########

##########
# FUNCTION: VISUALIZE DATA
# future: could probably clean this up and separate into two steps instead 1) process 2) plot
def spectrumdex_charts(user_request):
	
	# base $erg in sigUSD
	sigusd = spectrumdex_data("erg")
	
	# token
	token_data = spectrumdex_data(user_request)

	# join data 
	df = pd.merge(sigusd, token_data, on='timestamp')
	df['token_price'] = df['price_x'] / df['price_y']
	df = df[['datetime_x', 'price_x', 'token_price']]
	df = df.rename(columns={'datetime_x': 'datetime', 'price_x': 'sigusd_price'})

	# if requesting "erg" price then replace data values
	if user_request == "erg":
		df['token_price'] = df['sigusd_price']
		pass

	# latest price
	dx = df.tail(1)

	# save plot
	plt.clf()
	plt.figure(figsize=(15,10))
	plt.plot(df.datetime, df.token_price, marker='o')
	plt.axhline(y=dx.token_price.item(), linestyle=':')
	plt.ylabel("Price ($)")
	plt.ylim(0, df.token_price.max()*1.20)
	plt.title(user_request, fontsize=15, horizontalalignment='left', x=0.05)
	plt.savefig("toast.png")
##########

