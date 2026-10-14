class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return current
            current = current.next
        return None

    def add_front(self, item):
        node = DNode(item)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self._size += 1
        return node

    def add_rear(self, item):
        node = DNode(item)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self._size += 1
        return node

    def remove_front(self):
        if self.is_empty():
            raise IndexError("remove from empty list")
        data = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        self._size -= 1
        return data

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("remove from empty list")
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        self._size -= 1
        return data

    def insert_before(self, node, item):
        new_node = DNode(item)
        new_node.next = node
        new_node.prev = node.prev
        if node.prev is not None:
            node.prev.next = new_node
        else:
            self.head = new_node
        node.prev = new_node
        self._size += 1
        return new_node

    def insert_after(self, node, item):
        new_node = DNode(item)
        new_node.prev = node
        new_node.next = node.next
        if node.next is not None:
            node.next.prev = new_node
        else:
            self.tail = new_node
        node.next = new_node
        self._size += 1
        return new_node

    def remove_node(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        self._size -= 1
        return node.data

    def __str__(self):
        items = []
        current = self.head
        while current is not None:
            items.append(str(current.data))
            current = current.next
        return "[" + ", ".join(items) + "]"


def run_tests():
    dl = DoubleList()

    dl.add_front(2)
    dl.add_rear(3)
    n1 = dl.add_front(1)
    print("add_front/add_rear:", dl, "size:", dl.size())

    print("search(2):", dl.search(2).data)
    print("search(99):", dl.search(99))

    dl.insert_after(n1, 15)
    print("insert_after(1, 15):", dl)

    dl.insert_before(n1, 5)
    print("insert_before(1, 5):", dl)

    dl.remove_node(dl.search(15))
    print("remove_node(15):", dl)

    print("remove_front:", dl.remove_front(), "->", dl)
    print("remove_rear:", dl.remove_rear(), "->", dl)

    print("is_empty:", dl.is_empty(), "size:", dl.size())


if __name__ == "__main__":
    run_tests()