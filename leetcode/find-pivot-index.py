class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        [1,8,11,17,22,28]
        [29,28,21,18,11,6]
        #prefix
        total = sum(nums) 
        left = 0
        for i in range(len(nums)):
            right = total - left - nums[i]
            if left == right:
                return i
            left = left + nums[i]
            
        return -1