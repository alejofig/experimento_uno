'''Para correr el experimento, se debe ejecutar el siguiente comando: python run_experiment.py
Tambien se debe iniciar el health_check.py, que existe dentro de be_apigateway/health_check.py '''
import requests
import random
import time

for i in range(400):
    # numero aleatoerio entre 1 y 10
    random_client = random.randint(1, 10)

    # numero aleatorio entre 0 y 1
    random_event = random.randint(0, 1)

    urls = [f"https://n3dox8jtg5.execute-api.us-east-1.amazonaws.com/dev/v1/pedidos/{random_client}",
            f"https://n3dox8jtg5.execute-api.us-east-1.amazonaws.com/dev/v1/clients/{random_client}"]

    url = urls[random_event]

    data = {}
    response = requests.post(url, data=data)

    # delay de 1 segundo
    time.sleep(1)

    print(f"Peticion numero:{i}, {response.content}")
