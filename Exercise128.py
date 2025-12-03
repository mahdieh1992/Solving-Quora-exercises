#greedy Algoritm
arr = list(map(int, input().split()))
ln = len(arr)
i = 0
result = []
found = False
while i < ln - 1:
    s = 0
    for j in range(i + 1,ln):
        if arr[j] == arr[j - 1]:
            continue
        s += arr[j] - arr[j - 1]
        if s >= 3:
            if i + 1 not in result:
                result.append(i +1)
            if j + 1 not in result:
                result.append(j + 1)
            i = j 
            found = True
            break
    if not found:
        i += 1
print(*result)