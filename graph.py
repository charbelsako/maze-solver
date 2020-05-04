from node import Node


class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, n, i, j):
        self.nodes[i][j] = Node(n, i, j)

    def add_edge(self, u, v):
        """Adds an edge between u and v

        Arguments:
            u {Node} -- a node in the graph
            v {Node} -- another node in the graph
        """

    def add_neighbors(self):
        pass

    def a_star(self, start, finish):
        pass
