import random
import turtle
from turtle import Turtle, Screen

is_race_on =False
screen =Screen()
screen.setup(1000 ,500)
user_bet=screen.textinput(title="make your bet",prompt="Enter the turtle color you bet: ").lower()
colors = [ "green", "blue", "yellow", "purple", "orange", "red"]
y_position=[-50, -100, 0, 50, 100,150]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-470, y=y_position[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on =True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>450:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color== user_bet:
                print(f"you've won ! The {winning_color} turtle is the winner! ")
            else:
                print(f"you've lost ! The {winning_color} turtle is the winner! ")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# tom = Turtle("turtle")
# tom.penup()
# tom.color("purple")
# tom.goto(x=-470,y=50)
#
# tommy = Turtle("turtle")
# tommy.penup()
# tommy.color("orange")
# tommy.goto(x=-470,y=-50)
#
# timmy = Turtle("turtle")
# timmy.penup()
# timmy.color("yellow")
# timmy.goto(x=-470,y=100)
#
# tos = Turtle("turtle")
# tos.penup()
# tos.color("green")
# tos.goto(x=-470,y=-100)
#
# tossy = Turtle("turtle")
# tossy.penup()
# tossy.color("blue")
# tossy.goto(x=-470,y=150)

screen.exitonclick()