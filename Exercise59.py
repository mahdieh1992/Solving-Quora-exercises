# اتل متل
n, k = map(int, input().split())
num = []
# create list of pair number
for i in range(1,n + 1):
    num.append(i)
    num.append(i)

while True:
    count_num = len(num) 
    if len(num) == 2 and num[0] == num[1]:
        print(f"winner:{num[0]}")
        break
    if len(num) == 1:
        print(f"winner:{num[0]}")
        break
    if count_num == k:
        print(*num[0:k])
        num.pop(-1) 
     
    elif count_num < k:
        t = k - count_num
        tt = k - count_num
        j = 0 
        while j < tt:
            num.append(num[j])
            j += 1
        print(*num)
        num.pop(-1)
        del num[0: t]

    else:
        print(*num[0:k])
        t = count_num  - k
        for i in range(t):
            num.insert(0,num.pop(-1))
        num.pop(-1)