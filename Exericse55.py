# کشف معادله
from math import floor
def equation1(list_x,list_y):
    result = []
    for i in range(len(list_x)):
        y = list_y[i]
        out_y = list_x[i] - floor(list_x[i])
        if abs(y - out_y) <= 0.2:
            result.append(True)
        else:
            result.append(False)
    if all(result):
        return True

def equation2(list_x,list_y):
    result = []
    for i in range(len(list_x)):
        y = list_y[i]
        x = list_x[i]
        out_y = x ** 2 + x
        if abs(y - out_y) <= 0.2:
            result.append(True)
        else:
            result.append(False)
    if all(result):
        return True
                
def equation3(list_x,list_y):
    result = []
    for i in range(len(list_x)):
        y = list_y[i]
        x = list_x[i]
        out_y = abs(- x ** 3 + 1) + x ** 3
        if abs(y - out_y) <= 0.2:
            result.append(True)
        else:
            result.append(False)
    if all(result):
        return True
      
list_x = []
list_y = []
n = int(input())
for i in range(n):
    x, y = map(float, input().split())
    list_x.append(x)
    list_y.append(y)
    
result = []
if equation1(list_x,list_y):
    result.append(1)
if equation2(list_x,list_y):
    result.append(2)
if equation3(list_x,list_y):
    result.append(3)
if result:
    for r in result:
        print(r)
else:
    print("No ones")

