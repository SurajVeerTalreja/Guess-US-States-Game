import turtle
import pandas
from locateandupdate import LocateAndUpdate

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()


locate = LocateAndUpdate()

guessed_states = []
states_to_learn = []

while True:
    answer_state = screen.textinput(title=f"{locate.score}/50 Correct States",
                                    prompt="Guess the next state's name").title()

    if answer_state == "Exit":
        break

    # check if any row contains the entered state by user
    if (data.state == answer_state).any():
        guessed_states.append(answer_state)
        correct_answer = data[data.state == answer_state]
        new_x = float(correct_answer.x)
        new_y = float(correct_answer.y)

        locate.state_on_map(new_x, new_y, answer_state)
        locate.and_refresh_score()

for state in all_states:
    if state not in guessed_states:
        states_to_learn.append(state)

df = pandas.DataFrame(states_to_learn)
df.to_csv("state to learn.csv")
