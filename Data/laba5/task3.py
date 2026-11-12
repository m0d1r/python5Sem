from graph import Graph


def topological_sort(graph):
    visited = set()
    result = []

    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph.neighbors(vertex):
            if neighbor not in visited:
                dfs(neighbor)
        result.append(vertex)

    for vertex in graph.vertices:
        if vertex not in visited:
            dfs(vertex)

    return result[::-1]


if __name__ == "__main__":
    graph = Graph()
    steps = [
        ("3/4 чашки молока", "Смешать ингредиенты"),
        ("1 яйцо", "Смешать ингредиенты"),
        ("1 столовая ложка масла", "Смешать ингредиенты"),
        ("Смешать ингредиенты", "Налить тесто на сковороду"),
        ("Смешать ингредиенты", "Разогреть сироп"),
        ("Разогреть сковороду", "Налить тесто на сковороду"),
        ("Налить тесто на сковороду", "Перевернуть блин"),
        ("Перевернуть блин", "Съесть блины"),
        ("Разогреть сироп", "Съесть блины"),
    ]
    for start, end in steps:
        graph.add_edge(start, end)

    for number, step in enumerate(topological_sort(graph), 1):
        print(f"{number}. {step}")
