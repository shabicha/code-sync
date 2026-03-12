class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        #optimized non-chud solution
        hashMap={} #B:2, A:1, C:1
        start =0
        tsum =0
        largest=0
        maxF=0
        for end in range(len(s)):

            #add end to hashmap 
            if s[end] not in hashMap:
                hashMap[s[end]] =1
            else:
                hashMap[s[end]] +=1
            maxF = max(maxF, hashMap[s[end]])

            if maxF+k < end-start+1:
                hashMap[s[start]]-=1
                start+=1
            
         
            tsum = max(end-start+1, tsum)
        return tsum