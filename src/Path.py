
class Path:
    def __init__(self):
        self.lines = []
        
    def addLine(self, line):
        self.lines.append(line)
    
    def length(self):
        result = 0
        for line in self.lines:
            result = result + line.length()
        return result
    
    def isConnected(self):
        if len(self.lines) == 0: return False
        for i in range(0, len(self.lines) - 1):
            l1 = self.lines[i]
            l2 = self.lines[i+1]
            if l1.p2 != l2.p1:
                return False
        if self.lines[-1].p2 != self.lines[0].p1:
            return False
        return True
