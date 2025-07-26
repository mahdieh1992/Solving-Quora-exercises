# دیتابیس خیلی بزرگ جستجو دودویی
n, q = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
if len(arr) != n:
    print(f"count number must be {n}")
newList = []
def binary_search(arr,x):
    if arr[-1] == x:
        return 1
    if arr[-1] < x:
        return 0
    low = 0
    high = len(arr) -1
    while high - low > 1:
        mid = (high + low) // 2
        if arr[mid] <= x:
            low = mid
        else:
            high = mid
    if arr[low] == x:
        return 1
    return 0
for i in range(q):
    a, x = input().split()
    newList.append(binary_search(arr,int(x)))
print("\n".join(map(str,newList)))




