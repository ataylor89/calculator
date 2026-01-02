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

def perform_operation(operators, operands):
    operator = operators.pop()
    if operator == '_':
        if len(operands) == 0:
            raise InvalidExpression('A negation operation is missing an operand')
        operand1 = operands.pop()
        operands.append(-1 * operand1)
    elif operator in valid_operators:
        if len(operands) < 2:
            raise InvalidExpression('A binary operation is missing one or more operands')
        operand2 = operands.pop()
        operand1 = operands.pop()
        if operator == '+':
            operands.append(operand1 + operand2)
        elif operator == '-':
            operands.append(operand1 - operand2)    
        elif operator == '*':
            operands.append(operand1 * operand2)
        elif operator == '/':
            if operator == '/' and operand2 == 0:
                raise InvalidExpression('Division by zero is not allowed')
            operands.append(operand1 / operand2)
        elif operator == '^':
            operands.append(operand1 ** operand2)

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
            while operators and operators[-1] != '(':
                perform_operation(operators, operands)
            operators.pop()
        elif token in valid_operators:
            la = is_left_associative(token)
            while ops and ops[-1] != '(' and (pr(ops[-1]) > pr(token) or (pr(ops[-1]) == pr(token) and la)):
                perform_operation(operators, operands)
            operators.append(token)
    
    while operators:
        perform_operation(operators, operands)

    return operands.pop()
