import unittest
from resta import restar

class Testrestar(unittest.TestCase):
    
    def test_sumar(self):
        self.assertEqual(restar(3, 2), 1)
        self.assertEqual(restar(-1, 1), -2)
        self.assertEqual(restar(-1, -1), 0)

if __name__ == '__main__':
    unittest.main()