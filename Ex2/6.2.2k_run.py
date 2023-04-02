import time
from functools import reduce


def timer(f, *args):
    start_time = time.time()
    print(f(*args))
    return time.time() - start_time


print('Run time:', timer(reduce, lambda x, y: x * y, [1, 2, 3, 4, 5]), 'Sec')
