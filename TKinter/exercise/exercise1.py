from tkinter import *
from tkinter import ttk

app = Tk()
app.minsize(width=600, height=350)

# app label
label = ttk.Label(text="This is a Label".title(), foreground="purple", font=("Dank Mono", 20, "bold"))
label.pack()

app.mainloop()