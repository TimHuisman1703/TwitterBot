import os
from os import environ

acc1 = "WeatherInDelft"

def get_keys(account):
	if account == acc1:
		consumer_key = environ["CONSUMER_KEY"]
		consumer_key_secret = environ["CONSUMER_SECRET"]
		access_token = environ["ACCESS_KEY"]
		access_token_secret = environ["ACCESS_SECRET"]
	else:
		consumer_key = ""
		consumer_key_secret = ""
		access_token = ""
		access_token_secret = ""
	
	return consumer_key, consumer_key_secret, access_token, access_token_secret