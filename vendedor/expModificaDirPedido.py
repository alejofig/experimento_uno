import requests
import json

url = "https://n3dox8jtg5.execute-api.us-east-1.amazonaws.com/dev/v1/pedidos"

'''traer los pedidos del vendedor y'''
payload = json.dumps({
  "pedido_id": 2,
  "nueva_direccion_entrega": "avenida siempre viva 742"
})
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3OTAyOTEzOCwianRpIjoiYTg4MzU4Y2YtNjZiNC00MDY3LTg4MzQtYTRjZjZlYWU0NGEzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjc5MDI5MTM4LCJleHAiOjE2NzkwMzAwMzh9.lxC-7mxnHLOpxEWJMJ3M3RlO2vI5V544Xmm5KF6rTyw',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)