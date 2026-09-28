class ListNode():
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {} # reference to key: ListNode(key, value)
        self.head = ListNode(0,0)
        self.curr = self.head
        self.length = 0

 
    def remove(self, node):
        node.prev.next = node.next
        if node.next: 
            node.next.prev = node.prev
        else:
            self.curr = node.prev

    def add(self,node):
        self.curr.next = node
        node.next = None
        node.prev = self.curr
        self.curr = node

    def get(self, key: int) -> int:
        #return key val else -1
        if key in self.hashMap:
            #remove
            node = self.hashMap[key]
            self.remove(node)
            #add
            self.add(node)
            return self.hashMap[key].value
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        #remove existing
        node = ListNode(key,value)
        if key in self.hashMap:
            self.length-=1
            self.remove(self.hashMap[key])
    
        #if over capacity remove first node
        if self.length == self.capacity:            
            del self.hashMap[self.head.next.key]
            self.remove(self.head.next)
            self.length-=1
            
        self.add(node)
        self.length +=1
        self.hashMap[key] = node


        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)