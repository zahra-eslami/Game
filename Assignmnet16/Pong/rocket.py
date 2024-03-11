import arcade

class Rocket(arcade.Sprite):
    def __init__(self,x,y,c,n):
        super().__init__()
        self.center_x=x
        self.center_y=y
        self.color=c
        self.name=n
        self.change_x=0
        self.change_y=0
        self.width=20
        self.height=140
        self.speed=4
        self.score=0

    def move(self, game, ball):
        if ball.center_x > game.width // 2:
            if self.height - 55 < ball.center_y < game.height - self.height + 55:
                self.center_y = ball.center_y
            else:
                if ball.center_y < self.height - 55:
                    self.center_y = self.height - 55
                elif ball.center_y > game.height - self.height + 55:
                    self.center_y = game.height - self.height + 55

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,
                                     self.width,self.height,self.color)
