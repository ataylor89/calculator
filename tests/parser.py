def load_valid_inputs():
    data = []
    with open('tests/test_data/valid_inputs.txt', 'r') as file:
        contents = file.read()
        for line in contents.split('\n'):
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

def load_invalid_inputs():
    data = []
    with open('tests/test_data/invalid_inputs.txt', 'r') as file:
        contents = file.read()
        for line in contents.split('\n'):
            test_input = line.strip()
            if test_input:
                data.append(test_input)
    return data

def load_infix_to_postfix():
    data = []
    with open('tests/test_data/infix_to_postfix.txt', 'r') as file:
        contents = file.read()
        lines = [line.strip() for line in contents.split('\n') if line.strip()]
        if len(lines) % 2 == 0:
            for i in range(0, len(lines), 2):
                test_input = lines[i]
                desired_output = [token.strip() for token in lines[i+1].split(" ")]
                data.append((test_input, desired_output))
    return data

def load_parse_expressions():
    data = []
    with open('tests/test_data/parse_expressions.txt', 'r') as file:
        contents = file.read()
        lines = [line.strip() for line in contents.split('\n') if line.strip()]
        if len(lines) % 2 == 0:
            for i in range(0, len(lines), 2):
                test_input = lines[i]
                desired_output = [token.strip() for token in lines[i+1].split(" ")]
                data.append((test_input, desired_output))
    return data

def load_eval_postfix():
    data = []
    with open('tests/test_data/eval_postfix.txt', 'r') as file:
        contents = file.read()
        for line in contents.split('\n'):
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
