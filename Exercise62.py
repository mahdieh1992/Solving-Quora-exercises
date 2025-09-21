# کوچک‌ترین مضرب 
p, d = map(int, input().split())
if p % 2 != 0:
    print("P must be even")
    exit()
else:
    i = 1
    while True:
        m = (d * i) % p
        if m >= 0 and m <= p // 2:
            print(d * i)
            break
        i += 1