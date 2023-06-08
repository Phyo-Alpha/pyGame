from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.goto(0,0)

    def reposition(self, x, y):
        self.goto(x, y)
