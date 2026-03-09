class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        tsum=0
        hashMap ={} 
        curr =0
        start =0
        for end in range(len(nums)):
            #increase, add end to curr, until k value reached
            curr += nums[end]
            if nums[end] in hashMap:
                hashMap[nums[end]] +=1
            else:
                hashMap[nums[end]] =0

            if end-start +1 == k:
                if len(hashMap) == k:
                    tsum = max(tsum, curr)

                curr -=nums[start]
                if hashMap[nums[start]] >=1:
                    hashMap[nums[start]] -=1
                else:
                    del hashMap[nums[start]]
                start+=1
        return tsum








        #loop until end, if new element in m, reset pointers