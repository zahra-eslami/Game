import arcade
from ball import Ball
from rocket import Rocket

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1000,height=600,title="Pong 2024(❁´◡`❁)")
        arcade.set_background_color(arcade.color.DARK_CERULEAN)
        self.player_1=Rocket(40,self.height//2,
                             arcade.color.PERSIAN_ROSE,"Zahra")
        self.player_2=Rocket(self.width-40,self.height//2,
                             arcade.color.YELLOW_ROSE,"AI")      

        self.player_1_lives = 5
        self.heart_symbol = "♥️"
        self.ball=Ball(self)
        self.game_over = False

    def on_draw(self):
        arcade.start_render()

        arcade.draw_rectangle_outline(self.width//2,self.height//2,
                                      self.width-20,self.height-20,
                                      arcade.color.BLANCHED_ALMOND,border_width=10)
        
        if not self.game_over:
            # Draw  simple line
            # arcade.draw_line(self.width//2,30,self.width//2,self.height-30,
            #                  color=arcade.color.BLANCHED_ALMOND,line_width=10)
            
            # Draw dashed line
            line_length = self.height - 60  
            dash_length = 10  
            gap_length = 10  
            num_dashes = int(line_length / (dash_length + gap_length))

            for i in range(num_dashes):
                start_x = self.width // 2
                start_y = 30 + i * (dash_length + gap_length)
                end_x = start_x
                end_y = start_y + dash_length
                arcade.draw_line(start_x, start_y, end_x, end_y,
                                color=arcade.color.BLANCHED_ALMOND, line_width=10)
                
            arcade.draw_text(f"Player 1 Score: {self.player_1.score}", self.width // 4, self.height - 40,
                            arcade.color.WHITE, 20, anchor_x="center")
            arcade.draw_text(f"Player 2 Score: {self.player_2.score}", 3 * self.width // 4, self.height - 40,
                            arcade.color.WHITE, 20, anchor_x="center")
            
            for i in range(self.player_1_lives):
                arcade.draw_text(self.heart_symbol+" ", 20 + i * 30, 20,
                                arcade.color.RED, 24)
        else:
            arcade.draw_text("Game Over!", self.width // 2, self.height // 2,
                         arcade.color.RED, 50, anchor_x="center")
            arcade.draw_text(f"Player 1 Score: {self.player_1.score}", self.width // 2, self.height // 2 - 40,
                            arcade.color.WHITE, 20, anchor_x="center")
            arcade.draw_text(f"Player 2 Score: {self.player_2.score}", self.width // 2, self.height // 2 - 80,
                            arcade.color.WHITE, 20, anchor_x="center")


        self.player_1.draw()
        self.player_2.draw()
        self.ball.draw()

        arcade.finish_render()

    def on_mouse_motion(self, x:int, y:int,dx:int,dy:int):
        # self.player_1.center_x=x
        if self.player_1.height-55<y<self.height-self.player_1.height+55:
          self.player_1.center_y=y

    def on_update(self, delta_time: float):
        if self.game_over:
            self.ball.kill()
            return
        
        self.ball.move()
        self.player_2.move(self, self.ball)

        if self.ball.center_y < 30 or self.ball.center_y > self.height - 30:
            self.ball.change_y *= -1 

        if arcade.check_for_collision(self.player_1, self.ball) or \
                arcade.check_for_collision(self.player_2, self.ball):
            self.ball.change_x *= -1

        if self.ball.center_x < 0:
            self.player_2.score += 1
            self.player_1_lives -= 1
            del self.ball
            self.ball = Ball(self)
            if self.player_1_lives == 0:
                self.game_over = True

        if self.ball.center_x > self.width:
            self.player_1.score += 1
            del self.ball
            self.ball = Ball(self)

def main():
    game = Game()
    arcade.run()

if __name__ == "__main__":
    main()
