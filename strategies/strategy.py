from abc import ABC, abstractmethod
from strategies.exceptions import InvalidExpression

class AbstractStrategy(ABC):
    def __init__(self):
        self._digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        self._operators = {'+', '-', '*', '/', '_', '^'}
        self._parentheses = {'(', ')'}

    @abstractmethod
    def eval(self, expression):
        pass

    def parse(self, expression):
        str = ''
        expression = expression.strip().replace(' ', '')
        for c in expression:
            if c in self._parentheses or c in self._operators:
                str += ' ' + c + ' '
            elif c in self._digits or c == '.':
                str += c
            else:
                raise InvalidExpression('The expression contains an invalid token')
        tokens = str.split()
        for i in range(0, len(tokens)):
            if tokens[i] == '-' and (i == 0 or tokens[i-1] == '(' or tokens[i-1] in self._operators):
                tokens[i] = '_'
        return tokens

    def is_number(self, s):
        try:
            float(s)
            return True
        except:
            return False

    def is_left_associative(self, operator):
        if operator in ('^', '_'):
            return False
        return True

    def precedence(self, operator):
        if operator in ('+', '-'):
            return 0
        elif operator in ('*', '/', '_'):
            return 1
        elif operator == '^':
            return 2
