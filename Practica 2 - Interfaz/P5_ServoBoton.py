##Ejercicio 5 - Servo con boton
from tkinter import *
from gpiozero import AngularServo

def ServoMotor():
    global abierto
    if abierto:
        sermot.angle=0
        servoEtqBoton="Abrir"
    else:
        sermot.angle=90
        servoEtqBoton="Cerrar"
    btn_servo.configure(text=servoEtqBoton)
    abierto=not ruido

gpioservo=16
abierto=False
sermot=Buzzer(gpioservo)
root=Tk()
btn_servo=Button(root, text="Abrir",command=ServoMotor)
btn_servo.pack(anchor=CENTER)
root.mainloop()
