from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard
import random
import time


class GameUI:

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=1000, height=800)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)

        self.velocity = 0.003
        self.snake = GameUI.set_snake()

        self.food = Food()

        self.scoreboard = ScoreBoard()
        self.populateFood()

        self.set_keylistener()
        self.screen.listen()

    @staticmethod
    def set_snake():
        return Snake()

    def set_keylistener(self):
        self.screen.onkeypress(key="w", fun=self.snake.facenorth)
        self.screen.onkeypress(key="s", fun=self.snake.facesouth)
        self.screen.onkeypress(key="a", fun=self.snake.facewest)
        self.screen.onkeypress(key="d", fun=self.snake.faceeast)

    def populateFood(self):
        x = random.randint(-450, 450)
        y = random.randint(-350, 330)
        self.food.reposition(x,y)

    def isSnakeNearFood(self):
        distance = self.snake.head.distance(self.food)
        if distance < 15:
            return True
        return False

    def snakeEatFood(self):
        self.snake.add_bodypart()
        self.populateFood()
        self.scoreboard.increase_score()
        self.velocity += 0.001
    def game_over(self):
        if self.snake.detect_bodycollision() or self.snake.detect_border():
            return True
        return False

    def run(self):
        while True:
            if not self.game_over():
                time.sleep(0.06 - self.velocity)
                self.snake.move()

                if self.isSnakeNearFood():
                    self.snakeEatFood()

            self.screen.update()
