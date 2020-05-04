from graph import Graph
from copy import deepcopy
import array

my_graph = Graph()
# read file character by character
with open("maze1.txt") as file:
    line_list = file.readlines()
    # minus 1 because the `\n` is a character
    line_width = len(line_list[0]) - 1
    # array had to be manually generated
    my_graph.nodes = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i, line in enumerate(line_list):
        for j, ch in enumerate(line):
            print(ch, end=' ')
            if ch is '\n':
                continue
            # create a node for each character
            my_graph.add_node(ch, i, j)
            # check above and below to add edges

# now you can add the edges
# loop over the nodes
for i, line in enumerate(my_graph.nodes):
    for j, node in enumerate(line):
        # check above
        if my_graph.nodes[i-1][j].title == ' ' or my_graph.nodes[i-1][j].title == 'A' or my_graph.nodes[i-1][j].title == 'B':
            my_graph.nodes[i][j].neighbors.append(my_graph.nodes[i-1][j])
            my_graph.nodes[i-1][j].neighbors.append(my_graph.nodes[i][j])
        # check left
        if my_graph.nodes[i][j-1].title == ' ' or my_graph.nodes[i][j-1].title == 'A' or my_graph.nodes[i][j-1].title == 'B':
            my_graph.nodes[i][j].neighbors.append(my_graph.nodes[i][j-1])
            my_graph.nodes[i][j-1].neighbors.append(my_graph.nodes[i][j])
        # if my_graph.nodes[i][j-1].title == ' ' or my_graph.nodes[i][j-1].title == 'A' or my_graph.nodes[i][j-1].title == 'B':
        #     my_graph.nodes[i][j].neighbors.append(my_graph.nodes[i][j-1])

print(my_graph.nodes)

print(my_graph.nodes[1][1].neighbors)
