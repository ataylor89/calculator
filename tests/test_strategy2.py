from strategies.strategy2 import Strategy2
from exceptions import InvalidExpression
from unittest import TestCase
import csv

class TestStrategy2(TestCase):
    
    def test_eval_with_valid_inputs(self):
        strategy = Strategy2()
        with open('tests/test_data/valid_inputs.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if not row:
                    continue
                input = row[0]
                expected = float(row[1])
                assert strategy.eval(input) == expected

    def test_eval_with_invalid_inputs(self):
        strategy = Strategy2()
        with open('tests/test_data/invalid_inputs.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if not row:
                    continue
                input = row[0]
                with self.assertRaises(InvalidExpression):
                    strategy.eval(input)
