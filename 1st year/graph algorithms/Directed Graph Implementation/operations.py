import random
import copy
from graph import DiGraph, GraphError


def read_file():
    g = None
    with open(r'C:\Users\lexig\PycharmProjects\directed_graph_moment\graph_file_2', "r") as f:
        initial_line = f.readline()
        initial_line = initial_line.split(" ")
        nodes = int(initial_line[0].strip())
        ls = []
        for n in range(nodes):
            ls.append(int(n))
        g = DiGraph(ls)
        for edge in f:
            line = edge.split(" ")
            g.add_edge(int(line[0].strip()), int(line[1].strip()), int(line[2].strip()))
    return g


def print_file(graph):
    with open(r'C:\Users\lexig\PycharmProjects\directed_graph_moment\graph_file', "w") as f:
        lines = []
        s = f"{graph.vertices} {graph.edges}\n"
        lines.append(s)

        for vertex in graph.vertex_iterator:
            for neighbour in graph.iterate_outbound_spec_vertex(vertex):
                s = ""
                s += f"{vertex} {neighbour} {graph.get_edge_value(vertex, neighbour)}"
                s += "\n"
                lines.append(s)
        f.writelines(lines)


def generate_graph(nodes, edges):
    if edges > nodes * (nodes - 1):
        raise GraphError("Too many edges!")
    ls = []
    for n in range(nodes):
        ls.append(n)
    g = DiGraph(ls)

    for e in range(edges):
        out = random.randint(0, nodes-1)
        inb = random.randint(0, nodes-1)
        while g.check_edge_existence(out, inb) or out == inb:
            out = random.randint(0, nodes-1)
            inb = random.randint(0, nodes-1)
        g.add_edge(out, inb, random.randint(0, 100))
    return g


"""
Backtrace function that gets the path based on the already done BFS
"""


def created_path(parent, start, end):
    path = [end]
    i = end
    while i != start:
        path.append(parent[i])
        i = parent[i]
    #  path.reverse() - modify this if reversed
    return path


"""
BFS function that searches with a reversed breadth-first search the shortest path from the start node to the end node.
Returns the shortest path, or None if there is no path.
"""


def bfs(graph, end, start):
    been_here = []
    parent = []
    for i in range(graph.vertices + 1):
        been_here.append(False)
        parent.append(-1)
    q = [end]
    while len(q) > 0:
        print(q)  # so we can visualize the queue
        print("---------------")
        current = q[0]
        q.pop(0)
        if current == start:
            return created_path(parent, end, start)
        been_here[current] = True
        for neighbor in graph.iterate_inbound_spec_vertex(current):
            if not been_here[neighbor] and neighbor not in q:
                parent[neighbor] = current
                q.append(neighbor)


NUM = 1000000


def create_matrix(n):
    mat = []
    for i in range(n):
        col = []
        for j in range(n):
            col.append(NUM)
        mat.append(col)
    return copy.deepcopy(mat)


def create_cost_matrix(graph):
    mat = create_matrix(graph.vertices)

    for v in graph.vertex_iterator:
        for j in graph.iterate_outbound_spec_vertex(v):
            mat[v][j] = graph.get_edge_value(v, j)

    for v in graph.vertex_iterator:
        mat[v][v] = 0

    return copy.deepcopy(mat)


def multiply(m1, m2):
    res = create_matrix(len(m1))
    for i in range(len(res)):
        for j in range(len(res)):
            for k in range(len(res)):
                if m1[i][k] != NUM and m2[k][j] != NUM:
                    res[i][j] = min(res[i][j], m1[i][k] + m2[k][j])
    return copy.deepcopy(res)


def has_negative_cycles(graph):
    power_cost = create_cost_matrix(graph)
    for i in range(graph.vertices - 2):
        power_cost = multiply(power_cost, create_cost_matrix(graph))
    cost = multiply(power_cost, create_cost_matrix(graph))
    for i in range(graph.vertices):
        for j in range(graph.vertices):
            if cost[i][j] != power_cost[i][j]:
                return True
    return False


def create_lowest_cost_walk(graph, start, end):
    neg = has_negative_cycles(graph)
    if neg:
        print("THERE ARE NEGATIVE COST CYCLES IN THE GRAPH!\n")
        return
    ls = []

    cost = create_cost_matrix(graph)
    for i in range(graph.vertices - 2):
        cost = multiply(cost, create_cost_matrix(graph))
    if cost[start][end] == NUM:
        print(f"There is no walk between {start} and {end}")
        return
    print(f"The lowest cost walk has cost: {cost[start][end]}\n")

    init_cost = create_cost_matrix(graph)
    current = start
    ls.append(start)
    while current != end:
        if init_cost[current][end] == cost[current][end]:
            ls.append(end)
            break
        for i in range(len(cost)):
            if i != current and init_cost[current][i] + cost[i][end] == cost[start][end]:
                ls.append(i)
                current = i
                break

    print(ls)
