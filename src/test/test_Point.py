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

        