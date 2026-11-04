class SmallestInfiniteSet:

    def __init__(self):
        self.SmallestInfiniteSet = set()
        self.SmallestInfiniteHeap = []
        self.cur = 1

    def popSmallest(self) -> int:
        #remove heep peek
        if self.SmallestInfiniteHeap:
            smallest = heapq.heappop(self.SmallestInfiniteHeap)
            self.SmallestInfiniteSet.remove(smallest)
            return smallest
        self.cur +=1
        return self.cur -1

    def addBack(self, num: int) -> None:
        #add num in set
        if num < self.cur and num not in self.SmallestInfiniteSet:
            heapq.heappush(self.SmallestInfiniteHeap, num)
            self.SmallestInfiniteSet.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)