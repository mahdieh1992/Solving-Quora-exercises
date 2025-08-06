n, m = map(int, input().split())
arr = list(map(int, input().split()))

if len(arr) != n:
    print(f"please enter count number {n}")
    exit()

for i in range(n):
    if m == 1:
        print(f"{i} to {i}")
    else:
        if i + m < n:
            count = 0
            for j in range(i, i + m - 1):
                if arr[j] <= arr[j + 1]:
                    count += 1
                else:
                    break
            if count == m - 1:
                print(f"{i} to {i + m - 1}")
