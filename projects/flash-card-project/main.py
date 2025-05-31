from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#b1ddc6"

df = pd.read_csv('./data/french_words.csv')
words_dict = df.to_dict(orient="records")

current_dict = {}

def next_card():
    global current_dict, flip_timer
    window.after_cancel(flip_timer)
    current_dict = random.choice(words_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_dict['French'], fill="black")
    canvas.itemconfig(card_image, image=card_front_image)

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_dict['English'], fill="white")  


window = Tk()
window.title('Flash Card')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526)

card_front_image = PhotoImage(file='./images/card_front.png')
card_back_image = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40))
card_word = canvas.create_text(400, 263, text="", font=('Ariel', 60, "bold"))
cross_image = PhotoImage(file='./images/wrong.png')
unkonwn_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unkonwn_button.grid(row=1, column=0)

check_image = PhotoImage(file='./images/right.png')
unkonwn_button = Button(image=check_image, highlightthickness=0, command=next_card)
unkonwn_button.grid(row=1, column=1)


next_card()
window.mainloop()