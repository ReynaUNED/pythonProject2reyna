import tkinter as tk
from tkinter import *

import cientifica




root = Tk ()

root.title("Calculadoras")
barramenu = Menu(root)
Calculadoras = Menu(barramenu,tearoff=0)
Calculadoras.add_command(label="Calculadora", command=Calculator)
Calculadoras.add_separator()
Calculadoras.add_command(label="salida",command=root.quit)
barramenu.add_cascade(label="calculadoras",menu =Calculadoras)

botcalculadora = Button(root,text= "ingresa",command=getInstance(Calculator))

root.config(menu=barramenu)

root.mainloop()
