import os
from os import environ

acc1 = "WeatherInDelft"

# get credentials for twitter app
def get_keys(account):
	if account == acc1:
		consumer_key = environ["CONSUMER_KEY_ACC1"]
		consumer_key_secret = environ["CONSUMER_SECRET_ACC1"]
		access_token = environ["ACCESS_KEY_ACC1"]
		access_token_secret = environ["ACCESS_SECRET_ACC1"]
	else:
		consumer_key = ""
		consumer_key_secret = ""
		access_token = ""
		access_token_secret = ""
	
	return consumer_key, consumer_key_secret, access_token, access_token_secret