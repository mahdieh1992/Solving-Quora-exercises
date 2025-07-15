dictChar = {'.': 0, '?': 0, '!': 0, ',': 0, '/': 0, '-': 0, '+': 0}
strSentence = input()
for _ in strSentence:
    if _ in dictChar:
        dictChar[_] = dictChar[_] + 1
print(dictChar)