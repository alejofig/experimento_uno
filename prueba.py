import requests
import json

url = "https://3xh4z4wwvicywc44y5wihsxzye0spget.lambda-url.us-east-1.on.aws/"

payload = json.dumps({
  "vendedor_id": 1,
  "numero_seguimiento": 1
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
