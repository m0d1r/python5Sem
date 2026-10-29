import hashlib
import hmac
import json
import secrets
from pathlib import Path


FILE = Path(__file__).with_name("users.json")


def load_users():
    if not FILE.exists():
        return {}
    with FILE.open(encoding="utf-8") as f:
        return json.load(f)


def register():
    users = load_users()
    login = input("Логин: ")
    if login in users:
        print("Такой пользователь уже существует")
        return

    password = input("Пароль: ")
    salt = secrets.token_bytes(32)
    password_hash = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)
    users[login] = {"salt": salt.hex(), "hash": password_hash.hex()}
    with FILE.open("w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)
    print("Регистрация выполнена")


def authorize():
    users = load_users()
    login = input("Логин: ")
    password = input("Пароль: ")
    user = users.get(login)
    if user is None:
        print("Пользователь не найден")
        return

    salt = bytes.fromhex(user["salt"])
    password_hash = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)
    if hmac.compare_digest(password_hash, bytes.fromhex(user["hash"])):
        print("Авторизация успешна")
    else:
        print("Неверный пароль")


if __name__ == "__main__":
    choice = input("1 - регистрация, 2 - авторизация: ")
    if choice == "1":
        register()
    elif choice == "2":
        authorize()
