from parser import Parser
from exceptions import InvalidExpression

class Strategy2:

    def __init__(self):
        self.parser = Parser()

    def eval(self, expression):
        tokens = self.parser.parse(expression)
        return self.eval_tokens(tokens)

    def perform_operation(self, operators, operands):
        operator = operators.pop()
        if operator == '_':
            if len(operands) == 0:
                raise InvalidExpression(f'The {operator} operation is missing an operand')
            operand1 = operands.pop()
            operands.append(-1 * operand1)
        elif operator in self.parser.operators:
            if len(operands) < 2:
                raise InvalidExpression(f'The {operator} operation is missing one or more operands')
            operand2 = operands.pop()
            operand1 = operands.pop()
            if operator == '+':
                operands.append(operand1 + operand2)
            elif operator == '-':
                operands.append(operand1 - operand2)
            elif operator == '*':
                operands.append(operand1 * operand2)
            elif operator == '/':
                if operand2 == 0:
                    raise InvalidExpression('Division by zero is not allowed')
                operands.append(operand1 / operand2)
            elif operator == '^':
                operands.append(operand1 ** operand2)

    def eval_tokens(self, tokens):
        operands = []
        operators = ops = []
        pr = self.parser.precedence

        for i in range(0, len(tokens)):
            token = tokens[i]
            if self.parser.is_number(token):
                operands.append(float(token))
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    self.perform_operation(operators, operands)
                operators.pop()
            elif token in self.parser.operators:
                left_assoc = self.parser.is_left_associative(token)
                while ops and ops[-1] != '(' and (pr(ops[-1]) > pr(token) or (pr(ops[-1]) == pr(token) and left_assoc)):
                    self.perform_operation(operators, operands)
                operators.append(token)

        while operators:
            self.perform_operation(operators, operands)

        result = operands.pop()
        return int(result) if result % 1 == 0 else result
