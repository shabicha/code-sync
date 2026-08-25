class Solution:
    def canFit(self, nums, mid, k):
        count = 1
        sumn = 0
        for num in nums: 
            sumn = sumn + num
            if sumn>mid:
                sumn = num
                count +=1
           
        if count <= k:
            return True
        return False
        #can array be split if no bag is allowed to be larged than mid

    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        soln = 0
        while low <= high:
            mid = (low + high)//2
            if self.canFit(nums, mid, k):
                soln = mid
                high = mid -1
            else:
                low = mid +1 
        return soln