from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_len=5)
        self.right(90)

    def up(self):
        self.backward(25)

    def down(self):
        self.forward(25)
