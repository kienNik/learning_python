from turtle import Turtle, Screen
import time
from enum import Enum

screen = Screen()
level = {'easy': 20, 'medium': 10, 'hard': 5}
screen.delay(level['medium'])


class Snake:
    def __init__(self):
        self.body: list[Turtle] = []

        # init snake's body
        for i in range(2):
            new_turtle = Turtle(shape='square')
            new_turtle.penup()
            new_turtle.setx(-i*20)
            self.body.append(new_turtle)

        self.game_over = False
        self.loop_delay = 0.05

    def check_input(self):
        screen.onkey(self.up, 'Up')
        screen.onkey(self.down, 'Down')
        screen.onkey(self.right, 'Right')
        screen.onkey(self.left, 'Left')
        screen.listen()

    def move(self):
        screen.tracer(False)  # turn off animation untill complete moving

        for i in range(len(self.body) - 1, 0, -1):
            next_pos = self.body[i-1].pos()
            self.body[i].setpos(next_pos)
        self.body[0].forward(20)
        
        screen.tracer(True)  # turn on animation

    def run(self):
        while not self.game_over:
            self.check_input()
            self.move()
            if self.is_collide_wall():
                self.game_over = True
            time.sleep(self.loop_delay)

    def is_collide_wall(self):
        snake_head_xcor = self.body[0].xcor()
        snake_head_ycor = self.body[0].ycor()
        if abs(snake_head_xcor) >= screen.window_width()/2 or abs(snake_head_ycor) >= screen.window_height()/2:
            return True
        return False
    
    def up(self):
        if self.body[0].heading() != 270:
            self.body[0].setheading(90)

    def down(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)

    def right(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)

    def left(self):
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)


snake = Snake()
snake.run()

screen.exitonclick()