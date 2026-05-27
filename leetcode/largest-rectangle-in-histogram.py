class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        maxVal = 0

        i=0
        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i+=1
            else:
                #pop and calculate distance w/ last stack value
                index = stack.pop()
                if not stack:
                    start = -1
                else:
                    start = stack[-1]
                val = (i - start-1)*heights[index]
                maxVal = max(maxVal, val)
        while stack:
            index = stack.pop()
            #end = i, and start = last stack or -1
            if stack:
                val = (i-stack[-1] -1)*heights[index]
            else:
                val = (i+1-1)*heights[index]
            maxVal = max(maxVal, val)
        return maxVal