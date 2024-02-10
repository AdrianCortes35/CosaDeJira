import unittest
from division import dividir

class TestDividir(unittest.TestCase):
    
    def test_multiplicar(self):
        self.assertEqual(dividir(15, 5), 3)
        self.assertEqual(dividir(3, 2), 1.5)
        self.assertEqual(dividir(-30, 5), -6)
        self.assertEqual(dividir(26, 0), "error")

if __name__ == '__main__':
    unittest.main()