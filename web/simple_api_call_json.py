# -*- coding: utf-8 -*-

import requests

url = "https://api.gameofthronesquotes.xyz/v1/random"
response = requests.get(url)

data = response.json()
sentence = data["sentence"]
name = data["character"]["name"]

print("Status Code:", response.status_code)
print(f"{name} says: '{sentence}'")
