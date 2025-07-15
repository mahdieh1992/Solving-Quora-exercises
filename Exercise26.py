names_list = input().split()
names_dict = {}
for _ in range(len(names_list)):
        names_dict[names_list[_]] = 0
while True:
    getScore = input().split()
    if "End" in getScore:
            break
    if getScore[0] in names_dict:
        names_dict[getScore[0]]  = names_dict[getScore[0]] + int(getScore[1])
maxValue = max(names_dict.values())
keys = ""
for key,value in names_dict.items():
      if value == maxValue:
            keys += f"{key} \n"
print(keys)
      





