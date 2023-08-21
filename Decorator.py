# cmt 1
# bacnx 1
# C1
# C2

def logit(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logit
def update_product():
    print("Updated")


class ABC:
    pass

class InheritABC(ABC):
    pass

print(type.__base__)
print(type({}))

from functools import wraps


def debug(func):
    '''decorator for debugging passed function'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Full name of this method:", func.__qualname__)
        return func(*args, **kwargs)

    return wrapper


def debugmethods(cls):
    '''class decorator make use of debug decorator
       to debug class methods '''

    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug(val))
    return cls


class debugMeta(type):
    '''meta class which feed created class object
       to debugmethod to get debug functionality
       enabled objects'''

    def __new__(cls, clsname, bases, clsdict):
        obj = super().__new__(cls, clsname, bases, clsdict)
        obj = debugmethods(obj)
        return obj

    # base class with metaclass 'debugMeta'


# now all the subclass of this
# will have debugging applied
class Base(metaclass=debugMeta): pass


# inheriting Base
class Calc(Base):
    def add(self, x, y):
        return x + y

    # inheriting Calc


class Calc_adv(Calc):
    def mul(self, x, y):
        return x * y

    # Now Calc_adv object showing


# debugging behaviour
mycal = Calc_adv()
print(mycal.mul(2, 3))


x = []
y = []
print(id(x))
print(id(y))
print(id(()))

import threading

# Global list to store the sum from each thread
global_sum = 0

# Function to calculate the sum of a sublist
def calculate_sum(sublist):
    global global_sum
    local_sum = sum(sublist)
    # Acquire the GIL to update the global sum
    #with threading.Lock():
    global_sum += local_sum

if __name__ == "__main__":
    # Sample list with elements
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Divide the list into two sublists
    mid = len(my_list) // 2
    sublist1 = my_list[:mid]
    sublist2 = my_list[mid:]

    # Create two threads to calculate the sum of sublists
    thread1 = threading.Thread(target=calculate_sum, args=(sublist1,))
    thread2 = threading.Thread(target=calculate_sum, args=(sublist2,))
    thread3 = threading.Thread(target=calculate_sum, args=(sublist1,))
    thread4 = threading.Thread(target=calculate_sum, args=(sublist2,))

    # Start the threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    # Print the result
    print("Global Sum:", global_sum)