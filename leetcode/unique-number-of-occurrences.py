class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        hashMap = {}
        set1 = set()

        for i in arr:
            if i in hashMap:
                hashMap[i] +=1
            else:
                hashMap[i] = 1
        
        for val in hashMap.values():
            if val in set1:
                return False
            set1.add(val)
        return True