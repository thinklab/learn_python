#!usr/bin/env python
class Graph:
    """
        All node indexes are zero based.
    """

    def __init__(self):
        self.num_nodes = 0
        self.outgoing = {}  # key=node number, value=list of outgoing indexes
        self.incoming = {}  # key=node number, value=list of incoming indexes
        self.weights = {}  # key=pair(start_node, end_node), value=value

    def _validate_node(self, node):
        if not (node < self.get_num_nodes() and node >= 0):
            raise ValueError("There is no node: (%i)" % (node))

    def add_edge(self, start_node, end_node, weight):
        """
            start_node: int
            end_node: int
            weight: float
            If edge is duplicate raise ValueError.
        """
        self._validate_node(start_node)
        self._validate_node(end_node)
        if (start_node, end_node) in self.weights:
            raise ValueError("Duplicate edge: %i -- %i" % (start_node, end_node))
        if start_node in self.outgoing:
            self.outgoing[start_node].append(end_node)
        else:
            self.outgoing[start_node] = [end_node]
        if end_node in self.incoming:
            self.incoming[end_node].append[start_node]
        else:
            self.incoming[end_node].append[start_node]
        self.weights[(start_node, end_node)] = weight

    def add_node(self):
        """
            Return index of the new node.
            First added node will get 0 index
        """
        self.num_nodes += 1
        return self.get_num_nodes() - 1

    def get_num_nodes(self):
        return self.num_nodes

    def get_outgoing(self, node):
        """
            node: int
            return: list of ints
            If there is no node in graph raise ValueError
        """
        self._validate_node(node)
        if node in self.outgoing:
            ret_list = self.outgoing[node]
        else:
            ret_list = []
        return ret_list

    def get_incoming(self, node):
        """
            node: int
            return: list of ints
            If there is no node in graph raise ValueError

        """
        self._validate_node(node)
        if node in self.incoming:
            ret_list = self.incoming[node]
        else:
            ret_list = []
        return ret_list

    def get_edge_weight(self, start_node, end_node):
        """
        start_node: int
        end_node: int
        return: float

        """
        self._validate_node(start_node)
        self._validate_node(end_node)
        if (start_node, end_node) not in self.weights:
            raise ValueError("No such edge: %i -- %i" % (start_node, end_node))
        if (start_node, end_node) in self.weights:
            return self.weights[(start_node, end_node)]


def shortest_path_length(g, start_node, end_node):
    """
    graph: Graph
    start_node: int
    end_node: int
    return: float
    """
    paths_lengths = {}  # key = number of vertice, value = shortest path to it
    paths_lengths[start_node] = 0

    queue = [start_node]

    while queue:
        node = queue[0]
        del queue[0]
        min_weight = 0
        incoming_list = g.get_incoming(node)
        for v in incoming_list:
            weight = g.get_edge_weight(v, node)
            min_weight = min(weight, min_weight)
        paths_lengths[queue[0]] = min_weight + paths_lengths[min(g.get_incoming(queue[0])), queue[0]]
        