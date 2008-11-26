from Point import Point

class Tree:
    "Representation of a tree in a forest"
    def __init__(self, position, value, length):
        self.position = position
        self.value = value
        self.length = length
    
    def __repr__(self):
        return "Tree(%s,%s,%s)" % (self.position, self.value, self.length)
        
class Forest:
    "Representation of a forest"
    def __init__(self):
        self.trees = []
        
    def __nonzero__(self):
        return len(self.trees) != 0
    
    def addTree(self, tree):
        self.trees.append(tree)

class ForestParsingError(Exception):
    def __init__(self, input, msg):
        self.input = input
        self.msg = msg

    def __str__(self):
        return "ForestParsing error: %s. When parsing input: %s" % (self.msg, self.input)

class ForestsFromFile:
    "Iterator for reading Forests from a forest file"
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __iter__(self):
        return self
    
    def _readtree(self):
        l = self.file.readline().rstrip()
        if len(l) < 7 or l[0] != ' ':
            raise ForestParsingError(l, "Expected 4 indented integers")
        spl = l.lstrip().split()
        if len(spl) != 4:
            raise ForestParsingError(l, "Expected 4 fields")
        try:
            px, py, value, length = map(int, spl)
            return Tree(Point(px, py), value, length)
        except:
            raise ForestParsingError(spl, "Non integer experienced")
        
    def _readforest(self):
        try:
            fl = self.file.readline().rstrip()
            if len(fl) < 1 or fl[0] == ' ' or not fl.isdigit:
                raise ForestParsingError(fl, "Expected non-indented integer")
            numTrees = int(fl)
            if numTrees < 0:
                raise ForestParsingError(fl, "Expected positive integer")
            if numTrees == 0:
                raise StopIteration

            forest = Forest()
            for i in range(0, numTrees):
                tree = self._readtree()
                forest.addTree(tree)
            return forest
        except:
            raise
    
    def next(self):
        try:
            if self.file is None:
                self.file = open(self.filename, 'ra')
            return self._readforest()
        except (StopIteration, IOError):
            self.file.close()
            self.file = None
            raise