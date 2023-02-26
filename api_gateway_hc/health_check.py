import datetime
import schedule
import time
import requests
import json
import csv
import random


def revisar_salud():
    # numero aleatoerio entre 1 y 2
    random_event = random.randint(0, 1)

    data = [{"url": "https://3xh4z4wwvicywc44y5wihsxzye0spget.lambda-url.us-east-1.on.aws/", "type": "PEDIDOS"},
            {"url": "https://f3edp7y6ricqwqb33lgf6m7i6e0ljahh.lambda-url.us-east-1.on.aws/", "type": "CLIENTES"}]

    url = data[random_event]["url"]

    # Enviar a lamda por medio de api
    payload = json.dumps({
        "vendedor_id": 1,
        "numero_seguimiento": 1
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    resultado = "SUCCESS"
    if response.content == b'Server Error':
        resultado = "ERROR"

    with open('data_health_check.csv', 'a', newline='') as file:
        data_to_csv = [str(response.content),
                       str(datetime.datetime.now()),
                       str(data[random_event]["type"]),
                       resultado]
        writer = csv.writer(file)
        writer.writerow(data_to_csv)

    print(f'{response.content}')


schedule.every(1).seconds.do(revisar_salud)

while True:
    schedule.run_pending()
    time.sleep(1)
