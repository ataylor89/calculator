digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
operators = {'+', '-', '*', '/', '^'}
parentheses = {'(', ')'}

precedence = {
    'addition': 0,
    'subtraction': 0,
    'multiplication': 1,
    'division': 1,
    'negation': 1,
    'exponentiation': 2
}

def eval(expression):
    try:
        tokens = parse(expression)
        return simplify(tokens)
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

def is_float(s):
    try:
        float(s)
        return True
    except:
        return False

def next(tokens):
    n = len(tokens)
    index = 0
    operation = None
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
        elif is_float(token):
            continue
        elif token == '(':
            nestedness += 1
            continue
        elif token == ')':
            nestedness -= 1
            continue
        elif token == '+':
            op = 'addition'
        elif token == '-':
            if i == 0 or tokens[i-1] in operators or tokens[i-1] == '(':
                op = 'negation'
            else:
                op = 'subtraction'
        elif token == '*':
            op  = 'multiplication'
        elif token == '/':
            op = 'division'
        elif token == '^':
            op = 'exponentiation'
        else:
            return None

        priority = precedence[op] + 3 * nestedness

        if priority > highest_priority:
            highest_priority = priority
            index = i
            operation = op

    return (index, operation)
            
def simplify(tokens):
    (index, operation) = next(tokens)

    if len(tokens) == 1:
        f = float(tokens[0])
        return int(f) if f.is_integer() else f

    if operation == 'negation':
        op1 = -1 * float(tokens[index+1])
        tokens[index] = op1
        del tokens[index+1]
    else:
        op1 = float(tokens[index-1])
        op2 = float(tokens[index+1])

        if operation == 'addition':
            op1 = op1 + op2
        elif operation == 'subtraction':
            op1 = op1 - op2
        elif operation == 'multiplication':
            op1 = op1 * op2
        elif operation == 'division':
            op1 = op1 / op2
        elif operation == 'exponentiation':
            op1 = op1 ** op2
        
        tokens[index-1] = op1 
        del tokens[index:index+2]

    return simplify(tokens)
