from heapq import heappush, heappop
from graph import Graph


def dijkstra(graph, start, finish):
    distances = {vertex: float("inf") for vertex in graph.vertices}
    previous = {}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        distance, vertex = heappop(queue)
        if distance > distances[vertex]:
            continue
        if vertex == finish:
            break
        for neighbor, weight in graph.neighbors(vertex).items():
            new_distance = distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = vertex
                heappush(queue, (new_distance, neighbor))

    if distances[finish] == float("inf"):
        return None

    path = [finish]
    while path[-1] != start:
        path.append(previous[path[-1]])
    return distances[finish], path[::-1]


if __name__ == "__main__":
    graph = Graph()
    routes = [
        ("Белово", "Ленинск-Кузнецкий", 38),
        ("Ленинск-Кузнецкий", "Киселевск", 99),
        ("Белово", "Киселевск", 70),
        ("Белово", "Гурьевск", 31),
        ("Гурьевск", "Киселевск", 97),
        ("Ленинск-Кузнецкий", "Мыски", 190),
        ("Киселевск", "Кемерово", 179),
        ("Кемерово", "Новосибирск", 265),
        ("Мыски", "Новосибирск", 420),
    ]
    for start, end, distance in routes:
        graph.add_edge(start, end, distance)

    start = input("Начальный город: ").strip()
    finish = input("Конечный город: ").strip()

    if start not in graph.vertices or finish not in graph.vertices:
        print("Город не найден")
    else:
        result = dijkstra(graph, start, finish)
        if result is None:
            print("Пути между городами нет")
        else:
            distance, path = result
            print("Расстояние:", distance, "км")
            print("Путь:", " -> ".join(path))
