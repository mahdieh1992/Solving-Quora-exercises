# آسمان شکر‌آباد
n,m = map(int, input().split())
list1 = [['0'] * m for i in range(n)]

count = 0
for i in range(n):
    getShape = input()
    for j in range(len(getShape)):
        list1[i][j] = getShape[j]
        if getShape[j] == '*':
            count += 1
print(count)

