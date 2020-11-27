from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

def acopiar():
    editor.clipboard_clear()
    editor.clipboard_append(editor.selection_get())

def apegar():
    editor.insert(INSERT, editor.clipboard_get())


def anuevo():
    editor.delete(1.0,END)

def aabrir():
    documento = askopenfile(filetypes=[("Archivo de texto","*.txt")])
    if documento != None:
        editor.insert(1.0, documento.read())

def aguardar():
    documento = asksaveasfile(filetypes=[("Archivo de texto","*.txt")])
    print(documento.write(editor.get(1.0, END)))

if __name__ == "__main__":
    ventana = Tk()
    menubar = Menu(ventana)
    archivo = Menu(menubar, tearoff=0)
    archivo.add_command(label="Nuevo", command=anuevo)
    archivo.add_command(label="Abrir", command=aabrir)
    archivo.add_command(label="Guardar", command=aguardar)
    archivo.add_command(label="Salir", command=ventana.quit)
    menubar.add_cascade(label="Notas", menu=archivo)

    editar = Menu(menubar, tearoff=0)
    editar.add_command(label="Copiar", command=acopiar)
    editar.add_command(label="Pegar", command=apegar)
    menubar.add_cascade(label="Edición", menu=editar)

    editor = Text(ventana, undo="true")
    editor.pack(side=TOP, fill=BOTH, expand=1)

    ventana.title("Bloc de notas")
    ventana.geometry("695x424")
    ventana.config(menu=menubar)
    ventana.mainloop()
