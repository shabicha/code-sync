class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        #[1,2,3,4,5,6,1]
        #tsum = 10
        tsum =0
        length = len(cardPoints) - k

        for i in range(length):
            tsum += cardPoints[i]
        
        l = length
        j = 0
        cur =tsum
        while l <len(cardPoints):
            cur =cur-cardPoints[j]+cardPoints[l]
            tsum = min(tsum, cur)
            l+=1
            j+=1
        return sum(cardPoints)-tsum