from strategies.strategy1 import Strategy1
from strategies.strategy2 import Strategy2
from strategies.strategy3 import Strategy3
from strategies.exceptions import InvalidExpression, InvalidStrategy
import argparse

def eval(expression, strategy=1):
    if strategy not in (1, 2, 3):
        raise InvalidStrategy()
    elif strategy == 1:
        strategy = Strategy1()
    elif strategy == 2:
        strategy = Strategy2()
    elif strategy == 3:
        strategy = Strategy3()
    return strategy.eval(expression)

def eval_and_print(expression, strategy=1):
    try:
        result = eval(expression, strategy)
        print(result)
    except (InvalidExpression, InvalidStrategy) as e:
        print(e)
    except Exception as e:
        print('There was an error while evaluating the expression')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='calculator.py', description='Evaluate an arithmetic expression')
    parser.add_argument('expression', type=str, nargs='?')
    parser.add_argument('-s', '--strategy', type=int, default=1)
    args = parser.parse_args()
    expression = args.expression
    strategy = args.strategy
    if expression:
        eval_and_print(expression, strategy)
    else:
        while True:
            user_input = input().strip()
            if not user_input or user_input == 'exit':
                break
            eval_and_print(user_input, strategy)
