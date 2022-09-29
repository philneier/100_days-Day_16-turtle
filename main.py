# import another_module
#
# print(another_module.another_variable)

# ---import module---
# import turtle
# ---tap into module (turtle.) and fetch a class (Turtle) from the module ---
# ---() constructs object from blueprint ---
# --- timmy = saves to object called timmy
# timmy = turtle.Turtle()
# same as
from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
# returns "<turtle.Turtle object at 0x000001C32616A0E0>"
# which means the object is saved to specified location in computer memory
timmy.shape("turtle")
timmy.color("cyan")

# move turtle forward 100 paces
timmy.forward(100)

# Accessing attributes
my_screen = Screen()
print(my_screen.canvheight)

# Object methods
# ---keeps screen up until closed by clicking on screen
my_screen.exitonclick()