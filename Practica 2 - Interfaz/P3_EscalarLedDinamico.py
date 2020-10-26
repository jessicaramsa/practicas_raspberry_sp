##Ejercicio 3 - Escalar Led Dinamico
import RPi.GPIO as GPIO
from tkinter import *

def Valor():
    selection = f"Intensidad: {str(var.get())}"
    labelintensidad.config(text=selection)
    led.ChangeDutyCycle(var.get())
    root.after(500, Valor)

def IniciarPines(ledpwm):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledpwm, GPIO.OUT)

ledpwm = 14
IniciarPines(ledpwm)
led = GPIO.PWM(ledpwm, 100)
led.start(0)
root = Tk()
var = DoubleVar()
scale = Scale(root, variable=var)
scale.pack(anchor=CENTER)
labelintensidad = Label(root)
labelintensidad.pack()
Valor()
root.mainloop()
led.stop()
GPIO.cleanup()
