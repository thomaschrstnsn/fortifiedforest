import unittest
from Point import Point

class PointTestCase(unittest.TestCase):
    def setUp(self):
        self.p0 = Point(0,0)
        
    def testEquality(self):
        p = Point(1,2)
        self.assertTrue(self.p0 == self.p0)
        self.assertFalse(self.p0 != self.p0)
        
        self.assertTrue(p != self.p0)
        self.assertFalse(p == self.p0)
        
        ps = Point(1,2)
        self.assertTrue(ps == p)
        self.assertFalse(ps != p)

    def testAdding(self):
        self.assertEquals(self.p0 + self.p0, self.p0)
        
        p1 = Point(1,2)
        p2 = -p1
        self.assertEquals(p1 + p2, self.p0)
        self.assertEquals(p1 + p1, Point(2,4))
        self.assertEquals(p1 + self.p0, p1)
    
    def testSubtraction(self):
        p = Point(3, 4)
        q = Point(-5, 10)
        
        self.assertEquals(p - self.p0, p)
        self.assertEquals(p - p, self.p0)
        self.assertEquals(p - q, Point(8, -6))
        self.assertEquals(q - p, Point(-8, 6))