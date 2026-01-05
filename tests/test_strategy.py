from unittest import TestCase
from strategies.strategy import AbstractStrategy
from strategies.exceptions import InvalidExpression
from tests.test_data import parser_data

class ConcreteStrategy(AbstractStrategy):

    def __init__(self):
        super().__init__()

    def eval(self, expression):
        pass

class TestAbstractStrategy(TestCase):
    
    def test_parser(self):
        strategy = ConcreteStrategy()
        test_data = parser_data.test_data()
        for (test_input, desired_output) in test_data:
            assert strategy.parse(test_input) == desired_output
