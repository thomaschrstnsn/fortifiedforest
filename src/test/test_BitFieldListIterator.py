import unittest
from BitFieldListIterator import BitFieldListIterator

class BitFieldListIteratorTestCase(unittest.TestCase):
    def setUp(self):
        self.zeroToFifteen = {0:[], 1:[1], 2:[2], 3:[1,2], 4:[3], 5:[1,3], 6:[2,3], 7:[1,2,3],
                              8:[4], 9:[1,4], 10:[2,4], 11:[1,2,4], 12:[3,4], 13:[1,3,4], 
                              14:[2,3,4], 15:[1,2,3,4]}
        
        self.zeroToFifteenZeroIndex = {}
        for k in self.zeroToFifteen.keys():
            self.zeroToFifteenZeroIndex[k] = [x - 1 for x in self.zeroToFifteen[k]]
    
    def testZeroToFifteen(self):
        bfit = BitFieldListIterator(4)
        expected = 0
        for bf in bfit:
            self.assertEquals(bf, self.zeroToFifteen[expected])
            expected = expected + 1
        self.assertEquals(expected, 16) # last iteration was 15, next expected must be 16

    def testZeroToFifteenZeroIndex(self):
        bfit = BitFieldListIterator(4, zeroIndexed = True)
        expected = 0
        for bf in bfit:
            self.assertEquals(bf, self.zeroToFifteenZeroIndex[expected])
            expected = expected + 1
        self.assertEquals(expected, 16) # last iteration was 15, next expected must be 16
    
    def testZeroToSeven(self):
        zeroToSeven = {}
        for i in range(0, 8):
            zeroToSeven[i] = self.zeroToFifteen[i]
        
        bfit = BitFieldListIterator(3)
        expected = 0
        for bf in bfit:
            self.assertEquals(bf, zeroToSeven[expected])
            expected = expected + 1
        self.assertEquals(expected, 8) # last iteration was 7, next expected must be 8
        
    def testStep3(self):
        bfit = BitFieldListIterator(4, stepsize=3)
        expected = 0
        for bf in bfit:
            self.assertEquals(bf, self.zeroToFifteen[expected])
            expected = expected + 3
        self.assertEquals(expected, 18) # last iteration was 15, next expected must be 18

    def testStep3Start1(self):
        bfit = BitFieldListIterator(4, stepsize=3, startValue=1)
        expected = 1
        for bf in bfit:
            self.assertEquals(bf, self.zeroToFifteen[expected])
            expected = expected + 3
        self.assertEquals(expected, 16) # last iteration was 13, next expected must be 16
