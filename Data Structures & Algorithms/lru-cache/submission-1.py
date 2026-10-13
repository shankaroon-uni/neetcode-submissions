class Node:
    def __init__(self, key, value, prev=None, nxt=None):
        self.key = key
        self.val = value
        self.prev = prev
        self.nxt = nxt

class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.right = Node(0, 0, None, None) 
        self.left = Node(0, 0, None, None)
        self.left.nxt = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key, None) != None:
            self.cache[key].val = value
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
        else:
            if len(self.cache.values()) == self.size:
                self.cache.pop(self.left.nxt.key)
                self.remove(self.left.nxt)
                node = Node(key, value)
                self.cache[key] = node
                self.insert(node)

            else:
                node = Node(key, value, self.left, self.right)
                self.cache[key] = node
                self.insert(node)
            
    def remove(self, node):
        tmp = node.prev
        tmp.nxt = node.nxt
        node.nxt.prev = tmp

    def insert(self, node):
        tmp = self.right.prev
        self.right.prev = node
        node.nxt = self.right
        node.prev = tmp
        tmp.nxt = node