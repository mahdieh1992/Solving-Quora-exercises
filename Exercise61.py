# جدول ضرب گنده
n = int(input())
result = [[i * j for j in range(1,n + 1)] for i in range(1, n + 1)]
for _ in result:
    print(*_)