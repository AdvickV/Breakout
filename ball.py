from turtle import *


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y = 10
        self.x = 10
        self.move_speed = 0.1
        self.cons_hits = 0
        self.goto(0, -260)

    def move_ball(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1

    def increase_speed(self):
        self.move_speed *= 1
