import arcade

class Bullet(arcade.Sprite):
    def __init__(self, position_x, position_y):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.center_x = position_x
        self.center_y = position_y
        self.change_y = 5