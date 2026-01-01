import math

digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
operators = {'+', '-', '*', '/', '^'}
parentheses = {'(', ')'}

def eval(expression):
    try:
        tokens = parse(expression)
        postfix = convert_to_postfix(tokens)
        result = eval_postfix(postfix)
        return int(result) if result % 1 == 0 else result
    except ValueError as err:
        print(err)

def parse(expression):
    str = ''
    expression = expression.strip().replace(' ', '')
    for c in expression:
        if c in parentheses or c in operators:
            str += ' ' + c + ' '
        elif c in digits or c == '.':
            str += c
        else:
            raise ValueError('The expression contains invalid input')
    return str.split()

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

def is_negation(token, index, tokens):
    if token == '-' and (index == 0 or tokens[index-1] == '(' or tokens[index-1] in operators):
        return True
    return False

def precedence(operator):
    if operator in ('+', '-'):
        return 0
    elif operator in ('*', '/', '_'):
        return 1
    elif operator == '^':
        return 2
    else:
        return -1

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
        else:
            if is_negation(token, i, tokens):
                token = '_'
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
            val = stack.pop()
            stack.append(-1 * val)
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            if token == '+':
                stack.append(val2 + val1)
            elif token == '-':
                stack.append(val2 - val1)
            elif token == '*':
                stack.append(val2 * val1)
            elif token == '/':
                stack.append(val2 / val1)
            elif token == '^':
                stack.append(math.pow(val2, val1))
    return stack.pop()
