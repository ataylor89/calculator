from strategies.strategy import AbstractStrategy
from strategies.exceptions import InvalidExpression

class Strategy1(AbstractStrategy):
    def __init__(self):
        super().__init__()

    def eval(self, expression):
        tokens = self.parse(expression)
        postfix = self.convert_to_postfix(tokens)
        result = self.eval_postfix(postfix)
        return int(result) if result % 1 == 0 else result

    def convert_to_postfix(self, tokens):
        st = []
        res = []
        pr = self.precedence
        for i in range(0, len(tokens)):
            token = tokens[i]
            if self.is_number(token):
                res.append(float(token))
            elif token == '(':
                st.append(token)
            elif token == ')':
                while st and st[-1] != '(':
                    res.append(st.pop())
                st.pop()
            elif token in self._operators:
                la = self.is_left_associative(token)
                while st and st[-1] != '(' and (pr(st[-1]) > pr(token) or (pr(st[-1]) == pr(token) and la)):
                    res.append(st.pop())
                st.append(token)
        while st:
            res.append(st.pop())
        return res

    def eval_postfix(self, tokens):
        stack = []
        for token in tokens:
            if self.is_number(token):
                stack.append(token)
            elif token == '_':
                if len(stack) == 0:
                    raise InvalidExpression('A negation operation is missing an operand')
                val = stack.pop()
                stack.append(-1 * val)
            else:
                if len(stack) < 2:
                    raise InvalidExpression('A binary operation is missing one or more operands')
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
            raise InvalidExpression('The resulting stack after postfix evaluation has multiple elements.')
        return stack.pop()
