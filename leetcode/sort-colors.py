class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #count hou many of each then iterate through list to place them in order
        #= o(n)
        count = [0,0,0]
        for i in range(len(nums)):
            if nums[i] == 0:
                count[0] +=1
            elif nums[i] == 1:
                count[1] +=1
            else :
                count[2] +=1

       
        nums[0:count[0]] = count[0] * [0]
        nums[count[0]:count[1]+count[0]] = count[1] * [1]
        nums[count[1]+count[0]:] = count[2] * [2]