import unittest
from Point import Point
from Line import Line

class LineTestCase(unittest.TestCase):
    def setUp(self):
        p0 = Point(0,0)
        p1 = Point(3,0)
        p2 = Point(3,4)
 
        self.l1 = Line(p0, p1)
        self.l2 = Line(p1, p2)
        self.l3 = Line(p2, p0)
    
    def testLengths(self):
        self.assertAlmostEqual(self.l1.length(), 3.0)
        self.assertAlmostEqual(self.l2.length(), 4.0)
        self.assertAlmostEqual(self.l3.length(), 5.0)
