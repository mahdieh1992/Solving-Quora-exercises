# تغییرات آرایوی
n = int(input())
myList = []
newList = []
for _ in range(n):
    listOperate = input().split()
    if listOperate[0] == '+':
        myList.insert(int(listOperate[1]) -1 ,int(listOperate[2]))
        newList.append(list(myList))
    elif listOperate[0] == '-':
        myList.pop(int(listOperate[1]) -1) 
        newList.append(list(myList))      
for i in range(len(newList)):
    strList = ''
    if len(newList[i]) == 0:
        strList += "EMPTY"
    else:
        for j in range(len(newList[i])):    
            strList +=f"{newList[i][j]} "
    print(strList)
    strList = ''