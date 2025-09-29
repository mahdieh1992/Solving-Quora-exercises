#بتایپ
s = input().strip("=")
newString = []
for chr in s:
    if chr == "=":
        newString.pop()
    else:
        newString.append(chr)
newString = "".join(newString)      
print(newString)