"""
Stack Implementation
"""

class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    
    def __init__(self):
        self.top = None
        
    def is_empty(self) -> bool:
        return self.top is None
    
    def push(self, value):
        """
        Actual stack: top → [30] → [20] → [10] → None
        New value added: top → [42] → [30] → [20] → [10] → None
        
        1. Create a new Node object. The node stores the value and 
            its next is initially None
        2. The new node points to whatever the stack is currently pointing to (the old top)
        3. Now self.top points to the new node
        """
        new_node = Node(value)
        new_node.next = self.top # Point new node to the current top
        self.top = new_node # Update top to new node
        
    def pop(self):
        """
        top → [A] → [B] → [C] → None
        
        When pop() is called:
            1. We save the value of [A]
            2. We update self.top to point to [B]
        Now, the node [A] is no longer referenced anywhere,
        so the garbage collector delete it from the memory
        """
        if not self.is_empty():
            popped_value = self.top.value # Store the top value
            self.top = self.top.next # Move top down one node
            return popped_value
        
        raise IndexError("Trying to pop from an empty stack")
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty - nothing to peek")
        
        return self.top.value
        
    def print_stack(self):
        current = self.top
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        print("Stack (top to bottom):", elements)
        
        
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.print_stack()
    stack.pop()
    stack.print_stack()
    stack.pop()
    stack.pop()
    stack.print_stack()
    stack.pop()