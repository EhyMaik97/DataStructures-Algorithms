"""
HashMap Implementation
"""

class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        index = self._hash(key)
        new_node = HashNode(key, value)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            if current.key == key:
                current.value = value
            else:
                current.next = new_node

    def get(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(f"Key {key} not found in HashMap")

    def remove(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return
            prev = current
            current = current.next
        raise KeyError(f"Key {key} not found in HashMap")

    def contains(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def print_map(self):
        for i in range(self.size):
            current = self.table[i]
            elements = []
            while current:
                elements.append((current.key, current.value))
                current = current.next
            print(f"Bucket {i}: {elements}")

if __name__ == "__main__":
    hashmap = HashMap()
    hashmap.add("name", "Alice")
    hashmap.add("age", 30)
    hashmap.add("city", "Vancouver")
    hashmap.add("test", "Example")
    hashmap.print_map()
