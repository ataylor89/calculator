from strategies.exceptions import InvalidExpression

digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
operators = {'+', '-', '*', '/', '_', '^'}
parentheses = {'(', ')'}

def eval(expression):
    tokens = parse(expression)
    return simplify(tokens)

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

def precedence(operator):
    if operator in ('+', '-'):
        return 0
    elif operator in ('*', '/', '_'):
        return 1
    elif operator == '^':
        return 2
    else:
        return -1

def next(tokens):
    n = len(tokens)
    index = 0
    nestedness = 0
    highest_priority = -1

    for i in range(0, n):
        token = tokens[i]

        if i < n - 1 and tokens[i:i+2] == '()':
            del tokens[i:i+2]
            return next(tokens)
        if i < n - 2 and tokens[i] == '(' and tokens[i+2] == ')':
            del tokens[i]
            del tokens[i+1]
            return next(tokens)
        elif is_number(token):
            continue
        elif token == '(':
            nestedness += 1
            continue
        elif token == ')':
            nestedness -= 1
            continue
        elif token in operators:
            priority = precedence(token) + 3 * nestedness
            if priority > highest_priority:
                highest_priority = priority
                index = i
        else:
            return None

    return index
            
def simplify(tokens):
    if len(tokens) == 1:
        f = float(tokens[0])
        return int(f) if f.is_integer() else f

    index = next(tokens)
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
        else:
            raise InvalidExpression('The token %s is not valid' %operator)
        
        tokens[index-1] = result
        del tokens[index:index+2]

    return simplify(tokens)
