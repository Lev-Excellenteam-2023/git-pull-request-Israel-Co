import time
from functools import reduce


def timer(f, *args):
    """
    Measure how long is the running time of function f with parameters in which are in args
    :param f: function
    :param args: Input parameters for f 
    :return: The running time of f in seconds
    """
    start_time = time.time()
    print(f(*args))
    return time.time() - start_time


# running example
print('Run time:', timer(reduce, lambda x, y: x * y, [1, 2, 3, 4, 5]), 'Sec')
