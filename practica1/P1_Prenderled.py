import RPi.GPIO as GPIO

led_on_off = 14

GPIO.setmode(GPIO.BCM)
GPIO.setuo(led_on_off, GPIO.OUT)
estado = True

GPIO.output(led_on_off, estado)
