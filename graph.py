class Graph:
    def __init__(self):
        self.adj_list = {} #just an empty dictionary

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list[v2] and v2 in self.adj_list[v1]:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for each_vertex in self.adj_list[vertex]:
                self.adj_list[each_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

myGraph = Graph()

myGraph.add_vertex('A')
myGraph.add_vertex('B')
myGraph.add_vertex('C')
myGraph.add_vertex('D')
myGraph.add_edge('A','B')
myGraph.add_edge('B','C')
myGraph.add_edge('C','A')
myGraph.add_edge('A','D')
myGraph.add_edge('B','D')
myGraph.add_edge('C','D')
print("Original Setup:")
myGraph.print_graph()

myGraph.remove_edge('A','B')
print("Remove A and B edges")
myGraph.print_graph()
print("Remove vertex D")
myGraph.remove_vertex('D')
myGraph.print_graph()