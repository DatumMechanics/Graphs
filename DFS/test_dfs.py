from typing import Dict, List, Optional
from graph import DirectedGraph


# Initialize graph
graph: DirectedGraph = DirectedGraph()
graph.add_directed_edge("A", "B")
graph.add_directed_edge("A", "C")
graph.add_directed_edge("B", "D")
graph.add_directed_edge("C", "E")

graph.display()
print()

# Run DFS starting at vertex 'A'
traversal_path: List[str] = graph.dfs("A")
print("DFS Traversal Order:", " -> ".join(traversal_path))
