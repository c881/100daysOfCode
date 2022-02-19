"""Trying to call the International Space Station(ISS) API for the current ISS Location.
	Day33 of the course '100 Days of code'
	"""
from datetime import datetime
import requests
import time

MY_LAT = 31.928855
MY_LNG = 34.798594

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.content)
# for _ in range(5):
# 	response = requests.get(url="http://api.kanye.rest")
# 	response.raise_for_status()
# 	text_quote = response.json()
# 	print(text_quote["quote"])
# 	time.sleep(3)

parameters = {
	"lat": MY_LAT,
	"lng": MY_LNG,
	"formatted": 0}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()
sunrise_hour = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_hour = data["results"]["sunset"].split("T")[1].split(":")[0]
print(f'sunrise: {sunrise_hour}\nsubset: {sunset_hour}')
# print(time.)
print(datetime.now.hour)
