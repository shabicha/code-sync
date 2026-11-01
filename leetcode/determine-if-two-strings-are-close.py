class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        #if frequencies are same
        #check for same distinct characters 
        hash1 = {}
        hash2 = {}
        for i in word1:
            if i in hash1:
                hash1[i] += 1
            else:
                hash1[i] = 1
    
        for i in word2:
            if i in hash2:
                hash2[i] += 1
            else:
                hash2[i] = 1
        if hash1.keys() != hash2.keys():
            return False

        if sorted(list(hash1.values())) != sorted(list(hash2.values())):
            return False
        return True