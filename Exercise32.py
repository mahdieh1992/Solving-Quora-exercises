unorderedList = [5,8,1,3,2,6]
n = len(unorderedList)
for _ in range(n):
    minNum = min(unorderedList[_:])
    indexValue = unorderedList.index(minNum)
    unorderedList.pop(indexValue)
    unorderedList.insert(_,minNum)
print(unorderedList)
