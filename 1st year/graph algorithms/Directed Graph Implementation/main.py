from graph import DiGraph, GraphError
from operations import *

if __name__ == "__main__":
    nodes = 5
    edges = 100
    try:
        g = generate_graph(nodes, edges)
        print(g)
    except ValueError as ve:
        print(ve)
    nodes = 5
    edges = 10
    g = generate_graph(nodes, edges)
    g.add_edge(1, 2, 10)
    g.remove_vertex(1)
    print(g)
    try:
        g.remove_vertex(1)
    except GraphError as ge:
        print(ge)
    f = g.get_copy()
    print(f)
    g = read_file()
    print(g)
