from unittest import TestCase
from strategies.strategy1 import Strategy1
from strategies.exceptions import InvalidExpression

class TestStrategy1(TestCase):
    
    def load_valid_inputs(self):
        valid_inputs = []
        with open('tests/test_data/valid_inputs.txt', 'r') as file:
            for line in file:
                parts = line.split("=")
                test_input = parts[0].strip()
                desired_output = float(parts[1].strip())
                if desired_output % 1 == 0:
                    desired_output = int(desired_output)
                valid_inputs.append((test_input, desired_output))
        return valid_inputs

    def load_invalid_inputs(self):
        invalid_inputs = []
        with open('tests/test_data/invalid_inputs.txt', 'r') as file:
            for line in file:
                invalid_inputs.append(line.strip())
        return invalid_inputs

    def test_eval_with_valid_inputs(self):
        strategy = Strategy1()
        test_data = self.load_valid_inputs()
        for (test_input, desired_output) in test_data:
            assert strategy.eval(test_input) == desired_output

    def test_eval_with_invalid_inputs(self):
        strategy = Strategy1()
        test_data = self.load_invalid_inputs()
        for test_input in test_data:
            with self.assertRaises(InvalidExpression):
                strategy.eval(test_input)
