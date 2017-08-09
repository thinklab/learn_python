#!/usr/bin/env python
 
from __future__ import print_function, division
 
world = ['        ',
         '    x   ',
         '    xxx ',
         '   xx   ',
         '    x   ',
         '  xxx   ',
         '        ',
         '        ',
         '        ',
         '        '
         ]
 
world = ['  ',
         '  ']
 
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
            #if (i+1, j) in v:
            #    g.add_edge(nij, v[(i+1, j)])
            if (i-1, j) in v:
                g.add_edge(nij, v[(i-1, j)])
            #if (i, j+1) in v:
            #    g.add_edge(nij, v[(i, j+1)])
            if (i, j-1) in v:
                g.add_edge(nij, v[(i, j-1)])    
 
    return g
 
DEBUG = False

def prnt(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


def test_is_connected():
    world = ['  ',
            '  ']
    world = []
    draw_world(world)
    print(is_connected(world_to_graph(world)))
    print()

    world = ['']
    draw_world(world)
    print(is_connected(world_to_graph(world)))
    print()

    world = ['',
             '']
    draw_world(world)
    print(is_connected(world_to_graph(world)))
    print()

    world = ['x']
    draw_world(world)
    print(is_connected(world_to_graph(world)))
    print()

    world = ['                                                      ',
             '                                                      ',
             '                                                      ',
             '                                                      ',
             '                                                      ',
             '                                                      ',
             '                                                      ',
             '                                                      ',
             '                                                      ',
             '                                                      '
             ]
    draw_world(world)
    print(is_connected(world_to_graph(world)))
    print()

    world = ['xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
             '                                                      ',
             '           x                                          ',
             'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
             '                                                      ',
             'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
             '                                                      ',
             'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
             '                                                      ',
             'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
             ]
    draw_world(world)
    print(is_connected(world_to_graph(world)))
    print()

    world = ['xxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxx',
             'x                                                     ',
             'x          x                                          ',
             'xxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxx',
             '                                                      ',
             'xxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
             '                                                      ',
             'xxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
             '                                                      ',
             'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxx'
             ]
    draw_world(world)
    print(is_connected(world_to_graph(world)))
    print()


def is_connected(g):
    if g.get_num_nodes() == 0: return True
    burning = []
    burning.append(0)
    burned = set()
    while burning:
        prnt("-----------------------------------------")
        prnt('burning =', burning)
        prnt('burned  =', burned) 
        prnt('burning match = ', burning[0])
        if not(burning[0] in burned):
            prnt('match isnt burned')
            burning_match = burning[0]
        else:
            prnt('match was burned')
            del burning[0]
            continue
        for i in g.get_node_neighbours(burning_match):
            prnt('burning neighbour ', i)
            burning.append(i)
        burned.add(burning_match)
        prnt(burning_match, 'was burned') 
        del burning[0]
    if len(burned) == g.get_num_nodes():
        return True
    else:
        return False
 
   
class Graph:
    """
        All node indexes are zero based.
    """
    def __init__(self):
        self.num_nodes = 0
        self.neighbours = {}# key=node number, value=list of neighbours indexes
         
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
 
def graph_to_graphviz(g):
    """
    Return a string that contains GraphViz code that draws 'g'.
     
    graph G {
        n1 -- n2;
        n1 -- n3;
        n3 -- n4;
    }
    """
    s = "graph G {\n"
    for i in range(g.get_num_nodes()):
        nbrs = g.get_node_neighbours(i)
        for j in range(len(nbrs)):
            if i <= nbrs[j]:
                s += str(i) + " -- " + str(nbrs[j]) + ";\n"
    s += "}"
    return s
         
class SerezhinGraph:
    def __init__(self):
        self.neighbors = {}
         
    def add_node(self):
        new_node = len(self.neighbors)
        self.neighbors[new_node] = set()
        return new_node
         
    def add_edge(self, a, b):
        self.neighbors[a].add(b)
        self.neighbors[b].add(a)
         
    def get_num_nodes(self):
        return len(self.neighbors)
         
    def get_node_neighbours(self, node):
        return self.neighbors[node]
 
def serezhin_world_to_graph(world):
    g = SerezhinGraph()
    v = []
    for i in range(len(world)):
        v.append([])
        for j in range(len(world[i])):
            if world[i][j] != 'x':
                v[-1].append(g.add_node())
            else:
                v[-1].append(None)
 
    for i in range(len(world)):
        for j in range(len(world[i])):
            if world[i][j] == 'x':
                continue
            if i-1 >= 0 and v[i-1][j] != None:
                g.add_edge(v[i][j], v[i-1][j])
            if j-1 >= 0 and v[i][j-1] != None:
                g.add_edge(v[i][j], v[i][j-1])
 
    return g
 
def main():
    #draw_world(world)
    #g = world_to_graph(world)
    #print(graph_to_graphviz(g))
    #print(is_connected(g))
    test_is_connected()
 
if __name__ == "__main__":
    main()
 
def fun_with_map():
    m = {}
    m[42] = 1
    print(m[42])
    print(m[43])# raises exception KeyError
    print(42 in m) # True
    print(43 in m) # False
 
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

    path = None
    return path