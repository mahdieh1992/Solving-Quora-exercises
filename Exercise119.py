# Sorted Selection
def sorted_paper(list_number:list,status) -> list:
    ln = len(list_number)
    if status == 0:
        for i in range(ln):
            max = i 
            for j in range(i + 1, ln):
                if list_number[j] > list_number[max]:
                    max = j
            list_number[i] , list_number[max] = list_number[max] , list_number[i]
        return list_number
    
    if status == 1:
        for i in range(ln):
            min = i 
            for j in range(i + 1, ln):
                if list_number[j] < list_number[min]:
                    min = j
            list_number[i] , list_number[min] = list_number[min] , list_number[i]
        return list_number

 
list_number = list(map(int, input().split()))
status = int(input())   
print(sorted_paper(list_number,status))
