#  مرتب سازی درجی 
n = int(input())
myList = list(map(int,input().split()))
count_List = len(myList)
if count_List < n:
    print(f"count of number entranced must be {n}")
if any(x > 1000000000 for x in myList):
    print(f"number must be less or equal 1000000000")
else:
    for i in range(1,count_List):
        j = i 
        while j > 0 and myList[j] < myList[j - 1]:
            myList[j - 1], myList[j] = myList[j], myList[j - 1]
            j -= 1
print(' '.join(map(str,myList)))