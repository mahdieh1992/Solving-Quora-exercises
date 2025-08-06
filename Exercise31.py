def detectionWinner(n):
    players = list(range(1,n + 1))
    if n == 1:
        return 1 
    elif n % 2 == 0:
        return 2 * detectionWinner(n // 2) - 1
    elif n % 2 != 0:
        return 2 * detectionWinner((n - 1) // 2) + 1
    

n = int(input())
print(detectionWinner(n))
