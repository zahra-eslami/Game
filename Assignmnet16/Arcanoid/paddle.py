import os
import arcade

current_directory = os.path.dirname(os.path.abspath(__file__))

class Paddle(arcade.Sprite):
    def __init__(self, x, y, c, n):
        super().__init__(current_directory + "/paddle.png")
        self.center_x = x
        self.center_y = y
        self.color = c
        self.name = n
        self.width = 150
        self.height = 30
        self.score = 0

    def move(self, x):
        self.center_x = x

    def check_collision(self, ball):
        if arcade.check_for_collision(self, ball):
            ball.change_y *= -1