from math import sqrt
from turtle import *


def sommet(c, x, y):
    up()
    setpos(x, y)
    down()
    circle(15)
    up()
    setpos(x, y + 5)
    write(c, False, align="center", font=("Ariel", 10, "normal"))


def arc(x, y, z, t):
    up()
    setpos(z, t + 30)
    left(90)
    down()
    circle(sqrt((x - z) * (x - z) + (y - t) * (y - t)) / 2, 180)


clearscreen()
sommet(10, 50, 200)
sommet(20, 300, 200)
arc(50, 200, 300, 200)


def graph(m):
    for i in range(len(m)):
        sommet(i, i * 100, i * 100)
