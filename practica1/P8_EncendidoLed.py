
#ejercicio 8 - Encendido de Led por tiempo
import gpiozero as LED
from time import *

led = LED(18)
led.on()
sleep(1)
led.off()
