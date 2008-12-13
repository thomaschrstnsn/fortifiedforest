import unittest
from ForestGenerator import ForestGenerator

class ForestGeneratorTestCase(unittest.TestCase):
    def testSimple(self):
        fg = ForestGenerator(numTrees = 10, xrange = (-5, 5), yrange = (-5, 5), 
                             valuerange = (1, 20), lengthrange = (1, 5))
        
        forest = fg.newForest()
        
        self.assertEqual(len(forest.trees), 10)
        for tree in forest.trees:
            self.assertTrue(tree.position.x >= -5 and tree.position.x < 5)
            self.assertTrue(tree.position.y >= -5 and tree.position.y < 5)
            self.assertTrue(tree.value >= 1 and tree.value < 20)
            self.assertTrue(tree.length >= 1 and tree.length < 5)
