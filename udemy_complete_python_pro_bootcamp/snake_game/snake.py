from turtle import Turtle, Screen
import time
from food import Food

screen = Screen()

class Snake:
    def __init__(self):
        self.body: list[Turtle] = []
        self.food = Food(screen.window_height())

        # init snake's body, if the head is square then a gap will appeared so use circle
        new_turtle = Turtle(shape='circle')
        new_turtle.penup()
        self.body.append(new_turtle)

        # use an extra square to cover the round head
        new_turtle = Turtle(shape='square')
        new_turtle.penup()
        self.body.append(new_turtle)

        self.game_over = False
        self.loop_delay = 0.1

    def check_input(self):
        screen.onkey(self.up, 'Up')
        screen.onkey(self.down, 'Down')
        screen.onkey(self.right, 'Right')
        screen.onkey(self.left, 'Left')
        screen.listen()

    def move(self):
        screen.tracer(False)  # turn off animation untill complete moving

        self.body[0].forward(20)
        for i in range(len(self.body) - 1, 0, -1):
            next_pos = self.body[i-1].pos()
            self.body[i].setpos(next_pos)
        
        screen.tracer(True)  # turn on animation

    def run(self):
        while not self.game_over:
            self.check_input()
            self.move()
            if self.is_collide_wall():
                self.game_over = True
            if self.is_collide_food():
                new_turtle = Turtle(shape='square')
                new_turtle.penup()
                self.body.append(new_turtle)
            time.sleep(self.loop_delay)

    def is_collide_food(self):
        diff_x = abs(self.food.pos()[0] - self.body[0].xcor())
        diff_y = abs(self.food.pos()[1] - self.body[0].ycor())
        if diff_x <= 20 and diff_y <= 20:
            screen.tracer(False)
            self.food.reinit()
            screen.tracer(True)
            return True
        return False

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