class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r= deque([])
        d= deque([])
        #set r & d
        for i in range(len(senate)):
            if senate[i] == "R":
                r.append(i)
            else:
                d.append(i)

        #iterate if senate[i], RRD
        i=0
        while r and d:
            rI = r.popleft()
            dI = d.popleft()
            if rI < dI:
                r.append(rI + len(senate))
            else:
                d.append(dI + len(senate))
        
        if r:
            return "Radiant"
        if d:
            return "Dire"