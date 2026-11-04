class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        start = intervals[0]
        removal = 0
        for i in range(1,len(intervals)):
            if start[1] > intervals[i][0]:
                removal +=1
                #keep smaller interval
                if intervals[i][1] < start[1]:
                    start = intervals[i]

            else:
                start = intervals[i]
        return removal