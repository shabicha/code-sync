class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """

        hashMap ={}
        tsum =0
        start =0
        cur=0
        for end in range(len(fruits)):
            
            #add to end
            if fruits[end] in hashMap:
                hashMap[fruits[end]] += 1
            else:
                hashMap[fruits[end]] = 0
            cur +=1

            if len(hashMap) > 2:
                while len(hashMap) > 2:
                    if hashMap[fruits[start]] >0:
                        hashMap[fruits[start]] -=1
                    else:
                        del hashMap[fruits[start]]
                    start+=1
                    cur-=1
            
            tsum = max(tsum, end-start+1)

        return tsum