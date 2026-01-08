class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
      

        prefix =[1]
        for i in range(len(nums)-1):
            prefix.append(prefix[-1]*nums[i])

        suffix =[1]*(len(nums))
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = suffix[i+1]*nums[i+1]

        for i in range(len(suffix)):
            suffix[i] = prefix[i]*suffix[i]
        return suffix