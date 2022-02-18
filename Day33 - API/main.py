"""Trying to call the International Space Station(ISS) API for the current ISS Location.
	Day33 of the course '100 Days of code'
	"""
import time

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.content)
for _ in range(5):
	response = requests.get(url="http://api.kanye.rest")
	text_quote = response.json()
	print(text_quote["quote"])
	time.sleep(3)