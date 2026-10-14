class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found and current is not None:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if not found:
            raise ValueError(f"{item} not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    # 1. Оставшиеся методы

    def append(self, item):
        temp = Node(item)
        if self.head is None:
            self.head = temp
            return
        current = self.head
        while current.get_next() is not None:
            current = current.get_next()
        current.set_next(temp)

    def index(self, item):
        current = self.head
        pos = 0
        while current is not None:
            if current.get_data() == item:
                return pos
            current = current.get_next()
            pos += 1
        raise ValueError(f"{item} not in list")

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
            return
        if pos >= self.size():
            self.append(item)
            return
        temp = Node(item)
        current = self.head
        previous = None
        for _ in range(pos):
            previous = current
            current = current.get_next()
        previous.set_next(temp)
        temp.set_next(current)

    def pop(self, pos=None):
        if self.is_empty():
            raise IndexError("pop from empty list")
        if pos is None:
            pos = self.size() - 1
        if pos < 0 or pos >= self.size():
            raise IndexError("pop index out of range")
        if pos == 0:
            data = self.head.get_data()
            self.head = self.head.get_next()
            return data
        current = self.head
        previous = None
        for _ in range(pos):
            previous = current
            current = current.get_next()
        data = current.get_data()
        previous.set_next(current.get_next())
        return data

    # 2. __str__ в Python-стиле

    def __str__(self):
        items = []
        current = self.head
        while current is not None:
            items.append(str(current.get_data()))
            current = current.get_next()
        return "[" + ", ".join(items) + "]"

    # 3. Срез

    def slice(self, start, stop):
        result = UnorderedList()
        current = self.head
        pos = 0
        while current is not None and pos < stop:
            if pos >= start:
                result.append(current.get_data())
            current = current.get_next()
            pos += 1
        return result


if __name__ == "__main__":
    # Пункт 1: append, index, insert, pop, pop(pos)
    lst = UnorderedList()
    for x in [10, 20, 30]:
        lst.append(x)
    print("1.1 append:", lst)

    print("1.2 index(20):", lst.index(20))

    lst.insert(1, 15)
    print("1.3 insert(1, 15):", lst)

    print("1.4 pop():", lst.pop(), "->", lst)

    print("1.5 pop(0):", lst.pop(0), "->", lst)

    # Пункт 2: __str__
    lst2 = UnorderedList()
    print("2.1 str(пустой):", lst2)
    for x in [1, 2, 3]:
        lst2.append(x)
    print("2.2 str(заполненный):", lst2)

    # Пункт 3: slice
    lst3 = UnorderedList()
    for x in range(10):
        lst3.append(x)
    print("3.1 slice(2, 6):", lst3.slice(2, 6))
    print("3.2 slice(0, 0):", lst3.slice(0, 0))
    print("3.3 slice(5, 100):", lst3.slice(5, 100))