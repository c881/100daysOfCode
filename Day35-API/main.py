import requests
from env_params import *

params = {
    "lat":31.9274384,
    "lon":34.8060315,
    "exclude":"daily",
    "appid": API_KEY
    }
responce = requests.get(url=ONEPOINT_ENDPOINT,params=params).json()
# data = responce.content
print(responce['hourly'])