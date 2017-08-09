#!/usr/bin/env python
from __future__ import print_function, division
import random

world = ['   ',
         '   ',
         '   ']


def weighted_graph_to_graphviz(g):
    """
    Return a string that contains GraphViz code that draws 'g'.

    graph G {
        n1 -- n2 [label = "12"];
        n1 -- n3;
        n3 -- n4;
    }
    """
    s = "graph G {\n"
    for i in range(g.get_num_nodes()):
        nbrs = g.get_node_neighbours(i)
        for j in range(len(nbrs)):
            if i <= nbrs[j]:
                s += str(i) + " -- " + str(nbrs[j]) + """ [ label = """ + str(g.get_edge_weight(i, nbrs[j])) + """ ] """ + ";\n"
    s += "}"
    return s


def relaxation():
    return None



def draw_world(world):
    if world == []:
        print("++\n++")
        return
    print("+", end="")
    for i in range(len(world[0])):
        print("-", end="")
    print("+")
    for i in range(len(world)):
        print("|", end="")
        print(world[i], end="")
        print("|")
    print("+", end="")
    for i in range(len(world[0])):
        print("-", end="")
    print("+")


def world_to_graph(world):
    g = Graph()
    v = {}
    for i in range(len(world)):
        for j in range(len(world[i])):
            if world[i][j] != "x":
                v[(i, j)] = g.add_node()
    for i in range(len(world)):
        for j in range(len(world[i])):
            if not ((i, j) in v):
                continue
            nij = v[(i, j)]
            if (i - 1, j) in v:
                g.add_edge(nij, v[(i - 1, j)])
            if (i, j - 1) in v:
                g.add_edge(nij, v[(i, j - 1)])

    return g


DEBUG = False


def prnt(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


class Graph:
    """
        All node indexes are zero based.
    """

    def __init__(self):
        self.num_nodes = 0
        self.neighbours = {}  # key=node number, value=list of neighbours indexes
        self.weights = {}  # key=pair(start_node, end_node), value=value

    def add_edge(self, a, b):
        """
            a: int
            b: int
        """
        if a in self.neighbours:
            self.neighbours[a].append(b)
        else:
            self.neighbours[a] = [b]
        if b in self.neighbours:
            self.neighbours[b].append(a)
        else:
            self.neighbours[b] = [a]
        rand_weight = random.randrange(1, 100)
        self.weights[(a, b)] = rand_weight
        self.weights[(b, a)] = rand_weight

    def add_node(self):
        """
            Return index of the new node.
            First added node will get 0 index
        """
        self.num_nodes += 1
        return self.get_num_nodes() - 1

    def get_num_nodes(self):
        return self.num_nodes

    def get_node_neighbours(self, node):
        """
            node: int
            return: list of ints
        """
        if node in self.neighbours:
            ret_list = self.neighbours[node]
        else:
            ret_list = []
        return ret_list

    def get_edge_weight(self, start_node, end_node):
        if start_node != end_node and (start_node, end_node) in self.weights:
            return self.weights[(start_node, end_node)]


def main():
    #draw_world()
    g = world_to_graph(world)
    print(weighted_graph_to_graphviz(g))
    # print(is_connected(g))


if __name__ == "__main__":
    main()


def fun_with_map():
    m = {}
    m[42] = 1
    print(m[42])
    print(m[43])  # raises exception KeyError
    print(42 in m)  # True
    print(43 in m)  # False


def fun_with_sets():
    s = set()
    s.add(42)
    print(42 in s)
    print(43 in s)
    if s:
        print('s is not empty!')
    s.remove(42)


def draw_path(p):
    None


def dijkstra(g, start, end):
    s = {start: 0}
    while
