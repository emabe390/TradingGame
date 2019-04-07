import random
class Coordinate(object):
    def __init__(self, x=None, y=None):
        if x is None and y is None:
            x, y = random_xy()
        self.x = float(x)
        self.y = float(y)

    def __sub__(self, other):
        return Coordinate(self.x-other.x, self.y-other.y)

    def __add__(self, other):
        return Coordinate(self.x+other.x, self.y+other.y)

    def __mul__(self, other):
        return Coordinate(self.x * other, self.y * other)

    def distance(self, other):
        return pow(pow(self.x-other.x, 2) + pow(self.y-other.y, 2), 0.5)

    def deltaCoord(self, other, maxLength=None):
        result = other - self
        if maxLength is not None:
            d = self.distance(other)
            if d > maxLength:
                result = result * (maxLength / d)
        return result

    def isZero(self):
        return self.x == 0.0 and self.y == 0.0

    def __str__(self):
        return "(%0.2f, %0.2f)" % (self.x, self.y)

    def is_target(self):
        return False

def random_xy(x_min=-100, x_max=100, y_min=-100, y_max=100):
    return random.randint(x_min, x_max), random.randint(y_min, y_max)

def RandomCoordinate(x_min=-100, x_max=100, y_min=-100, y_max=100):
    x, y = random_xy(x_min, x_max, y_min, y_max)
    return Coordinate(x, y)