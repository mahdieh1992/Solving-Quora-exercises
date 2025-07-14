# آرایه بازی
n,q = map(int, input().split())
list1 = list(map(int, input().split()))
if len(list1) != n:
    print(f"count of number must be {n}")
list2 = [[int(j) for j in input().split()] for i in range(q)]
sumNumbers = []
for i in range(len(list2)):
    index1 = list2[i][1]
    index2 = list2[i][2]
    if list2[i][0] == 1:
        sub_List = list1[index1 -1:index2]
        sumNum = sum(sub_List)
        sumNumbers.append(sumNum)
    elif list2[i][0] == 2:
        delNum = list1.pop(index2 -1)
        list1.insert(index1 -1,delNum)
for _ in range(len(sumNumbers)):
    print(sumNumbers[_])

