s = input().strip()
p = input().strip()
lp, ls = len(p), len(s)
dictP = {}
count = 0

# counter each letter in p input and add to dictP
for char in p:
    dictP[char] = dictP.get(char,0) + 1
    
# counter each letter in s input and add to dictS   
for i in range(ls - lp + 1):
    dictS = {}
    count_question = 0
    substring = s[i:i + lp]
    for char in substring:
        if char == '?':
            count_question += 1
        else:
            dictS[char] = dictS.get(char,0) + 1
    required = 0         
    for char in dictP:
        countS = dictS.get(char,0)
        if countS > dictP[char]:
            break
        required += dictP[char] - countS

    if required == count_question:
        count += 1
print(count)

