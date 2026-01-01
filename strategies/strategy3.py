from strategies.exceptions import InvalidExpression

digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
valid_operators = {'+', '-', '*', '/', '_', '^'}
parentheses = {'(', ')'}

def eval(expression):
    tokens = parse(expression)
    result = eval_tokens(tokens)
    return int(result) if result % 1 == 0 else result

def parse(expression):
    str = ''
    expression = expression.strip().replace(' ', '')
    for c in expression:
        if c in parentheses or c in valid_operators:
            str += ' ' + c + ' '
        elif c in digits or c == '.':
            str += c
        else:
            raise InvalidExpression('The expression contains an invalid token')
    tokens = str.split()
    for i in range(0, len(tokens)):
        if tokens[i] == '-' and (i == 0 or tokens[i-1] == '(' or tokens[i-1] in valid_operators):
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
    else:
        return -1

def performOperation(operators, operands):
    operator = operators.pop()
    
    if operator == '_':
        operand1 = operands.pop()
        operands.append(-1 * operand1)
    elif operator in valid_operators:
        operand2 = operands.pop()
        operand1 = operands.pop()
        if operator == '+':
            operands.append(operand1 + operand2)
        elif operator == '-':
            operands.append(operand1 - operand2)    
        elif operator == '*':
            operands.append(operand1 * operand2)
        elif operator == '/':
            operands.append(operand1 / operand2)
        elif operator == '^':
            operands.append(operand1 ** operand2)
    else:
        raise InvalidExpression('Tried to perform an invalid operation.')

def eval_tokens(tokens):
    operands = []
    operators = ops = []
    pr = precedence

    for i in range(0, len(tokens)):
        token = tokens[i]
        if is_number(token):
            operands.append(float(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators[-1] != '(':
                performOperation(operators, operands)
            operators.pop()
        else:
            la = is_left_associative(token)
            while ops and ops[-1] != '(' and (pr(ops[-1]) > pr(token) or (pr(ops[-1]) == pr(token) and la)):
                performOperation(operators, operands)
            operators.append(token)
    
    while operators:
        performOperation(operators, operands)

    return operands.pop()
