class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        #find max
        result = []
        maxV = max(candies)
        for i in candies:
            if i + extraCandies>=maxV:
                result.append(True)
            else:
                result.append(False)
        return result