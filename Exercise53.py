# در جستجوی پدر
#تابع محاسبه‌ی مجموع ارقام 
def sumNumber(num):
    num = str(num)
    number = list(map(int,num))
    sumNum = 0
    for _ in range(len(number)):
        sumNum += number[_]
    return sumNum

#تابع بررسی اعداد اول یک عدد
def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
            else:
                return True

number_prime = [num for num in range(1,1001) if is_prime(num)]  

#تابع محاسبه عوامل اول
def sum_prime(num):
    number_prime1 = []
    i = 0
    while i < num:
        n = number_prime[i]
        if num % n == 0:
            while num % n == 0:
                if n not in number_prime1:
                  number_prime1.append(n)
                num = num // n
        elif num == 1:
            break
        i += 1               
    return sum(number_prime1)

def CalCulate_D(x):
    calculate = x + sumNumber(x) + sum_prime(x)
    return calculate

t = int(input())
result = []
for i in range(t):     
    n = int(input())
    x = [i for i in range(1,n)]
    r = list(map(CalCulate_D,x))
    if any(_ == n for _ in r):
        result.append("Yes")
    else:
        result.append("No")
print("\n".join(result))
    

