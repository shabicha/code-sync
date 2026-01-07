class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        result = []



        i=0
        while i <= len(intervals) -1:
            if i+1<=len(intervals)-1 and intervals[i][1] >= intervals[i+1][0]:
                if intervals[i][1]< intervals[i+1][1]:
                    intervals[i:i+2] = [[intervals[i][0], intervals[i+1][1]]]
                else:
                    intervals[i:i+2] = [[intervals[i][0], intervals[i][1]]]
            else:
                result.append(intervals[i])
                i+=1

        return result