import unittest
from unittest.mock import patch
from io import StringIO
import app.calculator as calc

class TestCalculatorInteractive(unittest.TestCase):

    @patch("builtins.input", side_effect=["2", "3", "+"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_addition(self, mock_stdout, mock_input):
        result = calc.run_calculator()
        self.assertEqual(result, 5.0)
        output = mock_stdout.getvalue()
        self.assertIn("Result: 5.0", output)

    @patch("builtins.input", side_effect=["10", "4", "-"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_subtraction(self, mock_stdout, mock_input):
        result = calc.run_calculator()
        self.assertEqual(result, 6.0)
        output = mock_stdout.getvalue()
        self.assertIn("Result: 6.0", output)

    @patch("builtins.input", side_effect=["3", "4", "*"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_multiplication(self, mock_stdout, mock_input):
        result = calc.run_calculator()
        self.assertEqual(result, 12.0)
        output = mock_stdout.getvalue()
        self.assertIn("Result: 12.0", output)

    @patch("builtins.input", side_effect=["5", "2", "/"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_invalid_operation(self, mock_stdout, mock_input):
        result = calc.run_calculator()
        self.assertIsNone(result)
        output = mock_stdout.getvalue()
        self.assertIn("Invalid operation", output)

if __name__ == "__main__":
    unittest.main()
