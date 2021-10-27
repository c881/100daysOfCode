"""Trying to call the International Space Station(ISS) API for the current ISS Location.
	Day33 of the course '100 Days of code'
	"""

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
