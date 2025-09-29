#کارمند زیادی
count_employee = int(input())
employee = {}
for i in range(count_employee):
    get_employee = list(input().split())
    employee[get_employee[0]] = employee.get(get_employee[0],0) + 1

colorNeed = max(employee.values())    
print(colorNeed)