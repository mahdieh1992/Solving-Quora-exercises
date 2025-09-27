import re
# دانشجویان بیکار
def solve(string):
    stringR = re.sub(r'\+ | \=','',string).split()
    len_s = len(stringR)
    get_index = 0
    result = 0
    for i in range(len_s):
        if "#" in stringR[i]:
            get_index = i
        else:
            stringR[i] = int(stringR[i])
    if get_index == 0:
        result = stringR[2] - stringR[1]
    elif get_index == 1:
        result = stringR[2] - stringR[0]
    else:
        result = stringR[0] + stringR[1]   
    pattern = stringR[get_index].replace("#","\d*")
    if re.match(f"^{pattern}$",str(result)):
        stringR[get_index] = str(result)
        return "{} + {} = {}".format(stringR[0],stringR[1],stringR[2])
    else:
        return "-1"
string = "15 + 1#2 = 136"
print(solve(string))