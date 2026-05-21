from typing import Dict, List

class UndirectedGraph:
    def __init__(self) -> None:
        """Initializes an empty undirected graph."""
        self.adj_list: Dict[str, List[str]] = {}

    def add_vertex(self, vertex: str) -> None:
        """Adds a new vertex to the graph if it does not exist."""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_undirected_edge(self, u: str, v: str) -> None:
        """Adds a bidirectional edge between vertex u and vertex v."""
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def display(self) -> None:
        """Prints the adjacency list representation."""
        print("--- Undirected Graph ---")
        for vertex, neighbors in self.adj_list.items():
            neighbors_str: str = ", ".join(neighbors)
            print(f"{vertex}: [{neighbors_str}]")


class DirectedGraph:
    def __init__(self) -> None:
        """Initializes an empty directed graph."""
        self.adj_list: Dict[str, List[str]] = {}

    def add_vertex(self, vertex: str) -> None:
        """Adds a new vertex to the graph if it does not exist."""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_directed_edge(self, source: str, destination: str) -> None:
        """Adds a one-way edge from source vertex to destination vertex."""
        self.add_vertex(source)
        self.add_vertex(destination)
        self.adj_list[source].append(destination)

    def display(self) -> None:
        """Prints the adjacency list representation."""
        print("--- Directed Graph ---")
        for vertex, neighbors in self.adj_list.items():
            neighbors_str: str = " -> ".join(neighbors)
            print(f"{vertex}: {neighbors_str}")
