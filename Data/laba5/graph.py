class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, start, end, weight=1):
        self.add_vertex(start)
        self.add_vertex(end)
        self.vertices[start][end] = weight

    def neighbors(self, vertex):
        return self.vertices[vertex]
