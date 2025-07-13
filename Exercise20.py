# جمع دو ماتریس

n, m =map(int ,input().split())

listA = [[int(j) for j in input().split()] for i in range(1,n + 1)]
listB = [[int(j) for j in input().split()] for i in range(1,n + 1)]
listC = [[listA[i][j] + listB[i][j] for j in range(m)] for i in range(n)]

for i in range(len(listC)):
    for j in range(len(listC[i])):
        print(f"{listC[i][j]}",end=" ")
    print()
