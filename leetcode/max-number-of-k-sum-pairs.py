class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashMap = {} #nums[i] : num of occurances 
        output = 0
        for i in range(len(nums)):
            if k - nums[i] not in hashMap:
                if nums[i] not in hashMap:
                    hashMap[nums[i]] = 0
                else:
                    hashMap[nums[i]] +=1
            else:
                output +=1
                if hashMap[k - nums[i]] == 0:
                    del hashMap[k - nums[i]]
                else:
                    hashMap[k - nums[i]]-=1
        return output