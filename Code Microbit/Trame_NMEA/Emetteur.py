from microbit import *
import radio

radio.on()
radio.config(group=1, length=251)
uart.init(baudrate=9600, tx=pin14, rx=pin0) # Configuration de l'UART afin de recevoir des trames sur la carte microbit à l'aide du module GROVE

display.show("E")

while True:
    # S'il reçoit quelconque communication
    if uart.any():
        ligne = uart.readline()
        if ligne:
            radio.send(str(ligne, 'ascii')) # Si une ligne est écrite (donc une trame), on donne la ligne à la carte microbit réceptrice
            display.set_pixel(2, 2, 9)
            sleep(50)
            display.set_pixel(2, 2, 0)
    sleep(10)