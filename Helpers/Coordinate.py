import random

class Square(object):
    def __init__(self, lower_x, lower_y, upper_x, upper_y):
        if lower_x > upper_x:
            lower_x, upper_x = upper_x, lower_x
        if lower_y > upper_y:
            lower_y, upper_y = upper_y, lower_y
        self.lower_x = lower_x
        self.lower_y = lower_y
        self.upper_x = upper_x
        self.upper_y = upper_y

    def inside(self, coordinate):
        return coordinate.x < self.lower_x and coordinate.x <= self.upper_x and coordinate.y < self.lower_y and coordinate.y <= self.upper_y

    def intersect(self, square):
        #print(self.lower_x, self.lower_y, self.upper_x, self.upper_y, "-", square.lower_x, square.lower_y, square.upper_x, square.upper_y)
        if self.lower_x > square.upper_x or self.upper_x < square.lower_x:
            return False
        if self.lower_y > square.upper_y or self.upper_y < square.lower_y:
            return False
        return True

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