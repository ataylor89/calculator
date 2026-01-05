equations = '''

1 = 1
-1 = -1
--1 = 1
---1 = -1
1 + 2 = 3
1 + 2 * 3 = 7
1 + 2 * 3 - 4 / 5 = 6.2
1 + 2 * 3 - 4 / 5 + 6^7 = 279942.2
1 + 2 * 3 - (4 + 5) - (6 * 7) = -44
1 / 3 = 0.3333333333333333
2^(3/2) = 2.8284271247461903
16^(1/2) = 4
16^(-1/2) = 0.25
(2^3)^4 = 4096
2^(3^4) = 2417851639229258349412352
2^3^4 = 2417851639229258349412352

'''

def parse():
    data = []
    for line in equations.split('\n'):
        line = line.strip()
        if not line:
            continue
        parts = line.split("=")
        test_input = parts[0].strip()
        desired_output = float(parts[1].strip())
        if desired_output % 1 == 0:
            desired_output = int(desired_output)
        data.append((test_input, desired_output))
    return data
