class Solution:
    def helper(self, nums, limit, k):
        count = 1
        sum1 = 0

        for num in nums:
            if sum1 + num > limit:
                sum1 = num
                count +=1
            else:
                sum1 +=num
        return count <= k



    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        soln = 0

        while low <= high:
            mid = (low + high)//2
            if self.helper(nums, mid, k):
                soln = mid
                high = mid - 1
            else:
                low = mid+1
        return soln