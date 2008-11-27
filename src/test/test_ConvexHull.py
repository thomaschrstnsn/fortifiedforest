import unittest
from ConvexHull import *

class ConvexHullTestCase(unittest.TestCase):
    def setUp(self):
        self.middlepoints = [Point(1,1), Point(1,2), Point(2,1), Point(2,2)]
        self.cornerpoints1 = [Point(0, -10), Point(0, 10), Point(-10, 0), Point(10,0)]
        self.cornerpoints2 = [Point(-50, -50), Point(50,50), Point(-50, 50), Point(50, -50)]
    
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