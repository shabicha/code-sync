class Solution:
    def reverseWords(self, s: str) -> str:
        #seperate by spaces
        newString = ""
        splitS = s.split()
        print(splitS)
        #loop reverse and add to new string with space between, " " + s[i]
        for i in range(len(splitS)-1, 0, -1):
            newString += splitS[i] + " "
        newString += splitS[0]
        return newString