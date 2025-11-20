# selection algoritm best team
arr = list(map(int, input().split()))
n = len(arr)
def selection_arr(arr):
    best_team = [(arr[i], i + 1) for i in range(n)]
    for i in range(3):
        max_tall = i 
        for j in range(i + 1, n):
            if best_team[j][0] > best_team[max_tall][0]:
                max_tall = j
        best_team[i],best_team[max_tall] = best_team[max_tall],best_team[i]
    return best_team
result = selection_arr(arr)
for i in range(3):
    print(f"شماره {result[i][1]} با قد {result[i][0]}")