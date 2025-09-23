#اسم‌ها
n = int(input())
result = max([len(set(input())) for i in range(n)])
print(result)