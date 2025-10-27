#تردکاری
import functions
from threading import Thread

def threadize() -> None:
    ln = len(functions.f)
    lg = len(functions.g)
    thread_f = []
    thread_g = []
    for i in range(ln):
        thread_f.append(Thread(target=functions.f[i], name= str(i + 1)))
        
    for thr in thread_f:
        thr.start()
    for thr in thread_f:
        thr.join()
        
    for i in range(lg):
        thread_g.append(Thread(target=functions.g[i], name= str(i + 1)))
        
    for thr in thread_g:
        thr.start()
    for thr in thread_g:
        thr.join()
        
    thread_h = Thread(target= functions.h[0], name= '1')
    thread_h.start()
    thread_h.join() 

    
