import RPi.GPIO as GPIO
from time import sleep

led_on_off = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_on_off, GPIO.OUT)
estado = True

GPIO.output(led_on_off, estado)

sleep(10)
estado = False
GPIO.output(led_on_off, estado)
GPIO.cleanup()
