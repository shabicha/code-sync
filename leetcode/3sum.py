class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result =[]
        #[-4,-1,-1,0,1,2]
        # i   j. j j   k
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            if i!=0 and nums[i] == nums[i-1]:
                continue

            while j < k:
                target = nums[i] + nums[k] + nums[j]
                if target < 0:
                    j+=1
                elif target > 0:
                    k-=1
                else:
                    result.append([nums[i], nums[k], nums[j]])
                    j+=1
                    while j<len(nums)-1 and nums[j] == nums[j-1]:
                        j+=1


        return result