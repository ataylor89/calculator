from tests import util

expressions = '''

1 + 2
1 2 +

1 + 2 * 3
1 2 3 * +

1 + 2 * 3 - 4 / 5
1 2 3 * + 4 5 / -

'''

def test_data():
    data = []
    lines = [line.strip() for line in expressions.split('\n') if line.strip()]
    if len(lines) % 2 == 0:
        for i in range(0, len(lines), 2):
            infix = lines[i]
            postfix = util.parse_list(lines[i+1], " ", to_float=True)
            data.append((infix, postfix))
    return data
