from collections import deque
class RecentCounter:

    def __init__(self):
        self.counter = deque([])
        

    def ping(self, t: int) -> int:
        #add new req
        #return  new req + now - 3000 miliseconds 
        #iterate through loop and popleft for out of bounds & return len
        self.counter.append(t)
        p1= t-3000
        p2 = t
        while self.counter[0] < p1:
            self.counter.popleft()
            
        return len(self.counter)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)