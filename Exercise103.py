#کمبود وقت
from threading import Thread
import time


def grow_plants(duration):
    time.sleep(duration)
    print("The plants are grown!")


def listen_to_music(duration):
    time.sleep(duration)
    print("The music is played!")


def cook_meal(duration):
    time.sleep(duration)
    print("The meal is cooked!")

def run_sequential(durations):
    start_time = time.time()
    dict_func = {'0': grow_plants, '1':listen_to_music,'2': cook_meal}    
    for i in range(len(durations)):
        if str(i) in dict_func.keys():
           func = dict_func[str(i)]
           get_time = durations[i]
           func(get_time)
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Sequential execution time: {elapsed_time:.1f} seconds")


def run_threaded(durations):
    start_time = time.time() 
    ls_thread = [grow_plants,listen_to_music,cook_meal] 
    threaded_list = [] 
    for i in range(len(durations)):
        func = ls_thread[i]
        duration = durations[i]
        threaded_list.append(Thread(target=func,args=(duration,)))
        
    for thr in threaded_list:
        thr.start()
        
    for thr in threaded_list:
        thr.join()
        
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Threaded execution time: {elapsed_time:.1f} seconds")


durations = list(map(float, input().split()))
run_sequential(durations)
run_threaded(durations)
