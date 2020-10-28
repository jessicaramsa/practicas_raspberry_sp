import RPi.GPIO as GPIO
from tkinter import *
 
def destroy():
    return root.destroy()
 
def Sonido():    
    try:
        while 1:
            PWM = int(ventana2.get())
            HZ = int(ventana4.get())
            print("Ciclo: ", PWM)
            print("Frecuencia: ", HZ)
            pwm_led=GPIO.PWM(pin_buzz, HZ)
            pwm_led.start(PWM)
    except KeyboadInterrupt:
        # CTRL+C
        print("\n Interrupción por teclado")
    except:
        print("Otra interrupción")
    finally:
        GPIO.cleanup()

pin_buzz=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_buzz,GPIO.OUT)
root = Tk()
root.geometry('400x200')
frame = Frame(raiz, width=1000, height=500)
frame.pack() 

 
ventana1 = Label(frame, text="Ingresa el ciclo de trabajo (1 a 99):", width=17)
ventana1.grid(row=0, column=0)
ventana2 = Entry(frame, width=17)
ventana2.grid(row=0, column=1)

ventana3 = Label(frame,text="Ingresa la frecuencia en Hz(0 a 2000):",width=17)
ventana3.grid(row=1, column=0)
ventana4 = Entry(frame, width=17)
ventana4.grid(row=1, column=1)
  
#--------------------------------Boton Sonido-------------------------------------------#
boton = Button(frame, text="Obtener", command=Sonido, width=17)
boton.grid(row=10, column=1)
 
#-------------------------------Boton de salir----------------------------------------------#
boton = Button(frame, text="salir", command=destroy, width=17)
boton.grid(row=10, column=2)
#------------------------------------------------------------------------------------#


 
root.mainloop()
