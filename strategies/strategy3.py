from parser import Parser
from exceptions import InvalidExpression

class Strategy3:

    def __init__(self):
        self.parser = Parser()

    def eval(self, expression):
        tokens = self.parser.parse(expression)
        return self.simplify(tokens)

    def next(self, tokens):
        n = len(tokens)
        index = None
        nestedness = 0
        highest_priority = -1

        for i in range(0, n):
            token = tokens[i]

            if i < n - 1 and tokens[i:i+2] == '()':
                del tokens[i:i+2]
                return self.next(tokens)
            if i < n - 2 and tokens[i] == '(' and tokens[i+2] == ')':
                del tokens[i]
                del tokens[i+1]
                return self.next(tokens)
            elif self.parser.is_number(token):
                continue
            elif token == '(':
                nestedness += 1
                continue
            elif token == ')':
                nestedness -= 1
                continue
            elif token in self.parser.operators:
                priority = self.parser.precedence(token) + 3 * nestedness
                right_assoc = self.parser.is_right_associative(token)
                if priority > highest_priority or (priority == highest_priority and right_assoc):
                    highest_priority = priority
                    index = i

        return index

    def validate(self, index, tokens):
        operator = tokens[index]

        if operator == '_':
            if len(tokens) < index + 2:
                raise InvalidExpression(f'The {operator} operation is missing an operand')

            operand = tokens[index+1]

            if not self.parser.is_number(operand):
                raise InvalidExpression(f'The {operator} operation has an invalid operand')
        else:
            if index == 0 or len(tokens) < index + 2:
                raise InvalidExpression(f'The {operator} operation is missing one or more operands')

            operand1 = tokens[index-1]
            operand2 = tokens[index+1]

            if not self.parser.is_number(operand1) or not self.parser.is_number(operand2):
                raise InvalidExpression(f'The {operator} operation has one or more invalid operands')

            if operator == '/' and float(operand2) == 0:
                raise InvalidExpression('Division by zero is not allowed')

    def simplify(self, tokens):
        if len(tokens) == 1 and self.parser.is_number(tokens[0]):
            f = float(tokens[0])
            return int(f) if f.is_integer() else f

        index = self.next(tokens)

        if index is None:
            raise InvalidExpression('Unable to find an operation to perform')

        self.validate(index, tokens)
        operator = tokens[index]

        if operator == '_':
            result = -1 * float(tokens[index+1])
            tokens[index] = result
            del tokens[index+1]
        else:
            op1 = float(tokens[index-1])
            op2 = float(tokens[index+1])

            if operator == '+':
                result = op1 + op2
            elif operator == '-':
                result = op1 - op2
            elif operator == '*':
                result = op1 * op2
            elif operator == '/':
                result = op1 / op2
            elif operator == '^':
                result = op1 ** op2

            tokens[index-1] = result
            del tokens[index:index+2]

        return self.simplify(tokens)
