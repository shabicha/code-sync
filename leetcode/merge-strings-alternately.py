class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        x=0
        mergedString = ""
        while len(word1)-1 >= x and len(word2)-1>= x:
            mergedString += word1[x]
            mergedString += word2[x]
            x+=1
        
        if len(word1)> x:
            mergedString += word1[x:]

        if len(word2)> x:
            mergedString += word2[x:]
        return mergedString