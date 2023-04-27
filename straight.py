from math import sqrt

class Straight:
    A, B, C = 0, 0, 0
    x1, y1, x2, y2 = 0, 0, 0, 0

    @classmethod
    def set_straight(cls, x1=None, y1=None, x2=None, y2=None ):
        if x1 is None:
            x1 = float(input('x1 --> '))
        if y1 is None:
            y1 = float(input('y1 --> '))
        if x2 is None:
            x2 = float(input('x2 --> '))
        if y2 is None:
            y2 = float(input('y2 --> '))
        a = y2 - y1
        b = x1 - x2
        c = - b * y1 - a * x1
        if c > 0:
            sgn = -1
        else:
            sgn = 1
        j = sgn/sqrt(a**2 + b**2)
        cls.A = a*j
        cls.B = b*j
        cls.C = c*j
        cls.x1, cls.y1, cls.x2, cls.y2 = x1, y1, x2, y2

    @classmethod
    def ambit(cls, x, y):
        return 0 < abs(cls.A * x + cls.B * y + cls.C) < 1




