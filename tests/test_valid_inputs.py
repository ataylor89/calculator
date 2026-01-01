import unittest
from strategies import strategy1, strategy2, strategy3

class TestValidInputs(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.test_data = []
        with open('tests/valid_inputs.txt', 'r') as file:
            for line in file:
                parts = line.split("=")
                test_input = parts[0].strip()
                desired_output = float(parts[1].strip())
                if desired_output % 1 == 0:
                    desired_output = int(desired_output)
                cls.test_data.append((test_input, desired_output))
    
    def test_strategy1(self):
        for (test_input, desired_output) in self.test_data:
            assert strategy1.eval(test_input) == desired_output

    def test_strategy2(self):
        for (test_input, desired_output) in self.test_data:
            assert strategy2.eval(test_input) == desired_output

    def test_strategy3(self):
        for (test_input, desired_output) in self.test_data:
            assert strategy3.eval(test_input) == desired_output
