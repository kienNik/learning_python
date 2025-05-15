from turtle import Turtle
class Snake:
    def __init__(self):
        self.body: list[Turtle] = []

        # init snake's body, if the head is square then a gap will appeared so use circle
        new_turtle = Turtle(shape='circle')
        new_turtle.penup()
        self.body.append(new_turtle)

        # use an extra square to cover the round head
        new_turtle = Turtle(shape='square')
        new_turtle.penup()
        self.body.append(new_turtle)

    def move(self):
        self.body[0].forward(20)
        for i in range(len(self.body) - 1, 0, -1):
            next_pos = self.body[i-1].pos()
            self.body[i].setpos(next_pos)

    def is_collide_tail(self):
        for i in range(len(self.body)-1, 3, -1):
            if self.body[i].distance(self.body[0].pos()) <= 5:
                return True
        return False

    def is_collide_wall(self, screen_height):
        snake_head_xcor = self.body[0].xcor()
        snake_head_ycor = self.body[0].ycor()
        if abs(snake_head_xcor) >= screen_height/2 or abs(snake_head_ycor) >= screen_height/2:
            return True
        return False
    
    def extend(self):
        new_turtle = Turtle(shape='square', visible=False)
        new_turtle.penup()
        # TODO: fix delay when collide with food
        new_turtle.setpos(self.body[-1].pos())
        self.body.append(new_turtle)
        new_turtle.showturtle()

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