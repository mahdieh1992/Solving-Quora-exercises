#مراقب غذا باش... Algoritm for find min and max
def temperature_max(list_temp: list) :
    max_index, temp_max = 0 , list_temp[0]          
    for index,temp in enumerate(list_temp):
        if temp > temp_max:
            temp_max = temp
            max_index = index
    return f"مراقب قابلمه {max_index + 1} باش"

def temperatur_low(list_temp: list) :
    min_index, temp_min = 0 , list_temp[0]
    for index,temp in enumerate(list_temp):
        if temp < temp_min:
            temp_min = temp
            min_index = index 
    return f"زیر قابلمه {min_index + 1} را زیاد کن"

inputs = list(map(int, input().split()))
print(temperature_max(inputs))
print(temperatur_low(inputs))