from Forest import Forest, Tree
from Point import Point
from random import randrange

def trand(tuple):
    return randrange(tuple[0], tuple[1])    

class ForestGenerator:
    def __init__(self, numTrees, xrange = (0, 10), yrange = (0, 10), valuerange = (1, 10), lengthrange = (1, 4)):
        self.numTrees = numTrees
        self.xrange = xrange
        self.yrange = yrange
        self.valuerange = valuerange
        self.lengthrange = lengthrange
    
    def newForest(self):
        forest = Forest()
        for i in xrange(0, self.numTrees):
            position = Point(trand(self.xrange), trand(self.yrange))
            tree = Tree(position=position, value = trand(self.valuerange), 
                        length = trand(self.lengthrange))
            tree.id = i
            forest.addTree(tree)
        return forest