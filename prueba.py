from urllib.request import Request
import requests

var = requests.get("https://api.npoint.io/046ff1b0b99ae039ee33").json()
print(var[0]["body"])