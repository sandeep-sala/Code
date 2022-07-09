# Graph Representation
#   Adjacency Matrix (indicates pairs are adjacent or not)
#       Graph is Complete
#   Adjacency List (collection of list(set of neighbors of vertix))
#       Number of edges are few

from collections import defaultdict

class Graph:

    def __init__(self, gdict={}):
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        if vertex not in self.gdict:
            self.gdict[vertex] = [edge]
        else:
            self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        """
            # BFS ( Breadth First Search ) -- level Order
                enqueue any starting vertex
                while queue is not empty
                    p = dequeue()
                    if p is unvisited
                        mark it visited
                        enqueue all adjacent
                        unvisited vertices of p
            Time  : O(v+e)
            Space : O(v+e)
        """
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)

    def dfs(self, vertex):
        """
            # DFS ( Depth First Search )
                push any starting vertex
                while stack is not empty
                    p = pop()
                    if p is unvisited
                        mark it visited
                        push all adjacent
                        unvisited vertices of p
            Time  : O(v+e)
            Space : O(v+e)
        """
        visited = [vertex]
        stack = [vertex]
        while stack:
            deVertex = stack.pop()
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)

class NewGraph:

    def __init__(self, number_of_vertices):
        self.graph = defaultdict(list)
        self.number_of_vertices = number_of_vertices

    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topo_logical_sort_util(self, v, visited, stack):
        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topo_logical_sort_util(i, visited, stack)
        stack.insert(0,v)

    def topo_logical_sort(self):
        visited = []
        stack   = []

        for k in list(self.graph):
            if k not in visited:
                self.topo_logical_sort_util(k, visited, stack)
        
        print(stack)


# cDict = {
#     "a" : ["b","c"],
#     "b" : ["a","d","e"],
#     "c" : ["a","e"],
#     "d" : ["b","e","f"],
#     "e" : ["d","f"],
#     "f" : ["d","e"],
# }
graph = NewGraph(8)
graph.add_edge("a", "c")
graph.add_edge("c", "e")
graph.add_edge("b", "c")
graph.add_edge("b", "d")
graph.add_edge("c", "e")
graph.add_edge("e", "h")
graph.add_edge("e", "f")
graph.add_edge("d", "f")
graph.add_edge("f", "g")

graph.topo_logical_sort()