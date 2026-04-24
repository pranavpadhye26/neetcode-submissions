class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        else:
            node = self.mapping[key]
            self.remove(node)
            self.insert_at_head(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.remove(self.mapping[key])

        node = Node(key,value)
        self.insert_at_head(node)
        self.mapping[key] = node
        if len(self.mapping) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.mapping[lru.key]
    
    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert_at_head(self,node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head


        
