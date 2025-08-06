def func(a):
    listFinal = ""
    for i in range(len(a)):
        if i == 0 or i == 1:
            listFinal += f"{' '.join(map(str, a[i]))}\n"
        elif i == 2 :
            a[i][1]= 2
            listFinal += f"{' '.join(map(str, a[i]))}\n"
        else:
            for j in range(1,i):
                a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
            listFinal += f"{' '.join(map(str, a[i]))}\n"
    return listFinal
n = int(input())
myList = [[1 for j in range(i + 1)]for i in range(n)]
print(func(myList))


    