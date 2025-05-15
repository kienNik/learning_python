from turtle import Turtle, Screen
import time
from enum import Enum
from food import Food
from snake import Snake

class Level(float, Enum):
    EASY = 0.1
    MEDIUM = 0.05
    HARD = 0.02

class SnakeGame:
    def __init__(self):
        self.screen = Screen()
        self.snake = Snake()
        self.food = Food(self.screen.window_height())

        self.game_over = False
        self.game_over_txt = Turtle(visible=False)
        self.score_txt = Turtle(visible=False)
        self.score = 0
        self.loop_delay = Level.MEDIUM

        self.high_score = 0
        self.load_high_score()

        # init score text
        self.score_txt.penup()
        self.score_txt.sety(self.screen.window_height()/2 - 30)
        self.score_txt.write("Score: " + str(self.score) + "/" + str(self.high_score), align='center', font=("Arial", 15, "normal"))

    def load_high_score(self):
        with open('high_score.txt', 'r') as file:
            self.high_score = int(file.read())
    
    def update_high_score(self):
        with open('high_score.txt', 'w') as file:
            file.write(str(self.high_score))

    def exitonclick(self):
        self.screen.exitonclick()

    def check_input(self):
        #TODO: fix delay when turn
        self.screen.onkey(self.snake.up, 'Up')
        self.screen.onkey(self.snake.down, 'Down')
        self.screen.onkey(self.snake.right, 'Right')
        self.screen.onkey(self.snake.left, 'Left')
        self.screen.listen()

    def is_collide_food(self):
        if self.snake.body[0].distance(self.food.food.pos()) <= 20:
            self.screen.tracer(False)
            self.food.reinit()
            self.screen.tracer(True)
            self.score += 1
            if self.score > self.high_score:
                self.high_score = self.score
                self.update_high_score()

            self.score_txt.clear()
            self.score_txt.write("Score: " + str(self.score) + "/" + str(self.high_score), align='center', font=("Arial", 15, "normal"))
            return True
        return False

    def run(self):
        while not self.game_over:
            self.check_input()

            self.screen.tracer(False) # turn off animation untill complete moving
            self.snake.move()
            self.screen.tracer(True) # turn on animation

            if self.snake.is_collide_wall(self.screen.window_height()) or self.snake.is_collide_tail():
                self.game_over = True
                self.game_over_txt.write("GAME OVER", align='center', font=("Arial", 18, "bold"))
                continue
            if self.is_collide_food():
                self.snake.extend()
            time.sleep(self.loop_delay)

game = SnakeGame()
game.run()
game.exitonclick()