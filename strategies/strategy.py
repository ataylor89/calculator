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
        tokens = []
        buffer = ''
        expression = expression.strip()
        n = len(expression)
        for i in range(0, n):
            ch = expression[i]
            if ch in self._operators or ch in self._parentheses:
                if buffer:
                    if self.is_number(buffer):
                        tokens.append(buffer)
                        buffer = ''
                    else:
                        raise InvalidExpression('The string buffer cannot be parsed as a number')
                tokens.append(ch)
            elif ch == ' ':
                if buffer:
                    if self.is_number(buffer):
                        tokens.append(buffer)
                        buffer = ''
                    else:
                        raise InvalidExpression('The string buffer cannot be parsed as a number')
            elif ch in self._digits or ch == '.':
                buffer += ch
                if buffer and i == n - 1:
                    if self.is_number(buffer):
                        tokens.append(buffer)
                        buffer = ''
                    else:
                        raise InvalidExpression('The string buffer cannot be parsed as a number')
            else:
                raise InvalidExpression('The expression contains one or more invalid characters')
        if not tokens:
            raise InvalidExpression('The expression is empty')
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
        return operator in ('+', '-', '*', '/')

    def is_right_associative(self, operator):
        return operator in ('^', '_')

    def precedence(self, operator):
        if operator in ('+', '-'):
            return 0
        elif operator in ('*', '/', '_'):
            return 1
        elif operator == '^':
            return 2
