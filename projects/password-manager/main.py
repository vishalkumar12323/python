from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import string
import pyperclip

def generate_password():
    letters = list(string.ascii_letters)  # a-z + A-Z
    numbers = list(string.digits)         # 0-9
    symbols = list('!#$%&()*+')

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 5))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 5))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def save_credenial():
    website_label = website_entry.get()
    email_label = email_entry.get()
    password_label = password_entry.get()
    
    if len(website_label) == 0 or len(password_label) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any field empty.")
        return
    is_ok = messagebox.askokcancel(title=website_label, message=f"These are the details entered:\nEmail: {email_label}\nPassword: {password_label}\nIs it ok to save?")
    if is_ok:
        data = f"{website_label} | {email_label} | {password_label}\n"
        with open("./data.txt", "a") as file:
            file.write(data)

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()
    else:
        return

window = Tk()
window.title("Password Manager")
window.config(bg="white", padx=50, pady=50)
# setup logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# setup labels
website_label = Label(text="Website", pady=5)
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# buttons
generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, pady=5, command=save_credenial)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()