class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        minV = min(len(str1), len(str2))
        for i in range(minV,0,-1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                return str1[:i]