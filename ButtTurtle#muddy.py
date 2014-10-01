from turtle import Turtle
from random import random

def random_color():
    return(random(),random(),random())



muddy = Turtle()
muddy.pensize(7)

while True:
    for count in range(4):
        muddy.pencolor(random_color())
        muddy.forward(100)
        muddy.right(90)
    muddy.right(10)
