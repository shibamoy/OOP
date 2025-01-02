from turtle import Turtle, Screen
import random

race = False
screen = Screen()
screen.setup(width= 500, height=400)
bet = screen.textinput(title="Place your bet", prompt="Which one will win? Enter a color.")

colors = ["red", "yellow", "blue", "green", "purple", "orange"]
y_coord = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for turtles in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtles])
    tim.penup()
    tim.goto(x= -230,y=y_coord[turtles])
    all_turtles.append(tim)
print(all_turtles)
if bet:
    race = True
while race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race = False
            win = turtle.pencolor()
            if win == bet:
                print(f"You win! {win} turtle is the winner")
            else:
                print(f"You lost. {win} turlte is the winner")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
