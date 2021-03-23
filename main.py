from graph import Graph
from copy import deepcopy
from priority_item import PrioritizedItem

my_graph = Graph()
# read file character by character
with open("maze1.txt") as file:
    line_list = file.readlines()
    # minus 1 because the `\n` is a character
    line_width = len(line_list[0]) - 1
    # line height?
    line_height = len(line_list)
    # array had to be manually generated
    for i in range(line_height):
        my_graph.nodes.append(['0'] * line_width)
    # print(my_graph.nodes)
    print("MAZE:")
    print("------")
    for i, line in enumerate(line_list):
        for j, ch in enumerate(line):
            print(ch, end='')
            if ch == '\n':
                continue
            # create a node for each character
            my_graph.add_node(ch, i, j)
            # check above and below to add edges
    print()

# print(my_graph.nodes)
my_graph.add_neighbors()
# Use the algorithm to get the answer then draw it.
my_graph.a_star()