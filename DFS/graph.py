from typing import Dict, List, Optional, Set

# --- Stack ---
class Node:
    def __init__(self, value: str) -> None:
        self.value: str = value
        self.next: Optional[Node] = None

class Stack:
    def __init__(self) -> None:
        self.top: Optional[Node] = None

    def push(self, value: str) -> None:
        new_node: Node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self) -> str:
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        popped_node: Node = self.top  # type: ignore
        self.top = popped_node.next
        return popped_node.value

    def is_empty(self) -> bool:
        return self.top is None


# --- Directed Graph ---
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

    def dfs(self, start_vertex: str) -> List[str]:
        """Performs an iterative depth-first search using a typed Set for visited tracking."""
        if start_vertex not in self.adj_list:
            return []

        # Explicitly typed set to keep track of unique visited nodes
        visited: Set[str] = set()
        order_of_visit: List[str] = []
        
        stack: Stack = Stack()
        stack.push(start_vertex)

        while not stack.is_empty():
            current_vertex: str = stack.pop()

            # Using 'not in' with a set provides O(1) average time complexity lookups
            if current_vertex not in visited:
                visited.add(current_vertex)
                order_of_visit.append(current_vertex)

                # Push unvisited neighbors in reverse order
                for neighbor in reversed(self.adj_list[current_vertex]):
                    if neighbor not in visited:
                        stack.push(neighbor)

        return order_of_visit
