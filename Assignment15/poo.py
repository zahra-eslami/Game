import arcade
import random
import os


current_directory = os.path.dirname(os.path.abspath(__file__))

class Poo(arcade.Sprite):
    def __init__(self, game):
        super().__init__(current_directory + "/poo.png")
        self.width = 35
        self.height = 35
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)
        self.change_x = 0
        self.change_y = 0