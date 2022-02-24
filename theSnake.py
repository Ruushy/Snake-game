from turtle import Turtle

STAR_POSITION = [(0 , 0 ) , (-20 , 0) , (-40 , 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class snake:
    def __init__(self):
        self.segmetan = []
        self.create_snake()
        self.head = self.segmetan[0]
    def create_snake(self):
        for position in STAR_POSITION:
            self.add(position)
    def add(self , position):
        new_segmeten = Turtle("square")
        new_segmeten.color("white")
        new_segmeten.penup()
        new_segmeten.goto(position)
        self.segmetan.append(new_segmeten)
    def extand(self):
        self.add(self.segmetan[-1].position())
    def move(self):
        for seg in range(len(self.segmetan) - 1, 0, -1):
            newX = self.segmetan[seg - 1].xcor()
            newy = self.segmetan[seg - 1].ycor()
            self.segmetan[seg].goto(newX, newy)

        self.head.forward(10)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
