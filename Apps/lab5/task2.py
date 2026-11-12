import sys
from zipfile import ZipFile


def human_size(size):
    units = ('Б', 'КБ', 'МБ', 'ГБ', 'ТБ')
    i = 0
    while size > 1023 and i < len(units) - 1:
        size /= 1024
        i += 1
    return f'{round(size)}{units[i]}'


def show_tree(tree, level=0):
    for name, value in tree.items():
        print('  ' * level + name + ('' if isinstance(value, dict) else ' ' + human_size(value)))
        if isinstance(value, dict):
            show_tree(value, level + 1)


with ZipFile(sys.argv[1]) as archive:
    tree = {}
    for info in archive.infolist():
        parts = info.filename.strip('/').split('/')
        if parts == ['']:
            continue
        current = tree
        for part in parts[:-1]:
            current = current.setdefault(part, {})
        if info.is_dir():
            current.setdefault(parts[-1], {})
        else:
            current[parts[-1]] = info.file_size
    show_tree(tree)
