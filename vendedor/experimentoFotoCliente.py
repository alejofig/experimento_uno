'''para correr el experimento: en una terminal meterse a la carpeta de apigateway darle flask run
en otra terminal en la carpeta del proyecto correr el comando python experimentoFotoCliente.py'''

import requests
import random
import csv
from utils import generate_token
import datetime

# En este experimento se espera enviar solicitud de clientes de un usuario identificado por token
# Para 25 de esas solicitudes se envia el token y las otras sin token
# Se debería verificar que el 25 de las solicitudes buenas queden en la base de datos de respuesta

# Definimos la URL para hacer el login
user = "admin"
password = "admin"
token = generate_token(user, password)

# Datos de las URL aleatorias a las que haremos solicitudes
url = "https://n3dox8jtg5.execute-api.us-east-1.amazonaws.com/dev/v1/clients"

for i in range(0, 50):
    payload = {}
    if i in range(0, 25):
        headers = {'Authorization': f'Bearer {token}'}
    else:
        headers = {'Authorization': 'Bearer Token'}
    response = requests.request("POST", url, headers=headers, data=payload)

    resultado = "SUCCESS"
    if response.content == b'{"message": "Internal Server Error"}\n':
        resultado = "ERROR"

    with open('data_health_check_exp_2.csv', 'a', newline='') as file:
        data_to_csv = [str(response.content),
                       str(datetime.datetime.now()),
                       resultado]
        writer = csv.writer(file)
        writer.writerow(data_to_csv)

    print(f'{response.content}', resultado)
