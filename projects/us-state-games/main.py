import pandas as pd
from turtle import Screen, Turtle

def init():
    map_screen = Screen()
    map_screen.title("U.S. States Game")
    map_screen.bgpic("blank_states_img.gif")
    df = pd.read_csv("50_states.csv")
    states = df['state'].to_list()
    guessed_state = []


    while len(guessed_state) < 50:
        user_ans = map_screen.textinput(title=f"{len(guessed_state)}/50 States correct", prompt="What's another state name?").title()

        if user_ans == "Exit":
            # using list-comprehension 
            missing_states = [state for state in states if state not in guessed_state]
            # for state in states:
            #     if state not in guessed_state:
            #         missing_states.append(state)

            data_dict = {
                "missing_state": missing_states
            }
            pd.DataFrame(data_dict).to_csv("./result.csv")
            break
        if user_ans in states:
            guessed_state.append(user_ans)
            pen = Turtle()

            coordinates = df[df["state"] == user_ans][['x', 'y']].values[0]
            x = coordinates[0]
            y = coordinates[1]

            pen.hideturtle()
            pen.penup()
            pen.goto(x=x, y=y)
            pen.write(user_ans, align="center", font=("Sans serif", 11, "normal"))
            pen.pendown()
 

init()