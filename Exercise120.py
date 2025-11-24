# Sorted Selection
def sorted_paper(list_number:list,val) -> list:
    ln = len(list_number)
    for i in range(ln):
        min = i 
        for j in range(i + 1, ln):
            if list_number[j] < list_number[min]:
                min = j
        list_number[i] , list_number[min] = list_number[min] , list_number[i]
    val = - val
    return list_number[val]

list_number = list(map(int, input().split()))
status = int(input())   
print(sorted_paper(list_number,status))
