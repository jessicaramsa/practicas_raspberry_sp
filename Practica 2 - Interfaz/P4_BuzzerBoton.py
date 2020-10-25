##Ejercicio 4 - Buzzer con boton
from tkinter import *
from gpiozero import Buzzer

def RuidoBuzzer():
    global bz
    global ruido
    if ruido:
        bz.off()
    else:
        bz.on()
    ruido=not ruido

gpiobuzzer=16
bz=Buzzer(gpiobuzzer)
ruido=False
root=Tk()
btn_Buz16=Button(root, text="RuidoBuzzer",command=RuidoBuzzer)
btn_Buz16.pack()
root.mainloop()
GPIO.cleanup()
