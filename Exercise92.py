import re
def real_numbers(numbers: list[str]) -> list[str]:
    pattern = r'^\s*[-+]?(\d+(.\d+)?)([Ee]?[+-]?\d+)?\s*$'
    flag = 0
    result = []
    for number in numbers:
        if re.match(pattern,number):
            result.append('LEGAL') 
        else:
             result.append('ILLEGAL')
    return result
print(real_numbers(['1.5e+2', '3.', '1.1.1', '1+e5', ' -123.45 ', '0', '+10E-5', 'abc', '1. ', '.5', '5e', '5e1.0']))