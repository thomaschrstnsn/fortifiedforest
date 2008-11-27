import unittest
from Line import Line
from Point import Point
from Path import Path

class PathTestCase(unittest.TestCase):
    def setUp(self):
        p0 = Point(1, 2)
        p1 = Point(2, 3)
        p2 = Point(4, 5)
        p3 = Point(6, 7)
        
        self.l0 = Line(p0, p1)
        self.l1 = Line(p1, p2)
        self.l2 = Line(p2, p3)
        self.l3 = Line(p3, p0)

    def testEmpty(self):
        emptyPath = Path()
        self.assertFalse(emptyPath.isConnected())
        self.assertEquals(emptyPath.length(), 0)
    
    def testValid(self):
        validPath = Path()
        validPath.addLine(self.l0)
        validPath.addLine(self.l1)
        validPath.addLine(self.l2)
        validPath.addLine(self.l3)
        self.assertTrue(validPath.isConnected())
    
    def testDisconnected(self):
        disconnectedPath = Path()
        disconnectedPath.addLine(self.l0)
        disconnectedPath.addLine(self.l1)
        disconnectedPath.addLine(self.l2)
        self.assertFalse(disconnectedPath.isConnected())

    def testHole(self):
        holePath = Path()
        holePath.addLine(self.l0)
        holePath.addLine(self.l1)
        holePath.addLine(self.l3)
        self.assertFalse(holePath.isConnected())
    
    def testLength(self):
        p0 = Path()
        p0.addLine(self.l0)
        
        self.assertEquals(p0.length(), self.l0.length())
        p0.addLine(self.l1)
        self.assertEquals(p0.length(), self.l0.length() + self.l1.length())
