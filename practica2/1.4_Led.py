from gpiozero import LED
from time import sleep

orange = LED(18)
orange.on()
sleep(2)
orange.off()
