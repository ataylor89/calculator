from strategies.strategy1 import Strategy1
from exceptions import InvalidExpression
from unittest import TestCase
import csv

class TestStrategy1(TestCase):
    
    def test_eval_with_valid_inputs(self):
        strategy = Strategy1()
        with open('tests/test_data/valid_inputs.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if not row:
                    continue
                input = row[0]
                expected = float(row[1])
                assert strategy.eval(input) == expected

    def test_eval_with_invalid_inputs(self):
        strategy = Strategy1()
        with open('tests/test_data/invalid_inputs.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if not row:
                    continue
                input = row[0]
                with self.assertRaises(InvalidExpression):
                    strategy.eval(input)

    def test_infix_to_postfix(self):
        strategy = Strategy1()
        with open('tests/test_data/infix_to_postfix.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if not row:
                    continue
                input = row[0]
                expected = row[1].split()
                assert strategy.convert_to_postfix(input) == expected

    def test_eval_postfix(self):
        strategy = Strategy1()
        with open('tests/test_data/eval_postfix.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if not row:
                    continue
                input = row[0].split()
                expected = float(row[1])
                assert strategy.eval_postfix(input) == expected
