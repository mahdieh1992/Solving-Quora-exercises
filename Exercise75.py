#کارمند زیادی
def calc(arr):
    ln = len(arr)
    # earn avg numbers in arr
    avg = sum(arr) / ln
    # earn mid in array
    if ln % 2 == 0:
        m = ln // 2
        n = (ln // 2) + 1
        mid = (arr[m - 1] + arr[n -1]) / 2
    else :
        m = (ln - 1) // 2
        mid = arr[m]
    #get max number in array
    maxNum = max(arr)
    return avg,mid,maxNum

myList = [2, 20, 30, 29]
print(calc(myList))