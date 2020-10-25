##Ejercicio 8 - Radar uso de Canvas
import RPI.GPIO as GPIO
from tkinter import *
import time
from tkinter import Canvas

def Hcsr04():
    GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
    GPIO.setup(GPIO_ECHO,GPIO.IN)
    GPIO.output(GPIO_TRIGGER,False)
    GPIO.output(GPIO_TRIGGER,True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER,False)
    start=time.time()
    while GPIO.input(GPIO_ECHO)==0:
        start=time.time()
    while GPIO.input(GPIO_ECHO)==1:
        stop=time.time()
        elapsed=stop-start
        distance=(elapsed*34300)/2
        print("Distancia ",distance)
    if distance>100:
        distance=100
    for i in range(0,100,10):
        canvasdistancia.create_arc(200-i,200-i,10+i,10+i,start=315,extent=90,fill='green')
    canvasdistancia.create_arc(100+distance,100+distance,110-distance,100-distance,start=315,extent=90,fill='red')
    selection="Distancia= "+str(distance)
    labeldistancia.config(text=selection)
    root.after(500,Hcsr04)

def IniciarPines():
    GPIO.setup(GPIO.BCM)

GPIO_TRIGGER=8
GPIO_ECHO=7
IniciarPines()
root=Tk()
canvasdistancia=Canvas(root)
canvasdistancia.pack()
labeldistancia=Label(root)
labeldistancia.pack()
Hcsr04()
root.mainloop()
GPIO.cleanup()
