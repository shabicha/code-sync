class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        newIntervals = [intervals[0]]
        for i in range(1,len(intervals)):
            if newIntervals[-1][1] >= intervals[i][0]:
                newIntervals[-1][1] = max(newIntervals[-1][1], intervals[i][1])
            else:
                newIntervals.append(intervals[i])
        return newIntervals