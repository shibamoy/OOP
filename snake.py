from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.all_segments = []
        self.start()
        self.head = self.all_segments[0]

    def start(self):
        for position in STARTING_POSITION:
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.all_segments.append(segment)

    def move(self):
        for seg in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[seg - 1].xcor()
            new_y = self.all_segments[seg - 1].ycor()
            self.all_segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(180)

