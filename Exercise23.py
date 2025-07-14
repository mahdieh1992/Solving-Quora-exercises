#دومین چهار
n = int(input())
listNumber = list(map(int, input().split()))
flag = -1
count = 0
for _ in range(n):
    if listNumber[_] == 4:
        flag = _ + 1
        count += 1
    if listNumber[_] == 4 and count == 2:
        print(flag)
if count < 2:
    print(-1)
