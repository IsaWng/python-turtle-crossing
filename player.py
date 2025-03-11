from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.back_to_starting_point()
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def back_to_starting_point(self):
        self.goto(STARTING_POSITION)

    def is_finish_game(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
