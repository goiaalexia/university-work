import copy


class GraphError(Exception):
    """
    exception class used for graph specific errors uwu
    """
    pass


class DiGraph:
    def __init__(self, vertices):
        """
        the graph will take the form of a dictionary:
        graph = {vertex_out : [{vertex_in, weight}, ...], ... }
        :param vertices: the number of vertices of the graph
        """
        self.__graph = {}
        self.__inverted_graph = {}
        for vertex in vertices:
            self.__graph[vertex] = []
            self.__inverted_graph[vertex] = []

    @property
    def graph(self):
        """
        getter of the graph
        :return: the graph
        """
        return self.__graph

    @property
    def graph_inv(self):
        """
        getter of the inverted graph
        :return: the inverted graph
        """
        return self.__inverted_graph

    @property
    def vertices(self):
        """
        getter of the no. of vertices
        :return: the no. of vertices
        """
        return len(self.graph.keys())

    @property
    def edges(self):
        """
        getter for the no. of edges
        :return: the no. of edges
        """
        n = 0
        for vertex in self.graph:
            n += len(self.graph[vertex])
        return n

    def add_vertex(self, new_vertex_out):
        """
        function that adds a new vertex to the graph
        :param new_vertex_out: the vertex to be added
        :return: none
        """
        if new_vertex_out not in self.graph.keys():
            self.__graph[new_vertex_out] = []
            self.__inverted_graph[new_vertex_out] = []
        else:
            raise GraphError("Vertex already exists!")

    def remove_vertex(self, vertex):
        """
        the function that removes an existing vertex from the graph
        :param vertex: the vertex to be removed
        :return: none
        """
        if vertex in self.graph:
            del self.__graph[vertex]
            del self.__inverted_graph[vertex]
            for vertex_out in self.graph:
                try:
                    self.remove_edge(vertex_out, vertex)
                except GraphError:
                    pass
        else:
            raise GraphError("The vertex doesn't exist, therefore it can't be removed!")

    def add_edge(self, vertex_out, vertex_in, weight):
        """
        the function that adds an edge between two vertices
        :param vertex_in: the vertex it goes in
        :param vertex_out: the vertex it comes out of
        :param weight: the edge's weight
        :return: none
        """
        if self.check_edge_existence(vertex_out, vertex_in) is False:
            self.__graph[vertex_out].append({vertex_in: weight})  # we add it
            self.__inverted_graph[vertex_in].append({vertex_out: weight})
        else:
            raise GraphError("Edge already exists!")

    def remove_edge(self, vertex_out, vertex_in):
        """
        the function that removes the edge between two vertices
        :param vertex_in: the vertex it goes in
        :param vertex_out: the vertex it comes out of
        :return:
        """
        if self.check_edge_existence(vertex_out, vertex_in) is True:
            self.__graph[vertex_out].remove([x for x in self.__graph[vertex_out] if vertex_in in x.keys()][0])
            self.__inverted_graph[vertex_in].remove([x for x in self.__inverted_graph[vertex_in] if vertex_out in x.keys()][0])
        else:
            raise GraphError("The edge doesn't exist, therefore it can't be removed!")

    def check_edge_existence(self, vertex_out, vertex_in):
        """
        the function that checks whether an edge exists or not
        :param vertex_in: the vertex it goes in
        :param vertex_out: the vertex it comes out of
        :return: boolean value of it's existence
        """
        for edge in self.graph[vertex_out]:
            if vertex_in in edge.keys():
                return True
        return False

    def get_in_degree(self, vertex_in):
        """
        the getter for the degree of a vertex (in)
        :param vertex_in: the vertex they go in
        :return: the no. of edges that go in it
        """
        return len(self.__inverted_graph[vertex_in])

    def get_out_degree(self, vertex_out):
        """
        the getter for the degree of a vertex (out)
        :param vertex_out: the vertex they go out of
        :return: the no. of edge that go out of it
        """
        return len(self.graph[vertex_out])

    def iterate_outbound_spec_vertex(self, vertex_out):
        """
        parse (iterate) the set of outbound edges of a specified vertex
        (that is, provide an iterator).
        for each outbound edge, the iterator shall provide the target vertex.
        :param: vertex_out: the vertex they go out of
        :return: the specified iterator
        """
        aux = []
        for edge in self.graph[vertex_out]:
            aux.append(list(edge.keys())[0])
        return iter(aux)

    def iterate_inbound_spec_vertex(self, vertex_in):
        """
        parse the set of inbound edges of a specified vertex (as above)
        :param vertex_in: the vertex it goes in
        :return: the specified iterator
        """
        aux = []
        for vertex_out in self.graph:
            for edge in self.graph[vertex_out]:
                if vertex_in in edge:
                    aux.append(vertex_out)
        return iter(aux)

    def get_edge_value(self, vertex_out, vertex_in):
        """
        getter for the edge's value
        :param vertex_out: the vertex it goes out of
        :param vertex_in: the vertex it comes into
        :return: the edge's value
        """
        if self.check_edge_existence(vertex_out, vertex_in):
            for edge in self.graph[vertex_out]:
                if vertex_in in edge:
                    return edge[vertex_in]
        raise GraphError("The edge doesn't exist!")

    def set_edge_value(self, vertex_out, vertex_in, weight):
        """
        setter for the edge's value
        :param vertex_out: the vertex it goes out of
        :param vertex_in: the vertex it comes into
        :param weight: the new weight/value
        :return: none
        """
        if self.check_edge_existence(vertex_out, vertex_in):
            for edge in self.__graph[vertex_out]:
                if vertex_in in edge:
                    edge[vertex_in] = weight
                    return
        if self.check_edge_existence(vertex_out, vertex_in):
            for edge in self.__inverted_graph[vertex_in]:
                if vertex_out in edge:
                    edge[vertex_out] = weight
                    return
        raise GraphError("The edge doesn't exist!")

    def get_copy(self):
        """
        the function that returns a copy for the graph
        :return: the graph's copy
        """
        return copy.deepcopy(self)

    @property
    def vertex_iterator(self):
        return iter(self.graph.keys())

    def __str__(self):
        """
        to string function
        :return: the string to be printed
        """
        lines = []
        s = f"{self.vertices} {self.edges}\n"
        lines.append(s)
        for vertex_out in self.graph:
            for edge in self.graph[vertex_out]:
                s += f"EDGE ({vertex_out},{list(edge.keys())[0]}) WITH WEIGHT {list(edge.values())[0]}\n"
        return s
