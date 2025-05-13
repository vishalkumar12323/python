from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

root_window = Tk()
root_window.title("Pomodoro")
root_window.config(padx=150, pady=75, bg=YELLOW)

label = Label()
label.config(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=2)


start_button = Button()
start_button.config(text="start", padx=10, pady=3, font=(FONT_NAME, 12), fg="black")
start_button.grid(column=0, row=3)

reset_button = Button()
reset_button.config(text="reset", padx=10, pady=3, font=(FONT_NAME, 12), fg="black")
reset_button.grid(column=2, row=3)


completed_task = Label()
completed_task.config(text="✔️", font=(FONT_NAME, 15, 'bold'), fg=GREEN)
completed_task.grid(column=1, row=4)

root_window.mainloop()