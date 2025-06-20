class Graph:
    def __init__(self):
        self.graph = {}

    def addVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = set()

    def addEdge(self, u, v):
        self.addVertex(u)  # u가 그래프에 없으면 추가
        self.addVertex(v)  # v가 그래프에 없으면 추가
        self.graph[u].add(v)
        self.graph[v].add(u)
