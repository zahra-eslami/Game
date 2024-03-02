import arcade

class Snake(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.width=28
        self.height=28
        self.radius = 16
        self.center_x=game.width//2
        self.center_y=game.height//2
        self.color=arcade.color.PINE_GREEN
        self.change_x=0
        self.change_y=0
        self.speed=1.5
        self.score=0
        self.body=[] 
        self.body_colors = [arcade.color.RED,  arcade.color.GREEN]
    
    def eat(self,food):
        del food 
        # print("score:",self.score)   
       
    def move(self): 
        self.body.append({'x':self.center_x,'y':self.center_y})   
        if len(self.body)>self.score*4:
            self.body.pop(0)

        self.center_x += self.change_x*self.speed
        self.center_y += self.change_y*self.speed

    # def draw(self):
    #     arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)
    #     # arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)

    #     for part in self.body:
    #         # arcade.draw_rectangle_filled(part['x'],part['y'],self.width,self.height,self.color)

    #         arcade.draw_circle_filled(part['x'], part['y'], self.radius, self.color)
    
    def draw(self):
        # Draw the head of the snake with green color
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, arcade.color.GREEN)

        # Draw the body segments alternating between red and green
        for i, part in enumerate(self.body):
            if i % 2 == 0:
                color = arcade.color.RED
            else:
                color = arcade.color.GREEN
            
            arcade.draw_circle_filled(part['x'], part['y'], self.radius, color)