#محاسبه‌گر
def calculator(n: int, m: int, ls: list[int]) -> int:
    ls = [sum(ls[i:i + m]) for i in range(0,n,m)]
    result = 0
    for index,item in enumerate(ls):
        if index % 2 == 0:
            result += item
        else:
            result -= item
    return result

print(calculator(8, 3, [1, 2, 3, 4, 5, 6, 7, 8]))
    
