from parser import Parser
from exceptions import InvalidExpression

class Strategy1:

    def __init__(self):
        self.parser = Parser()

    def eval(self, expression):
        tokens = self.parser.parse(expression)
        postfix = self.convert_to_postfix(tokens)
        return self.eval_postfix(postfix)

    def convert_to_postfix(self, tokens):
        stack = []
        result = []
        pr = self.parser.precedence
        for token in tokens:
            if self.parser.is_number(token):
                result.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()
            elif token in self.parser.operators:
                left_assoc = self.parser.is_left_associative(token)
                while stack and stack[-1] != '(' and (pr(stack[-1]) > pr(token) or (pr(stack[-1]) == pr(token) and left_assoc)):
                    result.append(stack.pop())
                stack.append(token)
        while stack:
            result.append(stack.pop())
        return result

    def eval_postfix(self, tokens):
        stack = []
        for token in tokens:
            if self.parser.is_number(token):
                stack.append(float(token))
            elif token == '_':
                if len(stack) == 0:
                    raise InvalidExpression(f'The {token} operation is missing an operand')
                val = stack.pop()
                stack.append(-1 * val)
            else:
                if len(stack) < 2:
                    raise InvalidExpression(f'The {token} operation is missing one or more operands')
                val2 = stack.pop()
                val1 = stack.pop()
                if token == '+':
                    stack.append(val1 + val2)
                elif token == '-':
                    stack.append(val1 - val2)
                elif token == '*':
                    stack.append(val1 * val2)
                elif token == '/':
                    if val2 == 0:
                        raise InvalidExpression('Division by zero is not allowed')
                    stack.append(val1 / val2)
                elif token == '^':
                    stack.append(val1 ** val2)
        if len(stack) > 1:
            raise InvalidExpression('The expression is invalid')
        result = stack.pop()
        return int(result) if result % 1 == 0 else result
