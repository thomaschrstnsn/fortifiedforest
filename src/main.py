from Forest import *

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
        for t in f.trees:
            print t

if __name__ == "__main__":
    main()    