##Ejercicio 5 - Servo con boton
'''from tkinter import *
from gpiozero import Servo

def ServoMotor():
    global abierto
    
    if abierto:
        sermot.angle = 0
        servoEtqBoton = "Abrir"
    else:
        sermot.angle = 90
        servoEtqBoton = "Cerrar"
        
    btn_servo.configure(text=servoEtqBoton)
    abierto = not ruido

gpioservo = 25
abierto = False
sermot = Servo(gpioservo)
root = Tk()
btn_servo=Button(root, text="Abrir", command=ServoMotor)
btn_servo.pack(anchor=CENTER)
root.mainloop()'''

from gpiozero import Servo
from time import sleep

servo = Servo(25)

while True:
    servo.mid()
    print("mid")
    sleep(0.5)
    servo.min()
    print("min")
    sleep(1)
    servo.mid()
    print("mid")
    sleep(0.5)
    servo.max()
    print("max")
    sleep(1)