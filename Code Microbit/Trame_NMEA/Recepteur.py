from microbit import *
import radio

radio.on()
radio.config(group=1, length=251)
display.show("R")

while True:
    message = radio.receive()
    if message:
        print(message)
        display.show(Image.YES)
        sleep(100)
        display.clear()