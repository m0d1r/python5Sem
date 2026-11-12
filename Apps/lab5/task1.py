import os


def human_size(size):
    units = ('Б', 'КБ', 'МБ', 'ГБ', 'ТБ')
    i = 0
    while size > 1023 and i < len(units) - 1:
        size /= 1024
        i += 1
    return f'{round(size)}{units[i]}'


def file_sizes():
    return '\n'.join(f'{entry.name} {human_size(entry.stat().st_size)}'
                     for entry in os.scandir('.') if entry.is_file())


if __name__ == '__main__':
    print(file_sizes())
