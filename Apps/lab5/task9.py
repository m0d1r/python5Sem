import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--sort', action='store_true')
parser.add_argument('pairs', nargs='*')
args = parser.parse_intermixed_args()
pairs = [pair.split('=', 1) for pair in args.pairs]
if args.sort:
    pairs.sort(key=lambda pair: pair[0])
for key, value in pairs:
    print(f'Key: {key} Value: {value}')
