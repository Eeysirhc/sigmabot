##############################
# Author: eeysirhc
# Date written: 2022-08-12
# Last updated: 2022-08-13
##############################

# LOAD PYTHON MODULES
import requests

##########
# FUNCTION: RETRIEVE BLOCK HEIGHT FROM EXPLORER API 
def blox_height():
	
	url_ergoplatform = "https://api.ergoplatform.com/api/v1/networkState"
	ergoplatform = requests.get(url_ergoplatform).json()
	block_height = str(ergoplatform['height'])

	current_height = "Ergo Block Height: " + "`" + block_height + "`"

	return(current_height)
##########



