import unittest
from strategies.strategy1 import Strategy1
from strategies.strategy2 import Strategy2
from strategies.strategy3 import Strategy3

class TestValidInputs(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.test_data = []
        with open('tests/test_data/valid_inputs.txt', 'r') as file:
            for line in file:
                parts = line.split("=")
                test_input = parts[0].strip()
                desired_output = float(parts[1].strip())
                if desired_output % 1 == 0:
                    desired_output = int(desired_output)
                cls.test_data.append((test_input, desired_output))
    
    def test_strategy1(self):
        strategy = Strategy1()
        for (test_input, desired_output) in self.test_data:
            assert strategy.eval(test_input) == desired_output

    def test_strategy2(self):
        strategy = Strategy2()
        for (test_input, desired_output) in self.test_data:
            assert strategy.eval(test_input) == desired_output

    def test_strategy3(self):
        strategy = Strategy3()
        for (test_input, desired_output) in self.test_data:
            assert strategy.eval(test_input) == desired_output
