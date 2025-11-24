def check_device(n,list_paper):
    n = int(n)
    ln = len(list_paper)
    if n < 1 or n > 3:
        return f".لطفا بین ۱ تا ۳ وارد کنید"
    else:
        if n == 1:
            for i in range(ln):
                if list_paper[i] % 2 == 0:
                   list_paper[i] -= 3
        elif n == 2:
            for i in range(ln):
                if list_paper[i] % 2 !=0:
                    list_paper[i] **= 2
        elif n == 3:
            for i in range(ln):
                if i % 4 == 0:
                    list_paper[i] += list_paper[i + 1]
    return " ".join(map(str, list_paper))
        
n = input()
list_paper = list(map(int, input().split()))
result = check_device(n,list_paper)
print(result)