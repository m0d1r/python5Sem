import os
import shutil
import sys
from datetime import datetime


def make_reserve_arc(source, dest):
    os.makedirs(dest, exist_ok=True)
    source = os.path.abspath(source)
    name = f'{os.path.basename(source)}_{datetime.now():%Y-%m-%d_%H-%M-%S}'
    return shutil.make_archive(os.path.join(dest, name), 'zip',
                               root_dir=os.path.dirname(source),
                               base_dir=os.path.basename(source))


if __name__ == '__main__':
    print(make_reserve_arc(sys.argv[1], sys.argv[2]))
