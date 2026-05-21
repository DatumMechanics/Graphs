from graph import UndirectedGraph, DirectedGraph

# Test Undirected Graph
u_graph: UndirectedGraph = UndirectedGraph()
u_graph.add_undirected_edge("A", "B")
u_graph.add_undirected_edge("B", "C")
u_graph.display()

print() # Blank line

# Test Directed Graph
d_graph: DirectedGraph = DirectedGraph()
d_graph.add_directed_edge("A", "B")
d_graph.add_directed_edge("B", "C")
d_graph.display()
