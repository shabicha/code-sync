class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        newIntervals =[]
        i=0
        while i< len(intervals) and newInterval[0] > intervals[i][1]:
            newIntervals.append(intervals[i])
            i+=1
        #add edge case if made to end of list here
        if i == len(intervals):
            newIntervals.append(newInterval)
            return newIntervals

        print(newIntervals)
        if newInterval[1] < intervals[i][0]:
                #add newint b4
            newIntervals.append(newInterval)
        else:
                
            intervals[i][0] = min(intervals[i][0], newInterval[0])
            intervals[i][1] = max(intervals[i][1], newInterval[1])
            newIntervals.append(intervals[i])

        print(newIntervals)
        while i < len(intervals):
            if newIntervals[-1][1] >= intervals[i][0]:
                newIntervals[-1][1] = max(newIntervals[-1][1], intervals[i][1])
            else:
                newIntervals.append(intervals[i])
            i+=1
        
        return newIntervals