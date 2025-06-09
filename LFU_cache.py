# Design and implement a data structure for a Least Frequently Used (LFU) cache.

# Implement the LFUCache class:

# LFUCache(int capacity) Initializes the object with the capacity of the data structure.
# int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
# void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
# To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

# When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

# The functions get and put must each run in O(1) average time complexity.

 



import collections


class Node:
    def __init__(self,key,prev=None,next=None):
        self.key = key
        self.prev = prev
        self.next = next

class LinkedList: 
    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left
        self.map = {} #key ->Node
    
    def length(self):
        return len(self.map)
    
    def remove(self,key): #removes node of that key
        if key in self.map:
            node = self.map[key]

            prv = node.prev
            nxt= node.next
            prv.next = nxt 
            nxt.prev = prv
            self.map.pop(key,None)

    def popLeft(self):
        to_pop = self.left.next.key
        self.remove(self.left.next.key)
        return to_pop

    def insert (self,key):
        node= Node(key,self.right.prev,self.right)
        self.map[key]=node
        self.right.prev = node
        node.prev.next = node
        

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #key -> val
        self.freq = collections.defaultdict(LinkedList) #frq -> LinkedList
        self.count = collections.defaultdict(int) # key -> freq
        self.lfu = 0

    def counter(self,key):
        cnt = self.count[key]
        self.count[key] = cnt+1
        self.freq[cnt].remove(key)
        self.freq[cnt+1].insert(key)

        if cnt == self.lfu and self.freq[cnt].length() == 0 :
            self.lfu+=1

    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.counter(key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.counter(key)

        elif len(self.cache) < self.capacity :
            self.cache[key]= value
            self.counter(key)
            self.lfu = min(self.lfu, self.count[key])
        
        else:
            node_to_remove = self.freq[self.lfu].popLeft()
            self.count.pop(node_to_remove)
            self.cache.pop(node_to_remove)
            
            self.cache[key]= value
            self.counter(key)
            self.lfu = min(self.lfu, self.count[key])
