from Forest import *
from BitFieldListIterator import BitFieldListIterator

class Solution:
    def __init__(self, forest):
        self.forest = forest
        self.isDone = False
        self.treesCut = []
        self.extraWood = 0.0
    
    def __str__(self):
        return """Forest %d
Completed solution: %d
""" % (self.forest.id, self.isDone)

def bruteforce(forest):
    result = Solution(forest)
    
    numTrees = len(forest.trees)
    bitit = BitFieldListIterator(numBits = numTrees, startValue = 1, stepsize = 1, zeroIndexed = True)
    for cutIndices in bitit:
        numTreesToCut = len(cutIndices)
        if numTreesToCut is 0 or numTreesToCut is numTrees:
            "No need to cut nothing or everything"
            continue

        cutTrees = set([forest.trees[index] for index in cutIndices])
        remainingTrees = set(forest.trees) - cutTrees
        print "cut", len(cutTrees), "remaining",  len(remainingTrees)
    
    return result

def main():
    """ Trying to solve the problem described here: 
            http://www.karrels.org/Ed/ACM/99/prob_d.html
        
        Approach:
        Bruteforce through the possible states, 2^n for a forest of n trees. 
        Either a tree is cut or it is not.
        Verify of the proposed solution is valid (does the length of the cut 
        trees match the surcomference of the convex hull of the points).
        Find the maximum solution.  
"""
    it = ForestsFromFile('test/data/simple_forest')
    for f in it:
        sol = bruteforce(f)
        print sol

if __name__ == "__main__":
    main()    