import unittest
from strategies.strategy1 import Strategy1
from strategies.strategy2 import Strategy2
from strategies.strategy3 import Strategy3
from strategies.exceptions import InvalidExpression

class TestInvalidInputs(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.test_data = []
        with open('tests/test_data/invalid_inputs.txt', 'r') as file:
            for line in file:
                cls.test_data.append(line.strip())
    
    def test_strategy1(self):
        strategy = Strategy1()
        for test_input in self.test_data:
            with self.assertRaises(InvalidExpression):
                strategy.eval(test_input)

    def test_strategy2(self):
        strategy = Strategy2()
        for test_input in self.test_data:
            with self.assertRaises(InvalidExpression):
                strategy.eval(test_input)

    def test_strategy3(self):
        strategy = Strategy3()
        for test_input in self.test_data:
            with self.assertRaises(InvalidExpression):
                strategy.eval(test_input)
