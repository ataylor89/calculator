equations = '''

1 2 + = 3
1 2 + 3 * = 9
1 2 + 3 2 / * = 4.5
1 2 + 3 4 * + 2 * = 30

'''

def parse():
    data = []
    for line in equations.split('\n'):
        line = line.strip()
        if not line:
            continue
        parts = line.split("=")
        test_input = parts[0].strip().split(" ")
        desired_output = float(parts[1].strip())
        if desired_output % 1 == 0:
            desired_output = int(desired_output)
        data.append((test_input, desired_output))
    return data
