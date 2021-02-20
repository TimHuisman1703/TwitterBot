import tweepy
from . import keys

def set_twitter(account):
	consumer_key, consumer_key_secret, access_token, access_token_secret = keys.get_keys(account)

	# authentication
	auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	return api

def post_tweet(text, account):
	# get right twitter account
	twitter = set_twitter(account)

	# post tweet
	twitter.update_status(text)
	print(f"Succesfully posted:\n{text}\n")