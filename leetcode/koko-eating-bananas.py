class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #calc hours (h) needed to eat k bananas 
        #return hours <= h 
        right = max(piles)
        left = 1 

        while right >= left:
            mid = (left+right)//2
            #calc hours needed for mid = k bananas
            hours = 0
            for i in piles:
                hour = (i+mid-1)//mid
                hours +=hour

            if hours <= h:
                res=mid
                #how high can we go?
                right = mid-1
            elif hours > h:
                left = mid+1
        return res