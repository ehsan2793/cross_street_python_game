from turtle import Turtle

FONT = ('Courier', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.level = 0
        self.goto(-270, 270)
        self.write(arg=f"Level: {self.level}", font=FONT)

    def add_score(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color('yellow')
        self.write(arg=f"Game Over", align='center', font=FONT)
