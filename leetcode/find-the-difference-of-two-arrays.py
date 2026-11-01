class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums2Hash = set(nums2)
        nums1Hash = set(nums1)
   
        nums1D =[]
        nums2D =[]
        array = []

        for i in nums1Hash:
            if i not in nums2Hash:
                nums1D.append(i)

        for i in nums2Hash:
            if i not in nums1Hash:
                nums2D.append(i)
        array.append(nums1D)
        array.append(nums2D)
        return array