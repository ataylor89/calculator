from strategies.exceptions import InvalidExpression

digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
operators = {'+', '-', '*', '/', '_', '^'}
parentheses = {'(', ')'}

def eval(expression):
    tokens = parse(expression)
    postfix = convert_to_postfix(tokens)
    result = eval_postfix(postfix)
    return int(result) if result % 1 == 0 else result

def parse(expression):
    str = ''
    expression = expression.strip().replace(' ', '')
    for c in expression:
        if c in parentheses or c in operators:
            str += ' ' + c + ' '
        elif c in digits or c == '.':
            str += c
        else:
            raise InvalidExpression('The expression contains an invalid token')
    tokens = str.split()
    for i in range(0, len(tokens)):
        if tokens[i] == '-' and (i == 0 or tokens[i-1] == '(' or tokens[i-1] in operators):
            tokens[i] = '_'
    return tokens

def is_number(s):
    try:
        float(s)
        return True
    except:
        return False

def is_left_associative(operator):
    if operator in ('^', '_'):
        return False
    return True

def precedence(operator):
    if operator in ('+', '-'):
        return 0
    elif operator in ('*', '/', '_'):
        return 1
    elif operator == '^':
        return 2

def convert_to_postfix(tokens):
    st = []
    res = []
    pr = precedence
    for i in range(0, len(tokens)):
        token = tokens[i]
        if is_number(token):
            res.append(float(token))
        elif token == '(':
            st.append(token)
        elif token == ')':
            while st and st[-1] != '(':
                res.append(st.pop())
            st.pop()
        elif token in operators:
            la = is_left_associative(token)
            while st and st[-1] != '(' and (pr(st[-1]) > pr(token) or (pr(st[-1]) == pr(token) and la)):
                res.append(st.pop())
            st.append(token)
    while st:
        res.append(st.pop())
    return res

def eval_postfix(tokens):
    stack = []
    for token in tokens:
        if is_number(token):
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
