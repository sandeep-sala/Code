# Single source sortest path

# BFS (Unweighted)
# Dijksta's Algo
# Bellman Ford Algo

from collections import defaultdict

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs(self, start, end):
        """
            O(E)
        """
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node =  path[-1]
            if node == end:
                return path
            for adj in self.gdict.get(node,[]):
                new_path = list(path)
                new_path.append(adj)
                queue.append(new_path)

class NewGraph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distance = {}

    def addNode(self, value):
        self.nodes.add(value)

    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distance[(fromNode,toNode)] = distance 

def dijkstra(graph, initial):
    visited = {initial:0}
    path = defaultdict(list)

    nodes = set(graph.nodes)
    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode =  node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distance[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)

    return visited, path


g = NewGraph()
g.addNode("a")
g.addNode("b")
g.addNode("c")
g.addNode("d")
g.addNode("e")
g.addNode("f")
g.addNode("g")
g.addEdge("a","b",2)
g.addEdge("a","c",5)
g.addEdge("b","c",6)
g.addEdge("b","d",1)
g.addEdge("b","e",3)
g.addEdge("c","f",8)
g.addEdge("d","e",4)
g.addEdge("e","g",9)
g.addEdge("f","g",7)

print(dijkstra(g, "a"))