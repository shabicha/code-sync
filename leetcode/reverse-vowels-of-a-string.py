class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s)-1
        s= list(s)
        print(s)
        leftV = False
        rightV = False
        while l < r:
            while leftV == False and l<r:
                if s[l] == 'a' or s[l] == 'e' or s[l] == 'i' or s[l] == 'o' or s[l] == 'u' or s[l] == 'A' or s[l] == 'E' or s[l] == 'I' or s[l] == 'O' or s[l] == 'U':
                    leftV = True
                else:
                    l+=1
                
            while rightV == False and l<r:
                if s[r] == 'A' or s[r] == 'E' or s[r] == 'I' or s[r] == 'O' or s[r] == 'U' or s[r] == 'a' or s[r] == 'e' or s[r] == 'i' or s[r] == 'o' or s[r] == 'u':
                    rightV = True
                else:
                    r-=1      
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
            leftV = False
            rightV = False
        s = "".join(s) 
        return s