import tkinter as tk

window = tk.Tk()
window.title("Welcome, continue to login")
window.minsize(width=500, height=300)
form_label = tk.Label(text="Email or username")
form_label.grid(column=0, row=0)

def retrieve_input():
    input_value = entry.get()
    form_label.config(text=input_value)

entry = tk.Entry(window, width=20)
entry.grid(column=5, row=5)

button = tk.Button(window, text="Change Label", background="black", foreground="white", command=retrieve_input)
button.grid(column=2, row=2)


button1 = tk.Button(window, text="New Button", background="purple", foreground="black")
button1.grid(column=3, row=0)
window.mainloop()
