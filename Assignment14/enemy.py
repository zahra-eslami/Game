import arcade
import random

class Enemy(arcade.Sprite):
    def __init__(self, w, h, name):
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        self.angle = 180
        self.center_x = random.randint(0, w)  # Random x-coordinate
        self.center_y = h  # Set initial y-coordinate to the top of the screen
        self.width = 35
        self.height = 35
        self.name = name 
        self.speed_x = 0  # Horizontal movement
        self.speed_y = -random.uniform(0.5, 1)  # downward movement
        self.move_left = False
        self.move_right = False

    def move(self):
        self.center_x += self.speed_x
        self.center_y += self.speed_y