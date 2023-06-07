from turtle import Screen as s
from paddle import Paddle

class GameUIControl():
    
    def __init__(self):
        self.screen = s()
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Pong")
        self.screen.tracer(0)
        
        self.setUpPaddle()
    
    def setUpPaddle(self):
        self.paddle1 = Paddle()
        self.paddle1.goto(-350, 0)
        
        self.paddle2 = Paddle()
        self.paddle2.goto(350, 0)
        
        self.screen.listen()
        self.screen.onkeypress(self.paddle1.go_up, "w")
        self.screen.onkeypress(self.paddle1.go_down, "s")
        self.screen.onkeypress(self.paddle2.go_up, "Up")
        self.screen.onkeypress(self.paddle2.go_down, "Down")
        
    def run(self):
        while True:
            self.screen.update()