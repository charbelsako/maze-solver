from node import Node
from queue import PriorityQueue
from priority_item import PrioritizedItem
from math import sqrt, pow

class Graph:
    def __init__(self):
        self.nodes = []
        self.start = None
        self.finish = None
        self.path = []

    def add_node(self, n, i, j):
        self.nodes[i][j] = Node(n, i, j)

    def add_edge(self, u, v):
        """Adds an edge between u and v

        Arguments:
            u {Node} -- a node in the graph
            v {Node} -- another node in the graph
        """

    def add_neighbors(self):
        # now you can add the edges
        # loop over the nodes
        for i, line in enumerate(self.nodes):
            for j, node in enumerate(line):
                # if i == 1 and j > 0:
                    # print('WHAT')
                if self.nodes[i][j].title == 'A':
                    self.start = self.nodes[i][j]
                if self.nodes[i][j].title == 'B':
                    self.finish = self.nodes[i][j]

                if self.nodes[i][j].title == ' ' or self.nodes[i][j].title == 'A' or self.nodes[i][j].title == 'B':
                    if i > 0:
                        # check above
                        if self.nodes[i-1][j].title == ' ' or self.nodes[i-1][j].title == 'A' or self.nodes[i-1][j].title == 'B':
                            self.nodes[i][j].neighbors.append(self.nodes[i-1][j])
                            self.nodes[i-1][j].neighbors.append(self.nodes[i][j])
                    if j > 0:
                        # check left
                        if self.nodes[i][j-1].title == ' ' or self.nodes[i][j-1].title == 'A' or self.nodes[i][j-1].title == 'B':
                            self.nodes[i][j].neighbors.append(self.nodes[i][j-1])
                            self.nodes[i][j-1].neighbors.append(self.nodes[i][j])


    def heuristic(self, node):
        # get the distance from node to finish
        distance = sqrt(pow(int(node.i) - int(self.finish.i), 2) + pow(int(node.j) - int(self.finish.j),2))
        return distance

    def distance(self, a, b):
        distance = sqrt(pow(int(a.i) - int(b.i), 2) + pow(int(a.j) - int(b.j),2))
        return distance

    def a_star(self):
        open_set = PriorityQueue()
        self.start.g = 0
        self.start.f = self.heuristic(self.start)
        open_set.put(PrioritizedItem(self.start.f, self.start))
        while not open_set.empty():
            current = open_set.get()
            if current.item == self.finish:
                self.get_path(current)
                self.draw_path()
                return
            for neighbor in current.item.neighbors:
                tentative_gscore = current.item.g + self.distance(current.item, neighbor)
                if tentative_gscore < neighbor.g:
                    neighbor.previous = current
                    neighbor.g = tentative_gscore
                    neighbor.f = neighbor.g + self.heuristic(neighbor)
                    if neighbor not in list(open_set.queue):
                        open_set.put(PrioritizedItem(neighbor.f, neighbor))

    def get_path(self, current):
        count = 0
        # if you wish to add the end in the path
        # self.path.append((current.item.i, current.item.j))
        # if you wish to add the beginning in the path switch the next two lines
        # while current.item.previous is not None:
        while current.item.previous.item.previous is not None:
            count = count + 1
            current = current.item.previous
            self.path.append((current.item.i, current.item.j))

        # print(self.path)
        # print(count)

    def draw_path(self):
        print('Solution:')
        print('----------')
        for i, j in self.path:
            self.nodes[int(i)][int(j)] = Node('S', -1, -1)
        for i, row in enumerate(self.nodes):
            for j, col in enumerate(row):
                print(self.nodes[i][j].title, end='')
            print('\n', end='')