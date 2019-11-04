from math import sqrt
import turtle
import numpy as np

t = turtle.Turtle()


def move_to(x: int, y: int, write: bool = False):
    if write is False:
        t.pendown()
    t.setheading(0)
    t.setpos(x, y)
    t.pendown()


def sommet(c, x, y):
    t.setheading(0)
    t.up()
    t.setpos(x, y)
    t.down()
    t.circle(15)
    t.up()
    t.setpos(x, y + 5)
    t.write(c, False, align="center", font=("Ariel", 10, "normal"))


def arc(x, y, a, b):
    t.setheading(0)
    t.up()
    t.setpos(a, b + 30)
    t.left(90)
    t.down()
    t.circle(sqrt((x - a) * (x - a) + (y - b) * (y - b)) / 2, 180)


def arcp(x, y, a, b, p):
    t.setheading(0)
    t.up()
    t.setpos(a, b + 30)
    t.left(90)
    t.down()
    t.circle(sqrt((x - a) * (x - a) + (y - b) * (y - b)) / 2, 90)
    t.write(p, align="center")
    t.circle(sqrt((x - a) * (x - a) + (y - b) * (y - b)) / 2, 90)


def graph(m: np.ndarray):
    r = range(len(m))
    for i in r:
        sommet(i, i * 100, 0)
    for i in r:
        for j in r:
            if m[i, j] != 0:
                arcp(i * 100, 0, j * 100, 0, m[i, j])


if __name__ == "__main__":
    graph(np.ones((3, 3)))

    input()
