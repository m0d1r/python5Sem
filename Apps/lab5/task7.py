import argparse


parser = argparse.ArgumentParser()
parser.add_argument('params', nargs='*')
args = parser.parse_args()
print('\n'.join(args.params) if args.params else 'no args')
