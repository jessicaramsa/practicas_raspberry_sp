
#ejercicio 8 - Encendido de Led por tiempo
from gpiozero import LED
from time import *

led = LED(14)
led.on()
sleep(1)
led.off()
