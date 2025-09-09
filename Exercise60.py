# مربع جادویی
def square_magic(n,m):
    square_list = [[0 for j in range(n)] for i in range(n)]
    i = 0
    j = (n + 1) // 2 - 1
    square_list[i][j] = m
    lm = m + n ** 2 - 1
    while m < lm:
        m += 1
        iMain = i
        jMain = j
        i -= 1
        j += 1 
        if i < 0:
            i = n - 1
        if j == n:
            j = 0
        if square_list[i][j] == 0 :    
            square_list[i][j] = m
        else: 
            i = iMain + 1
            j = jMain
            square_list[i][j] = m 
    return square_list

n, m = map(int, input().split())
result = square_magic(n,m)
for _ in result:
    print(*_)