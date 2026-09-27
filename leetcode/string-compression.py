class Solution:
    def compress(self, chars: list[str]) -> int:

        s=[]
        count =0
        total = 0
        i=0
        while i < len(chars):
            s=[]
            s.append(chars[i])
            count = 0
            while i < len(chars) and chars[i] == s[0]:
                i+=1
                count +=1
            if count != 1:
                s+= list(str(count))
            #how to replace within chars?
            
            chars[total:total+len(s)] = s
            total += len(s)
        return total