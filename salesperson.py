import random

def visited_all_nodes(visited_vertices):
    for vertex in visited_vertices:
        if visited_vertices[vertex] == "unvisited":
            return False
    return True

def traveling_salesperson(graph):
    final_path = []
    visited_vertices = {vertex: 'unvisited' for vertex in graph.graph_dict}

    current_vertex = random.choice(list(graph.graph_dict))
    visited_vertices[current_vertex] = 'visited'
    final_path.append(current_vertex)
    visited_all_vertices = visited_all_nodes(visited_vertices)
  
    while not visited_all_vertices:
        current_vertex_edges = graph.graph_dict[current_vertex].get_edges()
        current_vertex_edge_weights = {}
        for edge in current_vertex_edges:
            current_vertex_edge_weights[edge] = graph.graph_dict[current_vertex].get_edge_weight(edge)
    
        found_next_vertex = False
        next_vertex = ''
        while not found_next_vertex:
            if current_vertex_edge_weights is None:
                break

            next_vertex = min(current_vertex_edge_weights, key = current_vertex_edge_weights.get)
            if visited_vertices[next_vertex] == 'visited':
                current_vertex_edge_weights.pop(next_vertex)
            else:
                found_next_vertex = True

        if current_vertex_edge_weights is None:
            visited_all_vertices = True
        
        current_vertex = next_vertex
        visited_vertices[current_vertex] = "visited"
        final_path.append(current_vertex)
    
        visited_all_vertices = visited_all_nodes(visited_vertices)

    print('->'.join(final_path))