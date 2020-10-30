##Ejercicio 4 - Buzzer con boton
'''from tkinter import *
from gpiozero import Buzzer

def RuidoBuzzer():
    global bz
    global ruido
    if ruido:
        bz.off()
    else:
        bz.on()
    ruido = not ruido

gpiobuzzer = 16
bz = Buzzer(gpiobuzzer)
ruido = False
root = Tk()
btn_Buz16=Button(root, text="RuidoBuzzer",command=RuidoBuzzer)
btn_Buz16.pack()
root.mainloop()
GPIO.cleanup()
'''

import RPi.GPIO as GPIO
# desactivamos mensajes de error
GPIO.setwarnings(False)
# guardamos en una variable el pin de salida
pin = 24
# indicamos el uso de  la identificacion BCM para los GPIO
GPIO.setmode(GPIO.BCM)
# indicamos que el GPIO18 es de salida de corriente
GPIO.setup(pin, GPIO.OUT)
# bucle que se repite de forma indefinida
while (True):
    # input para introducir el PWM
    PWM = input("Enter PWM (1 to 99): ")
    # input para introducir los Herzios
    HZ = input("Enter Hz (0 to 2000): ")
    # pasamos los valores a integer
    pwm = int(PWM)
    hz = int(HZ)
    # enviamos el sonido
    pwm_led = GPIO.PWM(pin, hz)
    pwm_led.start(pwm)
