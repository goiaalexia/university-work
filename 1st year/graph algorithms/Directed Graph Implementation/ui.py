from graph import DiGraph, GraphError
from operations import *


# PROBLEM NUMBER #2 FOR PRACTICAL WORK 2
# PROBLEM NUMBER #6 FOR PRACTICAL WORK 3


def print_menu():
    print()
    print("0. Exit")
    print("1. Print Graph")
    print("2. Generate Graph")
    print("3. New graph")
    print("4. Add edge")
    print("5. Add vertex")
    print("6. Remove edge")
    print("7. Remove vertex")
    print("8. Get edge cost")
    print("9. Set edge cost")
    print("10. Get outbound degree")
    print("11. Get inbound degree")
    print("12. Get graph from file")
    print("13. Get shortest length path")
    print("14. Get lowest cost walk")
    print()


if __name__ == "__main__":
    nodes = 11
    edges = 30
    g = generate_graph(nodes, edges)

    running = True
    while running:
        print_menu()
        c = int(input("Enter option: "))
        if c == 1:
            print(g)

        elif c == 2:
            nodes = int(input("Enter node number: "))
            edges = int(input("Enter edge number: "))
            try:
                g = generate_graph(nodes, edges)
            except ValueError as ve:
                print(ve)
            except GraphError as ge:
                print(ge)
        elif c == 3:
            ls = []
            nodes = int(input("Enter node number: "))
            for i in range(0, nodes):
                ls.append(i + 1)
            g = DiGraph(ls)
        elif c == 4:
            outbound = int(input("Enter outbound node: "))
            inbound = int(input("Enter inbound node: "))
            cost = int(input("Enter weight: "))
            try:
                g.add_edge(outbound, inbound, cost)
            except GraphError as ge:
                print(ge)
            except KeyError:
                print("Not valid!")
        elif c == 5:
            outbound = int(input("Enter node: "))
            try:
                g.add_vertex(outbound)
            except GraphError as ge:
                print(ge)
            except KeyError:
                print("Not valid!")
        elif c == 6:
            outbound = int(input("Enter outbound node: "))
            inbound = int(input("Enter inbound node: "))

            try:
                g.remove_edge(outbound, inbound)
            except GraphError as ge:
                print(ge)
            except KeyError:
                print("Not valid!")
        elif c == 7:
            outbound = int(input("Enter node: "))
            try:
                g.remove_vertex(outbound)
            except GraphError as ge:
                print(ge)
            except KeyError:
                print("Not valid!")
        elif c == 8:
            outbound = int(input("Enter outbound node: "))
            inbound = int(input("Enter inbound node: "))
            try:
                print(g.get_edge_value(outbound, inbound))
            except GraphError as ge:
                print(ge)
            except KeyError:
                print("Not valid!")
        elif c == 9:
            outbound = int(input("Enter outbound node: "))
            inbound = int(input("Enter inbound node: "))
            cost = int(input("Enter new weight: "))
            try:
                g.set_edge_value(outbound, inbound, cost)
            except GraphError as ge:
                print(ge)
            except KeyError:
                print("Not valid!")
        elif c == 10:
            outbound = int(input("Enter node: "))

            try:
                print(g.get_out_degree(outbound))
            except GraphError as ge:
                print(ge)
            except KeyError:
                print("Not valid!")
        elif c == 11:
            outbound = int(input("Enter node: "))
            try:
                print(g.get_in_degree(outbound))
            except GraphError as ge:
                print(ge)
            except KeyError:
                print("Not valid!")
        elif c == 12:
            g = read_file()
        elif c == 13:  # BFS
            try:
                node1 = int(input("Input the first node: "))
                node2 = int(input("Input the second node: "))
            except ValueError:
                print("Invalid input!")
                node1 = node2 = 0
            if bfs(g, node2, node1) is not None:
                print("Shortest path:", bfs(g, node2, node1), "of length ", len(bfs(g, node2, node1)))
            else:
                print("There is no path between those two nodes!")

        elif c == 0:
            running = False
        elif c == 14:
            try:
                node1 = int(input("Input the first node: "))
                node2 = int(input("Input the second node: "))
            except ValueError:
                print("Invalid input!")
                node1 = node2 = 0
            create_lowest_cost_walk(g, node1, node2)
        else:
            print("Invalid command")

""" COPY DEMONSTRATION

    print_file(g)
    print("Copy demonstration")
    g = generate_graph(4, 4)
    cpy = g.get_copy()
    g = generate_graph(4, 4)
    print("This is the original graph, now overwritten")
    print(g)
    print("This is the copy, having original data")
    print(cpy)
"""
