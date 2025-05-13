from tkinter import *
from tkinter import ttk


root = Tk()
root.minsize(width=500, height=300)
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Entry(frm, width=10).grid(column=0, row=2)
root.mainloop()