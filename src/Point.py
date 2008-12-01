import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "Point(%s,%s)" % (self.x, self.y)
        
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return not self == other
    
    def __neg__(self):
        return Point(-self.x, -self.y)
    
    def __abs__(self):
        return Point(abs(self.x), abs(self.y))

    def size(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    def distanceTo(self, other):
        return (self - other).size()
    
    def perpdot(self, other):
        return self.x * other.y - self.y * other.x

    def dot(self, other):
        return self * other