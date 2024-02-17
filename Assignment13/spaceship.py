import random
import arcade

class Spaceship(arcade.Sprite):
    def __init__(self, w, name):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x = w // 2
        self.center_y = 100
        self.width = 55
        self.height = 55
        self.name = name 
        self.speed = 2
        self.move_left = False
        self.move_right = False

class Enemy(arcade.Sprite):
    def __init__(self, w, h, name):
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        self.angle = 180
        self.center_x = random.randint(0, w)  # Random x-coordinate
        self.center_y = h  # Set initial y-coordinate to the top of the screen
        self.width = 45
        self.height = 45
        self.name = name 
        self.speed_x = 0  # Horizontal movement
        self.speed_y = -random.uniform(0.5, 1)  # downward movement
        self.move_left = False
        self.move_right = False

    def move(self):
        self.center_x += self.speed_x
        self.center_y += self.speed_y

class Game(arcade.Window):
    def __init__(self):
        screen_width, screen_height = arcade.get_display_size()
        window_width = screen_width // 2
        window_height = screen_height -100
        super().__init__(width=window_width, height=window_height, title="SpaceShip 2024")

        # Calculate the position of the window to center it on the screen
        window_position_x = (screen_width - window_width) // 2
        window_position_y = (screen_height - window_height) // 2
        self.set_location(window_position_x, window_position_y)

        arcade.set_background_color(arcade.color.DARK_IMPERIAL_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")

        self.me = Spaceship(window_width, "me")
        self.enemies = arcade.SpriteList()

        # Timer for enemy spawning
        self.enemy_spawn_timer = 0
        self.enemy_spawn_interval = 6  # Spawn every 6 seconds
        self.enemy_spawn_count = 2  # Number of enemies to spawn simultaneously

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.me.draw()
        self.enemies.draw()

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

        # Update enemy movement
        for enemy in self.enemies:
            enemy.move()

        # Spawn enemies
        self.enemy_spawn_timer += delta_time
        if self.enemy_spawn_timer >= self.enemy_spawn_interval:
            self.spawn_enemy()
            self.enemy_spawn_timer = 0

    def spawn_enemy(self):
        for _ in range(self.enemy_spawn_count):
            enemy = Enemy(self.width, self.height, "enemy")
            self.enemies.append(enemy)

window = Game()
arcade.run()
