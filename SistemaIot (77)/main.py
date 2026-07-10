from banco import criar_tabela, salvar_leitura
from serial_io import ler_sensor
import time

criar_tabela()

print("Sistema IoT iniciado!")

while True:
    luminosidade = ler_sensor()

    if luminosidade > 300:
        status = "Muito escuro!"
    elif luminosidade < 50:
        status = "Muito claro!"
    else:
        status = "Ambiente Ideal!"

    salvar_leitura(luminosidade, status)

    print(f"Luminosidade: {luminosidade} | Status: {status}")

    time.sleep(1)