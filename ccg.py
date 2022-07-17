
# Online Python compiler (interpreter) to run Python online.
# Write Pd")
from turtle import Turtle, Screen
import random

colours = ["aquamarine", "hot pink", "cyan", "pale green", "deep sky blue", "chartreuse", "powder blue", "medium slate blue", "deep pink", "dark orange", "blue", "cornflower blue", "light sky blue", "medium spring green", "yellow", "blue violet", "yellow", "magenta"]
timmy = Turtle()
timmy.shape("turtle")


screen = Screen()
for n in range(3, 15):
    rno = random.randint(0,len(colours)-1)
    timmy.color(colours[rno])
    for i in range(n):
        timmy.forward(80)
        timmy.left(360/n)

timmy.forward(40)
timmy.right(90)
timmy.color("pink")
timmy.forward(300)

screen.exitonclick()