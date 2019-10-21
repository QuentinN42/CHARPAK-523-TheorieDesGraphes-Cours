import turtle as tr
import numpy as np
from math import pi
from cmath import exp


class Sommet:
    def __init__(self, name, x, y=None):
        self.name = str(name)
        if type(x) is complex:
            self.x = int(x.real)
            self.y = int(x.imag)
        else:
            self.x = int(x)
            self.y = int(y)

    def __add__(self, other):
        return Sommet(self.name, self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Sommet(self.name, self.x - other.x, self.y - other.y)


class Tortue(tr.Turtle):
    def __init__(self, color: str = "red", *args):
        super().__init__(*args)
        super().color(color)
        self.radius = 8

    def move_to(self, x: int, y: int, write: bool = False):
        if write is False:
            super().penup()
        super().setheading(0)
        super().setpos(x, y)
        super().pendown()

    def sommet(self, sommet):
        self.move_to(sommet.x, sommet.y - self.radius)
        super().color("red")
        super().begin_fill()
        super().circle(self.radius)
        super().end_fill()
        super().color("black")
        super().write(sommet.name, align="center")

    def arc(self, s1: Sommet, s2: Sommet):
        super().color("blue")
        self.move_to(s1.x, s1.y)
        self.move_to(s2.x, s2.y, write=True)


def graph(m: np.ndarray):
    t = Tortue()
    n = len(m)
    sommets = [Sommet(k, 50 * exp(complex(0, 2 * pi * k / n))) for k in range(n)]
    for i in range(n):
        for j in range(i, n):
            if m[i][j]:
                t.arc(sommets[i], sommets[j])

    for sommet in sommets:
        t.sommet(sommet)


graph(np.ones((5, 5)))
input()
