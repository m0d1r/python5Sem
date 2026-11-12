from collections import deque
from graph import Graph


def person_is_seller(name):
    return name[0] == 'a'


graph = Graph()
for start, end in [
    ("you", "alice"),
    ("you", "bob"),
    ("you", "claire"),
    ("bob", "anuj"),
    ("bob", "peggy"),
    ("alice", "peggy"),
    ("claire", "thom"),
    ("claire", "jonny"),
]:
    graph.add_edge(start, end)


def search(name):
    search_queue = deque()
    search_queue += graph.neighbors(name)
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph.neighbors(person)
                searched.add(person)
    return False


if __name__ == "__main__":
    search("you")
