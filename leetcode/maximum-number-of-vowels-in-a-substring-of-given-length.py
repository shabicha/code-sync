class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxSubstring = 0
        
        p1=0
        set1 = {'a', 'e', 'i', 'o', 'u'}
        for i in range(k):
            if s[i] in set1:
                maxSubstring +=1
        substringC = maxSubstring
        for p2 in range(k, len(s)):
            if s[p1] in set1:
                substringC -=1
            if s[p2] in set1:
                substringC +=1
            maxSubstring = max(substringC, maxSubstring)
            p1+=1
        return maxSubstring