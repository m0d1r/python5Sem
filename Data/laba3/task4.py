import time
from collections import deque as py_deque
from task1 import UnorderedList


class Stack:
    def __init__(self):
        self.items = UnorderedList()

    def is_empty(self):
        return self.items.is_empty()

    def push(self, item):
        self.items.add(item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items.head.get_data()

    def size(self):
        return self.items.size()


class Queue:
    def __init__(self):
        self.items = UnorderedList()

    def is_empty(self):
        return self.items.is_empty()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return self.items.size()


class Deque:
    def __init__(self):
        self.items = UnorderedList()

    def is_empty(self):
        return self.items.is_empty()

    def add_front(self, item):
        self.items.add(item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def size(self):
        return self.items.size()


def run_tests():
    s = Stack()
    for i in [1, 2, 3]:
        s.push(i)
    print("Stack:", [s.pop() for _ in range(3)])

    q = Queue()
    for i in [1, 2, 3]:
        q.enqueue(i)
    print("Queue:", [q.dequeue() for _ in range(3)])

    d = Deque()
    d.add_rear(2)
    d.add_rear(3)
    d.add_front(1)
    print("Deque:", [d.remove_front(), d.remove_rear(), d.remove_front()])


def bench_stack(n):
    t0 = time.perf_counter()
    st = []
    for i in range(n):
        st.append(i)
    for _ in range(n):
        st.pop()
    t_list = time.perf_counter() - t0

    t0 = time.perf_counter()
    st = Stack()
    for i in range(n):
        st.push(i)
    for _ in range(n):
        st.pop()
    t_linked = time.perf_counter() - t0

    print(f"Стек  (n={n}): list={t_list:.4f}s, linked={t_linked:.4f}s")


def bench_queue(n):
    t0 = time.perf_counter()
    q = py_deque()
    for i in range(n):
        q.append(i)
    for _ in range(n):
        q.popleft()
    t_deque = time.perf_counter() - t0

    t0 = time.perf_counter()
    q = Queue()
    for i in range(n):
        q.enqueue(i)
    for _ in range(n):
        q.dequeue()
    t_linked = time.perf_counter() - t0

    print(f"Очередь (n={n}): deque={t_deque:.4f}s, linked={t_linked:.4f}s")


if __name__ == "__main__":
    run_tests()
    print()
    for n in [5000, 10000, 20000]:
        bench_stack(n)
        bench_queue(n)
        print()