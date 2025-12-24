import random
class RandomizedSet(object):

    def __init__(self):
        self.hashMap={}
        self.array = []

      

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.hashMap:
            
            self.array.append(val)
            self.hashMap[val] = len(self.array)-1
            return True
        else:
            return False    

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.hashMap:
            i = self.hashMap[val] 
            j = len(self.array)-1
            self.hashMap[self.array[j]] = i

            
            self.array[i], self.array[j] = self.array[j], self.array[i]
            
            del self.hashMap[self.array[j]]
            self.array.pop()
            return True    
        else:
            return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        randomInteger = random.randint(0,len(self.array)-1)
        return self.array[randomInteger]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()