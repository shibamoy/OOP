class Snake:
    from turtle import Turtle
    def __init__(self):
        self.starting_position = starting_position = [(0,0), (-20,0), (-40,0)]
        self.all_segments = []


    def move(self):
        for position in self.starting_position:
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.all_segments.append(segment)
        for seg in range(len(self.all_segments) - 1, 0, -1):
            print(seg)
            new_x = self.all_segments[seg - 1].xcor()
            new_y = self.all_segments[seg - 1].ycor()
            self.all_segments[seg].goto(new_x, new_y)
        self.all_segments[0].forward(20)
