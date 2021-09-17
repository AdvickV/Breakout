from turtle import *


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("deep sky blue")
        self.penup()
        self.goto(x=0, y=-280)
        self.shapesize(stretch_wid=0.5, stretch_len=4)

    def go_left(self):
        new_x = self.xcor() - 20
        self.setx(new_x)

    def go_right(self):
        new_x = self.xcor() + 20
        self.setx(new_x)
