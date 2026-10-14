from task1 import UnorderedList


def move_to_front(n, reader=input):
    lst = UnorderedList()
    for i in range(n):
        s = reader(f"Строка {i + 1}: ")
        if lst.search(s):
            lst.remove(s)
        lst.add(s)
        print(f"  после ввода {s!r}: {lst}")
    return lst


def run_tests():    
    inputs = iter(["one", "two", "three", "one", "one"])
    print("\nТест: one, two, three, one, one")
    move_to_front(5, reader=lambda _: next(inputs))


if __name__ == "__main__":
    run_tests()