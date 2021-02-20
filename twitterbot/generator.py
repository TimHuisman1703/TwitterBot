import sys, os, requests
from datetime import date
import random

months = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "october", "november", "december"]

def random_from_list(li):
	index = random.randint(0, len(li) - 1)
	print(index)
	return li[index]

def get_weather_rating_delft():
	url = "https://www.weeronline.nl/Europa/Nederland/Delft/4057853"
	
	# get html page
	req = requests.get(url, allow_redirects=True)
	html = str(req.content)

	# get a rating
	index = html.find("wol-forecastDay-module__weatherRating___")
	index = html.find("grade_", index) + 6
	
	return int(html[index:(index+1 if html[index+1] != "0" else index+2])

def generate_weather_message():
	# read responses from file
	rating_messages = [line.split("; ") for line in open("text/weather_in_delft.txt").read().split("\n")]

	rating = get_weather_rating_delft()
	day = str(date.today()).split("-")
	
	# generate message
	message = f"{day[2]} {months[int(day[1])-1]} {day[0]}: {random_from_list(rating_messages[rating-1])}"

	return message