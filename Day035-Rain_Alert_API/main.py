import requests
import os
from twilio.rest import Client
from env_params import *

params = {
    "lat": 31.9274384,
    "lon": 34.8060315,
    "exclude": "current,minutely,daily,alerts",
    "appid": API_KEY
    }
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)


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
    message = client.messages \
                .create(
                     body="Bring an umbrella ☂",
                     from_=FROM_NUMBER,
                     to=TO_NUMBER
                 )
    print(message.status)