class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        counter =0
     
        for i in range(len(nums)-1,-1,-1):
            left = 0
            right = i-1

            while left < right:
                if nums[left]+ nums[right]> nums[i]:
                    #add combs to counter
                    counter += right-left 
                    right-=1
                else:
                    left +=1
        return counter