import unittest
from strategies import strategy1, strategy2, strategy3

class TestInvalidInputs(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.test_data = []
        with open('tests/invalid_inputs.txt', 'r') as file:
            for line in file:
                cls.test_data.append(line.strip())
    
    def test_strategy1(self):
        for test_input in self.test_data:
            with self.assertRaises(Exception):
                strategy1.eval(test_input)

    def test_strategy2(self):
        for test_input in self.test_data:
            with self.assertRaises(Exception):
                strategy2.eval(test_input)

    def test_strategy3(self):
        for test_input in self.test_data:
            with self.assertRaises(Exception):
                strategy3.eval(test_input)
