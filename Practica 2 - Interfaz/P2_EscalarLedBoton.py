##Ejercicio 2 - Escalar con Led
from tkinter import *
import RPi.GPIO as GPIO

def Sel():
    selection = f"Intensidad: {str(var.get())}"
    labelintensidad.config(text=selection)
    led.ChangeDutyCycle(var.get())

gpiopin = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpiopin, GPIO.OUT)
led = GPIO.PWM(gpiopin, 100)
led.start(0)
root = Tk()
var = DoubleVar()
scale = Scale(root, variable=var)
scale.pack(anchor=CENTER)

button = Button(root, text="Obtener valor del escalar", command=Sel)
button.pack(anchor=CENTER)

labelintensidad = Label(root)
labelintensidad.pack()

root.mainloop()
GPIO.cleanup()
