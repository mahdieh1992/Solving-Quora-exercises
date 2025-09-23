#رمز
def find_pass(password,k):
    s = 0
    for i in range(k):
        lock = input()
        # check number exist in lock
        if password[i] in lock:
            # get index number
            index_ = lock.find(password[i])
            #get min length to get to index from start and end lock
            ll = len(lock[0:index_])
            lr = len(lock[index_:])
            if ll < lr:
                s += ll
            else:
                s += lr    
    return s

k = int(input())
password = input().strip()
print(find_pass(password,k))