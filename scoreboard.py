from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-250, 250)
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT, align="left")

    def update_level(self):
        self.level += 1
        self.write_level()

    def write_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align="center")
