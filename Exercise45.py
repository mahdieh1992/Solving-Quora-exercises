#رشته تو رشته
string_Main = input()
lenStr = len(string_Main)
s = input()
n = len(s)
for i in range(lenStr):
    if string_Main[i:i + n] == s:
        print(f"{i + 1}",end=" ")