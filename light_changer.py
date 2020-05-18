import requests

token = ""

headers = {
    "Authorization": "Bearer %s" % token,
}

payload = {
    "color": "#ffffff",
}

response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
