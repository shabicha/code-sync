class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        [4,2,1,3,3]
        p1 = 0
        p2 = k 
        sum1 = 0
        for i in range(k):
            sum1+=nums[i]
        maxAvg = sum1/k
        while p2 < len(nums):
            sum1 = sum1-nums[p1]+ nums[p2]
            avg = (sum1)/k
            maxAvg = max(maxAvg, avg)
            p1+=1
            p2+=1
        return maxAvg