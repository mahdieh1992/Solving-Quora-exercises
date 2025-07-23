#دیتابیس نسبتا بزرگ
n, q = map(int,input().split())
listNumber = list(map(int,input().split()))
if len(listNumber) != n:
    print(f"count number must be {n}")
    exit(1)
listSearch = []
for _ in range(q):
    num = input().split()
    listSearch.append(int(num[1]))
def search_num(arr,size,key):
    for i in range(size):
        if arr[i] == key:
            return 1
    return 0
for _ in range(len(listSearch)):
    print(search_num(listNumber,n,listSearch[_]))