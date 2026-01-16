'''
eg:) Multiprocessing for cpu bound tasks for factiorial calci
especially for large numbers,
involve significant computational work.
Multiprocessing can be used to distribute the workload across multiple cpu cores , improving performance

'''

import multiprocessing
import math
import sys
import time

## increase the max number of digits for integer conversion
sys.set_int_max_str_digits(1000000)

## fxn to compute factorials of a given number

def compute_factorial(n):
    print(f"Computing factorial of {n}")
    result = math.factorial(n)
    print(f"Factorial of {n} computed")
    return result

if __name__ == "__main__":
    numbers = [5000, 6000, 7000, 8000]

    start_time = time.time()

    # create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results=pool.map(compute_factorial,numbers)
    
    endtime=time.time()

    print(f"Results: {results}")
    print(f"Time taken: {endtime - start_time} seconds")

    