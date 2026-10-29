import hashlib
from pathlib import Path


folder = Path(input("Путь к директории: ").strip().strip('"'))

if not folder.is_dir():
    print("Директория не найдена")
else:
    hashes = {}
    for path in folder.iterdir():
        if path.is_file():
            digest = hashlib.sha256()
            with path.open("rb") as f:
                for block in iter(lambda: f.read(65536), b""):
                    digest.update(block)
            hashes.setdefault(digest.hexdigest(), []).append(path.name)

    found = False
    for files in hashes.values():
        if len(files) > 1:
            print("Дубликаты:", ", ".join(files))
            found = True

    if not found:
        print("Дубликаты не найдены")
