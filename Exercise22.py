#نه‌ـ‌به‌ـ‌واج‌آرایی
n = int(input())
newList = [[j for j in input()] for i in range(n)]
listUnique = []
for _ in range(len(newList)):
    listUnique.append(list(set(newList[_])))
lenList = [len(listUnique[_])  for _ in range(n)]
print(max(lenList))


