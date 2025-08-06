#تست بینایی
n = int(input())
word = input()
new_word = input()
if not 1 <= n <= 100000:
    print("len word between 1 and 100000")
elif len(word) != len(new_word):
    print("please Enter length word correct")
else:
    count = 0
    for i in range(n):
        if word[i] != new_word[i]:
            count += 1
    print(count)
            