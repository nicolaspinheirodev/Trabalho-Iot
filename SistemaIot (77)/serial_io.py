import serial
import time

PORTA = "COM4"
BAUD = 9600

arduino = serial.Serial(PORTA, BAUD)

time.sleep(2)

def ler_sensor():
    valor = arduino.readline().decode().strip()

    if valor:
        return int(valor)

    return 0