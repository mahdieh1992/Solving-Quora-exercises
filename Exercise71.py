numberList = []
i = 0
while i < 1000:
    n = int(input())
    if n == 0:
        break
    else:
        numberList.append(n)
numberList.reverse()
for num in numberList:
    print(num)