from Line import Line

class Path:
    def __init__(self):
        self.points = []
        
    def addPoint(self, point):
        self.points.append(point)
    
    def length(self):
        result = 0
        for i in range(0, len(self.points) - 1):
            line = Line(self.points[i], self.points[i+1])
            result = result + line.length()
        return result
    
    def isConnected(self):
        if len(self.points) < 2: return False
        return self.points[0] == self.points[-1]