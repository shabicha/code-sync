class Solution:
    def largestAltitude(self, gain: list[int]) -> int:

        maxAlt = 0
        start = 0
        for i in range(len(gain)):
            start = gain[i]+start
            maxAlt = max(maxAlt, start)

        return maxAlt