from tests import util

def load_parser_data():
    parser_data = []
    with open('tests/test_data/parser_data.txt', 'r') as file:
        lines = file.read().split('\n')
        lines = [line for line in lines if line and not line.isspace()]
        if len(lines) % 2 == 0:
            for i in range(0, len(lines), 2):
                test_input = lines[i]
                desired_output = util.parse_list(lines[i+1], ",")
                parser_data.append((test_input, desired_output))
    return parser_data

def load_infix_to_postfix():
    infix_to_postfix = []
    with open('tests/test_data/infix_to_postfix.txt', 'r') as file:
        lines = file.read().split('\n')
        lines = [line for line in lines if line and not line.isspace()]
        if len(lines) % 2 == 0:
            for i in range(0, len(lines), 2):
                infix = lines[i]
                postfix = util.parse_list(lines[i+1], " ", to_float=True)
                infix_to_postfix.append((infix, postfix))
    return infix_to_postfix    

def load_valid_inputs():
    valid_inputs = []
    with open('tests/test_data/valid_inputs.txt', 'r') as file:
        for line in file:
            parts = line.split("=")
            test_input = parts[0].strip()
            desired_output = float(parts[1].strip())
            if desired_output % 1 == 0:
                desired_output = int(desired_output)
            valid_inputs.append((test_input, desired_output))
    return valid_inputs

def load_invalid_inputs():
    invalid_inputs = []
    with open('tests/test_data/invalid_inputs.txt', 'r') as file:
        for line in file:
            invalid_inputs.append(line.strip())
    return invalid_inputs
