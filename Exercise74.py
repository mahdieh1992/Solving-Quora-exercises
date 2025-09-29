print(*sorted([num for index,num in enumerate(list(map(int, input().split()))) if num % 6 == 0 and (index + 1) % 6 == 0])) 
