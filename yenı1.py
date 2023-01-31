# -*- coding: utf-8 -*-
 
from tkinter import *
 
from tkinter import messagebox
 
pencere = Tk()
 
pencere.title("Uygulamalar")
pencere.geometry("600x400")
 
uygulama = Frame(pencere)
uygulama.grid()
 
Lb1 = Listbox(uygulama)
Lb1.insert(1, "Java")
Lb1.insert(2, "Python")
Lb1.insert(3, "CSharp")
Lb1.insert(4, "C++")
Lb1.insert(5, "Node.Js")
Lb1.grid(padx=110, pady=10)
 
pencere.mainloop()
