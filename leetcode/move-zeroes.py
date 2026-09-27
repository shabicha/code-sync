class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1=0
        p2=0
        [1,0,0,3,12]
        [1,3,12,0,0]

        while p1< len(nums) and nums[p1] != 0:
            p1+=1
        p2=p1
        while p2 < len(nums):
            if nums[p2] !=0:
                nums[p2], nums[p1] = nums[p1], nums[p2]
                while nums[p1] != 0:
                    p1+=1
            p2+=1