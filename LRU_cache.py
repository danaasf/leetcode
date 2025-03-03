# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.stack = deque([])
        self.size = capacity 
        

    def get(self, key: int) -> int:
        if not key in self.hashmap: 
            return -1 
        else:
            self.stack.remove(key)
            self.stack.append(key)
            return self.hashmap[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key] = value 
            self.stack.remove(key)
            self.stack.append(key)
        else:
            if len(self.hashmap) == self.size:
                x = self.stack.popleft()
                if x in self.stack:
                    self.stack.remove(x)
                self.hashmap.pop(x)
                self.hashmap[key]=value
                self.stack.append(key)
            else:
                self.hashmap[key]=value
                self.stack.append(key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)