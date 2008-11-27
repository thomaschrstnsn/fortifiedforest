import unittest
from Line import Line
from Point import Point
from Path import Path

class PathTestCase(unittest.TestCase):
    def setUp(self):
        self.p0 = Point(1, 2)
        self.p1 = Point(2, 3)
        self.p2 = Point(4, 5)
        self.p3 = Point(6, 7)

    def testEmpty(self):
        emptyPath = Path()
        self.assertFalse(emptyPath.isConnected())
        self.assertEquals(emptyPath.length(), 0)
    
    def testValid(self):
        validPath = Path()
        validPath.addPoint(self.p0)
        validPath.addPoint(self.p1)
        validPath.addPoint(self.p2)
        validPath.addPoint(self.p0)
        self.assertTrue(validPath.isConnected())
    
    def testDisconnected(self):
        disconnectedPath = Path()
        disconnectedPath.addPoint(self.p0)
        disconnectedPath.addPoint(self.p1)
        disconnectedPath.addPoint(self.p2)
        self.assertFalse(disconnectedPath.isConnected())

    def testLength(self):
        p = Path()
        p.addPoint(self.p0)
        p.addPoint(self.p1)
        
        l0 = Line(self.p0, self.p1)
        l1 = Line(self.p1, self.p2)
        self.assertEquals(p.length(), l0.length())
        p.addPoint(self.p2)
        self.assertEquals(p.length(), l0.length() + l1.length())
