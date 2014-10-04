from turtle import Turtle
from random import random


def random_color():
    return (random(),random(),random())


shelldo = Turtle()
shelldo.pensize(100)

while True:
    for count in range(4):
        shelldo.pencolor(random_color())
        shelldo.forward(100)
        shelldo.right(90)
    shelldo.right(10)
    
