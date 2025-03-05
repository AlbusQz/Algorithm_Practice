#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start

class Node:
    
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(-1,0.5)
        self.tail = Node(-1,1.1)
        self.head.next = self.tail
        self.head.prev = None
        self.tail.next = None
        self.tail.prev = self.head
        self.nodes = {}
    def get(self, key: int) -> int:
        if key in self.nodes:
            node = self.nodes[key]
            node.next.prev = node.prev
            node.prev.next = node.next
            
            node.prev = self.head
            node.next = self.head.next
            
            node.next.prev = node
            self.head.next = node
            
            return node.val
        else:
            return -1            

    def put(self, key: int, value: int) -> None:      
        if key in self.nodes:
            node = self.nodes[key]
            node.next.prev = node.prev
            node.prev.next = node.next
            node.val = value
        else:
            node = Node(key,value)
            if len(self.nodes) == self.cap:
                lru_node = self.tail.prev
                lru_node.prev.next = self.tail
                self.tail.prev = lru_node.prev
                self.nodes.pop(lru_node.key)
            self.nodes[key] = node
        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

