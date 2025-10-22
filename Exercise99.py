import random
class RandomList:
    def __init__(self,data):
        self._data = list(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self._data) == 0:
           raise StopIteration
        index = random.randint(0,len(self._data) -1 )
        return self._data.pop(index)     
myList = [1,1,2,3,4,2,1,44,5]    
rand = RandomList(myList)
rand1 = iter(rand)
print(*rand1)
