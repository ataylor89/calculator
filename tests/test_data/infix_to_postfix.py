expressions = '''

1 + 2
1 2 +

1 + 2 * 3
1 2 3 * +

1 + 2 * 3 - 4 / 5
1 2 3 * + 4 5 / -

'''

def parse():
    data = []
    lines = [line.strip() for line in expressions.split('\n') if line.strip()]
    if len(lines) % 2 == 0:
        for i in range(0, len(lines), 2):
            infix = lines[i]
            postfix = [token.strip() for token in lines[i+1].split(" ")]
            data.append((infix, postfix))
    return data
