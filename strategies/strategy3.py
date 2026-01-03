from strategies.strategy import AbstractStrategy
from strategies.exceptions import InvalidExpression

class Strategy3(AbstractStrategy):
    def __init__(self):
        super().__init__()

    def eval(self, expression):
        tokens = super().parse(expression)
        if len(tokens) == 0:
            raise InvalidExpression('The expression is empty')
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
            elif super().is_number(token):
                continue
            elif token == '(':
                nestedness += 1
                continue
            elif token == ')':
                nestedness -= 1
                continue
            elif token in self._operators:
                priority = super().precedence(token) + 3 * nestedness
                if priority > highest_priority:
                    highest_priority = priority
                    index = i

        return index

    def validate(self, index, tokens):
        operator = tokens[index]

        if operator == '_':
            if len(tokens) < index + 2:
                raise InvalidExpression('A negation operation is missing an operand')

            operand = tokens[index+1]

            if not super().is_number(operand):
                raise InvalidExpression('A negation operation has an invalid operand')
        else:
            if index == 0 or len(tokens) < index + 2:
                raise InvalidExpression('A binary operation is missing one or more operands')

            operand1 = tokens[index-1]
            operand2 = tokens[index+1]

            if not super().is_number(operand1) or not super().is_number(operand2):
                raise InvalidExpression('A binary operation has one or more invalid operands')

            if operator == '/' and float(operand2) == 0:
                raise InvalidExpression('Division by zero is not allowed')

    def simplify(self, tokens):
        if len(tokens) == 1 and super().is_number(tokens[0]):
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
