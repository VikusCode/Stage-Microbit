import serial
import time

port_serie = "/dev/ttyACM0" 

try:
    microbit = serial.Serial(port_serie, 115200, timeout=0.1)
    print("ÉCOUTE DES TRAMES COMPLÈTES...")
    while True:
        if microbit.in_waiting > 0:
            ligne = microbit.readline().decode('utf-8').strip()
            if ligne:
                print(f"Trame reçue : {ligne}")
        time.sleep(0.05)

except Exception as e:
    print(f"Erreur : {e}")
finally:
    if 'microbit' in locals():
        microbit.close()