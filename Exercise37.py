# دانشجویابی
n = int(input())
myList = list(map(int,input().split()))
count_List = len(myList)
num_Not_Exists = 0
if any(x < 0 or x > 1000 for x in myList):
    print("number of list must be between 1 and 1000")
for i in range(1, n + 1):
    if not i in myList:
        num_Not_Exists = i
print(num_Not_Exists)
