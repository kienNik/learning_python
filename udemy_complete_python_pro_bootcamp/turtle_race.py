from turtle import Turtle, Screen
from random import randint

screen = Screen()

# config
screen_width = 500
screen_height = 500
turtle_distance = 50  # distance between 2 turtles
start_distance = 20  # distance from the left side of screen to start with

screen.setup(width=screen_width, height=screen_height)
turtle_list = []

# to add a turtle, add a color to the list
turtle_color = ['red', 'green', 'blue', 'yellow', 'pink']

num_of_turtles = len(turtle_color)

def create_turtles():
    for i in range(num_of_turtles):
        new_turtle = Turtle(shape='turtle')
        new_turtle.pos()
        new_turtle.color(turtle_color[i])
        new_turtle.penup()
        new_turtle.setpos(-screen_width/2 + start_distance, -turtle_distance*num_of_turtles/2 + i*turtle_distance)
        turtle_list.append(new_turtle)

create_turtles()

guess = screen.textinput(title='Make a bet', prompt='Which turtle will win? Enter a color: ')

finish = False

while not finish:
    for i in range(num_of_turtles):
        turtle_list[i].forward(randint(1, 5))
        if turtle_list[i].pos()[0] >= screen_width/2 - 10:
            finish = True
            print(f'{turtle_color[i]} turtle won.')
            if guess == turtle_color[i]:
                print('You win.')
            else:
                print('You lose.')

screen.exitonclick()