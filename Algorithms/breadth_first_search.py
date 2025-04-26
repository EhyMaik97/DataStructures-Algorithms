"""
Breadth First Search
Complexity: O(V+E) where V -> nodes; E -> edges
"""

from collections import deque

def bfs(graph, start):
    visited = []  # List to keep track of visited nodes
    queue = deque([start])  # Initialize the queue with the starting node
    while queue:  # While there are still nodes to process
        node = queue.popleft()  # Dequeue a node from the front of the queue

        if node not in visited:  # Check if the node has been visited
            visited.append(node)  # Mark the node as visited
            print(node, end=" ")  # Output the visited node
            # Enqueue all unvisited neighbors (children) of the current node
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)  # Add unvisited neighbors to the queue

graph = {
    'A': ['B', 'C'],  
    'B': ['D', 'E'],  
    'C': ['F', 'G'],  
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],  
    'G': ['N', 'O'],  
    'H': [], 'I': [], 'J': [], 'K': [],
    'L': [], 'M': [], 'N': [], 'O': []   
}

print(bfs(graph, 'A'))