class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        array = []
        potions.sort()
        for i in spells:
            p2 = len(potions)
            p1=0
            while p1<p2:
                mid = (p1+p2)//2
                if i * potions[mid]< success:
                    p1=mid+1
                else:
                    p2 = mid
            array.append(len(potions)-p1)
        return array