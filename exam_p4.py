"""
What is the most interesting/funny/cool thing(s) about Python that you learned from this class or from somewhere else.

You can use code or a short paragraph to illustrate it.
"""
"""
In the beginning of this course we did a class on interface design which was very cool. 
I had done something like this, using the Turtle module in primary school, but it was just giving an already made program 
the numerical instructions to travel the given amount of distance; therefore seeing the backend of the Turtle module was cool.
After looking at drawing basic shapes with the Turtle I looked into how we can use the turtle to write text and I have put a small code below.

"""
import turtle
import math
import random
from turtle import Turtle

t=Turtle()
 
# def random_drawing(turns,distance):
#     for x in range(turns):
#         right=t.right(random.randint(0,360))
#         left=t.left(random.randint(0,360))
#         t.color(random.choice(["blue","red","green"]))
#         random.choice([right,left])
#         t.fd(distance)
 
# random_drawing(100,50)
t.write("Python is cool", move = True, align="center", font=("Freestyle Script", 64, "normal"))

