# Classes, that creates equations

import enum


class Var(enum.Enum):
    x = 'x'
    y = 'y'


class Equation:
    def __init__(self):
        self.restrictions = {Var.x:[None, None], Var.y:[None, None]}

    def move(self, dx, dy):
        return self

    def __str__(self):
        return self.restrictions

    def get_restrictions(self):
        restrictions = ""
        for var in self.restrictions.keys():
            start = self.restrictions[var][0]
            end = self.restrictions[var][1]
            if start is not None:
                restrictions += f"+sqrt({var.name} - {start})-sqrt({var.name} - {start})"
            if end is not None:
                restrictions += f"+sqrt({end} - {var.name})-sqrt({end} - {var.name})"
        return restrictions

    def apply_restrictions(self, start=None, end=None, var=Var.x):
        self.restrictions[var] = [start, end]
        return self


class Line(Equation):
    # ax + by = c
    def __init__(self, x_coefficient, y_coefficient, free_coefficient):
        super().__init__()
        self.xCoefficient = x_coefficient
        self.yCoefficient = y_coefficient
        self.freeCoefficient = free_coefficient
        if self.xCoefficient == 0 and self.yCoefficient == 0:
            raise Exception('Not a line')

    def __str__(self):
        return f"{self.xCoefficient}x + {self.yCoefficient}y{self.get_restrictions()}= {-self.freeCoefficient}"

    def move(self, dx, dy):
        for i in range(2):
            if self.restrictions[Var.x][i] is not None:
                self.restrictions[Var.x][i] += dx
            if self.restrictions[Var.y][i] is not None:
                self.restrictions[Var.y][i] += dy
        if self.yCoefficient != 0:
            self.freeCoefficient -= self.yCoefficient * dy
        if self.xCoefficient != 0:
            self.freeCoefficient -= self.xCoefficient * dx
        return self


class Circle(Equation):
    # a(x - x0)^2 + b(y - y0)^2 = r^2
    def __init__(self, x_multiplier, y_multiplier, x_center, y_center, radius):
        super().__init__()
        self.xMultiplier = x_multiplier
        self.yMultiplier = y_multiplier
        self.center = (x_center, y_center)
        self.radius = radius
