class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        set1=set()
        start = 0
        tsum = 0
        
        for end in range(len(s)):
            #add end to set
            if s[end] not in set1:
                set1.add(s[end])
            else:
                while s[end] in set1:
                    set1.remove(s[start])
                    start +=1
                set1.add(s[end])
            tsum = max(tsum, end-start+1)
        return tsum