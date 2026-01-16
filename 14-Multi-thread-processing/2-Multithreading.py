##  MULTITHREADING
## When to use multi threading
## I/O bound tasks: Tasks that spend more time for I/O opertns(eg- file opertn,network requests)
## To perform concurrent execution

# eg
import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")
    
def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

## create 2 threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)
    
t=time.time()

# start the thread
t1.start()
t2.start()

## wait for the threads to complete
t1.join()
t2.join()

finished_time=time.time()-t
print(finished_time)