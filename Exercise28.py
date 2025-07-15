#بدرود
dictGuest = {'Ahmadi':2, 'Bagheri':4, 'Mortazavi':5, 'Hosseini':3, 'Mahmoodi':4}
listOut = []

while True:
    getGuest = input().split()
    if "End" in getGuest:
        break
    if not getGuest[0] in dictGuest:  
        listOut.append("Motasefane Shoma Davat Nistid!")  
    elif getGuest[0] in dictGuest:
        if dictGuest[getGuest[0]] < int(getGuest[1]):
            listOut.append("Tedade Afrade Davat Shode Kamtar Ast!")
        elif dictGuest[getGuest[0]] >= int(getGuest[1]):
            listOut.append("Khosh Amadid!")
for _ in range(len(listOut)):
    print(listOut[_])
