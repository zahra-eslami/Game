import random
import os
import arcade

current_directory = os.path.dirname(os.path.abspath(__file__))

class Ball(arcade.Sprite):
    def __init__(self,game):
        super().__init__(current_directory + "/ball (2).png")
        self.center_x=game.width//2
        self.center_y=game.height//2
        self.color=arcade.color.GREEN
        self.change_x=random.choice([-1,1])
        self.change_y=random.choice([-1,1])
        self.speed=5
        self.width = 44
        self.height = 44

    def move(self):
        self.center_x+=self.change_x*self.speed
        self.center_y+=self.change_y*self.speed