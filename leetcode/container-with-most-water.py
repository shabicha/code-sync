class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height)-1
        maxArea = 0
        while p1<p2:
            length = min(height[p1],height[p2])
            area = length*(p2-p1)
            maxArea = max(maxArea, area)
            if height[p1] > height[p2]:
                p2-=1
            else:
                p1+=1
        return maxArea