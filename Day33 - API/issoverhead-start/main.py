import smtplib
import time
from datetime import datetime

import requests
from config import *
smtp_server = "smtp.gmail.com"
port = 587  # For starttls




def is_iss_overhead():
    response = requests.get(url=ISS_END_POINT)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return (abs(iss_latitude - MY_LAT) < 5) and (abs(iss_longitude - MY_LONG))


def is_it_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(SUNRISE_SUNSET_END_POINT, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    return sunrise <= time_now.hour >= sunset


message = 'Subject: Look up \n\nISS is overhead'
while True:
    time.sleep(60)
    if is_it_night() and is_iss_overhead():
        with smtplib.SMTP(smtp_server, port) as server:
            try:
                server.starttls(context=context)  # Secure the connection
                server.login(sender_email, sender_pass)
                server.sendmail(from_addr=sender_email, to_addrs="jacov.g@gmail.com", msg=message)
            except Exception as e:
                # Print any error messages to stdout
                print(e)
