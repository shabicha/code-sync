class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        i=0
        count =0
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
            return True
            
        while i < len(flowerbed):
            if i-1 >=0 and i+1<len(flowerbed) and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] ==0:
                i +=2
                count +=1
            elif i-1<0 and i+1<len(flowerbed) and flowerbed[i+1]==0 and flowerbed[i] ==0:
                i+=2
                count +=1
            elif i+1>len(flowerbed)-1 and i-1 >=0 and flowerbed[i-1] ==0 and flowerbed[i] ==0:
                i+=2
                count +=1
            else:
                i+=1
        if count >= n:
            return True
        return False