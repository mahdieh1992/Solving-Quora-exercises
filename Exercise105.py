# مث جاوا
from threading import Thread, Lock

share_lock = Lock()
def synchronized(func):
    def wrapper_func(*args, **kwargs):
        with share_lock:
            return func(*args, **kwargs)
    return wrapper_func

a = 0

@synchronized
def f():
    global a
    for i in range(300000):
        a += 1

t = Thread(target=f)
s = Thread(target=f)

print("Starting threads...")

t.start()
s.start()

t.join()
s.join()

print("Threads finished.")

print(f'{a = }')