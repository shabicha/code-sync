"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
"""

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        #flatten
        intervalsList=[]
        freeTime =[]
        result =[]
        for employee in schedule:
            for i in range(len(employee)):
                s = employee[i].start
                e= employee[i].end
                intervalsList.append([s,e])
        intervalsList.sort()
        
        #merge
        freeTime.append(intervalsList[0])
        
        for i in range(1, len(intervalsList)):
            if freeTime[-1][1] >= intervalsList[i][0]:
                freeTime[-1][1] = max(freeTime[-1][1], intervalsList[i][1])
            else:
                freeTime.append(intervalsList[i])
        #find negative space between
        prev = 0
        for i in range(1,len(freeTime)):
            result.append(Interval(freeTime[prev][1], freeTime[i][0]))
            prev+=1
        
        return result