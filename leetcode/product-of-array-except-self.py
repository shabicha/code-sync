class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        prefix = [1,1,2,6,24]
        suffix = [24,24,12,4,1]

        # create suffix & prefix
        prefix = [1]
        for i in range(len(nums)):
            prefix.append(prefix[-1] * nums[i])

        suffix = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]
        
        result = []
      
        for i in range(len(nums)):
            result.append(prefix[i] * suffix [i])

        return result