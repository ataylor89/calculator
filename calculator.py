from strategies import strategy1, strategy2
import argparse

def main():
    parser = argparse.ArgumentParser(prog='calculator.py', description='Evaluate an arithmetic expression')
    parser.add_argument('expression', type=str)
    parser.add_argument('-s', '--strategy', type=int, default=1)
    args = parser.parse_args()
    if args.strategy == 1:
        result = strategy1.eval(args.expression)
        print(result)
    elif args.strategy == 2:
        result = strategy2.eval(args.expression)
        print(result)
    else:
        print('Strategy not supported.')

if __name__ == '__main__':
    main()
