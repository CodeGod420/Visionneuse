from picamera import PiCamera
from time import sleep

import subprocess
import datetime
import time
import sys
import threading
import select

# Variable global para indicar si se debe detener la grabación
stop_recording = False

def capture_video(duration_milliseconds, output_filename):
    global stop_recording

    # Construir el comando raspivid con la duración y nombre de archivo
    command = f"raspivid -t {duration_milliseconds} -o {output_filename}"

    try:
        # Iniciar la grabación en un hilo separado
        recording_thread = threading.Thread(target=subprocess.run, args=(command,), kwargs={'shell': True, 'check': True})
        recording_thread.start()

        # Monitorear la entrada del usuario para detener la grabación
        while recording_thread.is_alive():
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                key = sys.stdin.read(1)
                if key == 'g':
                    stop_recording = True
                    break

            time.sleep(0.1)

        # Esperar a que finalice la grabación
        recording_thread.join()

        print(f"Video guardado como {output_filename}")

    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")

if __name__ == "__main__":
    # Solicitar al usuario la duración de la grabación en minutos
    duration_minutes = int(input("Ingrese la duración de la grabación en minutos: "))

    # Convertir minutos a milisegundos
    duration_milliseconds = duration_minutes * 60 * 1000

    # Obtener la marca de tiempo actual
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Crear el nombre del archivo de salida
    output_filename = f"video_{timestamp}.h264"

    print("Presione 'g' para detener y guardar la grabación antes del tiempo especificado.")

    # Iniciar la grabación
    capture_video(duration_milliseconds, output_filename)