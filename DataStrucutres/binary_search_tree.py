class Node:
    def __init__(self, value, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right
    def set_left(self, node):
        self._left = node
    def set_right(self, node):
        self._right = node
        
class BinarySearchTree:
    def __init__(self):
        self._root = None
        
    def _search(self, value):
        parent = None
        # We start from the root, and its parent is None.
        node = self._root
        while node is not None:
            node_val = node.value()
            if node_val == value:
                return node, parent #Target found!
            elif value < node_val:
                parent = node
                node = node.left()
            else:
                parent = node
                node = node.right()
        return None, None # If it gets here, we broke out of the loop without finding the target

    def find_max_in_subtree(self):
        parent = None
        node = self
        while node.right() is not None:
            parent = node
            node = node.right()
        return node, parent
    
    def insert(self, value):
        node = self._root
        if node is None: # The tree is empty.
            self._root = Node(value)
        else:
            while node is not None:
                if value <= node.value():
                    if node.left() is None:
                        node.set_left(Node(value))
                        break
                    else:
                        node = node.left()
                elif node.right() is None:
                    node.set_right(Node(value))
                    break
                else: # We need to keep traversing the right branch of this subtree
                    node = node.right()