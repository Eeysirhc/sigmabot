##############################
# Author: eeysirhc
# Date written: 2022-08-13
# Last updated: 2022-08-14
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

# IMPORT TOKEN ID
# future: ideally API has all of this data instead of CSV maintenance (https://github.com/ergolabs/ergo-dex-backend/issues/38)
keys = pd.read_csv("lp.csv")


##########
# FUNCTION: GET TOKEN DETAILS FROM ERGOWATCH 
def token_details(token_id):

	request_url = "https://ergo.watch/api/v0/tokens/" + token_id 
	df_raw = requests.get(request_url).json()
	df = pd.DataFrame(df_raw, index=[0])

	return(df)
##########



##########
# FUNCTION: GET ERGO ADDRESS BALANCE HISTORY
## future: simplify with param payload but need to figure out
def address_history(address, token_name=""):

	base_url = "https://ergo.watch/api/v0/addresses/" + address + "/balance/history"
	url_params = "timestamps=true&flat=true&limit=1000&offset=0&desc=true"

	# if token is supplied then get details about decimal places
	if token_name == "":
		request_url = base_url + "?" + url_params
	else: 
		token_id = keys[keys['name'] == token_name]['token_id'].iloc[0]
		request_url = base_url + "?token_id=" + token_id + "&" + url_params
	
	df_raw = requests.get(request_url).json()
	df = pd.DataFrame.from_dict(df_raw).sort_values("heights")

	return(df)
##########


##########
# FUNCTION: PROCESS DATA
def address_process(history_data, token_name=""):

	history_data['datetime'] = [datetime.fromtimestamp(x) for x in history_data['timestamps'] / 1000]

	# clean up data for plotting and correct data values
	if token_name == "":
		history_data['balances'] = history_data['balances'] / 1e9
	else: 
		token_id = keys[keys['name'] == token_name]['token_id'].iloc[0]
		t_decimals = token_details(token_id).decimals.item()
		if t_decimals != 0:
			history_data['balances'] = history_data['balances'] / (10**t_decimals)
			pass

	return(history_data)
##########


##########
# FUNCTION: VISUALIZE DATA
def address_charts(address, token_name=""):

	df = address_history(address, token_name)
	df = address_process(df, token_name) 

	plt.clf()
	plt.figure(figsize=(15,10))
	plt.plot(df.datetime, df.balances, marker='o')
	plt.ylabel("Address Balance")
	plt.ylim(0, df.balances.max()*1.20)
	plt.title(address, fontsize=15, horizontalalignment='left', x=0.05)

	plt.savefig("addy.png")
##########
