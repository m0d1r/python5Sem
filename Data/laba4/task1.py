class HashTable:
    def __init__(self):
        self.size = 11
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.count = 0
        self.deleted = object()

    def _is_prime(self, n):
        return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))

    def _new_size(self, n):
        n = max(11, n)
        step = 0
        while True:
            for value in (n - step, n + step):
                if value >= 11 and value % 4 == 3 and self._is_prime(value):
                    return value
            step += 1

    def _position(self, key, insert=False):
        start = key % self.size
        deleted_pos = None

        for i in range(self.size):
            j = (i + 1) // 2
            pos = (start + (j * j if i % 2 else -j * j)) % self.size

            if self.keys[pos] is None:
                return (deleted_pos if deleted_pos is not None else pos) if insert else -1
            if self.keys[pos] is self.deleted:
                if insert and deleted_pos is None:
                    deleted_pos = pos
            elif self.keys[pos] == key:
                return pos

        return deleted_pos if insert else -1

    def _resize(self, n):
        old_keys, old_values = self.keys, self.values
        self.size = self._new_size(n)
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.count = 0

        for key, value in zip(old_keys, old_values):
            if key is not None and key is not self.deleted:
                self.put(key, value)

    def put(self, key, value):
        pos = self._position(key, True)
        if self.keys[pos] is None or self.keys[pos] is self.deleted:
            self.count += 1
        self.keys[pos] = key
        self.values[pos] = value

        if self.count / self.size > 0.7:
            self._resize(self.size * 2)

    def get(self, key):
        pos = self._position(key)
        return None if pos == -1 else self.values[pos]

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __len__(self):
        return self.count

    def __contains__(self, key):
        return self._position(key) != -1

    def __delitem__(self, key):
        pos = self._position(key)
        if pos == -1:
            raise KeyError(key)

        self.keys[pos] = self.deleted
        self.values[pos] = None
        self.count -= 1

        if self.size > 11 and self.count / self.size < 0.2:
            self._resize(self.size // 2)


def run_tests():
    table = HashTable()
    for key in (0, 11, 22):
        table[key] = key * 10

    assert [table.keys[i] for i in (0, 1, 10)] == [0, 11, 22]
    assert len(table) == 3 and 11 in table and 5 not in table
    print("Коллизии:", [table[key] for key in (0, 11, 22)])
    print("len:", len(table), "in:", 11 in table, 5 in table)

    table[11] = 999
    assert len(table) == 3 and table[11] == 999
    print("Обновление:", table[11])

    del table[11]
    assert 11 not in table and table[22] == 220
    table[11] = 110
    assert table[11] == 110
    print("Удаление и повторная вставка:", table[11])

    old_size = table.size
    for i in range(1, 30):
        table[i] = i
    assert table.size > old_size and len(table) == 30
    print("Увеличение:", old_size, "->", table.size)

    large_size = table.size
    for i in range(1, 30):
        del table[i]
    assert table.size < large_size and len(table) == 1 and table[0] == 0
    print("Уменьшение:", large_size, "->", table.size)
    print("Все тесты пройдены")


if __name__ == "__main__":
    run_tests()
