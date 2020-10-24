
#ejercicio 6 - Intensidad de Led
import RPi.GPIO as GPIO
from time import sleep

ledpwm=14
GPIO.setmode(ledpwn, GPIO.BCM)
GPIO.setup(ledpwn, GPIO.OUT)
led = GPIO.PWM(ledpwm, 100)
led.start(1)
led.ChangeDutyCycle(10)
sleep(1)
led.ChangeDutyCycle(20)
sleep(1)
led.ChangeDutyCycle(30)
sleep(1)
led.ChangeDutyCycle(40)
sleep(1)
led.ChangeDutyCycle(50)
sleep(1)
led.ChangeDutyCycle(60)
sleep(1)
led.ChangeDutyCycle(70)
sleep(1)
led.ChangeDutyCycle(80)
sleep(1)
led.ChangeDutyCycle(90)
sleep(1)
led.ChangeDutyCycle(100)
led.stop()
GPIO.cleanup()

