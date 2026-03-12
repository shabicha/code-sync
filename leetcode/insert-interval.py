class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        #unclean chud solution 
        
        merged =[]
        #loop until newInterval addable
        inserted = False

        i=0
        while i<len(intervals):
            #addable before
            if newInterval[0] <= intervals[i][0]:
                if newInterval[1]<intervals[i][0]:
                    #add both
                    merged.append(newInterval)
                    merged.append(intervals[i])
                    inserted = True
                    break

                else:
                    merged.append([newInterval[0], max(newInterval[1], intervals[i][1])])
                    inserted = True
                    break
            elif newInterval[0] <= intervals[i][1]:
                merged.append([intervals[i][0], max(newInterval[1], intervals[i][1])])
                inserted = True
                break
            else:
                merged.append(intervals[i])
                i+=1
        
        if inserted == False:
            merged.append(newInterval)   


        start = merged[-1][1]
        i+=1
        #loop merging next intervals until no more
        while i<len(intervals):
            if intervals[i][0] <= start:
                merged[-1][1] = max(start, intervals[i][1])
                start = merged[-1][1]
            else:
                merged.append(intervals[i])
            i+=1
        return merged