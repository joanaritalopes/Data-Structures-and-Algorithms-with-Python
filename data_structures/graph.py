class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_edge(self, vertex, weight=0):
        self.edges[vertex] = weight

    def get_edges(self):
        return list(self.edges.keys())
    
    def get_edge_weight(self, edge): 
        return self.edges[edge]


class Graph:
    def __init__(self, directed = False):
        self.graph_dict = {}
        self.directed = directed

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight = 0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex]
        # Use a dictionary to track which vertices we've already visited
        seen = {}
        while len(start) > 0:
            current_vertex = start.pop(0)
            # Update the `seen` variable  now that we've visited current_vertex
            seen[current_vertex] = True
            print("Visiting " + current_vertex)
            if current_vertex == end_vertex:
                return True
            else:
                vertices_to_visit = set(self.graph_dict[current_vertex].get_edges())
        
            # Filter next_vertices so it only includes vertices NOT IN seen
            next_vertices = [vertex for vertex in vertices_to_visit if vertex not in seen]
            start += next_vertices
        
        return False


# method to visualize our graph
def print_graph(graph):
    for vertex in graph.graph_dict:
        print("")
        print(vertex + " connected to")
        vertex_neighbors = graph.graph_dict[vertex].edges
        if len(vertex_neighbors) == 0:
            print("No edges!")
        for adjacent_vertex in vertex_neighbors:
            print("=> " + adjacent_vertex)