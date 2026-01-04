from unittest import TestCase
from strategies.strategy import AbstractStrategy
from strategies.exceptions import InvalidExpression

class ConcreteStrategy(AbstractStrategy):
    def __init__(self):
        super().__init__()

    def eval(self, expression):
        pass

class TestAbstractStrategy(TestCase):
    
    def load_parser_data(self):
        parser_data = []
        with open('tests/test_data/parser_data.txt', 'r') as file:
            lines = file.read().split('\n')
            lines = [line.strip() for line in lines if line and not line.isspace()]
            if len(lines) % 2 == 0:
                for i in range(0, len(lines), 2):
                    test_input, desired_output = lines[i], lines[i+1]
                    if desired_output.startswith("["):
                        desired_output = desired_output[1:]
                    if desired_output.endswith("]"):
                        desired_output = desired_output[:-1]
                    desired_output = [token.strip() for token in desired_output.split(",")]
                    parser_data.append((test_input, desired_output))
        return parser_data

    def test_parser(self):
        strategy = ConcreteStrategy()
        test_data = self.load_parser_data()
        for (test_input, desired_output) in test_data:
            assert strategy.parse(test_input) == desired_output

