import random
import arcade

from ball import Ball
from paddle import Paddle

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600, height=700, title="Breakout 2024")
        arcade.set_background_color(arcade.color.KHAKI)
        self.player = Paddle(40, 60, arcade.color.DIAMOND, "Player")
        self.ball = Ball(self)
        self.bricks = arcade.SpriteList()
        self.setup_bricks()
        self.score = 0
        self.lives = 3

        self.left_pressed = False
        self.right_pressed = False


    def setup_bricks(self):
        brick_width = 40
        brick_height = 15
        brick_spacing = 8
        rows = 5
        cols = self.width // (brick_width + brick_spacing)

        for row in range(rows):
            for col in range(cols - 1):
                brick = arcade.SpriteSolidColor(brick_width, brick_height, random.choice([
                    arcade.color.PERSIAN_ROSE, arcade.color.PERSIAN_ORANGE, arcade.color.PERSIAN_BLUE,
                    arcade.color.PERSIAN_GREEN,
                    arcade.color.PERSIAN_INDIGO, arcade.color.PERSIAN_PLUM
                ]))
                brick.center_x = brick_width // 2 + col * (brick_width + brick_spacing) + 40
                brick.center_y = self.height - brick_height // 2 - row * (brick_height + brick_spacing) - 80
                self.bricks.append(brick)


    def draw_lives(self):
        heart_icon = "♥️"
        heart_spacing = 30
        heart_x = self.width - heart_spacing-20
        heart_y = self.height - heart_spacing-15

        for _ in range(self.lives):
            arcade.draw_text(heart_icon, heart_x, heart_y, arcade.color.WHITE_SMOKE, 24)
            heart_x -= heart_spacing


    def on_draw(self):
        arcade.start_render()

        if self.lives > 0:
            arcade.draw_rectangle_outline(self.width // 2, self.height // 2, self.width - 20, self.height - 20,
                                          arcade.color.BLACK_LEATHER_JACKET, border_width=10)

            self.player.draw()
            self.ball.draw()
            self.bricks.draw()

            arcade.draw_text(f"Score: {self.score}", 20, self.height - 40, arcade.color.WHITE_SMOKE, 16)
            self.draw_lives()
        else:
            arcade.draw_text("Game Over", self.width // 2, self.height // 2,
                             arcade.color.RED, font_size=50, anchor_x="center")
            arcade.draw_text(f"Score: {self.score}", self.width // 2, self.height // 2 - 60,
                             arcade.color.RED, font_size=30, anchor_x="center")
            
        arcade.finish_render()
        

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True


    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False


    def on_mouse_motion(self, x, y, dx, dy):
        self.player.move(x)


    def on_update(self, delta_time):
        if self.lives > 0:
            if self.left_pressed:
                self.player.center_x -= 5
            elif self.right_pressed:
                self.player.center_x += 5

            self.ball.move()
            self.player.check_collision(self.ball)

            for brick in self.bricks:
                if arcade.check_for_collision(self.ball, brick):
                    brick.kill()
                    self.ball.change_y *= -1
                    self.score += 1

            if self.ball.center_y < 0:
                self.lives -= 1
                self.ball.kill()
                if self.lives > 0:
                    self.ball = Ball(self)

            if self.lives <= 0:
                self.ball.kill()
                self.ball = None  

        else:
            self.ball = None  


def main():
    game = Game()
    arcade.run()

if __name__ == "__main__":
    main()
