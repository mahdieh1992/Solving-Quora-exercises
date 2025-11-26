# الگوریتم حریصانه
def calculate(list_num : list,m :int) -> int :
    count = {}
    for num in list_num:
        x = m // num
        m = m % num
        count[num] = x
    count= dict(filter(lambda item:item[1] > 0, count.items()))
    return count

m = 30
list_num = list(map(int, input().split()))
print(calculate(list_num,m))