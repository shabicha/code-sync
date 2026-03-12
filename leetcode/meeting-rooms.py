class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True
        
        intervals.sort(key= lambda x : x[0])

        start = intervals[0][1]
        [[0,30],[5,10],[15,20]]

        for i in range(1,len(intervals)):
            if intervals[i][0] < start:
                return False
            start = intervals[i][1]
        return True