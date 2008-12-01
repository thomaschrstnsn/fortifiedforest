import unittest
from ConvexHull import *
from Point import Point

class ConvexHullTestCase(unittest.TestCase):
    def setUp(self):
        self.middlepoints = [Point(1,1), Point(1,2), Point(2,1), Point(2,2)]
        self.cornerpoints1 = [Point(0, -10), Point(0, 10), Point(-10, 0), Point(10,0)]
        self.cornerpoints2 = [Point(-50, -50), Point(50,50), Point(-50, 50), Point(50, -50)]
        self.forest1 = [Point(0,0), Point(1,4), Point(2,1), 
                        Point(4,1), Point(3,5), Point(2,3)]
    
    def testSimple1(self):
        points = self.middlepoints + self.cornerpoints1
        path = jarviswalk(points)
        self.assertTrue(path.isConnected())
        self.assertEquals(len(path.points) - 1, len(self.cornerpoints1)) # start/end point duplicated
        for p in self.cornerpoints1:
            self.assertTrue(p in path.points)
            
    def testSimple2(self):
        points = self.middlepoints + self.cornerpoints2
        path = jarviswalk(points)
        self.assertTrue(path.isConnected())
        self.assertEquals(len(path.points) - 1, len(self.cornerpoints2)) # start/end point duplicated
        for p in self.cornerpoints2:
            self.assertTrue(p in path.points)

    def _verifyForest(self, forest, cutIndices, expectedIndices, msg):
        expectedPoints = [forest[index] for index in expectedIndices]
        expectedPath = Path()
        expectedPath.points = expectedPoints
        self.assertTrue(expectedPath.isConnected(), 
                        "%s expected path is not connected" % msg)

        cut = [forest[index] for index in cutIndices]

        forest = filter(lambda x: x not in cut, forest)
        
        path = jarviswalk(forest)
        self.assertTrue(path.isConnected(),
                        "%s found path is not connected" % msg)
        self.assertEquals(len(expectedPath.points), len(path.points), 
                          "%s found path not containing expected number of points" % msg)
        self.assertEquals(expectedPath.length(), path.length(),
                          "%s found path not of expected length" % msg)
        for p in expectedPoints:
            self.assertTrue(p in path.points, 
                            "%s found path does not contain expected point: %s" % (msg, p))

    def testForest1(self):
        problems = [[self.forest1, [],  [0,1,4,3,0], "full"],
                    [self.forest1, [0], [1,4,3,2,1], "cut 0"],
                    [self.forest1, [1], [0,4,3,0],   "cut 1"],
                    [self.forest1, [2], [0,1,4,3,0], "cut 2"],
                    [self.forest1, [3], [0,1,4,2,0], "cut 3"],
                    [self.forest1, [4], [0,1,3,0],   "cut 4"],
                    [self.forest1, [5], [0,1,4,3,0], "cut 5"]]
        for p in problems:
            self._verifyForest(p[0],p[1],p[2],p[3])
