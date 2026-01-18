class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):
   

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity 
        self.cache = {} #key = node
        self.head = Node(0,0)
        self.tail=Node(0,0)
        self.head.next = self.tail
        self.tail.prev=self.head

        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            #resort linkedlist
            node = self.cache[key]


            self.remove(node)
            self.add(node)

            return node.value

        return -1

    def remove(self, node):
        node.prev.next=node.next
        node.next.prev=node.prev
    
    def add(self, node):
        saveNode = self.head.next
        saveNode.prev = node
        self.head.next = node

        node.prev = self.head
        node.next = saveNode

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache[key]
            self.cache[key].value = value
            self.remove(node)
            self.add(node)
        else:

            node = Node(key,value)
            self.cache[key] = node
            self.add(node)
            if len(self.cache)>self.capacity:
                tailed=self.tail.prev
                self.remove(tailed)
                del self.cache[tailed.key]
                

            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)