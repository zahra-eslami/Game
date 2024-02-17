import arcade

class Spaceship(arcade.Sprite):
    def __init__(self, w, name):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x = w // 2
        self.center_y = 100
        self.width = 60
        self.height = 60
        self.name = name 
        self.speed = 5 
        self.move_left = False
        self.move_right = False

class Enemy(arcade.Sprite):
    def __init__(self, w, name):
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        self.angle = 180
        self.center_x = w // 2 -100
        self.center_y = w //2 
        self.width = 60
        self.height = 60
        self.name = name 
        self.speed = 5 
        self.move_left = False
        self.move_right = False


class Game(arcade.Window):
    def __init__(self):
        screen_width, screen_height = arcade.get_display_size()
        window_width = screen_width - 300
        window_height = screen_height - 200
        super().__init__(width=window_width, height=window_height, title="SpaceShip 2024")

        # Calculate the position of the window to center it on the screen
        window_position_x = (screen_width - window_width) // 2
        window_position_y = (screen_height - window_height) // 2
        self.set_location(window_position_x, window_position_y)

        arcade.set_background_color(arcade.color.DARK_IMPERIAL_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")

        self.me = Spaceship(self.width, "me")
        self.enemy=Enemy(self.width, "enemy")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.me.draw()
        self.enemy.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.me.move_left = True
        elif symbol == arcade.key.RIGHT:
            self.me.move_right = True
 
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.me.move_left = False
        elif symbol == arcade.key.RIGHT:
            self.me.move_right = False

    def on_update(self, delta_time):
        if self.me.move_left:
            self.me.center_x -= self.me.speed
        elif self.me.move_right:
            self.me.center_x += self.me.speed

if __name__ == "__main__":
    window = Game()
    arcade.run()
