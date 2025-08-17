#شماره رند 
result = []
def numbers_check1(number):
    # if count of number at least 4 times repeat
    check1 = False
    numbers_unique = list(set(number))
    count_numbers = [number.count(num) for num in numbers_unique]
    if any(n>=4 for n in count_numbers):
        check1 = True
    return check1

def numbers_check2(number):
    # It has three consecutive digits of the repeating number.
    numbers_unique = list(set(number))
    result = []
    check2 = False
    for num in numbers_unique:
        if any(number[j] == num and number[j + 1] == num and number[j + 2] == num for j in range(len(number) -2)):
            result.append(True)
        else:
            result.append(False)
    if any(r for r in result):
        check2 = True
    return check2
    
def numbers_check3(number):
    # number with reverse number is equal
    check3 = False
    number_new = number[::-1]
    if number_new == number:
        check3 = True
    return check3

t = int(input())
for _ in range(t):
    number = input()
    while len(number) != 8 or not number.isnumeric():
        print("length number at least 8 and must be number")
        number = input()
    else:
        number = list(map(int,number))
        result_func = [numbers_check1(number),numbers_check2(number),numbers_check3(number)]
        if True in result_func:
            result.append("Ronde!")
        else:
            result.append("Rond Nist")

for r in result:
    print(r)