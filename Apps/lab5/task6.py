import sys


args = sys.argv[1:]
pairs = [arg.split('=', 1) for arg in args if arg != '--sort']
if '--sort' in args:
    pairs.sort(key=lambda pair: pair[0])
for key, value in pairs:
    print(f'Key: {key} Value: {value}')
