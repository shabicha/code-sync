class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        minHeap = nums[:k]
        heapq.heapify(minHeap)
        for i in range(k, len(nums)):
            if nums[i] > minHeap[0]:
                #pop top and add nums[i]
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, nums[i])
        return minHeap[0]