class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left =0
        right = len(height)-1
        leftMax =height[left]
        rightMax=height[right]
        tsum = 0

        while left < right:
            #check which side smaller
            #move to that side, if next val smaller, calc difference and add
            #if not, skip, edit new max val
            if height[left] < height[right]:
                if height[left+1] < leftMax:
                    tsum += leftMax - height[left+1]
                else:
                    leftMax = height[left+1]
                left+=1
            else:
                if height[right-1] < rightMax:
                    tsum += rightMax-height[right-1]
                else:
                    rightMax = height[right-1]
                right-=1

        return tsum