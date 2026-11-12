import os
import sys


def human_size(size):
    units = ('Б', 'КБ', 'МБ', 'ГБ', 'ТБ')
    i = 0
    while size > 1023 and i < len(units) - 1:
        size /= 1024
        i += 1
    return f'{round(size)}{units[i]}'


def total_size(path):
    if os.path.isfile(path):
        return os.path.getsize(path)
    return sum(os.path.getsize(os.path.join(root, name))
               for root, _, files in os.walk(path) for name in files)


path = sys.argv[1] if len(sys.argv) > 1 else '.'
items = [(entry.name, total_size(entry.path)) for entry in os.scandir(path)]
for name, size in sorted(items, key=lambda item: item[1], reverse=True)[:10]:
    print(f'{name:<60} - {human_size(size)}')
