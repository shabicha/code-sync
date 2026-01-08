class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        result = [intervals[0]]

        i=0
        while i <= len(intervals) -1:
            if result[-1][1]>= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])

            else:
                result.append(intervals[i])
            i+=1

        return result