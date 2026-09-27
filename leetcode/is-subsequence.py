class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps = 0
        pt = 0

        while pt< len(t) and ps < len(s):
            if t[pt] == s[ps]:
                ps+=1
            pt+=1
        if ps == len(s):
            return True

        return False