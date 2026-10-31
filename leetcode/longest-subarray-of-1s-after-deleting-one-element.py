class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        zero = 1
        p1=0
        maxV = 0
        subA = 0
        #[1,1,0,0,1,1,1,0,1]

        for p2 in range(len(nums)):
            if nums[p2] == 0 and zero>0:
                zero -=1
            elif nums[p2] == 0 and zero ==0:
                #decrease p1 until zero =1 + -1 subA
                while nums[p1] == 1:
                    p1+=1
                    subA-=1
                p1+=1      
            else:
                subA +=1  
            maxV = max(subA, maxV)
        if zero ==1:
            return maxV -1
        else:
            return maxV