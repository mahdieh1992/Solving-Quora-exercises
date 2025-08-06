n = int(input())
arr = list(map(int,input().split()))
if len(arr) != n:
    print(f"please enter count number equal {n}")
x = int(input())


def binary_Search(arr,x):
    arr.sort()
    if arr[-1] == x:
        return len(arr) - 1
    if arr[-1] < x:
        return -1
    low = 0
    high = len(arr) - 1
    while high - low > 1:
        m = (high + low) // 2
        if arr[m] <= x:
            low = m
        else:
            high = m
    if arr[low] ==  x:
        return low
    return -1
    
print(binary_Search(arr,x))


