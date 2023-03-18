import requests
import json
from utils import generate_token

#Lista de vendedores y sus pedidos asociados
# En esta prueba se espera que solo se cambie la dirección de los pedidos que tiene asociado el vendedor 
# que se envia por token
vendedores = {1:[3,4,5,6,7,8,9],
            2:[10,11,12,13,14,15,16,17],
            3:[18,19,20,21,22,23,24,25]}

user = "admin"
password = "admin"
token = generate_token(user,password)

url = "https://n3dox8jtg5.execute-api.us-east-1.amazonaws.com/dev/v1/pedidos"

for vendedor, pedidos in vendedores.items():
  for pedido in pedidos:
    payload = json.dumps({
      "pedido_id": pedido,
      "nueva_direccion_entrega": "Primera direccion"
    })
    headers = {
      'Authorization': f'Bearer {token}',
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)