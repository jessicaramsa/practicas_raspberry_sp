
#ejercicio 7 - Intensidad de Led por ingreso de datos
import RPi.GPIO as GPIO

ledpwm=18
GPIO.setmode(ledpwn, GPIO.BCM)
GPIO.setup(ledpwn, GPIO.OUT)
led = GPIO.PWM(ledpwm, 100)
led.start(1)
try:
    while True:
        intensidad=float(input("Intensidad: "))
        if intensidad<0:
            break
        elif intensidad<101:
            led.ChangeDutyCycle(intensidad)
        else:
            led.ChangeDutyCycle(100)
except KeyboardInterrupt:
    led.stop()
    GPIO.cleanup()        



