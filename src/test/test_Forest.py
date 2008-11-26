import unittest
from Forest import *

class ForestTestCase(unittest.TestCase):
    def setUp(self):
        self.filename = 'data/simple_forest'
        
    
    def testReading(self):
        try:
            it = ForestsFromFile(self.filename)
            forests = []
            for f in it:
                forests.append(f)
            self.assertEqual(len(forests), 2)

            self.assertEqual(len(forests[0].trees), 6)
            self.assertEqual(len(forests[1].trees), 3)
            
        except ForestParsingError, pe:
            print pe
            self.assertTrue(False, "No parsing exceptions")
