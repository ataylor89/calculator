from tests import util

expressions = '''

1 + 2
[1, +, 2]

1+2
[1, +, 2]

1 + 2 * 3 - 4^5
[1, +, 2, *, 3, -, 4, ^, 5]

1+2*3-4^5
[1, +, 2, *, 3, -, 4, ^, 5]

(1 + 2) * 3 - 4 ^ (5 + 6)
[(, 1, +, 2, ), *, 3, -, 4, ^, (, 5, +, 6, )]

(1+2)*3 - 4^(5+6)
[(, 1, +, 2, ), *, 3, -, 4, ^, (, 5, +, 6, )]

123 + 456 * 789 ^ 123
[123, +, 456, *, 789, ^, 123]

'''

def test_data():
    data = []
    lines = [line.strip() for line in expressions.split('\n') if line.strip()]
    if len(lines) % 2 == 0:
        for i in range(0, len(lines), 2):
            expression = lines[i]
            tokens = util.parse_list(lines[i+1], ",")
            data.append((expression, tokens))
    return data
