import requests
from env_params import *

params = {
    "lat":31.9274384,
    "lon":34.8060315,
    "exclude":"current,minutely,daily,alerts",
    "appid": API_KEY
    }

def will_it_rain(data):
    for hour in data:
        # print(hour["weather"][0]["id"])
        if hour["weather"][0]["id"] < 700:
            return True
    return False

response = requests.get(url=ONEPOINT_ENDPOINT, params=params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data['hourly'][:6])
if will_it_rain(weather_data['hourly'][:12]):
    print("Bring an umbrella")

    # print(data['hourly'][i]["weather"][0]["id"])
