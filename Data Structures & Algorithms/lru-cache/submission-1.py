class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.L, self.R = Node(0, 0), Node(0, 0)
        self.L.next, self.R.prev = self.R, self.L

    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv
    
    # insert at Right
    def insert(self, node):
        prv, nxt = self.R.prev, self.R
        prv.next = nxt.prev = node
        node.prev, node.next = prv, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            # remove LRU node
            LRU = self.L.next
            self.remove(LRU)
            del self.cache[LRU.key]
