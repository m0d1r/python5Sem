class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [UnorderedList() for _ in range(self.size)]
        self.count = 0

    def _hash(self, key):
        return key % self.size

    def _find(self, key):
        current = self.slots[self._hash(key)].head
        while current is not None:
            if current.getData()[0] == key:
                return current
            current = current.getNext()
        return None

    def _is_prime(self, n):
        return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))

    def _new_size(self, n):
        n = max(11, n)
        step = 0
        while True:
            for value in (n - step, n + step):
                if value >= 11 and self._is_prime(value):
                    return value
            step += 1

    def _resize(self, n):
        old_slots = self.slots
        self.size = self._new_size(n)
        self.slots = [UnorderedList() for _ in range(self.size)]
        self.count = 0

        for slot in old_slots:
            current = slot.head
            while current is not None:
                self.put(*current.getData())
                current = current.getNext()

    def put(self, key, value):
        node = self._find(key)
        if node is not None:
            node.setData((key, value))
            return

        self.slots[self._hash(key)].add((key, value))
        self.count += 1
        if self.count / self.size > 0.7:
            self._resize(self.size * 2)

    def get(self, key):
        node = self._find(key)
        return None if node is None else node.getData()[1]

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __len__(self):
        return self.count

    def __contains__(self, key):
        return self._find(key) is not None

    def __delitem__(self, key):
        node = self._find(key)
        if node is None:
            raise KeyError(key)

        self.slots[self._hash(key)].remove(node.getData())
        self.count -= 1
        if self.size > 11 and self.count / self.size < 0.2:
            self._resize(self.size // 2)


def run_tests():
    table = HashTable()
    for key in (0, 11, 22):
        table[key] = key * 10

    assert table.slots[0].size() == 3
    assert len(table) == 3 and 11 in table and 5 not in table
    print("Цепочка:", [table[key] for key in (0, 11, 22)])
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
