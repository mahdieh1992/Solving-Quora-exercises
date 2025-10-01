#تولید مقسوم‌علیه‌ها
def divs(n):
    i = 1
    while i <= n:
        if n % i == 0:
            yield i
        i += 1

my_divs = divs(4)
print(list(my_divs))