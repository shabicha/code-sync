class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        zeros =0
        p1=0
        maxV = 0
        #[1,1,1,0,0,0,1,1,1,1,0]
        for p2 in range(len(nums)):
            if nums[p2] == 0 and zeros != k:
                zeros +=1
            elif nums[p2] == 0 and zeros == k:
                while zeros == k:
                    if nums[p1] ==0:
                        zeros -=1
                    p1+=1
                zeros +=1
            maxV = max(maxV, p2-p1+1)
        return maxV