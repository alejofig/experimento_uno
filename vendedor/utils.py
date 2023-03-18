import requests
import json


def generate_token(user,password):
    url = "https://n3dox8jtg5.execute-api.us-east-1.amazonaws.com/dev/login"

    payload = json.dumps({
    "usuario": user,
    "contrasena": password
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text)["token"]