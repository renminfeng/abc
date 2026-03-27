import io
import unittest
from contextlib import redirect_stdout

from calculator_core import evaluate_expression, main


class CalculatorCoreTests(unittest.TestCase):
    def test_evaluate_expression_basic_math(self):
        self.assertEqual(evaluate_expression("1 + 2 * (3 - 1)"), 5.0)

    def test_evaluate_expression_rejects_bool_constants(self):
        with self.assertRaisesRegex(ValueError, "只允许数字"):
            evaluate_expression("True")

    def test_evaluate_expression_rejects_division_by_zero(self):
        with self.assertRaisesRegex(ValueError, "除数不能为 0"):
            evaluate_expression("1 / 0")

    def test_main_prints_result_for_cli_argument(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = main(["2 + 3"])
        self.assertEqual(code, 0)
        self.assertEqual(buffer.getvalue().strip(), "5.0")


if __name__ == "__main__":
    unittest.main()
