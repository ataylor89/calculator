from unittest import TestCase
from strategies.strategy1 import Strategy1
from strategies.exceptions import InvalidExpression
from tests import parser

class TestStrategy1(TestCase):
    
    def test_eval_with_valid_inputs(self):
        strategy = Strategy1()
        test_data = parser.load_valid_inputs()
        for (test_input, desired_output) in test_data:
            assert strategy.eval(test_input) == desired_output

    def test_eval_with_invalid_inputs(self):
        strategy = Strategy1()
        test_data = parser.load_invalid_inputs()
        for test_input in test_data:
            with self.assertRaises(InvalidExpression):
                strategy.eval(test_input)

    def test_infix_to_postfix(self):
        strategy = Strategy1()
        test_data = parser.load_infix_to_postfix()
        for (test_input, desired_output) in test_data:
            assert strategy.convert_to_postfix(test_input) == desired_output

    def test_eval_postfix(self):
        strategy = Strategy1()
        test_data = parser.load_eval_postfix()
        for (test_input, desired_output) in test_data:
            assert strategy.eval_postfix(test_input) == desired_output
