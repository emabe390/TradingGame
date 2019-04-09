import random

class Square(object):
    def __init__(self, lower_x, lower_y, upper_x, upper_y):
        if lower_x > upper_x:
            lower_x, upper_x = upper_x, lower_x
        if lower_y > upper_y:
            lower_y, upper_y = upper_y, lower_y
        self.lower_x = float(lower_x)
        self.lower_y = float(lower_y)
        self.upper_x = float(upper_x)
        self.upper_y = float(upper_y)

    def inside(self, coordinate):
        return coordinate.x > self.lower_x and coordinate.x <= self.upper_x and coordinate.y > self.lower_y and coordinate.y <= self.upper_y

    def intersect(self, square, slack=0):
        #print(self.lower_x, self.lower_y, self.upper_x, self.upper_y, "-", square.lower_x, square.lower_y, square.upper_x, square.upper_y)
        for delta in [-slack, 0, slack] if slack!=0 else [0]:
            res = True
            if self.lower_x+delta > square.upper_x or self.upper_x+delta < square.lower_x:
                res = False
            elif self.lower_y+delta > square.upper_y or self.upper_y+delta < square.lower_y:
                res = False
            if res:
                return True
        return False

    def __str__(self):
        return "%s.%s - %s.%s" % (self.lower_x, self.lower_y, self.upper_x, self.upper_y)

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
                perc = 0
                result = result * (maxLength / d)
            else:
                perc = 1.0-d/maxLength
            return result, perc
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