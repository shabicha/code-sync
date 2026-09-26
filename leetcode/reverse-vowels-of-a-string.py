class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s)-1
        s= list(s)
        print(s)
        vowels = set('aeiouAEIOU')
        leftV = False
        rightV = False
        while l < r:
            while leftV == False and l<r:
                if s[l] in vowels:
                    leftV = True
                else:
                    l+=1
                
            while rightV == False and l<r:
                if s[r] in vowels:
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