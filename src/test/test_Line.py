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

    def testDot(self):
        a0 = self.l2.angle(Point(1,1))
        a1 = self.l2.angle(Point(5, 1))
        a2 = self.l1.angle(Point(1,2))
        a3 = self.l1.angle(Point(1,-2))
        self.assertTrue(a0 > 0)
        self.assertTrue(a1 < 0)
        self.assertTrue(a2 > 0)
        self.assertTrue(a3 < 0)