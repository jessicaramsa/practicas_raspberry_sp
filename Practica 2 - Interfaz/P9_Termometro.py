##Ejercicio 9 - Termometro
import RPI.GPIO as GPIO
from tkinter import *
import time
from tkinter import PhotoImage
from tkinter import Canvas
import Adafruit_DHT

def Termometro():
    humidity, temperature=Dht11()
    selection = "Humedad"+str(humidity)
    labelhumedad.config(text=selection)
    selection = "Temperatura"+str(temperature)
    labeltemperatura.config(text=selection)
    print("Humedad",humidity)
    print("Temperatura",temperature)
    temperature=40-temperature
    canvastermometro.create_line(79,44,79,235,width=10,fill='white')
    canvastermometro.create_line(79,40+temperature*4.875,79,235,width=10,fill='red')
    root.after(100,Termometro)

def Dht11():
    sensor=Adafruit_DHT.DHT11
    return Adafruit_DHT.read_retry(sensor, gpiotemp)

def IniciarPines():
    GPIO.setmode(GPIO.BCM)
    
gpiotemp=2
IniciarPines()
root=Tk()
termoimagen=PhotoImage(file="termometro.gif")
canvastermometro.create_image(20,20,image=termoimagen,anchor=NW)
canvastermometro.pack()
labeltemperatura=Label(root)
labeltemperatura.pack()
labelhumedad=Label(root)
labelhumedad.pack()
Termometro()
root.mainloop()
GPIO.cleanup()
