def is_peak(number,n):
     pass
n = int(input())
numbers = list(map(int, input().split()))
if len(numbers) != n:
    print(f"count number must be equal {n}")
else:
    is_peak(numbers,n)