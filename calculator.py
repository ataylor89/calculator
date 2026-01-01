from strategies import strategy1, strategy2
from strategies.exceptions import InvalidExpression, InvalidStrategy
import argparse

def eval(expression, strategy=1):
    if strategy == 1:
        return strategy1.eval(expression)
    elif strategy == 2:
        return strategy2.eval(expression)
    else:
        raise InvalidStrategy()

def main():
    parser = argparse.ArgumentParser(prog='calculator.py', description='Evaluate an arithmetic expression')
    parser.add_argument('expression', type=str)
    parser.add_argument('-s', '--strategy', type=int, default=1)
    args = parser.parse_args()
    try:
        result = eval(args.expression, args.strategy)
        print(result)
    except (InvalidExpression, InvalidStrategy) as e:
        print(e)
    except Exception as e:
        print('There was an error while evaluating the expression')

if __name__ == '__main__':
    main()
