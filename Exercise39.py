#مرتب‌سازی خفن
n = int(input())
Students = [0] * n

for i in range(n):
    name = input().strip()
    grade_input = input().split()
    countGrade = int(grade_input[0])
    grades = list(map(float, grade_input[1:]))
    if len(grades) != countGrade:
        print(f"count of grade must be {countGrade}")
        exit(1)
    sport_input = input().split()
    countSport = int(sport_input[0])
    sports = sport_input[1:]
    if len(sports) != countSport:
        print(f"count of sport must be {countSport}")
        exit(1)
    avg_int = int(sum(grades) / countGrade)
    Students[i] = [name, avg_int, countSport, i]  # اضافه کردن شماره اولیه

m = len(Students)

def compare():
    for i in range(m):
        for j in range(i + 1, m):
            if Students[i][1] < Students[j][1]:
                Students[i], Students[j] = Students[j], Students[i]
            elif Students[i][1] == Students[j][1]:
                if Students[i][2] < Students[j][2]:
                    Students[i], Students[j] = Students[j], Students[i]
                elif Students[i][2] == Students[j][2]:
                    if Students[i][3] > Students[j][3]:
                        Students[i], Students[j] = Students[j], Students[i]

compare()
for s in Students:
    print(s[0])