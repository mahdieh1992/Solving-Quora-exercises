def sort_selection(list_num):
    n = len(list_num)
    for i in range(n):
       list_num[i] = list_num[i] + 1
    return list_num

a = list(map(int, input().split()))
result = sort_selection(a)
for num in result:
    print(num)