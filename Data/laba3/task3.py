from task1 import UnorderedList


def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.get_next()
        current.set_next(prev)
        prev = current
        current = next_node
    return prev


def run_tests():
    lst = UnorderedList()
    for x in [1, 2, 3, 4]:
        lst.append(x)
    print("Исходный:", lst)
    lst.head = reverse_list(lst.head)
    print("Развёрнутый:", lst)


if __name__ == "__main__":
    run_tests()