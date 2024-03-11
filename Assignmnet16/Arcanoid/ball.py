import random
import os
import arcade

current_directory = os.path.dirname(os.path.abspath(__file__))

class Ball(arcade.Sprite):
    def __init__(self, game):
        super().__init__(current_directory + "/ball.png")
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.change_x = random.choice([-1, 1])
        self.change_y = random.choice([-1, 1])
        self.speed = 5
        self.width = 30
        self.height = 30

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

        if self.center_x < self.width // 2 or self.center_x > 600 - self.width // 2:
            self.change_x *= -1

        if self.center_y > 700 - self.height // 2:
            self.change_y *= -1