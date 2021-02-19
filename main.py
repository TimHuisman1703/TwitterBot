import twitterbot
import time
import datetime

def post_delft_weather():
	account = "WeatherInDelft"

	message = twitterbot.generate_weather_message()
	twitterbot.post_tweet(message, account)

INTERVAL = 30 * 60
HOUR_OF_POSTING = 13

posted_today = False

while True:
	hour = datetime.datetime.now().hour

	if hour == HOUR_OF_POSTING and not posted_today:
		post_delft_weather()
		posted_today = True
	
	if hour == 1:
		posted_today = False

	time.sleep(INTERVAL)