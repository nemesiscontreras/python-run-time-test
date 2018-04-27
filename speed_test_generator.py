# Let's define a speed test decorator
# Similar to the exercise of importing time then using var/math to 'time' to time
# how long a list comprehension  vs a generator took to run
# This show the O(f(n)) as n exponentially increases a list will take longer to execute as opposed to a generator

from time import time
from functools import wraps

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time= time()
        print("Executing {}".format(fn.__name__))
        print("Time Elapsed {}".format(end_time - start_time))
        return result

    return wrapper


@speed_test
def sum_nums_gen():
    return sum(x for x in range(9000000))

@speed_test
def sum_nums_list():
    return sum([x for x in range(9000000)])

print(sum_nums_gen())
print(sum_nums_list())




