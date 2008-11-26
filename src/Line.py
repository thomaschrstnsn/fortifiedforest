
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return "Line(%s,%s)" % (self.p1, self.p2)
        
    def __invert__(self):
        return Line(self.p2, self.p1)

    def length(self):
        return (self.p1 - self.p2).size()