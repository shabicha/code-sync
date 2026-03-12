class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        #unoptimized chud solution
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
            if hashMap[s[end]]>maxF:
                maxF = hashMap[s[end]]
                largest =s[end]

            
            h =0
            for i in hashMap:
                if i != largest:
                    h+= hashMap[i]
            
            while h>k:
                
                if hashMap[s[start]]>1:
                    hashMap[s[start]]-=1
                else:
                    del hashMap[s[start]]    
                
                #check for largest again
                largest = max(hashMap, key=hashMap.get)
                maxF= hashMap[largest]
                start+=1
                #run loop to check condition again
                
                x =0
                for i in hashMap:
                    if i != largest:
                        x+= hashMap[i]
                h=x
            tsum = max(hashMap[largest]+h, tsum)
        return tsum