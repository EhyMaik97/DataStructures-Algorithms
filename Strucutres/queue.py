"""
Queue Implementation
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, value):
        """
        Add a value to the back of the queue.

        Example:
            q = Queue()
            q.enqueue(10)
            q.enqueue(20)
            q.enqueue(30)

            front → [10] → [20] → [30] → None
                                      ↑
                                      rear
        """
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node # First element
        else:
            self.rear.next = new_node # Link the current rear to the new node
            self.rear = new_node # Move rear pointer to the new node
    
    def dequeue(self):
        """
        Remove and return the front element of the queue.

        Example:
            q = Queue()
            q.enqueue(5)
            q.dequeue()  # Returns 5
        """
        if self.is_empty():
            raise IndexError("Trying to dequeue from an empty queue")
        
        dequeued_value = self.front.value
        self.front = self.front.next # Move front pointer forward
        if self.front is None: # If queue became empty
            self.rear = None
        return dequeued_value
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty - nothing to peek")
        return self.front.value
    
    def print_queue(self):
        current = self.front
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        print("Queue (front to back):", elements)
        
        
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.print_queue()
    # queue.enqueue(20)
    # queue.print_queue()
    # queue.enqueue(30)
    # queue.print_queue()
    
    # queue.dequeue()
    # queue.print_queue()
    # queue.dequeue()
    # queue.print_queue()
    