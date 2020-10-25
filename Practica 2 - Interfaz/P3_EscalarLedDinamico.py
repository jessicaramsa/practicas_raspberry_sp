##Ejercicio 3 - Escalar Led Dinamico
import RPI.GIO as GPIO
from tkinter import *

def Valor():
    selection="Intensidad= "+str(var.get())
    labelintensidad.config(text==selection)
    led.ChangeDutyCycle(var.get())
    root.after(500, Valor)

def IniciarPines():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledpwn, GPIO.OUT)

ledpwn=18
IniciarPines()
led=GPIO.PWM(gpiopin, 100)
led.start(0)
root=Tk()
var=DoubleVar()
scale=Scale(root, variable=var)
scale.pack(anchor=CENTER)
labelintensidad=Label(root)
labelintensidad.pack()
Valor()
root.mainloop()
led.stop()
GPIO.cleanup()
