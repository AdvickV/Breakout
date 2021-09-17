import random
import turtle
from turtle import *


class BlocksManager:
    def __init__(self):
        self.YELLOW_BLOCKS = []
        self.GREEN_BLOCKS = []
        self.ORANGE_BLOCKS = []
        self.RED_BLOCKS = []
        self.x = -372

        # Create yellow blocks
        self.y = 10
        for i in range(11):
            yellow_block = Turtle()
            yellow_block.shape("square")
            yellow_block.color("yellow")
            yellow_block.penup()
            yellow_block.goto(x=self.x, y=self.y)
            yellow_block.shapesize(stretch_wid=1.5, stretch_len=3.4)
            self.x += 74
            self.YELLOW_BLOCKS.append(yellow_block)
        self.x = -372

        # Create green blocks
        self.y = 45
        for i in range(11):
            green_block = Turtle()
            green_block.shape("square")
            green_block.color("green")
            green_block.penup()
            green_block.goto(x=self.x, y=self.y)
            green_block.shapesize(stretch_wid=1.5, stretch_len=3.4)
            self.x += 74
            self.GREEN_BLOCKS.append(green_block)
        self.x = -372

        # Create orange blocks
        self.y = 80
        for i in range(11):
            orange_block = Turtle()
            orange_block.shape("square")
            orange_block.color("orange")
            orange_block.penup()
            orange_block.goto(x=self.x, y=self.y)
            orange_block.shapesize(stretch_wid=1.5, stretch_len=3.4)
            self.x += 74
            self.ORANGE_BLOCKS.append(orange_block)
        self.x = -372

        # Create red blocks
        self.y = 115
        for i in range(11):
            red_block = Turtle()
            red_block.shape("square")
            red_block.color("red")
            red_block.penup()
            red_block.goto(x=self.x, y=self.y)
            red_block.shapesize(stretch_wid=1.5, stretch_len=3.4)
            self.x += 74
            self.RED_BLOCKS.append(red_block)

    def remove_block(self, block, b_color):
        block.hideturtle()
        if b_color == "YELLOW":
            self.YELLOW_BLOCKS.remove(block)
        if b_color == "GREEN":
            self.GREEN_BLOCKS.remove(block)
        if b_color == "ORANGE":
            self.ORANGE_BLOCKS.remove(block)
        if b_color == "RED":
            self.RED_BLOCKS.remove(block)



