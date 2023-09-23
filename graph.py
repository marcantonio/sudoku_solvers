class Graph:
    def __init__(self, initial_values, colors):
        # Add all nodes with each value as a color
        self.nodes = []
        for value in initial_values:
            self.add_node(color=value)

        # All possible color candidates
        self.colors = colors

        self.size = len(initial_values)

    # Connect all nodes to each other
    def connect_nodes(self, nodes):
        for idx in range(len(nodes)-1):
            for next_node in nodes[idx+1:]:
                self.add_edge(nodes[idx], next_node)

    def add_node(self, **kwargs):
        vertex = kwargs.get('vertex') or len(self.nodes)
        color = kwargs.get('color') or 0
        self.nodes.append(Node(vertex, color))

    def add_edge(self, src, dst):
        src.add_connection(dst)
        dst.add_connection(src)

    # Find a coloring solution
    def color_nodes(self):
        return self.__color_node(0)

    # Color node at vertex and recurse on the next in the list
    def __color_node(self, vertex):
        # Complete
        if vertex == self.size:
            return True

        node = self.nodes[vertex]

        # Skip constant nodes
        if node.color != 0:
            return self.__color_node(vertex+1)

        # Check each candidate color
        for color in self.colors:
            if node.is_valid_coloring(color):
                orig_color = node.color
                node.color = color
                if self.__color_node(vertex+1):
                    return True
                node.color = orig_color
        return False

    def __str__(self):
        s = ""
        for v in self.nodes:
            s += str(v) + "\n"
        return s[0:-1]

class Node:
    def __init__(self, vertex, color=0):
        self.vertex = vertex
        self.color = color
        self.connections = {}

    def add_connection(self, other):
        self.connections[other.vertex] = other

    # Check if the current node is valid
    def is_valid(self):
        return not any(self.color == other.color for other in self.connections.values())

    # Check if the current node would be valid with the given color
    def is_valid_coloring(self, color):
        return not any(color == other.color for other in self.connections.values())

    def __str__(self):
        conns = sorted(list(self.connections))
        return f"{self.vertex} ({self.color}) -> {conns}"
