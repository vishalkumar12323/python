from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import string
import pyperclip
import json


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


def search_password():
    website_name = website_entry.get()
    if len(website_name) != 0:
        with open("data.json", 'r') as data_file:
            data = json.load(data_file)
            try:
                result = data[website_name]
            except KeyError:
                messagebox.showerror(title="Not found error ", message=f'email with password does not found for the website {website_name}.')
                return
            else:
                messagebox.showinfo(title='password fetched', message=f"{website_name} website email or password.\n Email: {result['email']}\n, Password: {result['password']}.")
    else:
        messagebox.showerror(title="Error ", message="Please enter the website name that you want to search email or password.")
        return


def save_credenial():
    website_label = website_entry.get()
    email_label = email_entry.get()
    password_label = password_entry.get()
    
    if len(website_label) == 0 or len(password_label) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any field empty.")
        return
    else:
        new_data = {website_label: {
            'email': email_label,
            "password": password_label
        }}
        try:
            with open("./data.json", "r") as read_file:
                data = json.load(read_file)

        except FileNotFoundError as err:
            with open("./data.json", 'w') as write_file:
                json.dump(new_data, write_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

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
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text="Search Password", command=search_password)
search_button.grid(row=1, column=2)
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