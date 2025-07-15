#انتخاب بد
studentDict = {}
sumGrade = 0
count = 0
ListGreat = []
while True:
    getStudent = input().split()
    if "End" in getStudent:
        break
    studentDict[getStudent[0]] = float(getStudent[1])
    sumGrade += float(getStudent[1])
    count += 1
Avg = sumGrade / count
sumFinal = 0
countFinal = 0
for key,value in studentDict.items():
    if value >= Avg:
        ListGreat.append(key)
        sumFinal += value
        countFinal +=1
print(f"{ListGreat}\n{sumFinal/countFinal}")





