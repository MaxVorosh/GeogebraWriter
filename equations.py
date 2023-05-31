# Classes, that creates equations

import enum


class Var(enum.Enum):
    x = 'x'
    y = 'y'


class Equation:
    def __init__(self):
        self.restrictions = ""

    def move(self, x, y):
        pass

    def __str__(self):
        return self.restrictions

    def apply_restriction(self, start=None, end=None, var=Var.x):
        if start is not None:
            self.restrictions += f"+sqrt({var.name} - {start})-sqrt({var.name} - {start})"
        if end is not None:
            self.restrictions += f"+sqrt({end} - {var.name})-sqrt({end} - {var.name})"


class Line(Equation):
    # ax + by = c
    def __init__(self, x_coefficient, y_coefficient, free_coefficient):
        super().__init__()
        self.xCoefficient = x_coefficient
        self.yCoefficient = y_coefficient
        self.freeCoefficient = free_coefficient


class Circle(Equation):
    # a(x - x0)^2 + b(y - y0)^2 = r^2
    def __init__(self, x_multiplier, y_multiplier, x_center, y_center, radius):
        super().__init__()
        self.xMultiplier = x_multiplier
        self.yMultiplier = y_multiplier
        self.center = (x_center, y_center)
        self.radius = radius
