from task2 import HashTable as BaseHashTable


class HashTable(BaseHashTable):
    def _hash(self, key):
        if isinstance(key, str):
            result = 0
            for char in key:
                result = (result * 31 + ord(char)) % self.size
            return result
        return super()._hash(key)


if __name__ == "__main__":
    table = HashTable()
    table["кот"] = 1
    table["Кот"] = 2
    table["кот"] = 3
    print(table["кот"], table["Кот"])
    print("кот" in table, "собака" in table, len(table))
