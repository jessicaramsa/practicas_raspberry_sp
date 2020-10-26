#ejercicio 5 - Parpadeo de Led
import RPi.GPIO as GPIO
from time import sleep

ledonoff=14
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledonoff, GPIO.OUT)
try:
    while True:
        estado=True
        GPIO.output(ledonoff, estado)
        sleep(1)
        estado=False
        GPIO.output(ledonoff, estado)
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
        



