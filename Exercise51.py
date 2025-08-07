#باغچه رز
count_flower, month =map(int, input().split())
flower_list = []
count_w = [0] * count_flower
result = ""
for i in range(month):
    new_list = input().upper()
    if len(new_list) != count_flower:
       print(f"count flower must be {count_flower}")
       exit()
    else:  
         flower_list.append(list(new_list))
for i in range(month):
             for j in range(count_flower):
                 if flower_list[i][j] == "W":
                     count_w[j] = count_w[j] + 1
for num in count_w:
    if num % 2 == 0:
        result += "B"   
    else:
        result +="F"                      
print(result)