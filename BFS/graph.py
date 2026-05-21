from typing import Dict, List, Optional

# --- Queue for BFS ---
class Node:
    def __init__(self, value: str) -> None:
        self.value: str = value
        self.next: Optional[Node] = None

class Queue:
    """A FIFO queue implemented via a singly-linked list."""
    def __init__(self) -> None:
        self.first: Optional[Node] = None
        self.last: Optional[Node] = None

    def is_empty(self) -> bool:
        return self.first is None

    def enqueue(self, value: str) -> None:
        """Appends a new node with the given value at the rear of the queue."""
        new_node: Node = Node(value)
        if self.last is not None:
            self.last.next = new_node
        self.last = new_node
        if self.first is None:
            self.first = new_node

    def dequeue(self) -> str:
        """Removes and returns the front value from the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        
        popped_node: Node = self.first  # type: ignore
        self.first = popped_node.next
        
        # If the queue is now empty, reset last pointer as well
        if self.first is None:
            self.last = None
            
        return popped_node.value


# --- Graph Structure with BFS ---
class DirectedGraph:
    def __init__(self) -> None:
        self.adj_list: Dict[str, List[str]] = {}

    def add_vertex(self, vertex: str) -> None:
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_directed_edge(self, source: str, destination: str) -> None:
        self.add_vertex(source)
        self.add_vertex(destination)
        self.adj_list[source].append(destination)

    def bfs(self, start_vertex: str) -> List[str]:
        """Performs a breadth-first search starting from start_vertex."""
        if start_vertex not in self.adj_list:
            return []

        # Dictionary to track visited nodes and list for final output order
        visited: Set[str] = {start_vertex}
        order_of_visit: List[str] = []
        
        # Instantiate your custom Queue
        queue: Queue = Queue()
        queue.enqueue(start_vertex)

        while not queue.is_empty():
            current_vertex: str = queue.dequeue()
            order_of_visit.append(current_vertex)

            # Enqueue all unvisited neighbors level by level
            for neighbor in self.adj_list[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)

        return order_of_visit

    def display(self) -> None:
        """Prints the adjacency list representation."""
        print("--- Directed Graph ---")
        for vertex, neighbors in self.adj_list.items():
            neighbors_str: str = " -> ".join(neighbors)
            print(f"{vertex}: {neighbors_str}")
