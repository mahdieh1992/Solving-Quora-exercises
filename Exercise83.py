#چی‌سون؟
import json
my_Dict = {}
result = []
count_input = int(input())
for _ in range(count_input):
    string = input()
    if ':=' in string:
        varibale, value = string.split(":=", 1)
        varibale = varibale.strip()
        Data = json.loads(value)
        my_Dict[varibale] = Data
    elif string.rstrip("print"):
        get_key = string.removeprefix("print")
        get_key = get_key.strip()
        if '"' in get_key:
            start = get_key.find('["')
            end = get_key.find(']')
            inner_key = get_key[start + 1: end]
            key_main = get_key[:start]
            inner_key = json.loads(inner_key)
        else:
            start = get_key.find('[')
            end = get_key.find(']')
            inner_key = int(get_key[start + 1: end])
            key_main = get_key[:start]
        result.append(my_Dict[key_main][inner_key])
for _ in result:
    print(_)