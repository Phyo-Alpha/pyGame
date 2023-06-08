from turtle import Turtle


class Snake():

    def __init__(self):
        self.snake = []
        self.create_snakebody()
        self.head = self.snake[0]

    def create_snakebody(self):
        for i in range(5):
            snake_part = Turtle()
            snake_part.penup()
            snake_part.shape("circle")
            snake_part.color("pink")
            snake_part.goto(i * -20, 0)
            self.snake.append(snake_part)

    def add_bodypart(self):
        snake_part = Turtle()
        snake_part.penup()
        snake_part.shape("circle")
        snake_part.color("pink")
        self.snake.append(snake_part)

    def detect_bodycollision(self):
        head_position = self.head.position()
        for body_part in self.snake[1:]:
            if body_part.distance(head_position) < 10:
                return True
        return False

    def detect_border(self):
        x = self.head.xcor()
        y = self.head.ycor()
        screen_width = 950 / 2
        screen_height = 750 / 2

        if x > screen_width or x < -screen_width or y > screen_height or y < -screen_height:
            return True
        return False

    def facenorth(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def facewest(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def faceeast(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def facesouth(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)

        self.head.forward(20)

