import schedule
import time


def revisar_salud():
    print("Ejecutando tarea programada...")
    # Enviar mensaje con la data


schedule.every(5).seconds.do(revisar_salud)

while True:
    schedule.run_pending()
    time.sleep(1)
