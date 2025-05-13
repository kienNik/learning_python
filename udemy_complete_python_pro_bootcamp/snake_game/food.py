from turtle import Turtle
from random import randrange

class Food:
    def __init__(self, screen_size):
        self.coordinate_limit = screen_size/2
        self.food = Turtle(shape='circle')
        self.food.penup()
        random_x = randrange(-self.coordinate_limit+20, self.coordinate_limit-20)
        random_y = randrange(-self.coordinate_limit+20, self.coordinate_limit-20)
        self.food.setpos((random_x, random_y))

    def reinit(self):
        random_x = randrange(-self.coordinate_limit+20, self.coordinate_limit-20)
        random_y = randrange(-self.coordinate_limit+20, self.coordinate_limit-20)
        self.food.setpos((random_x, random_y))

    def pos(self):
        return self.food.pos()

