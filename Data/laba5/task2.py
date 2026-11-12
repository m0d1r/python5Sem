from graph import Graph


def reverse_graph(graph):
    result = Graph()
    for vertex in graph.vertices:
        result.add_vertex(vertex)
        for neighbor in graph.neighbors(vertex):
            result.add_edge(neighbor, vertex)
    return result


if __name__ == "__main__":
    adjacency = {0: [1, 2], 1: [3], 2: [1], 3: []}
    graph = Graph()
    for vertex, neighbors in adjacency.items():
        graph.add_vertex(vertex)
        for neighbor in neighbors:
            graph.add_edge(vertex, neighbor)

    print("Исходный граф:")
    for vertex in sorted(graph.vertices):
        print(vertex, "->", list(graph.neighbors(vertex)))

    print("Обращённый граф:")
    reversed_graph = reverse_graph(graph)
    for vertex in sorted(reversed_graph.vertices):
        print(vertex, "->", sorted(reversed_graph.neighbors(vertex)))
