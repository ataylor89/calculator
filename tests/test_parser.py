from parser import Parser
from exceptions import InvalidExpression
from unittest import TestCase
import csv

class TestParser(TestCase):

    def test_parser(self):
        parser = Parser()
        with open('tests/test_data/parse_expressions.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if not row:
                    continue
                input = row[0]
                expected = row[1].split()
                assert parser.parse(input) == expected
