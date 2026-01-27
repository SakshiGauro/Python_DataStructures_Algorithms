import unittest
class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge (self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys(): 
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try: 
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False 
    
    def remove_vertex (self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
            
        return False
    
#  +=====================================================+
#  |                                                     |
#  |        THE TEST CODE BELOW ARE TEST CASES           |
#  |                                                     |
#  +=====================================================+


# Constructor
class Test_Constructor(unittest.TestCase):    
    def test_Graph_init(self):    
        graph = Graph()

        self.assertIsNotNone(graph)

# Add Vertex
class Test_AddVertex(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_add_new_vertex(self):
        result = self.graph.add_vertex("A")
        self.assertTrue(result)
        self.assertIn("A", self.graph.adj_list)
        self.assertEqual(self.graph.adj_list["A"], [])

    def test_add_duplicate_vertex(self):
        self.graph.add_vertex("A")
        result = self.graph.add_vertex("A")
        self.assertFalse(result)

# Add Edge
class Test_AddEdge(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")

    def test_add_edge_success(self):
        result = self.graph.add_edge("A", "B")
        self.assertTrue(result)
        self.assertIn("B", self.graph.adj_list["A"])
        self.assertIn("A", self.graph.adj_list["B"])

    def test_add_edge_missing_vertex(self):
        result = self.graph.add_edge("A", "C")
        self.assertFalse(result)

# Remove Edge
class Test_RemoveEdge(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_edge("A", "B")

    def test_remove_existing_edge(self):
        result = self.graph.remove_edge("A", "B")
        self.assertTrue(result)
        self.assertNotIn("B", self.graph.adj_list["A"])
        self.assertNotIn("A", self.graph.adj_list["B"])

    def test_remove_nonexistent_edge(self):
        result = self.graph.remove_edge("A", "C")
        self.assertFalse(result)

    def test_remove_edge_twice(self):
        self.graph.remove_edge("A", "B")
        result = self.graph.remove_edge("A", "B")
        self.assertTrue(result)

# Remove Vertex
class Test_RemoveVertex(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        for v in ["A", "B", "C"]:
            self.graph.add_vertex(v)
        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "C")

    def test_remove_vertex_success(self):
        result = self.graph.remove_vertex("A")
        self.assertTrue(result)
        self.assertNotIn("A", self.graph.adj_list)
        self.assertNotIn("A", self.graph.adj_list["B"])
        self.assertNotIn("A", self.graph.adj_list["C"])

    def test_remove_nonexistent_vertex(self):
        result = self.graph.remove_vertex("D")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()     
        