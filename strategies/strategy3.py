from strategies.exceptions import InvalidExpression

digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
operators = {'+', '-', '*', '/', '_', '^'}
parentheses = {'(', ')'}

def eval(expression):
    tokens = parse(expression)
    if len(tokens) == 0:
        raise InvalidExpression('The expression is empty')
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

def next(tokens):
    n = len(tokens)
    index = None
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

    return index

def validate(index, tokens):
    operator = tokens[index]

    if operator == '_':
        if len(tokens) < index + 2:
            raise InvalidExpression('A negation operation is missing an operand')

        operand = tokens[index+1]

        if not is_number(operand):
            raise InvalidExpression('A negation operation has an invalid operand')
    else:
        if index == 0 or len(tokens) < index + 2:
            raise InvalidExpression('A binary operation is missing one or more operands')

        operand1 = tokens[index-1]
        operand2 = tokens[index+1]

        if not is_number(operand1) or not is_number(operand2):
            raise InvalidExpression('A binary operation has one or more invalid operands')

        if operator == '/' and float(operand2) == 0:
            raise InvalidExpression('Division by zero is not allowed')

def simplify(tokens):
    if len(tokens) == 1 and is_number(tokens[0]):
        f = float(tokens[0])
        return int(f) if f.is_integer() else f

    index = next(tokens)

    if index is None:
        raise InvalidExpression('Unable to find an operation to perform')

    validate(index, tokens)
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

    return simplify(tokens)
