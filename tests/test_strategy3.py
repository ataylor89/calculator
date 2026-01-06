from unittest import TestCase
from strategies.strategy3 import Strategy3
from strategies.exceptions import InvalidExpression
from tests import parser

class TestStrategy3(TestCase):
    
    def test_eval_with_valid_inputs(self):
        strategy = Strategy3()
        test_data = parser.load_valid_inputs()
        for (test_input, desired_output) in test_data:
            assert strategy.eval(test_input) == desired_output

    def test_eval_with_invalid_inputs(self):
        strategy = Strategy3()
        test_data = parser.load_invalid_inputs()
        for test_input in test_data:
            with self.assertRaises(InvalidExpression):
                strategy.eval(test_input)
