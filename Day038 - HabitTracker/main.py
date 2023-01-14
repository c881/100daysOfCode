"""Post, Get, Put, Delete
http request headers"""

import requests

PIXELA_ENDPOINT_CREATE = "https://pixe.la/v1/users"
PIXELA_ENDPOINT_CREATE_GRAPH = "https://pixe.la/v1/users/c881/graphs"
user_params={"token":"bnruS2010",
        "username":"c881",
        "agreeTermsOfService":"yes",
        "notMinor":"yes"}
        # ,"thanksCode":"ThisIsThanksCode"}
graph_params

""" First time was success.
Next time will get an error"""
# response = requests.post(url=PIXELA_ENDPOINT_CREATE, json=user_params)
# response.raise_for_status()
# print(response.text)