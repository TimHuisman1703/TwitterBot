import twitterbot
import time
import datetime

def post_delft_weather():
	account = "WeatherInDelft"

	message = twitterbot.generate_weather_message()
	twitterbot.post_tweet(message, account)

INTERVAL = 10 * 60		# check time every 10 minutes
HOUR_OF_POSTING = 7		# post at 7am GMT (8am in Delft)

posted_today = False

while True:
	hour = datetime.datetime.now().hour

	if hour == HOUR_OF_POSTING and not posted_today:
		post_delft_weather()
		posted_today = True
	
	if hour == 1:
		posted_today = False

	print("Still online")
	time.sleep(INTERVAL)