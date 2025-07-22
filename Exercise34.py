count_Entrance = int(input())
myList = list(map(int,input().split()))
n = len(myList)
if n < count_Entrance:
    print(f"count of number entrance must be {count_Entrance}")
if any(x > 1000000000 for x in myList):
    print(f"number must be less or equal 1000000000")
else:
    for i in range(n):
        for j in range(0,n-i-1):
            if myList[j] < myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]
newList = ' '.join(map(str,myList))
print(newList)
