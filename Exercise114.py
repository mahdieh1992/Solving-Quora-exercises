user_input = input()
A = [int(x) for x in user_input.split()]
n = len(A)
def temperature_low(list_temp):
    low = 20 
    for i in range(n):
        if list_temp[i] < low:
            low = list_temp[i]
            print("زیر قابلمه", i+1, "را زیاد کن")
    return low

def temperature_max(list_temp):
    high = 100 
    for i in range(n):
        if list_temp[i] > high:
            high = list_temp[i]
            print("مراقب قابلمه", i + 1, "باش")
    return high
    
temperature_max(A)
temperature_low(A)