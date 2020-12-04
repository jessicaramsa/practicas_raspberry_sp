from tkinter import *
from PIL import Image, ImageTk # pip install pillow
import time

class Slider:
    def __init__(self, root):
        self.root = root
        self.root.title("Slider")
        self.root.geometry("1350x700+0+0")

        # get array
        self.image1 = ImageTk.PhotoImage(file="imgs/image_1.jpg")
        self.image2 = ImageTk.PhotoImage(file="imgs/image_2.jpg")

        Frame_slider = Frame(self.root)
        Frame_slider.place(x=150, y=50, width=1100, height=500)
        self.label1 = Label(Frame_slider, image=self.image1)
        self.label1.place(x=0, y=0)
        self.label2 = Label(Frame_slider, image=self.image2)
        self.label2.place(x=0, y=0)

        self.x = 1100
        self.sliding()
    
    def sliding(self):
        self.x-=1
        if self.x == 0:
            self.x = 1100
            time.sleep(1)

            self.new_image = self.image1
            self.image1 = self.image2
            self.image2 = self.new_im

            self.label1.config(image=self.image1)
            self.label2.config(image=self.image2)
        self.label2.place(x=self.x, y=0)
        self.label2.after(1, self.sliding)

root = Tk()
app = Slider(root)
root.mainloop()
