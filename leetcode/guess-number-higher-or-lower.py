# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        p1= 1
        p2 = n
        while p1<=p2:
            mid = (p1+p2)//2
            result = guess(mid)
            if result == -1:
                p2 = mid-1
            elif result == 1:
                p1 = mid+1
            elif result ==0:
                return mid