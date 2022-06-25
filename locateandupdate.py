from turtle import Turtle


class LocateAndUpdate(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0

    def state_on_map(self, xcor, ycor, state):
        self.goto(xcor, ycor)
        self.write(state, align="center", font=("Courier", 8, "normal"))

    def and_refresh_score(self):
        self.score += 1
