##Ejercicio 7 - Reloj Prog. Orientada a Objetos
import tkinter as tk
import time

class App():
    def _init_(self):
        self.root=tk.Tk()
        self.label=tk.Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now=time.strtime("%d%m%y%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, update_clock)

app=App()
