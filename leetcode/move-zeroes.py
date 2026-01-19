class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #p1=0
        #p2 ++
        p1=0
        p2=0
   

        for i in range(len(nums)):
            if nums[p2] !=0:
                #swap
                nums[p1],nums[p2]=nums[p2],nums[p1]
                p1+=1
            p2+=1
        return nums