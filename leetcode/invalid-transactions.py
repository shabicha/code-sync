class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        
        hashMap={} #add index aswell
        #alice: [[20,800,mtv], [30,800,mtv]]
        result = set()
        resultArray=[]

        for i in range(len(transactions)):
            t = transactions[i].split(",")
            amount = int(t[2])
            time = int(t[1])
            #if greater than 1k add to set result
            if amount>1000:
                result.add(i)
            
            #loop
            if t[0] in hashMap:
                for ptime, pamount, pcity, index in hashMap[t[0]]:
                    if pcity != t[3] and abs(int(ptime) - time)<= 60:
                        result.add(i)
                        result.add(index)
                
            if t[0] in hashMap:
                hashMap[t[0]].append(t[1:] + [i])
            else:
                hashMap[t[0]] = [t[1:] + [i]]

        for i in result:
            resultArray.append(transactions[i])
            
        #loop through result add to resultArray
        return resultArray