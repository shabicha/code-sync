class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVal =0
        p1=0
        p2=len(height)-1

        while p1<p2:
            volume = (p2-p1)*min(height[p1], height[p2])
            if volume >maxVal:
                maxVal = volume
            if height[p1]<height[p2]:
                p1+=1
            else:
                p2-=1
        return maxVal