# تابع انتخابی
def fact(n):
    # factorial number
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)

def comb(n,k):
    # calculate combination with call function fact 
    if k == 0:
        return 1
    elif k > n:
        return 0 
    else:
        factN = fact(n)
        factK = fact(k)
        factNK = fact(n - k)
        result = factN // (factK * factNK)
        return result
n = 4
r = 4
print(comb(n,r))

