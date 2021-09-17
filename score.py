from turtle import Turtle


FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.write_score()

    def get_high_score(self):
        with open("highscore.txt") as file:
            return file.read()

    def write_score(self):
        self.clear()
        self.goto(-310, 260)
        self.write(f'Score: {self.score}', align='center', font=FONT)

        self.goto(0, 260)
        high_score = self.get_high_score()
        self.write(f'High Score: {high_score}', align='center', font=FONT)

    def game_over(self):
        if self.score > int(self.get_high_score()):
            with open("highscore.txt", "w") as file:
                file.write(str(self.score))
        self.write_score()

        self.goto(0, -200)
        self.write("GAME OVER", align='center', font=FONT)


