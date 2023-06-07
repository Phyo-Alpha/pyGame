from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
    
    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
    
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
    
    def detect_collision(self, paddle):
        if self.distance(paddle) <= 20:
            self.bounce_x()
    
    def check_border(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()
        
        if self.xcor() > 380 or self.xcor() < -380:
            self.bounce_x()
        
        