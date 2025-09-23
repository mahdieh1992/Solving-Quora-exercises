#محاسبات سخت
import math 
n = int(input())
x = math.ceil(math.pow(n,5/3) + math.tan(math.radians(n)))
y = math.floor(math.pow(math.pi,2 + math.atan(math.pow(math.sin(math.radians(n)),2))))
result = math.gcd(x,y)
print(result)