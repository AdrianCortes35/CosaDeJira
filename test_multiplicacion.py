import unittest
from multiplicacion import multiplicar

class TestMultiplicar(unittest.TestCase):
    
    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(-3, 5), -15)
        self.assertEqual(multiplicar(-156, 0), 0)

if __name__ == '__main__':
    unittest.main()