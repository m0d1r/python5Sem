import argparse


parser = argparse.ArgumentParser()
parser.add_argument('numbers', nargs='*')
args = parser.parse_args()
try:
    numbers = [int(number) for number in args.numbers]
    if not numbers:
        print('NO PARAMS')
    elif len(numbers) == 1:
        print('TOO FEW PARAMS')
    elif len(numbers) > 2:
        print('TOO MANY PARAMS')
    else:
        print(sum(numbers))
except ValueError as error:
    print(type(error).__name__)
