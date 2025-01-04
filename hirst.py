import random

import colorgram
from turtle import Turtle, Screen
screen = Screen()
screen.colormode(255)

x = -200
y = -150

colors = colorgram.extract('image.jpg', 6)
rgb_color = [
    (0, 0, 0),        # Black
    (255, 0, 0),      # Red
    (0, 255, 0),      # Green
    (0, 0, 255),      # Blue
    (255, 255, 0),    # Yellow
    (0, 255, 255),    # Cyan
    (255, 0, 255),    # Magenta
    (128, 128, 128),  # Gray
    (211, 211, 211),  # Light Gray
    (64, 64, 64),     # Dark Gray
    (255, 165, 0),    # Orange
    (128, 0, 128),    # Purple
    (255, 192, 203),  # Pink
    (139, 69, 19),    # Brown
]

tim = Turtle()
tim.shape("turtle")
tim.speed(0)
tim.penup()
tim.goto(x, y)
def making_circle():
    for _ in range(10):
        random_color = random.choice(rgb_color)
        tim.pencolor(random_color)
        tim.fillcolor(random_color)
        tim.begin_fill()
        tim.circle(20)
        tim.end_fill()
        tim.penup()
        tim.forward(50)
        tim.hideturtle()

def dot_move():
    for _ in range(10):
        random_color = random.choice(rgb_color)
        tim.dot(20,random_color)
        tim.penup()
        tim.forward(50)

for _ in range(10):
    dot_move()
    y += 50
    tim.goto(x, y)



screen.exitonclick()
