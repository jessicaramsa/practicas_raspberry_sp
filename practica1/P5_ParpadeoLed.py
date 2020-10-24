#ejercicio 5 - Parpadeo de Led
import RPi.GPIO as GPIO
from time import sleep

ledonoff=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(leodonoff, GPIO.OUT)
try:
    while True:
        estado=True
        GPIO.output(leodonoff, estado)
        sleep(1)
        estado=False
        GPIO.output(leodonoff, estado)
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
        



