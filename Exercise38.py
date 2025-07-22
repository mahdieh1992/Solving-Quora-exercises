# تقلب در شب یلدا!
numbers = list(map(int,input().split()))
n = len(numbers)
dict_numbers = {}
for i in range(n):
    if not numbers[i] in dict_numbers.keys() :
        count = 1
        j = i + 1
        while j < n:
            if numbers[i] == numbers[j]:
                count += 1
                dict_numbers[numbers[i]] = count
            j += 1
maxValue = max(dict_numbers.values())
listNew = []
for key in dict_numbers.keys():
    if dict_numbers[key] == maxValue:
        listNew.append(key)
print(min(listNew),maxValue)