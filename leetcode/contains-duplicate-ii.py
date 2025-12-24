class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = i
            else:
                j = hashMap[nums[i]]
                if abs(i-j) <=k:
                    return True
                hashMap[nums[i]] = i
        return False