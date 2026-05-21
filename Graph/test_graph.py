from graph import UndirectedGraph, DirectedGraph

# Test Undirected Graph
u_graph: UndirectedGraph = UndirectedGraph()
u_graph.add_undirected_edge("A", "B")
u_graph.add_undirected_edge("B", "C")
u_graph.add_undirected_edge("A", "D")
u_graph.add_undirected_edge("D", "E")
u_graph.add_undirected_edge("A", "E")
u_graph.add_undirected_edge("E", "F")
u_graph.display()

print() # Blank line

# Test Directed Graph
d_graph: DirectedGraph = DirectedGraph()
d_graph.add_directed_edge("A", "B")
d_graph.add_directed_edge("B", "C")
d_graph.add_directed_edge("A", "D")
d_graph.add_directed_edge("D", "E")
d_graph.add_directed_edge("A", "E")
d_graph.add_directed_edge("E", "F")
d_graph.display()
