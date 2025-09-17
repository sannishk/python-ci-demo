import unittest
from app.calculator import add, sub, mul, div, calculate

class TestCalculator(unittest.TestCase):
    def test_add(self): 
        self.assertEqual(add(2, 3), 5)

    def test_sub(self): 
        self.assertEqual(sub(5, 2), 3)

    def test_mul(self): 
        self.assertEqual(mul(4, 3), 12)

    def test_div(self):
        self.assertEqual(div(10, 2), 5)
        self.assertAlmostEqual(div(3, 2), 1.5)

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(1, 0)

    def test_calculate_add(self): 
        self.assertEqual(calculate(2, 3, "+"), 5)

    def test_calculate_div(self):
        self.assertEqual(calculate(9, 3, "/"), 3)

    def test_calculate_bad_op(self):
        with self.assertRaises(ValueError):
            calculate(1, 2, "%")

if __name__ == "__main__":
    unittest.main()

