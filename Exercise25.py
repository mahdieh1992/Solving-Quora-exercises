#یک دو زبانه
myDictEnglish = {
    1:'One',
    2:'Two',
    3:'Three',
    4:'Four', 
    5:'Five',
    }

myDictFranch ={
    1:'Un',
    2:'Deux',
    3:'Trois',
    4:'Quatre',
    5:'Cinq'  
}
newList = list()
getNumber =''
while True:
    getNumber = input().split()
    if "End" in getNumber:
        break
    if not 1 <= int(getNumber[0]) <=5:
        print('number must be 1 and 5')
    else:
        newList.append(getNumber)

for _ in range(len(newList)):
    if newList[_][1].capitalize() == 'En':
        key1 = int(newList[_][0])
        print(myDictEnglish[key1])
    elif newList[_][1].capitalize() == 'Fr':
        key1 = int(newList[_][0])
        print(myDictFranch[key1])
    else:
        print('None')
