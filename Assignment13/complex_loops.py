import arcade

class DiamondGrid(arcade.Window):
    def __init__(self):
        super().__init__(width=400, height=400, title="Diamond Grid")
        self.diamond_width = 15    
        self.diamond_height = 15    
        self.diamond_spacing = 8
        self.RED = arcade.color.RED
        self.BLUE = arcade.color.BLUE
        arcade.set_background_color(arcade.color.FLORAL_WHITE)

    def draw_diamond(self, center_x, center_y, width, height, color):
        points = ((center_x - width / 2, center_y),
                  (center_x, center_y + height / 2),
                  (center_x + width / 2, center_y),
                  (center_x, center_y - height / 2))
        arcade.draw_polygon_filled(points, color)

    def on_draw(self):
        arcade.start_render()

        for i in range(0, self.width, self.diamond_width + self.diamond_spacing):
            for j in range(0, self.height, self.diamond_height + self.diamond_spacing):
                if (i // (self.diamond_width + self.diamond_spacing) % 2 == j // (self.diamond_height + self.diamond_spacing) % 2):
                    color = self.RED 
                else:
                    color = self.BLUE

                self.draw_diamond(i + self.diamond_width / 2, j + self.diamond_height / 2, self.diamond_width, self.diamond_height, color)

diamond_grid = DiamondGrid()
arcade.run()
