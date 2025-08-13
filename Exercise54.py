# آلفا قنطورس
def  change_base(n, b):
    dict = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    new_list = []
    while not n == 0:
        r = n % b 
        n = n // b
        if r >= 10 and r < b:
            r = dict[r]
        new_list.append(r)
        result = "".join(map(str,new_list[::-1]))
    return result


n, b = map(int, input().split())
print(change_base(n, b))
