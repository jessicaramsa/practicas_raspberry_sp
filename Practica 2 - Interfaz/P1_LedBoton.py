##Ejercicio 1 - Led con boton
import RPi.GPIO as GPIO
from tkinter import *

def Ledonoff():
    global prendido
    prendido = not prendido
    GPIO.output(gpiopin, prendido)

gpiopin = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpiopin, GPIO.OUT)
prendido = False

root = Tk()
btn_led = Button(root, text="Led", command=Ledonoff)
btn_led.pack()
root.mainloop()
GPIO.cleanup()
